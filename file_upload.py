from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Set the upload folder (directory where uploaded files will be saved)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the request contains a file part
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files['file']

    # If no file is selected
    if file.filename == '':
        return jsonify({"message": "No file selected for uploading"}), 400

    # Save the file to the designated folder
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"message": f"File '{file.filename}' uploaded successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
