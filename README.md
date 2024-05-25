# PDF to SVG Converter

This is a simple web application that allows users to convert PDF files to SVG format. It provides a drag-and-drop interface where users can drop multiple PDF files or folders, and the application will return a zip file containing the converted SVG files.

## Features

- Drag-and-drop interface for easy file uploads.
- Supports multiple file uploads and folders.
- Converts PDF files to SVG using Inkscape.
- Returns a zip file containing all the converted SVG files.

## Requirements

- Python 3.x
- Flask
- Inkscape

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/spottenn/pdf-to-svg-converter.git
    cd pdf-to-svg-converter
    ```

2. **Install the required Python packages:**

    ```sh
    pip install Flask
    ```

3. **Ensure Inkscape is installed and available in your system's PATH or in the same directory as the app.py file.**

## Usage

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to `http://<your_machine_ip>:5000`.**

3. **Drag and drop your PDF files or folders into the designated area.**

4. **Open the zip file containing the converted SVG files.**

## File Structure

- `app.py`: The Flask backend that handles file uploads and conversion.
- `templates/index.html`: The frontend HTML file with drag-and-drop functionality.
- `uploads/`: Directory where uploaded files are temporarily stored.
- `converted/`: Directory where converted SVG files are stored.


## License

This project is licensed under the MIT License. 

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Inkscape](https://inkscape.org/)

## AI Citation

ChatGPT was used interactively to assist in creating, editing, and revising text. I, Nathan Spotten, have carefully reviewed said text and take ultimate responsibility for the content of this project.

