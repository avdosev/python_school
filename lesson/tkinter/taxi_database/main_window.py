from tkinter import *
from taxi import *


class MainWindow:
    def __init__(self, root):
        self.root = root

        self.dataFrame = Frame(root, bd=5)
        self.commandFrame = Frame(root, bd=5)

        self.saveButton = Button(self.commandFrame, text=u'Сохранить', command=self.save)
        self.cancelButton = Button(self.commandFrame, text=u'Отмена', command=self.cancel)
        self.firstRecordButton = Button(self.commandFrame, text=u'Первая запись', command=self.firstRecord)
        self.secondRecordButton = Button(self.commandFrame, text=u'Вторая запись', command=self.secondRecord)

        widgets = [self.dataFrame, self.commandFrame]
        for widget in widgets:
            widget.pack()

        commandButtons = [self.saveButton, self.cancelButton, self.firstRecordButton, self.secondRecordButton]
        for widget in commandButtons:
            widget.pack(side='left')

        self.routInput = Entry(self.dataFrame).grid(row=0, column=1)
        self.stationBegin = Entry(self.dataFrame).grid(row=1, column=1)
        self.stationEnd = Entry(self.dataFrame).grid(row=2, column=1)

        self.costInput = IntVar()
        self.costInput = Spinbox(self.dataFrame, from_=0, to=1000).grid(row=3, column=1)
        self.dateInput = Entry(self.dataFrame).grid(row=4, column=1)

        Label(self.dataFrame, text="Номер маршрута").grid(row=0, column=0)
        Label(self.dataFrame, text="Начальная станция").grid(row=1, column=0)
        Label(self.dataFrame, text="Конечная станция").grid(row=2, column=0)
        Label(self.dataFrame, text="Цена поездки").grid(row=3, column=0)
        Label(self.dataFrame, text="Дата поездки").grid(row=4, column=0)


    def save(self):
        pass

    def cancel(self):
        pass

    def firstRecord(self):
        pass

    def secondRecord(self):
        pass
