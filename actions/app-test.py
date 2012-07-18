import unittest, os, app

class AppTest( unittest.TestCase ):
    def test_creation_of_file( self ):
        self.assertTrue( app.create_file( './test-storage/test.json' ) )

    def test_list_of_files( self ):
        assertion_list = ['test.json']
        dir_list = app.list_files( './test-storage' )

        self.assertTrue( dir_list == assertion_list  )

    def test_remotion_of_file( self ):
        self.assertTrue( app.delete_file( './test-storage/test.json' ) )
if __name__ == '__main__':
    unittest.main()
