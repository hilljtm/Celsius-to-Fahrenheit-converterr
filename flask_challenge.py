from flask import Flask

app = Flask(__name__)

@app.route('/<int:celsius>')
def convert(celsius):
    farenheit = (celsius * 1.8) + 32
    return f'{farenheit}'
