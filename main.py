from file_reader import read_file
from code_writer import generate_code, generate_format
from code_executer import execute_code


def start(file_path, user_prompt):
    try:
        content = read_file(file_path)
        code = generate_code(file_path, content, user_prompt)
        result = execute_code(code)
        print("Generated Code:\n", code)
        res_format = generate_format(file_path, user_prompt)
        print(f'{res_format}:\n, {result}')
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_path = input("Enter the file path: ")
    user_prompt = input("Enter the prompt: ")
    start(file_path, user_prompt)


if __name__ == "__main__":
    main()

