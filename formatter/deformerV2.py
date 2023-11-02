# VS Code version with jkillian.custom-local-formatters-0.0.6
# Format text for RT Toolbox

import sys
import re

def main():
    input_content = sys.stdin.read()
    
    modified_content = ""

    for line in input_content.split('\n'):
        modified_line = add_single_quotes(line)
        modified_line = add_line_numbers(modified_line)

        modified_content += modified_line + '\n'

    sys.stdout.write(modified_content)

def add_single_quotes(line):
    line = re.sub("^\s*$", "'", line)
    return line

def add_line_numbers(line):
    if not re.match(r'^\d+ ', line):
        line = '1 ' + line
    return line

if __name__ == "__main__":
    main()