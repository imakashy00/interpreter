import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def generate_code(file, content, prompt):
    prompt_to_send = """
    Generate only an executable Python script strictly without **Explanation** to "<PROMPT>" for "<CONTENT>" as JSON like below:
    {
        "code":"<Executable Python script>"
    }
    Provide the <\"file\"> path in python script as provided in the input.
    """
    print("Generating Code!")
    response = model.generate_content(prompt_to_send.replace("<PROMPT>", prompt).replace("<CONTENT>", str(content)).replace("<\"file\">", file))
    print(response.text)
    return response.text.strip('```json')


def generate_format(file, prompt):
    print("Generating Format!")
    response = model.generate_content(f'Return in one sentence the message to show before printing the result to user for {prompt} for file {file}')
    print(response.text)
    return response.text