# MELFA-Basic language extension

Mitsubishi robot programming language support for VS Code

## Features

- Syntax highlight
- Snippets
- Custom color theme
- Formatter (additional extension required)


## Requirements

[Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters)

## Setup and usage

Clone the repo manually to `C:\Users\%userprofile%\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\`

### Activate theme

`Ctrl + Shift + P` -> `Preferences: Color Theme` -> `Dark Theme for MELFA-Basic`

### Activate formatter

Install [Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters)

Open settings.json *(Ctrl + Shift + P, delete >, type settings.json)*

Paste:
```
"customLocalFormatters.formatters": [
        {
            "command": "\"%localappdata%\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\MELFA-Basic\\formatter\\formatter.exe\"",
            "languages": ["prg"]
        }
    ],
```
First time for formatting you have to choose customLocalFormatters

**Enjoy!**

> Please open an issue if you found bugs or suggest features.
