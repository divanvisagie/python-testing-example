import unittest
import os
from text_analyser import analyse_text



class TextAnalysisTests(unittest.TestCase):
    """Tests for a function yo"""

    def setUp(self):
        """Create a file to use for tests"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now this is a file that I did not want to copy exactly\n'
                    'But I guess we need more than one line')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """do stuff"""
        analyse_text(self.filename)

    def test_line_count(self):
        """check that the line count is correct"""
        actual = analyse_text(self.filename)[0]
        self.assertEqual(2, actual)

    def test_character_count(self):
        "check that the character count is correct"
        actual = analyse_text(self.filename)[1]
        self.assertEqual(93, actual)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file"""
        with self.assertRaises(IOError):
            analyse_text('foobar')



if __name__ == '__main__':
    unittest.main()