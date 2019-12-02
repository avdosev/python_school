from tkinter import *

class MainWindow:
    def __init__(self, root):
        self.root = root

        self.initUi()

    def initUi(self):
        hello_label = Label(self.root, text="Hello, world!", font="Times 40")  
        hello_label.pack()

        # Привязка обработчиков - к событию и виджету:
        #виджет.bind(событие, обработчик)
        hello_label.bind('<Button-1>', self.handler1)
        hello_label.bind('<Button-3>', self.handler2)

    def handler1(self, event):
        print('Hello World! x=', event.x, 'y=', event.y)


    def handler2(self, event):
        exit()
