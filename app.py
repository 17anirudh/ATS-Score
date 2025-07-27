from docx import Document
from PyPDF2 import PdfReader
import requests as req
from flask import Flask, render_template, request
import json

app = Flask(__name__)

def docx_text(docx: Document) -> str:
    text: str = ""
    for paragraph in docx.paragraphs:
        text += paragraph.text
    return text

def pdf_text(pdf: PdfReader) -> str:
    text: str = ""
    page_content = pdf.pages
    for i in page_content:
        text += i.extract_text()
    return text    

def response(query: str)-> str:
    payload = {
        "model": "NorthEye:1.0",
        "prompt": query,
        "stream": False
    }
    response = req.post("http://localhost:11434/api/generate", headers={"Content-Type": "application/json"}, json=payload)
    if response.status_code == 200:
        print('Success')
        return response.json()
    else:
        print(f"Error: {response.status_code}") 
        return None

@app.route('/')
def index() -> render_template:
    return render_template('index.html')

@app.route('/rate', methods=['GET', 'POST'])
def rate() -> render_template:
    if request.method == 'POST':
        job_description = request.form.get('description', '')
        qualifications = request.form.get('qualifications', '')
        resume_file = request.files.get('resume')
        resume_text = ""
        
        if resume_file and resume_file.filename != '':
            filename = resume_file.filename
            ext = filename[filename.rfind("."):].lower()
            match(ext):
                case '.pdf': 
                    resume_text = pdf_text(PdfReader(resume_file))
                case '.docx': 
                    resume_text = docx_text(Document(resume_file))
                case '.txt':
                    resume_text = resume_file.read().decode('utf-8')
                case _: 
                    resume_text = ""

            prompt = f"""
                {{
                    Job Descriptions: {job_description.strip().replace('\n', '  ')},
                    Qualifications: {qualifications.strip().replace('\n', '  ')},
                    Resume: {resume_text.strip().replace('\n', '  ')}
                }}
            """
            res = response(prompt)
            if res and 'response' in res:
                response_text = json.loads(res['response'])
                json.dump(response_text, open('test.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
                print('Sending response........')
                return render_template('index.html', result=response_text), 200
            else:
                return render_template('index.html', error="Error processing request"), 500
            
        else:
            return render_template('index.html', error="Error processing request"), 500

if __name__ == '__main__':
    app.run(port=5400, host='0.0.0.0', debug=True)