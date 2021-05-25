import tkinter as tk
from ctypes import *
from ctypes.wintypes import POINT
from tkinter import *

mainWindow = tk.Tk()
mainWindow.title('Informed and Uninformed Searches')
canvas = tk.Canvas(mainWindow, height=725, width=725)
canvas.pack()
button_exit = Button(mainWindow, text="Exit", command=mainWindow.quit)
button_exit.pack()

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))


def create_node(event):
    global r
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    r = canvas.create_oval( pt.x -30, pt.y-30, pt.x+30, pt.y+30,fill="yellow", outline="black")

class Graph:
    def __init__(self, v):
        self.m_V = v
        v = r
        self.m_adj = [[] for i in range(v)]

    def addEdge(self, u, v):
        self.m_adj[u].append(v)



def create_line(event):
    global edge
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    edge = canvas.create_line( pt.x -30, pt.y-30, pt.x+30, pt.y+30, fill='red', width=5)


mainWindow.bind("<Button-1>", create_node)
mainWindow.bind("<Button-3>", create_line)
mainWindow.mainloop()


