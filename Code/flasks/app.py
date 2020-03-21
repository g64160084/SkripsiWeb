#C:\Users\DELL\miniconda3\envs\PYCHARM\python.exe C:/Users/DELL/Documents/SKRIPSI/PYCHARM/Code/flasks/app.py
from flask import Flask,flash, render_template, url_for, request, redirect,send_from_directory,current_app,send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from Code.ClippingWeb import clipweb

UPLOAD_FOLDER = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\static\img"
ALLOWED_EXTENSIONS = {'tiff', 'tif'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clipping')
def clip():
    return render_template('clipping.html')

@app.route('/cloudremoval')
def cloud():
    return "Cloudremoval!"

@app.route('/ndvimap')
def ndvi():
    return "Ndvimap!"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
            download =clipweb(os.path.join(uploads,filename))
            return send_file(download,as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)