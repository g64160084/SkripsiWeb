#C:\Users\DELL\miniconda3\envs\PYCHARM\python.exe C:/Users/DELL/Documents/SKRIPSI/PYCHARM/Code/flasks/app.py
from flask import Flask,flash, render_template, url_for, request, redirect,send_from_directory,current_app,send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from Code.ClippingWeb import clipweb
from Code.cloudremovalweb import cloudremove
import rasterio
from zipfile import ZipFile

UPLOAD_FOLDER = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\static\img"
UPLOAD_B4 =     r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\b4"
UPLOAD_B5 =     r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\b5"
UPLOAD_BQA =    r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\bqa"
ALLOWED_EXTENSIONS = {'tiff', 'tif'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_B4'] = UPLOAD_B4
app.config['UPLOAD_B5'] = UPLOAD_B5
app.config['UPLOAD_BQA'] = UPLOAD_BQA
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
    return render_template('cloud_removal.html')

@app.route('/ndvimap')
def ndvi():
    return render_template('ndvi_map.html')

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

@app.route('/upload1', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        # check if the post request has the file part
        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #if user does not select file, browser also
        #submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(files[0].filename)
            filename2 = secure_filename(files[1].filename)
            filename3 = secure_filename(files[2].filename)
            uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
            uploads2 = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
            uploads3 = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
            download = os.path.join(uploads, filename)
            download2 = os.path.join(uploads2, filename2)
            download3 = os.path.join(uploads3, filename3)
            file_list = [download, download2, download3]
            # Read metadata of first file
            with rasterio.open(file_list[0]) as src0:
                meta = src0.meta

            # Update meta to reflect the number of layers
            meta.update(count=len(file_list))

            # Read each layer and write it to stack
            with rasterio.open(r'C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\stack\stack.tif', 'w', **meta) as dst:
                for id, layer in enumerate(file_list, start=1):
                    with rasterio.open(layer) as src1:
                        dst.write_band(id, src1.read(1))
            stack = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\stack\stack.tif"
            jadi,jadi2 = cloudremove(stack,filename,filename2)
            zipObj = ZipFile(r'C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\zipped\CloudRemoved.zip', 'w')

            # Add multiple files to the zip
            zipObj.write(jadi)
            zipObj.write(jadi2)

            # close the Zip File
            zipObj.close()

    return send_file(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\uploads\zipped\CloudRemoved.zip",as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)