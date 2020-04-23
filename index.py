import utils
import io
from flask import Flask, request, render_template

app = Flask(__name__)


def writeFile(ndung):
    f = io.open('file', mode='w', encoding='utf-8')
    f.write(ndung)
    f.close()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="GET":
        input_text=''
        output_text=''
    else:
        input_text=request.form['input_text']
        output_text=utils.auto_correct(input_text)
    return render_template('index.html',data_render={'input_text':input_text,'output_text':output_text})


@app.route('/check', methods=['GET','POST'])
def check():
    if request.method=="GET":
        input_text=''
        input_text_err=''
        message=''
    else:
        input_text=request.form['input_text']
        print('input_text',input_text)
        input_text_err,message=utils.auto_check(input_text)
        print('input_text_err',input_text_err)
        print('message',message)
    return render_template('check.html',data_render={'input_text':input_text,'input_text_err':input_text_err,'message':message})


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)