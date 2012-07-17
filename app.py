# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
import actions.app

app = Flask( __name__ )

@app.route('/')
def index():
    conf = actions.app.configuration()
    return render_template( 'index.html', app=conf )

if __name__ == '__main__':
    app.debug = True

    app.run()
