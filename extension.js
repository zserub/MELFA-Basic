'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const cp = require("child_process");
const stream = require('stream');
const os = require("os");
var channel = null;
const fullRange = doc => doc.validateRange(new vscode.Range(0, 0, Number.MAX_VALUE, Number.MAX_VALUE));
const MODE = { language: 'melfa-basic' };

class MelfaFormatter {
    constructor() {
        this.machine_os = os.platform();
        console.log(this.machine_os);
        this.py = '';
        if (this.machine_os == 'win32') {
            this.py = 'python ';
        }
        this.formatter = '"'+ __dirname + '/formatter/formatter.py"';
    }

    formatDocument(document, range) {
        return new Promise((resolve, reject) => {
            this.format(document, range).then((res) => {
                return resolve(res);
            });

        });
    }

    format(document, range) {
        return new Promise((resolve, reject) => {
            let indentwidth = " --indentWidth=" + vscode.workspace.getConfiguration('formatter')['indentwidth'];
            let filename = ' -';
            var p = cp.exec(this.py + " " + this.formatter + " " + filename + indentwidth, (err, stdout, stderr) => {
                if (stdout != '') {
                    let toreplace = document.validateRange(new vscode.Range(range.start.line, 0, range.end.line + 1, 0));
                    var edit = [vscode.TextEdit.replace(toreplace, stdout)];
                    if (stderr != '') {
                        vscode.window.showWarningMessage('formatting warning:\n'+stderr);
                    }
                    return resolve(edit);
                }
                vscode.window.showErrorMessage('formatting failed:\n'+stderr);
                return resolve(null);
            });
            var stdinStream = new stream.Readable();
            stdinStream.push(document.getText());
            stdinStream.push(null);
            stdinStream.pipe(p.stdin);
        });
    }
}

exports.MelfaFormatter = MelfaFormatter;

class MelfaDocumentRangeFormatter {
    constructor() {
        this.formatter = new MelfaFormatter();
    }
    provideDocumentFormattingEdits(document, options, token) {
        return this.formatter.formatDocument(document, fullRange(document));
    }
    provideDocumentRangeFormattingEdits(document, range, options, token) {
        return this.formatter.formatDocument(document, range);
    }
}

function activate(context) {
    channel = vscode.window.createOutputChannel('formatter');
    const formatter = new MelfaDocumentRangeFormatter();
    context.subscriptions.push(vscode.languages.registerDocumentFormattingEditProvider(MODE, formatter));
    context.subscriptions.push(vscode.languages.registerDocumentRangeFormattingEditProvider(MODE, formatter));
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() {
}
exports.deactivate = deactivate;