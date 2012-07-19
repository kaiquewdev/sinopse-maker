# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect, request
import actions.app
import json

app = Flask( __name__ )

@app.route('/')
def index():
    conf = actions.app.configuration()
    
    return render_template( 'index.html', app=conf )

@app.route('/sinopses')
def sinopse_dashboard():
    conf = actions.app.configuration()

    sinopse = {
        'list': actions.app.list_files( './storage' )    
    }

    return render_template( 'sinopse.html', app=conf, sinopse=sinopse )

@app.route('/sinopses/<path:filepath>')
def sinopse_by_file( filepath ):
    conf = actions.app.configuration()
    
    # [0] = slug, [1] = file name
    filepath = filepath.split('/')

    if filepath[0] == 'view':
        if filepath[1]:
            sinopse = {
                'content': json.dumps( actions.app.read_file( './storage/%s' % ( filepath[ 1 ] ) ) )
            }

            return render_template( 'sinopse-view.html', app=conf, sinopse=sinopse )

        return redirect( url_for( 'sinopses' ) )
    elif filepath[0] == 'json':
        request.data = json.dumps( actions.app.read_file( './storage/%s' % ( filepath[ 1 ] ) ) )
        
        return request.data
    elif filepath[0] == 'remove':
        actions.app.delete_file( './storage/%s' % ( filepath[ 1 ] ) )
        
        return redirect( url_for( 'sinopse_dashboard' ) )

@app.route('/sinopse/new', methods=['POST'])
def sinopse_new_file():
    if request.method == 'POST':
        actions.app.create_file( './storage/%s.json' % ( request.form['file_name'] ) )
    
    return redirect( url_for( 'sinopse_dashboard' ) )


@app.route('/about')
def about():
    conf = actions.app.configuration()

    return render_template( 'about.html', app=conf )

if __name__ == '__main__':
    app.debug = True

    app.run()
