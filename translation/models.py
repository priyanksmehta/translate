# -*- coding: utf-8 -*-
from google.cloud import translate
from flask.views import MethodView
from flask import request, jsonify

class TextTranslation(MethodView):
  
    client = translate.Client()

    def post(self):
        data = request.get_json()
        text = data['text']
        target = data['target']
        return jsonify(self.client.translate(text, target_language=target))
