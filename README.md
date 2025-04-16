# Background Remover API

A simple Flask API that removes backgrounds from images using the 'rembg' library.

## Setup

1. Install Python (3.8 or newer)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   python app.py
   ```

The server will run on http://0.0.0.0:5000 and will be accessible to other devices on the same network.

## API Endpoints

- `GET /`: Check if API is running
- `POST /remove-bg`: Upload an image to remove its background
  - Request: Form data with 'image' file
  - Response: PNG image with transparent background 