from flask import Flask, request, send_file, jsonify, render_template
import subprocess
import zipfile
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

# Ensure upload and converted directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def pdf_to_svg(input_pdf, output_svg):
    """
    Converts a PDF file to an SVG file using Inkscape.
    
    Parameters:
    input_pdf (str): The path to the input PDF file.
    output_svg (str): The path to the output SVG file.
        """
    command = [
        'inkscape',
        input_pdf,
        '--export-type=svg',
        '--export-filename', output_svg,
        '--export-area-drawing',      # Crop to content
        '--export-background-opacity=0'  # Remove background
    ]

    
    subprocess.run(command, check=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify(error='No file part'), 400

    files = request.files.getlist('files[]')
    if not files:
        return jsonify(error='No selected files'), 400

    converted_files = []
    for file in files:
        if file:
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            output_filename = f"{os.path.splitext(filename)[0]}.svg"
            output_path = os.path.join(app.config['CONVERTED_FOLDER'], output_filename)
            pdf_to_svg(input_path, output_path)
            converted_files.append(output_path)

    # Create a zip file of all converted SVGs
    zip_path = os.path.join(app.config['CONVERTED_FOLDER'], 'converted_svgs.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in converted_files:
            zipf.write(file, os.path.basename(file))

    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
