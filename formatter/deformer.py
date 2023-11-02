# Test version
# Reads the content of the input .prg file and writes the modified content to the output file

import re

# Define the input and output file names
input_file = "formatted.prg"
output_file = "deformed.prg"

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
        
def add_line_numbers(input_line):
    modified_content = '1 ' + input_line
    return modified_content

def add_single_quotes(line):
    line = re.sub("^\s*$", "'", line)
    return line

def main():

    # Read the content of the input .prg file
    input_content = read_prg_file(input_file)
    # input_content = sys.stdin.read()

    if input_content is not None:
        modified_content = ""
        
        for line in input_content.split('\n'):
            modified_line = add_single_quotes(line)
            modified_line = add_line_numbers(modified_line)
            
            modified_content += modified_line + '\n'

        # Save the modified content to the output file
        write_prg_file(output_file, modified_content)
        # sys.stdout.write(modified_content)

if __name__ == "__main__":
    main()
