import openai
from pathlib import Path


def get_gitignore(file_path: Path):
    data = file_path.read_text()
    data = data.strip()
    data = data.split("\n")
    requirements = [line.strip().split("==")[0] for line in data]
    requirements = "\n".join(requirements)
    prompt = f"Generate a .gitignore file for a Python project with following requirements.\nRequirements:\n{requirements}\n End the response with #END"
    completion = openai.Completion.create(model="text-davinci-003" , api_key="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", prompt=prompt, max_tokens=100, temperature=0.3, top_p=1, frequency_penalty=0, presence_penalty=0.3, stop=["#END"])
    return completion.choices[0].text

