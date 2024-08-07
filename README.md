# MELFA-Basic language extension

**Mitsubishi robot programming language support for VS Code**

*Open melfa codes in VS Code, write then jump to RT Toolbox for upload.*

[![twitter](https://img.shields.io/badge/follow-zserub_-blue?style=flat&logo=Twitter)](https://twitter.com/zserub)
[![tea](https://img.shields.io/badge/buy%20me-%E2%98%95%EF%B8%8F%20tea-yellow.svg)](https://ko-fi.com/metaphysix)

*Do you want this syntax highlight online? Check out my [MELFA for highlight.js repo](https://github.com/zserub/MELFA-highlight.js)*

## Features

- **Syntax highlight**
- **Snippets**
- **Custom color theme**
- **2 type formatters** *(additional extension required)*

## Workflow

Create a new workspace in RT Toolbox, then open the prg file with VS Code

**or** Select an existing program for modification.

Format code to get rid of the line numbers.

Write your program. After finishing your program, run the `deformer` to apply back the line numbers (Toolbox will automatically update the ones).

Open the file in RT Toolbox, then upload to the robot.

<br>

![Showcase](etc/Screenshot.png)


### Requirements

- Python (or you can use formatter.exe instead)
- [Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters) (for running the 'deformer' in VS Code)

## Setup

**Install from marketplace**

or

#### *Manual installation:*

*Clone the repo to `C:\Users\%userprofile%\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\`*

### Activate theme

`Ctrl + Shift + P` **-->** `Preferences: Color Theme` **-->** `Dark Theme for MELFA-Basic`



## Setup 'deformer'

Install [Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters)

Open settings.json *([Ctrl + , ] --> custom local formatters --> `edit in settings.json`)*

Paste:
```
"customLocalFormatters.formatters": [
        {
            "command":"python \"%localappdata%\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\MELFA-Basic\\formatter\\deformerV2.py\"",
            "languages": ["melfa-basic"]
        }
    ],
```
**Deformer usage:**

`Ctrl + Shift + P` **-->** `Format document with...` **-->** `Custom Local Formatters`

## How formatter works

- Removes the line numbers and `'` in empty lines
- Adjust spaces
- Corrects uppercase in keywords

Indent with the following logic:
- Standard indentation rules for conditions and loops
- Reset indentation after new label

### Deformer

Formats the code for RT Toolbox.
- Insert line numbers (Toolbox will readjust)
- Comment empty lines so Toolbox won't delete them

<br>

> Please open an issue if you found bugs or suggest features.
