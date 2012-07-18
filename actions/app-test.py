import unittest, os, app

class AppTest( unittest.TestCase ):
    def test_creation_of_file( self ):
        self.assertTrue( app.create_file( './test-storage/test.json' ) )

    def test_list_of_files( self ):
        assertion_list = ['test.json', 'test.txt', 'percist.json']
        dir_list = app.list_files( './test-storage' )

        self.assertTrue( assertion_list, dir_list )
    
    def test_specific_list_of_files( self ):
        assertion_list = ['percist.json']
        dir_list = app.list_files( './test-storage', extension='.json' )

        self.assertEquals( assertion_list, dir_list  )
    
    def test_content_read_file( self ):
        assertion_content = {"testing": "file"}

        self.assertEquals( assertion_content, app.read_file( './test-storage/percist.json' ) )

    def test_writing_content_in_the_file( self ):
        assertion_content = {"testing": "file"}

        self.assertTrue( app.write_file( './test-storage/percist.json', assertion_content ) )

    def test_update_content_in_file( self ):
        assertion_content = {"testing": "file update"}

        self.assertTrue( assertion_content, app.update_file( './test-storage/percist.json', assertion_content ) )
        self.assertEquals( assertion_content, app.read_file( './test-storage/percist.json' ) )

    def test_remotion_of_file( self ):
        self.assertTrue( app.delete_file( './test-storage/test.json' ) )

if __name__ == '__main__':
    unittest.main()
