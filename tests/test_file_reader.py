import unittest
from file_reader import read_pdf, read_xlsx, read_csv, read_docx

class TestFileReader(unittest.TestCase):

    def test_read_pdf(self):
        content = read_pdf('masteringapi.pdf')
        self.assertIn('Sample PDF Content', content)

    def test_read_xlsx(self):
        content = read_xlsx('Output.xlsx')
        self.assertIsInstance(content, list)

    def test_read_csv(self):
        content = read_csv('country.csv')
        self.assertIn('Sample,CSV,Content', content)

    def test_read_docx(self):
        content = read_docx('Interpreter.docx')
        self.assertIn('Sample DOCX Content', content)

if __name__ == '__main__':
    unittest.main()
