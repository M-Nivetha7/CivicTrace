from flask import Flask, render_template, request
import os, zipfile, shutil
from model.image_detection import check_image_in_database

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Clear previous uploads
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER)

    # Get uploaded files
    db_file = request.files.get('database')
    img_file = request.files.get('image')

    if not db_file or not img_file:
        return "Please upload both database and image files!"

    # Save database (assuming ZIP)
    db_path = os.path.join(UPLOAD_FOLDER, 'database.zip')
    db_file.save(db_path)

    # Extract database
    db_extract_path = os.path.join(UPLOAD_FOLDER, 'database')
    with zipfile.ZipFile(db_path, 'r') as zip_ref:
        zip_ref.extractall(db_extract_path)

    # Save uploaded image
    img_path = os.path.join(UPLOAD_FOLDER, img_file.filename)
    img_file.save(img_path)

    # Check image in database
    result = check_image_in_database(img_path, db_extract_path)

    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True, port=5001)

