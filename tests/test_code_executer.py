import unittest
from code_executer import execute_code


class TestCodeExecutor(unittest.TestCase):

    def test_execute_code(self):
        code = "print('Hello, World!')"
        result = execute_code(code)
        self.assertIn('Hello, World!', result)


if __name__ == '__main__':
    unittest.main()
