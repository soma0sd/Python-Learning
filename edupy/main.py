# -*- coding: utf-8 -*-
import tkinter as tk
import os
import subprocess
from pygments import lex
from pygments.lexers import Python3Lexer as PythonLexer


class cApplication:
    def __init__(self):
        self.cnf = {'font': ('Consolas', 20)}
        self.root = tk.Tk()
        self.root.title('python class education tool')
        self.root.state('zoomed')
        self.root.update()

        self.menu = cMenuFrame(self.root, height=40, bg="#000")
        self.menu.AttachApp(self)

        self.view = cViewFrame(self.root, bg="#333")
        self.view.AttachApp(self)

    def mainloop(self):
        self.menu.Layout()
        self.view.Layout()
        self.root.mainloop()


class cMenuFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.app = None

    def AttachApp(self, app):
        self.app = app

    def Layout(self):
        _ = tk.Button(self, relief='groove', bg='#000', fg='#FFF')
        _.config(font=12, text='Open File', command=self._cmd_open_file)
        _.pack(side='left')
        _ = tk.Button(self, relief='groove', bg='#000', fg='#FFF')
        _.config(font=12, text='Open Git', command=self._cmd_open_git)
        _.pack(side='left')
        _ = tk.Button(self, relief='groove', bg='#000', fg='#FFF')
        _.config(font=12, text='Run Source', command=self._cmd_run)
        _.pack(side='left')
        self.pack(fill='x')

    def _cmd_open_file(self):
        from tkinter import filedialog
        tbox = self.app.view.t_raw
        path = os.path.dirname(__file__)
        filestr = filedialog.askopenfilename(initialdir=path)
        tbox.delete('1.0', 'end')
        with open(filestr, 'r', encoding='utf8') as f:
            for line in f.readlines():
                tbox.insert('end', line)
        tbox.LineNumberUpdate()
        tbox.SyntexHighlight()

    def _cmd_open_git(self):
        import requests
        root = tk.Toplevel(self.app.root)
        root.overrideredirect(True)
        tbox = self.app.view.t_raw
        label = tk.Label(root, text='Enter git url', font=('Consolas', 16))
        label.grid(row=0, column=0, columnspan=2)
        var = tk.StringVar()
        url = tk.Entry(root, textvariable=var)
        url.grid(row=1, column=0)

        def cmd():
            tbox.delete('1.0', 'end')
            get = requests.get(var.get())
            tbox.insert('end', get.text)
            tbox.LineNumberUpdate()
            tbox.LineNumberUpdate()
            tbox.SyntexHighlight()
            root.destroy()

        _b = tk.Button(root, text='Ok', command=cmd)
        _b.grid(row=1, column=1)
        root.geometry('200x150+{}+{}'.format(50, 50))

    def _cmd_run(self):
        txt = self.app.view.t_raw.get(1.0, tk.END)
        with open('test.py', 'w', encoding="utf-8") as f:
            f.write(txt)
        cmdstr = 'ipython {}/test.py'.format(os.path.dirname(__file__))
        subprocess.Popen(cmdstr)
        return None


class cViewFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.app = None

    def AttachApp(self, app):
        self.app = app

    def Layout(self):
        self.t_raw = cTextObject(self)
        self.t_raw.AttachApp(self.app)
        self.t_raw.Layout()
        self.pack(fill="both", expand=True)


class cTextObject(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.app = None
        self.frame = args[0]

    def AttachApp(self, app):
        self.app = app
        self.configure(font=app.cnf['font'])
        self.t_syn1 = ['import']

    def Layout(self):
        scroll = tk.Scrollbar(self, orient="vertical")
        scroll.configure(command=self.yview)
        scroll.pack(side='right', fill='y')
        self.line_num = tk.Canvas(self.frame, width=45)
        self.LineNumberUpdate()
        self.bind("<<Change>>", self.LineNumberUpdate)
        self.bind("<Configure>", self.LineNumberUpdate)
        self.bind("<Key>", self.LineNumberUpdate)
        self.bind("<MouseWheel>", self.LineNumberUpdate)
        self.bind("<<Change>>", self.SyntexHighlight)
        self.bind("<KeyRelease>", self.SyntexHighlight)
        self.line_num.pack(side="left", fill="y")
        self.configure(yscrollcommand=scroll.set)
        self.pack(fill="both", expand=True)

    def LineNumberUpdate(self, event=None):
        i = self.index(("@0,0"))
        self.line_num.delete("all")
        while True:
            dline = self.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            num = str(i).split(".")[0]
            self.line_num.create_text(2, y, anchor="nw",
                                      text=num, font=self.app.cnf['font'])
            i = self.index("%s+1line" % i)

    def SyntexHighlight(self, event=None):
        from tkinter.font import Font
        for tag in self.tag_names():
            self.tag_delete(tag)
        self.mark_set("range_start", "1.0")
        data = self._get_value()
        self.tag_configure("Token.Comment", foreground="#F00")
        bolder = Font(family=self.app.cnf['font'][0])
        bolder.config(size=self.app.cnf['font'][1]-2)
        bolder.config(weight="bold")
        for token, content in lex(data, PythonLexer()):
            self.mark_set("range_end", "range_start + %dc" % len(content))
            self.tag_add(str(token), "range_start", "range_end")
            self.mark_set("range_start", "range_end")
        self.tag_config("Token.Comment.Single", foreground="#F00")
        self.tag_config("Token.Literal.String.Doc", foreground="#F00")
        for tag in self.tag_names():
            if 'Token.Keyword' == tag:
                self.tag_config(tag, foreground="#008", font=bolder)
            elif 'Token.Keyword.Namespace' == tag:
                self.tag_config(tag, foreground="#00F", font=bolder)
            elif 'Token.Name.Class' in tag:
                self.tag_config(tag, foreground="#F30", background='#AFA')
            elif 'Token.Name.Function' in tag:
                self.tag_config(tag, foreground="#A3A", background='#FFA')
            elif 'Token.Literal' in tag:
                self.tag_config(tag, foreground="#6A0")
            elif 'Token.Operator' in tag:
                self.tag_config(tag, foreground="#A3A")
        print(self.tag_names())

    def _get_value(self):
        return self.get(1.0, 'end')

cApplication().mainloop()
