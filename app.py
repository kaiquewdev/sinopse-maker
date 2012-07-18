# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect, request
import actions.app

app = Flask( __name__ )

@app.route('/')
def index():
    conf = actions.app.configuration()
    
    return render_template( 'index.html', app=conf )

@app.route('/sinopses')
def sinopses():
    conf = actions.app.configuration()

    sinopse = {
        'list': actions.app.list_files( './storage' )    
    }

    return render_template( 'sinopse.html', app=conf, sinopse=sinopse )

@app.route('/sinopses/<path:filepath>', methods=['GET', 'POST'])
def sinopse_by_file( filepath ):
    filepath = filepath.split('/')

    if filepath[0] == 'view' and request.method == 'GET':
        pass
    elif filepath[0] == 'remove' and request.method == 'GET':
        if actions.app.delete_file( './storage/%s' % ( filepath[ 1 ] ) ):
            return redirect( url_for( 'sinopses' ) )

    return ''

@app.route('/sinopse/new', methods=['POST'])
def sinopse_new_file():
    if request.method == 'POST':
        actions.app.create_file( './storage/%s.json' % ( request.form['file_name'] ) )
    
    return redirect( url_for( 'sinopses' ) )


@app.route('/about')
def about():
    conf = actions.app.configuration()

    return render_template( 'sinopse.html', app=conf )

if __name__ == '__main__':
    app.debug = True

    app.run()
