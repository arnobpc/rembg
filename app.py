from flask import Flask, request, send_file
from remove_bg import remove_background
import os

app = Flask(_name_)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No image uploaded'}, 400

    file = request.files['image']
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(RESULT_FOLDER, file.filename)
    file.save(input_path)

    remove_background(input_path, output_path)
    return send_file(output_path, mimetype='image/png')

if _name_ == '_main_':
    app.run(debug=True)