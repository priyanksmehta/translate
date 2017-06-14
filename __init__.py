from .app import app

with app.app_context():
    from .translation import models, views
