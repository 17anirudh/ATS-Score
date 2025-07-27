
# antardvara.ssl
Offline, private, and powerful Resume Analyzer using a local LLM.

## Overview
**antardvara.ssl** is a local and secure ATS analyzer, which takes in job description, qualification and your resume sends it to internal local [gemma3n:e2b](https://ollama.com/library/gemma3n:e2b) based custom model (NorthEye), which analyzes and gives you the result

## Screenshot
![App Screenshot](/ss.png)

## Features
- Web interface built using Flask (Jinja2) and plain HTML+CSS for smooth user experience
- Traditional server-side form submission (secure because no exposed API endpoints)
- Lightweight Flask framework handles full backend logic
- Simple, minimal UX
- Completely offline — your data stays on your machine


## Tech Stack
- Model: Ollama
- Frontend: HTML and CSS
- Backend: Flask, PyPDF2, python docx
- Communication: Traditional server-side form submission


## Installation 
#### Prerequisites:
- Python v3.10+ 
- Git v2.49.0+ 
- Ollama v0.9.5+
- Storage: 5.6GB (for local model)
- RAM: 6GB+ (for model processing)

```dir
  git clone https://github.com/17anirudh/ATS-Score.git
```
- __Firstly,__ install all required modules
  ```ATS-Score
  pip install -r requirements.txt
  ```
- __Secondly, and most importantly ⚠️__ We have use ollama to create model specified (Note: Ensure Modelfile exists in the path)
  ```ATS-Score
  ollama create NorthEye:1.0
  ```
- Congrats, you can now run the local model and application, access here - [port:5400](localhost:5400)
  ```ATS-Score
  python app.py
  ```
