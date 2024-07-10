import re
import sys


class CodeFormatter:
    keywords = [
        'Accel', 'Act', 'And', 'Break', 'Case', 'Clear', 'Cnt', 'ColChk', 'Cmp', 'Dly', 'Def',
        'Default', 'Else', 'ElseIf', 'End', 'EndIf', 'EndSelect', 'Error', 'Exit', 'FEnd',
        'Fine', 'For', 'GoSub', 'GoTo', 'Go', 'HClose', 'HOpen', 'Hlt', 'If', 'JOvrd', 'JRC',
        'Jnt', 'Load', 'Mov', 'Mvs', 'Mvr', 'Mvr2', 'Mvr3', 'Mvrc', 'Mvra', 'Not', 'Ovrd', 'Or',
        'Pos', 'Prec', 'Priority', 'Reset', 'ResetErr', 'Return', 'Run', 'Select', 'Servo', 'Skip',
        'Spd', 'Spl', 'Stp', 'Stop', 'Switch', 'Then', 'Tool', 'Torq', 'Tune', 'WEnd', 'Wait', 'While',
        'Wth', 'WthIf', 'X', 'XClr', 'XLoad', 'XRst', 'XRun', 'XStp', 'Xor', 'Y', 'Z', 'Pos', 'Jnt', 'Inte',
        'Float', 'Call', 'Function', 'Def', 'On', 'Off'
    ]

    start_patterns = re.compile(
        r'(^\*\w+|Select|Case|Default|If|For|While)(\b)')
    end_patterns = r"(\s*)(End(If)?\b|Break\b)"
    # label=re.compile(r'(^\*\w+')
    # additional_endPatterns = r"'---.*"
    # spaced_patterns = re.compile(r'(\s*)(=|Or|And|<(?!>)|(?<!<)>)(\s*)')
    spaced_patterns = ['<>', 'Or', 'And']
    unspacing_patterns = ['=', '<', '>']

    def __init__(self, input_content):
        self.content = input_content
        self.cleancode = ""
        self.insert_tab_number = 0
        self.bool_DeleteNumbers = True

    def delete_line_numbers(self, line):
        modified_content = re.sub(r'^\d*', '', line)
        # print('line numbers removed')
        return modified_content

    def delete_single_quotes(self, line):
        stripped_line = line.strip()
        if stripped_line == "'":
            stripped_line = re.sub("'", '', stripped_line)
        # print('quotes removed in empty lines')
        return stripped_line

    def delete_whitespaces(self, line):
        modified_line = re.sub(r'^\s*', '', line)
        modified_line = re.sub(r'\s$', '', modified_line)
        # print('whitespaces removed')
        return modified_line

    def indent_content(self, line):

        end_patterns = re.compile(
            self.end_patterns)# + '|' + self.additional_endPatterns)

        if re.match(r"^\bElse\b", line):  # Else
            modified_line = '\t' * (self.insert_tab_number - 1) + line
        else:
            modified_line = '\t' * self.insert_tab_number + line
            
        if re.match(r"^\*\w+", line):    # Label
            self.insert_tab_number = 0
            modified_line = line

        if re.match(end_patterns, line) and self.insert_tab_number > 0:  # End pattern check
            self.insert_tab_number -= 1
        if re.match(self.start_patterns, line):  # Start pattern check
            self.insert_tab_number += 1
            


        # One line 'if-then' handling
        if not line.startswith("'") and re.search(r'\bThen\s(?=\w+)', line):
            self.insert_tab_number -= 1

        # print('indents added')
        return modified_line

    def add_spaces(self, line):
        for pattern in self.unspacing_patterns:
            line = re.sub(r'\s*{}\s*'.format(re.escape(pattern)), '{}'.format(pattern), line)
        for pattern in self.spaced_patterns:
            line = re.sub(r'\s*{}\s*'.format(re.escape(pattern)), ' {} '.format(pattern), line)
        # line = re.sub(r'\b=\b', ' = ', line)
        line = re.sub(r'(=<)|(<=)', ' <= ', line)
        line = re.sub(r'(=>)|(>=)', ' >= ', line)
        line = re.sub(r'(\s*)<(?!>|=)(\s*)', ' < ', line)
        line = re.sub(r'(?<!<)>(?!\=)', ' > ', line)
        line = re.sub(r'(?<![<>])=', ' = ', line)
            
        return line
    
    def check_keywords(self, line):
        for keyword in self.keywords:
            line = re.sub(r'\b{}\s+'.format(re.escape(keyword)), '{} '.format(keyword), line, flags=re.IGNORECASE)
        return line

    def process_code(self, line):
        modified_line = self.delete_line_numbers(line)
        modified_line = self.delete_single_quotes(modified_line)
        modified_line = self.delete_whitespaces(modified_line)
        modified_line = self.indent_content(modified_line)
        if not modified_line.startswith("'"):
            modified_line = self.add_spaces(modified_line)
        modified_line = self.check_keywords(modified_line)
        return modified_line


def main():

    formatter = CodeFormatter(sys.stdin.read())

    if formatter.content is not None:

        for line in formatter.content.split('\n'):

            modified_line = formatter.process_code(line)

            formatter.cleancode += modified_line + '\n'

        sys.stdout.write(formatter.cleancode)


if __name__ == "__main__":
    main()
