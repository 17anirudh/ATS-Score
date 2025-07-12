from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('alpine.html')

@app.route('/hello', methods=['POST'])
def getData():
    try:
        f = request.files.get('file')
        name = request.form.get('name')  
        age = request.form.get('age')   
        
        if f is not None and f.filename != '':
            if not os.path.exists('file'):
                os.makedirs('file')
            file_path = f"./file/{f.filename}"
            f.save(file_path)
            print(f"File saved: {f.filename} at {file_path}")
        
            return jsonify({
                "status": "success"
            })
            
        else:
            print("No file uploaded or empty filename")
            return jsonify({
                "status": "error"
            })
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=9000, host='localhost', debug=True)