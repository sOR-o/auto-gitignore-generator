# auto-gitignore-generator

AutoGitignoreGenerator is a Python tool that automates the creation of `.gitignore` files for your projects. It uses the OpenAI GPT-3 model to generate a customized `.gitignore` file based on your input requirements.

## How It Works

1. **Input Your Requirements** : Create a `req.txt` file and specify which files or directories you want to include or exclude from version control.

2. **Run the Script** : Use the provided script to interact with the GPT-3 chatbot. The script will read your `req.txt` file and send a request, which will generate a `.gitignore` file based on your input.

3. **Retrieve Your `.gitignore` File**: The generated `.gitignore` file will be provided as output, ready to be used in your project.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your OpenAI GPT-3 API credentials as environment variables.
4. Create a `req.txt` file with your specific requirements.
5. Run the script using `python main.py`.

## Dependencies

- OpenAI GPT-3 Python SDK
- Requests

