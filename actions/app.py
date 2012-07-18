def configuration():
    return {
        'title': 'Sinopse Maker',
        'name': 'Sinopse Maker',
        'description': 'Create sinopse, and save format json.',
        'author': 'Kaique da Silva <kaique.developer@gmail.com>'
    }     

def read_file( filename='' ):
    pass

def create_file( filename='' ):
    output = False

    try:
        import os

        if filename:
            new_file = open( filename, 'w' )
            new_file.close()

            if os.path.exists( filename ):
                output = True
        return output
    except Exception:
        return output

def update_file( filename='', content='' ):
    pass

def write_file( filename='', content='' ):
    pass

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

def list_files( filepath='' ):
    output = []

    try:
        import os

        if filepath:
            file_list = os.listdir( filepath )

            if file_list:
                output = file_list
        return output
    except Exception:
        return output
