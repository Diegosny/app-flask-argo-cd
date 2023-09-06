from flask import Flask

app = Flask(__name__)

from src.controllers.user import home