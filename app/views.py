from app import app
from flask import request, render_template, redirect, url_for, flash, abort, make_response, session, send_from_directory


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')












