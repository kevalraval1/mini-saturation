import xlsxwriter
import tkinter as tk
from tkinter import filedialog
import csv

window = tk.Tk()
window.title("Saturation Program")

baseList = ["G", "A", "T", "C"]

def selectResultDir():
    file_path = filedialog.askdirectory()
    setResultPATH(file_path)
    if(file_path!=''):
        label = tk.Label(frame, text=file_path, bg = 'gray')
        spaceText.window_create("end", window=label)
        spaceText.insert('end', '\n')

def setResultPATH(directory):
    global resultDir
    resultDir = directory

def main():
    with open(resultDir + "/" + name.get() + ".csv", mode = "w") as f:
        seq = seqEntry.get()

        count = 0
        column = 1
        for current, base in enumerate(seq):
            if current == count and count != 0 and count != len(seq) - 1:
                for x in baseList:
                    if x != base:
                        result = seq[:count] + x + seq[count + 1:]
                        f.write(result)
            if count == 0:
                for x in baseList:
                    if x != base:
                        result = x + seq[count + 1:]
                        f.write(result)
            if count == len(seq) - 1:
                for x in baseList:
                    if x != base:
                        result = seq[:count] + x
                        f.write(result)
            count += 1
    f.close()
    window.quit()

canvas = tk.Canvas(window, height = 200, width = 600)
canvas.pack()

frame = tk.Frame(window,relief='groove')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

welcome = tk.Label(frame, text = "Welcome to Saturation Program", fg = "Black")
welcome.pack(side = "top")

seqEntry = tk.Entry(frame, width=50)
seqEntry.pack(side='top')
seqEntry.insert(0,'Please enter sequence for saturation')

name = tk.Entry(frame, width=50)
name.pack(side='top')
name.insert(0,'Please enter name for file')

openDir = tk.Button(window, text='Open Result Directory', padx=10,pady=5,fg='black',bg='gray', command=selectResultDir)
openDir.pack()

sb = tk.Scrollbar(frame,orient='vertical')
spaceText = tk.Text(frame,width=40,height=20, yscrollcommand=sb.set, borderwidth=0)
sb.config(command=spaceText.yview)
sb.pack(side='right', fill='y')
spaceText.pack(side='right',fill='both' ,expand=True)

enterButton = tk.Button(window, text = "Start", padx = 10, pady = 5, fg = "Black", bg = "gray", command = main)
enterButton.pack()

window.mainloop()
