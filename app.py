from flask import Flask
import os, config
from __init__ import create_app


app = Flask(__name__)


if __name__ == "__main__":
    create_app(app).run()
