# Code Interpreter

## Overview

This project is a code interpreter that reads various file formats (PDF, XLSX, CSV, DOCX), generates Python code using Gemini API, executes the code, and returns the result to the user.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/imakashy00/interpreter.git
    cd interpreter
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up Gemini API key:
    ```sh
    export Gemini_API_KEY='your_gemini_api_key'
    ```

## Usage

To run the code interpreter:
```sh
python main.py
``` 

## Example
```
   Enter the file path: masteringapi.pdf
   Enter the prompt: Count the number of pages in the PDF file
```
