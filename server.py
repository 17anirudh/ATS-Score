from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('alpine.html')

@app.route('/hello', methods=['POST'])
def getData():
    f = request.files.get('file')
    name = request.form.get('name')  
    age = request.form.get('age')   
    print(f"{name}\n{age}") 
    f.save(f"./{f.filename}")
    
    return jsonify({
        "name": "Anirudh",
        "age": 20 
    })

app.run(port=9000, host='localhost', debug=True)