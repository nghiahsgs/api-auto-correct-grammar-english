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


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)