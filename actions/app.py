# -*- coding: utf-8 -*-
from flask import url_for

def configuration():
    return {
        'title': 'Sinopse Maker',
        'name': 'Sinopse Maker',
        'description': 'Create sinopse, and save format json.',
        'author': 'Kaique da Silva <kaique.developer@gmail.com>',
        'menu': [
            [
                'Inicio',
                url_for( 'index' )
            ],

            [
                'Sinopses',
                url_for( 'sinopses' )
            ],

            [
                'Sobre',
                url_for( 'about' )
            ]
        ]
    }     

def read_file( filepath='' ):
    '''
    Read file if json, and based on json notation.
    '''
    output = {}

    try:
        import os, json

        if ( 
            filepath and 
            os.path.exists( filepath ) and 
            filepath.endswith('.json') 
        ):
            opened_file = open( filepath )
            file_content = json.loads( opened_file.read() )
            opened_file.close()

            if file_content:
                output = file_content
        return output
    except Exception:
        return output

def create_file( filename='' ):
    output = False

    try:
        import os, json

        if filename and filename.endswith('.json'):
            new_file = open( filename, 'w' )
            new_file.write( json.dumps( {} ) )
            new_file.close()

            if os.path.exists( filename ):
                output = True
        return output
    except Exception:
        return output

def write_file( filename='', content={} ):
    output = False

    try:
        import json

        if filename and content:
            opened_file = open( filename, 'w' )
            opened_file.write( json.dumps( content ) )
            opened_file.close()
            
            output = True
        return output
    except Exception:
        return output

def update_file( filename='', content={} ):
    output = False

    try:
        if filename and content:
            last_content = new_content = read_file( filename )

            for k, v in content.iteritems():
                if last_content.has_key( k ) and last_content[ k ] != v:
                    new_content[ k ] = v
                if not last_content.has_key( k ):
                    new_content[ k ] = v
            
            if write_file( filename, new_content ):
                output = True
        return output
    except Exception:
       return output

def delete_file( filepath='' ):
    output = False

    try:
        import os

        if filepath:
            os.remove( filepath )
            
            if not os.path.exists( filepath ):
                output = True
        return output
    except Exception:
        return output

def list_files( filepath='', extension='' ):
    output = []

    try:
        import os

        if filepath:
            file_list = os.listdir( filepath )
            
            if file_list:
                if extension:
                    spec_list = []

                    for single in file_list:
                        if single.endswith( extension ):
                            spec_list.append( single )

                    file_list = spec_list

                output = file_list
        return output
    except Exception:
        return output
