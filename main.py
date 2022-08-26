from flask import Flask, render_template, Response,  request, session, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
# from resize_for_detection import crop
from pathlib import Path
import glob
import os
import cv2
import json
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "/home/anupamkumar/tf1/app/static/uploads"
@app.route('/', methods = ["GET", "POST"] )
def index():
    if request.method=="POST":
        if request.files:
            image = request.files["image"]
            # filename = "image.png"
            # image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['IMAGE_UPLOADS'], 'uploads.jpg')
            image.save(filepath)
            image = cv2.imread(filepath)
            # print(filename)
            flash('Generated Successfully!','success')
            #return redirect(request.url)
            #resizer(filepath, filename, image)
            # crop(filepath, filename, image)
            # html_file = Path(filename).stem
            # html_file = html_file+".html"
            # output_file_path = "static/output/"+html_file
            # if os.path.exists(output_file_path):
            #     f = open(output_file_path, "r")
            #     code = f.read()
            # else:
            #     print("The file does not Exist")
            # return render_template('upload.html', display_detection = filename, fname = filename, code = code, html_file = html_file)

    return render_template('upload.html', fileupload=True)



if __name__ == '__main__':
    app.secret_key='secret'
    app.run(debug=True)
