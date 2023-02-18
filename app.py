from flask import Flask,jsonify,render_template,request
import os
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    try:
        
        return render_template('index.html',u=0)
    except Exception as e:
        return jsonify(str(e))

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == "POST":
        file = request.files['image']
        file_path = os.path.join(app.root_path, 'static', file.filename)
        file.save(file_path)
     
        return render_template('index.html', img=file.filename,u=1)


if __name__ == "__main__":
    app.run(debug=True)


