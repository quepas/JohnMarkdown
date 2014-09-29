__author__ = 'quepas'

import os

def list_markdown(directory):
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".md"):
                markdown_files.append(root + "\\" + file)
    return markdown_files

def append_markdown(head_name, append_name, sep="\n"):
    head_file = open(head_name, "a")
    append_file = open(append_name, "r")
    head_file.write(sep + append_file.read())

def clear_output_file(path):
    open(path, 'w').close()

def go(directory, sep):
    md_files = list_markdown(".")
    num_md_files = len(md_files)
    if num_md_files <= 1:
        print("Nothing to merge")
    else:
        print("Mergin in alphabetic order")
        head = "output.md"
        clear_output_file(head)
        for i in range(0, num_md_files):
            append_markdown(head, md_files[i], sep)

go(".", "\n\n")


