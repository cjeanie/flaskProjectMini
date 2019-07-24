from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
# @app.route('/index')
# def index():
#     return render_template("/index.html")
    
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template ("index.html")
    
@app.route('/outputSentence', methods = ['GET', 'POST'])
def outputSentence():
    formData = dict(request.form)
    sentence = formData['sentence']
    output = model.evenOdd(sentence)
    return render_template ("outputSentence.html", sentence=sentence, output=output)