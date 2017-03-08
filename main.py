from flask import Flask, render_template, request
from werkzeug import secure_filename
import sys
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file1():
    print("test")
    if request.method == 'POST':

      f = request.files['file']
      f=f.stream.readlines()
      for line in f:
         print (line.decode("utf-8-sig").encode("utf-8"))
      return 'hello'

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)