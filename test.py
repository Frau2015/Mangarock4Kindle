import os 
import Tkinter as tk
from Tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.fileName = filedialog.askopenfilename()
root.deiconify()
k = input("sdf")
print(root.fileName)