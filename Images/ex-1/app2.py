from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

@app.route("/")
def main():
    # return 'Hello'
    return render_template('hi.html', name=socket.gethostname(), color=color_codes[COLOR])
