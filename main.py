from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')

@app.route('/image')
def get_image():
    # Replace 'image.jpg' with the path to your generated image
    image_path = 'image.jpg'
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
