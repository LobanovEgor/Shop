from builtins import *
from windows import MainWindow


if __name__ == '__main__':
    mainWindow = MainWindow()

    mainWindow.title('В магазине')
    mainWindow.geometry('1280x720')

    for c in range(5):
        mainWindow.columnconfigure(index=c, weight=1)
    for r in range(3):
        mainWindow.rowconfigure(index=r, weight=1)

    mainWindow.mainloop()
    mainWindow.payment()