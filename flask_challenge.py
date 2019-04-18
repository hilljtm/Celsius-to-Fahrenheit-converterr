from flask import Flask

app = Flask(__name__)

@app.route('/<int:celsius>')
def convert(celsius):
    farenheit = (celsius + 32) / 9/5
    return f'{farenheit}'
