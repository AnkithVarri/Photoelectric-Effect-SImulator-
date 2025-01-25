from tkinter import *
from tkinter import ttk
import random


import random
class CreateElectron:
    def __init__(self, root, subcanvas1, subcanvas2, colour, moving_electrons, get_colour_method):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.subcanvas2 = subcanvas2
        self.moving_electrons = moving_electrons
        self.releasecoords = (509, 550)
        self.get_colour_method = get_colour_method
        self.time = 50  # Default time interval for moving photons (controlled by slider)
        self.play_event = False  # Electrons are initially frozen
        self.photons_created = False  # Ensure photons aren't created multiple times unnecessarily

    def create_photon(self):
        """Create a new photon (circle) only when play starts."""
        if not self.play_event:  # Don't create new photons if paused
            return
        
        # Only create photons once when play starts (prevents flooding)
        if self.photons_created:  
            return  # Don't create more photons if they're already created

        # Create a photon at a random starting position
        radius = 1.5
        x1 = random.randint(self.releasecoords[0], self.releasecoords[1])  # Random x position for photon
        y1 = x1 - 410  # y1 is offset from x1 to start in the middle of the canvas
        x2 = x1 + radius * 2
        y2 = y1 + radius * 2

        # Get the color for the photon
        colour = self.get_colour_method()

        # Draw the circle and store its ID
        circle_id = self.subcanvas1.create_oval(x1, y1, x2, y2, fill=colour, outline="")
        self.moving_electrons.append(circle_id)

        # Mark that photons have been created
        self.photons_created = True

    def move_photons(self):
        """Move each circle diagonally in a fixed path (no random movement), based on time."""
        if self.play_event:
            # Create photons continuously as long as play is active
            self.create_photon()

            # Move each existing photon diagonally (fixed path)
            for circle_id in self.moving_electrons[:]:
                self.subcanvas1.move(circle_id, -15, 10)  # Fixed diagonal movement (x: -15, y: +10)

                # Check if the circle has moved out of bounds (left side of the canvas)
                x1, y1, x2, y2 = self.subcanvas1.coords(circle_id)
                if x1 < 230:
                    self.subcanvas1.delete(circle_id)  # Remove the circle from the canvas
                    self.moving_electrons.remove(circle_id)  # Remove the circle from the list

            # Schedule the next movement
            self.subcanvas1.after(self.time, self.move_photons)

    def toggle_play(self):
        """Toggle the play state of the animation (start/stop electrons)."""
        self.play_event = not self.play_event
        if self.play_event:
            print("Electrons moving!")
            self.move_photons()
        else:
            print("Electrons frozen!")

    def update_time(self, value):
        """Update the speed of the animation based on the intensity slider."""
        self.time = max(1, 200 - int(value))  # Adj
class CreateSpectrum:
    def __init__(self, root, subcanvas1, subcanvas2, moving_circles):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.subcanvas2 = subcanvas2
        self.moving_circles = moving_circles
        self.time = 50

        # Wavelength and intensity labels
        self.wavelength_label = Label(self.subcanvas1, text="Wavelength: 380 nm", bg="white", width=20)
        self.wavelength_label.place(x=835, y=185)
        self.intensity_label = Label(self.subcanvas1, text="Intensity: 0%", bg="white", width=20)
        self.intensity_label.place(x=830, y=12)

        # Intensity slider (to control the photon movement speed)
        self.intensity_slider = Scale(self.subcanvas1, from_=1, to=100, length=300, orient="horizontal", command=self.update_intensity_label)
        self.intensity_slider.place(x=750, y=30)
        self.intensity_slider.set(50)

        # Wavelength slider (for visual changes)
        self.wavelength_slider = Scale(self.subcanvas1, from_=380, to=750, length=300, orient="horizontal", command=self.update_wavelength_label)
        self.wavelength_slider.place(x=750, y=135)

        # Create the electron (photon) manager
        self.c1 = CreateElectron(root, subcanvas1, subcanvas2, "blue", self.moving_circles, self.get_colour) 

    def get_colour(self, value=None):
        """Determine the colour based on wavelength."""
        if value is None:
            value = self.wavelength_slider.get()

        if value < 380:
            value = 380
        elif value > 750:
            value = 750

        r, g, b = 0, 0, 0

        if value <= 380:  # Infrared
            r = 115
            g = 115
            b = 115
        elif 380 < value < 451:  # purple
            r = 255 * (450 - value) / 70
            g = 0
            b = 255
        elif 450 < value < 501:  # blue
            r = 0
            g = 255 * (value - 450) / 50
            b = 255
        elif 500 < value < 571:  # green
            r = 0
            g = 255
            b = 255 * (570 - value) / 70
        elif 570 < value < 601:  # yellow
            r = 255 * (value - 570) / 30
            g = 255
            b = 0
        elif 600 < value < 750:  # orange and red
            r = 255
            g = 255 * (750 - value) / 150
            b = 0
        elif value >= 750:  # Ultraviolet
            r = 45
            g = 45
            b = 45

        r = max(0, min(255, int(r)))
        g = max(0, min(255, int(g)))
        b = max(0, min(255, int(b)))

        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"  # Return a HEX color code

    def update_intensity_label(self, value):
        """Update the intensity label and photon speed."""
        self.time = max(1, int(value))  # Update the internal time
        self.intensity_label.config(text=f"Intensity: {value}%")
        self.c1.update_time(value)  # Update the photon speed

    def update_wavelength_label(self, value):
        """Update the wavelength label and color based on the slider value."""
        wavelength = int(value)  # Convert slider value to an integer wavelength
        color = self.get_colour(wavelength)
        self.wavelength_label.config(text=f"Wavelength: {wavelength} nm", bg=color)

    def run(self):
        """Start creating photons and moving them."""
        self.c1.create_photon()
        self.root.after(self.time, self.run)  # Loop the animation

class Visualise(CreateSpectrum):
    def __init__(self, root, subcanvas1, subcanvas2, moving_circles):
        super().__init__(root, subcanvas1, subcanvas2, moving_circles)

        # Create play button (oval shape)
        self.play = subcanvas1.create_oval(420, 695, 445, 720, fill="lightblue", tags="play")
        self.step = subcanvas1.create_oval(460, 695, 485, 720, fill="lightblue", tags="step")

        # Bind play button to pause/play toggle
        self.subcanvas1.tag_bind("play", "<Button-1>", self.pause_play_on_click)
        self.subcanvas1.tag_bind("step", "<Button-1>", self.step_on_click)

    def pause_play_on_click(self, event):
        """Toggle the electron animation."""
        self.c1.toggle_play()  # Toggle the movement state
        if self.c1.play_event:  # If the electrons are moving, start the animation loop
            self.run()
        self.c1.move_photons()

    def step_on_click(self, event):
        """Manually move the electrons by one step."""
        self.c1.create_photon()

def main():
    root = Tk()
    subcanvas1 = Canvas(root, width=500, height=800, bg="white")
    subcanvas1.pack()
    subcanvas2 = Canvas(root, width=500, height=800, bg="white")

    moving_circles = []  # List to track moving circles (electrons)

    # Create the Visualise instance, passing in the canvas and other necessary elements
    visualise = Visualise(root, subcanvas1, subcanvas2, moving_circles)

    root.mainloop()

if __name__ == "__main__":
    main()