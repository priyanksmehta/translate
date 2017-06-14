from flask import current_app as app
print app.name
from .models import TextTranslation

app.add_url_rule('/translate', view_func=TextTranslation.as_view('translate'))
