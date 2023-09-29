from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from gpt import get_gitignore


app = FastAPI()

home_file = Path(__file__).parent / "index.html"
gitignore = Path(__file__).parent / ".gitignore"


@app.get("/")
def root():
    resp = get_gitignore(Path("requirements.txt"))
    gitignore.write_text(resp)
    return resp

