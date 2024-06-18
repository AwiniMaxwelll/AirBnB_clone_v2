#!/usr/bin/python3
"""
Starting up flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
	"""displays hello HNBN"""
	return "Hello HNBN!"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
