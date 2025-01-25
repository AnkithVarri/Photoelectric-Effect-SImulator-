from tkinter import *
from tkinter import ttk
import random
class CreateParticle:
    def __init__(self,root,subcanvas1, subcanvas2,  get_colour_method, target_shape = None, trigger_callback = None):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.moving_photons = []
        self.releasecoords = (509,550)
        self.get_colour_method = get_colour_method
        self.time = 1000

        self.play_event = True
        self.running = False        
        self.target_shape = target_shape

        self.trigger_callback = trigger_callback
        self.coords = (230,280,235,480)

    def create_photon(self):
        if not self.play_event:  # Only create new photons if play_event is True
            return  # Don't create a new photon if paused
        radius = 2.5 
        x1 = random.randint(self.releasecoords[0], self.releasecoords[1])  # Start just outside the left edge of the canvas
        y1 = x1 - 410
        x2 = x1 + radius * 2
        y2 = y1 + radius * 2
        coords = (y1,y2)

        colour = self.get_colour_method()

        # Draw the circle and return its ID
        circle_id = self.subcanvas1.create_oval(x1, y1, x2, y2, fill=colour, outline="")
        self.moving_photons.append(circle_id)
        return coords
    

    #Intensity links to the number of particles produced per second


    def move_photons(self):
        if not self.running:
            return
        
        if self.play_event:
            for circle_id in self.moving_photons[:]:  # Iterate over a copy of the list
                self.move_pattern(circle_id)  

                coords = self.subcanvas1.coords(circle_id)  # Get the coordinates
                if coords:  # Ensure the object exists
                    x1, y1, x2, y2 = coords
                    # Check for collision with the target shape
                    if self.target_shape and self.coords:
                        if (x1 < self.coords[2] and x2 > self.coords[0] and y1 < self.coords[3] and y2 > self.coords[1]):
                            if self.trigger_callback:
                                self.trigger_callback((x1, y1)) # Trigger the second particle motion
                    
                    # Check if the particle goes out of bounds
                    if x1 < 225:
                        self.subcanvas1.delete(circle_id)  
                        self.moving_photons.remove(circle_id)  
            self.subcanvas1.after(50, self.move_photons) # Schedule the next movement



    def move_pattern(self,circle_id):
       self. subcanvas1.move(circle_id, -15, 10)


    def start(self):
        for i in range(50):
            print("done")
        if self.running == True:
            self.create_photon()  # Create an initial particle
            self.move_photons()  # Start moving particles
            self.subcanvas1.after(50, self.continuous_particle_creation)

    def continuous_particle_creation(self):
        """Continuously create new particles while running."""
        print("say less")
        if self.running:
            self.create_photon()
            new_time = int(1000 /self.time)
            self.subcanvas1.after(new_time, self.continuous_particle_creation)  #the INTENSITY SLIDER BIT


    def update_time(self, value):
        self.time = max(1, int(value))  # Ensure time is at least 1 ms

    def update_colour(self, colour):
        self.colour = colour # Changs colour to the colour chosen by the slider

