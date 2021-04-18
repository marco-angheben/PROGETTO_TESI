import os
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from flask_api import status
from analyzer.analyze_video import analyze_video
from analyzer.analyze_image import analyze_image

CWD = os.getcwd()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = f'{CWD}/temp'

@app.route('/api/video', methods = ['POST'])
@cross_origin()
def video():
    try:
        if 'video' not in request.files:
            return "Video not found", status.HTTP_400_BAD_REQUEST

        file = request.files['video']

        if file.filename == '':
            return "File without name", status.HTTP_400_BAD_REQUEST

        filename = file.filename
        saved_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(saved_file_path)
        output_file_path = analyze_video(saved_file_path)
        return send_file(output_file_path, attachment_filename='video.mp4')
        
    except Exception as e:
        return "Video not found", status.HTTP_500_INTERNAL_SERVER_ERROR



@app.route('/api/image', methods = ['POST'])
@cross_origin()
def image():
    try:
        print('image')
        if 'image' not in request.files:
            return "Image not found", status.HTTP_400_BAD_REQUEST

        file = request.files['image']

        if file.filename == '':
            return "File without name", status.HTTP_400_BAD_REQUEST

        filename = file.filename
        saved_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(saved_file_path)

        output_file_path = analyze_image(saved_file_path)
        return send_file(output_file_path, attachment_filename='image.jpg')
        
    except Exception as e:
        return "Image not found", status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(port=5000)