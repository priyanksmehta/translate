from flask import current_app as app
from .models import TextTranslation

app.add_url_rule('/translate', view_func=TextTranslation.as_view('translate'))
