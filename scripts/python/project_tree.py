import os

def print_project_tree(startpath):
    with open("project_tree.txt", "w") as f:
        for root, dirs, files in os.walk(startpath):
            # Ignore .env files, __init__.py, .gitkeep, .git, .venv, and __pycache__
            dirs[:] = [d for d in dirs if d not in ['.gitkeep', '__init__.py', '.git', '.venv', '__pycache__']]
            for file in files:
                if file.endswith('.env'):
                    continue
                f.write(os.path.relpath(os.path.join(root, file), startpath) + "\n")

if __name__ == "__main__":
    print_project_tree(".")
