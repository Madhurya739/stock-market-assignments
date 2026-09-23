import ast
import os

SRC_DIR = "src"

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    lines = source.splitlines()

    new_lines = lines[:]
    offset = 0

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            # Skip private functions
            if node.name.startswith("_"):
                continue

            # Check if docstring exists
            if not ast.get_docstring(node):
                # Insert placeholder after function definition line
                def_line = node.lineno - 1 + offset
                indent = " " * (node.col_offset + 4)
                new_lines.insert(def_line + 1, f'{indent}"""TODO: Add docstring."""')
                offset += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))


def walk_src():
    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(".py"):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    walk_src()
    print("Docstring placeholders added to all public functions in src/")
