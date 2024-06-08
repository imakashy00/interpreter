import unittest
from code_writer import generate_code
from file_reader import read_xlsx


class TestCodeWriter(unittest.TestCase):

    def test_generate_code(self):
        content = read_xlsx('Output.xlsx')
        prompt = "Summarize this content"
        code = generate_code('Output.xlsx', content, prompt)
        self.assertIn('def', code)


if __name__ == '__main__':
    unittest.main()
