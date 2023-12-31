import re
import sys

start_patterns = re.compile(r'(\s*)(\*\w*|Select|Case|Default|If|For|While)(\b)')
end_patterns = re.compile(r"(\s*)(End(If)?\b|'-----.*|Break\b)")
spaced_patterns = ['<=', '>=', '<>', 'Or', 'And']
        
def delete_line_numbers(input_line):
    modified_content = re.sub(r'^\d*', '', input_line)
    # print('line numbers removed')
    return modified_content

def delete_single_quotes(input_line):
    stripped_line = input_line.strip()
    if stripped_line == "'":
        stripped_line = re.sub(r"'", '', stripped_line)
    # print('quotes removed in empty lines')
    return stripped_line

def delete_whitespaces(input_line):
    modified_line = re.sub(r'^\s*', '', input_line)
    modified_line = re.sub(r'\s$', '', modified_line)
    # print('whitespaces removed')
    return modified_line

def indent_content(input_line, start_patterns, end_patterns, insert_tab_number):
    
    if re.match("^\s*Else\\b", input_line):                                 #Else handling
        modified_line = '\t' * (insert_tab_number - 1) + input_line
    else:
        modified_line = '\t' * insert_tab_number + input_line
           
    if re.match(end_patterns, input_line) and insert_tab_number > 0:        #End pattern check
        insert_tab_number -= 1
    if re.match(start_patterns, input_line):                                #Start pattern check
        insert_tab_number += 1
    if not input_line.startswith("'") and re.search('\\bThen\s(?=\w+)', input_line):    #One line 'if-then' handling
        insert_tab_number -= 1

    # print('indents added')
    return modified_line, insert_tab_number

def add_spaces(line):
    for pattern in spaced_patterns:
        line = re.sub(r'\s*{}\s*'.format(re.escape(pattern)), ' {} '.format(pattern), line)
    line = re.sub(r'(\s*)<(?!>|=)(\s*)', ' < ', line)
    line = re.sub(r'(\s*)(?<!<)>(?!=)(\s*)', ' > ', line)
    line = re.sub(r'(\s*)(?<!<|>)=(\s*)', ' = ', line)
        
        
    # print('spaces added')
    return line

def main():

    input_content = sys.stdin.read()

    if input_content is not None:
        modified_content = ""
        insert_tab_number = 0
        
        for line in input_content.split('\n'):
            modified_line = delete_line_numbers(line)
            modified_line = delete_single_quotes(modified_line)
            modified_line = delete_whitespaces(modified_line)
            [modified_line, insert_tab_number] = indent_content(modified_line, start_patterns, end_patterns, insert_tab_number)
            modified_line = add_spaces(modified_line)
            
            modified_content += modified_line + '\n'

        sys.stdout.write(modified_content)

if __name__ == "__main__":
    main()
