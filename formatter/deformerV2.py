import os
import re

def main():
    # Specify the relative path to the "programs" subfolder
    programs_folder = "./programs"

    # Iterate over the files in the "programs" subfolder
    for filename in os.listdir(programs_folder):
        if filename.endswith(".prg"):
            # Process the .prg file
            file_path = os.path.join(programs_folder, filename)
            process_prg_file(file_path)

def process_prg_file(file_path):
    # Read the content of the input .prg file
    input_content = read_prg_file(file_path)

    # Perform your desired actions on the input content
    modified_content = ""

    for line in input_content.split('\n'):
        modified_line = add_single_quotes(line)
        modified_line = add_line_numbers(modified_line)

        modified_content += modified_line + '\n'

    # Save the modified content to the output file
    write_prg_file(file_path, modified_content)

def read_prg_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def write_prg_file(input_file, content):
    try:
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File saved successfully: {input_file}")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

def add_single_quotes(line):
    line = re.sub("^\s*$", "'", line)
    return line

def add_line_numbers(line):
    if not re.match(r'^\d+ ', line):
        line = '1 ' + line
    return line

main()