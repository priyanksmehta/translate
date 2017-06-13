from models import TextTranslation
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.add_url_rule('/translate', view_func=TextTranslation.as_view('translate'))

if __name__ == '__main__':
    app.run('0.0.0.0')
