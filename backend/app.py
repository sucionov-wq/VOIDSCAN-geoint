from flask import Flask, request, jsonify
from PIL import Image
from PIL.ExifTags import TAGS

app = Flask(__name__)

def get_exif(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = str(value)
    return exif_data

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    img = Image.open(file)

    exif = get_exif(img)

    tips = [
        "Check language on signs",
        "Look at shadows to estimate time",
        "Check vehicle plates",
        "Analyze terrain and vegetation",
        "Identify architecture style",
        "Look for weather conditions clues"
    ]

    return jsonify({
        "exif": exif,
        "tips": tips
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
