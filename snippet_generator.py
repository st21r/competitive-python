import os
import glob
import json

EXTENSION = ".py"
INPUT_DIR = "./lib"
OUTPUT_DIR = "./.vscode/"
OUTPUT_FILE_NAME = "library.code-snippets"
COMMAND = "imlib"

def create_snippet(file_path):
    name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, mode="r") as f:
        text = f.read()
    snippet = {
        "prefix": COMMAND + " " + name,
        "body": text
    }
    return snippet


def create_snippets(dir_name):
    snippets = {}
    for file_path in glob.iglob(os.path.join(dir_name, "**", "*"), recursive=True):
        ext = os.path.splitext(file_path)[1]
        if os.path.isfile(file_path) and ext == EXTENSION:
            file_name = os.path.basename(file_path)
            snippets[file_name] = create_snippet(file_path)
    return snippets


if __name__ == "__main__":
    snippets = create_snippets(INPUT_DIR)
    with open(OUTPUT_DIR + OUTPUT_FILE_NAME, mode="w") as f:
        f.write(json.dumps(snippets, ensure_ascii=False, indent=4))
    print("snippets were generated successfully.")
