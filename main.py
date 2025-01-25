from tkinter import *
from tkinter import ttk
import os
import random
import numpy as np

from subproblem1 import *
from subproblem2 import *
from subproblem3 import *
from subproblem4 import *
from subproblem5 import *



def main():
    root = Tk() # List to keep track of moving circles

    subcanvas1 = Canvas(root, bg="grey93")
    subcanvas1.pack()           
    subcanvas2 = Canvas(root, bg="grey93")

    v1 = Visualise(root,subcanvas1, subcanvas2)
    v1() # visualise the whole circuitry and slideX r

    l1 = LinkedParticles(root,subcanvas1,subcanvas2)
    
    n1 = Notes(root, subcanvas1,subcanvas2)
    n1()

    
if __name__ == "__main__":
    main()





















'''
def main():
    root = Tk()
    moving_circles = []  # List to keep track of moving circles

    subcanvas1 = Canvas(root, bg="grey93")
    subcanvas1.pack()
    subcanvas2 = Canvas(root, bg="grey93")
    c1 = CreateElectron(root,subcanvas1,"black", moving_circles) 
    c1.()  # Start creating circles
    c1.move_photons()     # Start moving circles
    v1 = Visualise(root,subcanvas1, subcanvas2)
    v1()
    root.mainloop()

    

if __name__ == "__main__":
    main()
'''    