from tkinter import *
from tkinter import ttk
import math
import random
import matplotlib.pyplot as plt

import random
import tkinter as tk
from tkinter import Scale, Label

class CreateParticle:
    def __init__(self, root, subcanvas1, trigger_callback=None,get_colour_method=None):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.moving_photons = []
        self.releasecoords = (509, 550)
        self.get_colour_method = get_colour_method
        self.target_shape = self.subcanvas1.create_rectangle(777, 280, 782, 480, fill="grey", outline="black", width=2)
        self.trigger_callback = trigger_callback
        self.coords = (230, 280, 235, 480)
        self.running = False
        self.time = 1000

    def create_photon(self, colour =" #737373"):
        radius = 2.5
        x1 = random.randint(self.releasecoords[0], self.releasecoords[1])
        y1 = x1 - 410
        x2 = x1 + radius * 2
        y2 = y1 + radius * 2
        circle_id = self.subcanvas1.create_oval(x1, y1, x2, y2, fill=colour, outline="")
        self.moving_photons.append(circle_id)

    def move_photons(self):
        if not self.running:
            return
        for circle_id in self.moving_photons[:]:
            self.move_pattern(circle_id)
            coords = self.subcanvas1.coords(circle_id)
            if coords:
                x1, y1, x2, y2 = coords
                if self.coords:
                    if (x1 < self.coords[2] and x2 > self.coords[0] and y1 < self.coords[3] and y2 > self.coords[1]):
                        if self.trigger_callback:
                            self.trigger_callback((x1, y1))
                if x1 < 225:
                    self.subcanvas1.delete(circle_id)
                    self.moving_photons.remove(circle_id)
        self.subcanvas1.after(50, self.move_photons)

    def move_pattern(self, circle_id):
        self.subcanvas1.move(circle_id, -15, 10)

    def start(self):
            colour = self.get_colour_method()
            self.create_photon(colour)
            self.move_photons()
            self.subcanvas1.after(50, self.continuous_photon_creation)

    def continuous_photon_creation(self):
            colour = self.get_colour_method()
            self.create_photon(colour)
            new_time = int(1000 / self.time)
            self.after_id = self.subcanvas1.after(new_time, self.continuous_photon_creation)

    def update_time(self, value):
        self.time = max(1, int(value))

    def stop(self):
        self.running = False
