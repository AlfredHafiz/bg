from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io
import os
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return jsonify({"status": "API is running"})

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    # Check if image file is in the request
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    
    # Read the image
    input_image = Image.open(file.stream)
    
    # Remove the background
    output_image = remove(input_image)
    
    # Save to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    output_image.save(temp_file.name)
    temp_file.close()
    
    # Return the image
    return send_file(temp_file.name, mimetype='image/png', as_attachment=True, 
                     download_name='removed_bg.png')

@app.after_request
def after_request(response):
    # Clean up temp files if they exist
    if hasattr(response, '_temp_file'):
        os.unlink(response._temp_file)
    return response

if __name__ == '__main__':
    # Use 0.0.0.0 to make the server accessible from other devices on the network
    app.run(host='0.0.0.0', port=5000, debug=True) 