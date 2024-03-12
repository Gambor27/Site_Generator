from textnode import TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode
import shutil, os
from markdown_blocks import markdown_to_html_node

def directory_copy():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    directory_copy_r(None)

def directory_copy_r(directory):
    if directory:
        source_dir = os.path.join("./static", directory)
        target_dir = os.path.join("./public", directory)
    else:
        source_dir = "./static"
        target_dir = "./public"
    print(source_dir, target_dir)
    contents = os.listdir(source_dir)
    files = []
    directories = []
    for object in contents:
        if os.path.isfile(os.path.join(source_dir, object)):
            files.append(object)
        else:
            directories.append(object)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    for file in files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))
    if directory:
        for new_directory in directories:
            directory_copy_r(os.path.join(directory, new_directory))
    else:
        for new_directory in directories:
            directory_copy_r(new_directory)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        source_contents = file.read()
    with open(template_path, 'r') as file:
        template_contents = file.read()
    parent = markdown_to_html_node(source_contents)
    body = parent.to_html()
    title = extract_title(source_contents)
    output_html = template_contents.replace("{{ Title }}", title)
    output_html = output_html.replace("{{ Content }}", body)
    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(dest_path, 'w') as file:
        file.write(output_html)

        

    

def main():
    directory_copy()
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()