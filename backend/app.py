from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from copy import deepcopy
import os
import json
import secrets
from typing import List, Dict, Union, Callable, Any, Optional

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_DIR = os.path.join("static", "css")
IMG_DIR = os.path.join("static", "img")
JS_DIR = os.path.join("static", "js")
TEMP_DIR = "templates"
DATABASE_DIR = os.path.join("database", "website")



app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
app.json.sort_keys = False
app.secret_key = secrets.token_bytes(32)
