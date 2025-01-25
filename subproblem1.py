from tkinter import *
from tkinter import ttk

import math

from subproblem1 import *
from subproblem2 import *
from subproblem3 import *
from subproblem4 import *
from subproblem5 import *
import time

#LEARNT ABOUT CORRECT INHERITANCE DIAGRAM
# 1. Move the sliders and Labels to the ATTRIBUTE SECTION of the CreateSpectrum class
# 2. Create update_timemethod in CreateElectron class, and use that to UPDATE THE TIME
# 3. Add a new attribute to CreateElectron class, Get_colour, SO THAT ELECTRONS CAN DYNAMICALLY CHANGE COLOUR 
# 4. Colour can successfully be changed
# 5. Pause Play Button Works, By updating the pase_play function for the button to work
# 6. Added Ammeter, which should change depending on Metal work function/Energy Produced, etc...
# 7. Added Battery slider (with 0.1 increments)
# 7. Added Metal options
# 8. Created the work function and Kinetic_Energy function
# 9. Made and tested the electron motion inside the tube
# 10. Programmed the electron speed to change depending on incident Energy/Work function and VOLTAGE OF BATTERY
# 11. 
# 12. 
# 13. 





class CreateSpectrum:
    def __init__(self, root, subcanvas1, subcanvas2):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.subcanvas2 = subcanvas2

        self.time = 50
        self.volt = 0
        self.wavelength = 380
        
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

        battery_slider = Scale(self.subcanvas1, from_=-8.0, to=8.0, length=300, orient="horizontal", resolution=0.1, command=self.update_voltage)
        battery_slider.place(x=390, y=580)

        # Create the electron (photon) manager
        self.c1 = CreateParticle(root, subcanvas1, subcanvas2, self.get_colour)

    def get_rgb_from_position(self,position):
        #Determine the RGB values based on the normalized position 
        positioncalc = position * 255
        r,g,b = 0,0,0

        if position < 0 :
            r = None
            g = None
            b = None

        elif position< (70/370): # purple
            r = 255* (70-positioncalc)/70
            g = 0
            b = 255
        
        elif position < (120/370) and position > (70/370): # blue

            r = 0
            g = 255 * (positioncalc - 70)/50
            b = 255
        
        elif position < (190/370) and position > (120/370): # green
            r = 0
            g = 255
            b = 255* (190 - positioncalc)/70
        
        elif position < (220/370) and position > (190/370): # yellow
            r = 255* (positioncalc - 190)/30
            g = 255
            b = 0
        
        elif position < (370/370) and position > (220/370): # orange and red
            r = 255
            g = 255* (370 - positioncalc)/150
            b = 0
        
        elif position > (370/370):
            r = None
            g = None
            b = None

        if r == None or g == None or b == None:
            return r,g,b
        else:
            r =  int(r)
            g =  int(g)
            b =  int(b)
        

        return r,g,b

        

    def get_colour(self,value = None): # for outputting the associated wavelength to the chosen colour (done via the slider)
    #Converts the wavelength value to a colour

        if value is None:
            value = self.wavelength_slider.get()

        if value < 380:
            value = 380
        elif value > 750:
            value = 750

        r,g,b = 0,0,0

        if value <= 380: # Infrared
            r = 115
            g = 115
            b = 115

        elif value > 380 and value < 451: # purple
            r = 255* (450-value)/70
            g = 0
            b = 255

        elif value > 450 and value < 501: # blue
            r = 0
            g = 255* (value - 450)/50
            b = 255

        elif value > 500 and value < 571: # green
            r = 0
            g = 255
            b = 255* (570 - value)/70

        elif value > 570 and value < 601: # yellow
            r = 255* (value - 570)/30
            g = 255
            b = 0

        elif value > 600 and value < 750: # orange and red
            r = 255
            g = 255* (750 - value)/150
            b = 0

        elif value >= 750: #Ultraviolet
            r = 45
            g = 45
            b = 45

        r = max(0, min(255, int(r)))
        g = max(0, min(255, int(g)))
        b = max(0, min(255, int(b)))


        return f"#{int(r):02x}{int(g):02x}{int(b):02x}" # Return a HEX color code



    def update_intensity_label(self, value):
        self.time = max(1, int(value))  # Update the internal time
        self.intensity_label.config(text=f"Intensity: {value}%")
        self.c1.update_time(value)  # Update the photon speed

    
    def update_voltage(self, new_value):
        self.volt = float(new_value)  # Ensure the value is converted to a float
        #self.print_v()

    def return_voltage(self):
        return self.volt


    def return_wavelength(self):
        return self.wavelength

    def update_wavelength_label(self,value):                                                      
        wavelength = int(value)  # Convert slider value to an integer wavelength
        color = self.get_colour(wavelength)  
        self.wavelength_label.config( text=f"Wavelength: {wavelength} nm", bg=color ) # Retrieve the wavelength/intensity INFO from THESE VARIABLES
        self.wavelength = wavelength
        return self.wavelength
    

    

    def create_colour_spectrum(self, width, height):   #To create 1 line , representing each rgb combination of the light spectrum
        spectrum_start_x = 750  
        spectrum_width = 300    
        spectrum_top_y = 90    
        spectrum_height = 30    
        min_wavelength = 380    
        max_wavelength = 750   

        self.subcanvas1.create_rectangle(spectrum_start_x, spectrum_top_y, spectrum_start_x + spectrum_width, spectrum_top_y + spectrum_height, outline="black",  width=2)

        for i in range(spectrum_width):
            # Map pixel position to wavelength
            wavelength = min_wavelength + (i / spectrum_width) * (max_wavelength - min_wavelength)
            colour = self.get_colour(wavelength)
            self.subcanvas1.create_line(spectrum_start_x + i,spectrum_top_y, spectrum_start_x + i, spectrum_top_y + spectrum_height,fill=colour)



    def create_final_spectrum(self): # To assemble the whole colour spectrum
        enclosure_rectangle = self.subcanvas1.create_rectangle(700, 10, 1090, 220, outline="black", width=2)
        canvas_width = 300
        canvas_height = 40

        # Create the color spectrum
        self.create_colour_spectrum(canvas_width, canvas_height)
    

    
    def run(self):  # Animation loop
        time = self.time
        self.c1.create_photon()
        self.root.after(self.time, self.run) 












class ElectronMotion(CreateSpectrum, CreateParticle):
    def __init__(self, root, subcanvas1, subcanvas2):
        CreateSpectrum.__init__(self, root, subcanvas1, subcanvas2)
        CreateParticle.__init__(self, root, subcanvas1, subcanvas2, self.get_colour)

        # Work function values for different metals
        self.metal_work_functions = {
            "Calcium": 2.00,
            "Copper": 4.70,
            "Iron": 4.50,
            "Nickel": 5.01,
            "Sodium": 2.28
        }
        self.selected_var = StringVar(value="None")  # Default value is "None"
        self.place_options()
        self.tube_electrons = []

    def place_options(self):
        """Place the Radiobuttons for selecting metals."""
        calcium = Radiobutton(self.subcanvas2, text="Calcium", variable=self.selected_var, value="Calcium", command=self.on_metal_selected)
        calcium.place(x=20, y=10)

        copper = Radiobutton(self.subcanvas2, text="Copper", variable=self.selected_var, value="Copper", command=self.on_metal_selected)
        copper.place(x=20, y=40)

        iron = Radiobutton(self.subcanvas2, text="Iron", variable=self.selected_var, value="Iron", command=self.on_metal_selected)
        iron.place(x=20, y=70)

        nickel = Radiobutton(self.subcanvas2, text="Nickel", variable=self.selected_var, value="Nickel", command=self.on_metal_selected)
        nickel.place(x=20, y=100)

        sodium = Radiobutton(self.subcanvas2, text="Sodium", variable=self.selected_var, value="Sodium", command=self.on_metal_selected)
        sodium.place(x=20, y=130)



    def print_v(self):
        print(f"Updated Voltage: {self.volt}")

    def on_metal_selected(self):
        selected_metal = self.selected_var.get()

    def work_function(self):
        selected_metal = self.selected_var.get().title()  # Convert to title case
        if selected_metal == "None":
            return 0  # Return 0 if no metal is selected
        if selected_metal in self.metal_work_functions:
            work_function = self.metal_work_functions[selected_metal] * (1.6 * (10 ** -19))
            return work_function
        else:
            return 0
    
    def calculate_photon_energy(self, wavelength):
        PLANCK = 6.63 * (10 ** -34)
        LIGHT = 3 * (10 ** 8)
        energy = (PLANCK * LIGHT) / (wavelength*(10**-9))
        return energy
    
    def incident_energy(self):
        #print(self.calculate_photon_energy(self.return_wavelength()))
        return self.calculate_photon_energy(self.return_wavelength())
    
    def stopping_potential(self):
        voltage = self.return_voltage()
        stopping_potential_value = voltage * (1.6 * (10 ** -19))  # Convert to Joules
        print(f"Stopping Potential: {stopping_potential_value}")
        return stopping_potential_value
    
    
    
    def resultant_kinetic_energy(self):
        kinetic_energy = (self.incident_energy() - self.work_function()) -(self.stopping_potential())
        print(kinetic_energy)
        if kinetic_energy < 0:
            kinetic_energy = 0  # Ensure no negative kinetic energy
        return kinetic_energy
    
    def velocity(self):
        kinetic_energy = self.resultant_kinetic_energy()
        mass_of_electron = 9.11 * (10 ** -31)  # Mass of electron in kg
        if kinetic_energy > 0:
            velocity = math.sqrt((2 * kinetic_energy) / mass_of_electron)
            return velocity
        else:
            return 0
    
    def calculate_relative_speed(self):  # Scaling the velocity speed down
        velocity = self.velocity()
        relative_speed = (velocity * (10 ** -6)) * 8  # Convert velocity to a scaled simulation speed
        return int(relative_speed)
    
    def create_electron(self, x, y):
        radius = 2
        x2 = x + radius * 2
        y2 = y + radius * 2
        electron_id = self.subcanvas1.create_oval(x, y, x2, y2, fill="blue", outline="")
        self.tube_electrons.append(electron_id)
    
    def move_electrons(self):
        relative_speed = self.calculate_relative_speed()
        #print(f"Moving electrons at relative speed: {relative_speed}")
        if self.running:
            for electron in self.tube_electrons[:]:
                self.subcanvas1.move(electron, relative_speed, 0)  # Move horizontally at calculated speed
                if self.subcanvas1.coords(electron):
                    x1, y1, x2, y2 = self.subcanvas1.coords(electron)
                    if x1 > 777:  # Remove if out of bounds
                        self.subcanvas1.delete(electron)
                        self.tube_electrons.remove(electron)
                
            self.subcanvas1.after(5000, self.move_electrons)  # Continue moving at a steady interval
    
           #eject electrons (motion of ELECTRONS according to the voltage of the cell also)



#FIRST DRAFT OF THE CLASS
'''
class ElectronMotion(CreateSpectrum, CreateParticle):
    def __init__(self, root, subcanvas1, subcanvas2):
        CreateSpectrum.__init__(self, root, subcanvas1, subcanvas2)
        CreateParticle.__init__(self, root, subcanvas1, subcanvas2, self.get_colour)

        # Work function values for different metals
        self.metal_work_functions = {
            "Calcium": 2.00,
            "Copper": 4.70,
            "Iron": 4.50,
            "Nickel": 5.01,
            "Sodium": 2.28
        }
        self.selected_var = StringVar(value="None")  # Default value is "None"
        self.place_options()

    def place_options(self):
        """Place the Radiobuttons for selecting metals."""
        calcium = Radiobutton(self.subcanvas2, text="Calcium", variable=self.selected_var, value="Calcium", command=self.work_function)
        calcium.place(x=20, y=10)

        copper = Radiobutton(self.subcanvas2, text="Copper", variable=self.selected_var, value="Copper", command=self.work_function)
        copper.place(x=20, y=40)

        iron = Radiobutton(self.subcanvas2, text="Iron", variable=self.selected_var, value="Iron", command=self.work_function)
        iron.place(x=20, y=70)

        nickel = Radiobutton(self.subcanvas2, text="Nickel", variable=self.selected_var, value="Nickel", command=self.work_function)
        nickel.place(x=20, y=100)

        sodium = Radiobutton(self.subcanvas2, text="Sodium", variable=self.selected_var, value="Sodium", command=self.work_function)
        sodium.place(x=20, y=130)

    def work_function(self):
        selected_metal = self.selected_var.get()
        if selected_metal in self.metal_work_functions:
            work_function = self.metal_work_functions[selected_metal] * (1.6 * 10**-19)
            print(f"Selected Metal: {selected_metal}, Work Function: {work_function} J")
        else:
            print("No valid metal selected.")

    def calculate_photon_energy(self, wavelength):
        PLANCK = 6.63 * (10**-34)
        LIGHT = 3 * (10**8)
        energy = (PLANCK * LIGHT) / wavelength
        return energy

    def incident_energy(self):
        return self.calculate_photon_energy(self.return_wavelength())

    def stopping_potential(self):
        return self.return_voltage() * (1.6 * 10**-19)

    def resultant_kinetic_energy(self):
        work_function = self.metal_work_functions.get(self.selected_var.get(), 0) * (1.6 * 10**-19)
        ke = self.incident_energy() - work_function - self.stopping_potential()
        return max(0, ke)  # Ensure KE is non-negative

    def velocity(self):
        ke = self.resultant_kinetic_energy()
        electron_mass = 9.11 * 10**-31
        velocity = (2 * ke / electron_mass) ** 0.5
        print(f"Electron Velocity: {velocity:.2e} m/s")
        return velocity

    def calculate_relative_speed(self):
        speed = self.velocity() * (10**6) / 0.05  # Scale appropriately for canvas animation
        return max(1, int(speed))  # Ensure speed is at least 1 ms

    def create_electron(self, x, y):
        """Create an electron particle."""
        radius = 2
        x2 = x + radius * 2
        y2 = y + radius * 2
        electron_id = self.subcanvas1.create_oval(x, y, x2, y2, fill="blue", outline="")
        self.tube_electrons.append(electron_id)

    def move_electrons(self):
        """Move electrons after they are emitted."""
        for electron in self.tube_electrons[:]:
            self.subcanvas1.move(electron, 15, 0)  # Move the electron horizontally
            if self.subcanvas1.coords(electron):
                x1, y1, x2, y2 = self.subcanvas1.coords(electron)
                if x1 > 777:  # Remove if out of bounds
                    self.subcanvas1.delete(electron)
                    self.tube_electrons.remove(electron)

        if self.running:
            delay = self.calculate_relative_speed()  # Dynamically adjust speed
            self.subcanvas1.after(delay, self.move_electrons)
'''





#2nd DRAFT OF THAT CLASS


'''
class ElectronMotion(CreateSpectrum, CreateParticle):
    def __init__(self, root, subcanvas1, subcanvas2):
        CreateSpectrum.__init__(self, root, subcanvas1, subcanvas2)
        CreateParticle.__init__(self, root, subcanvas1, subcanvas2, self.get_colour)

        # Work function values for different metals
        self.metal_work_functions = {
            "Calcium": 2.00,
            "Copper": 4.70,
            "Iron": 4.50,
            "Nickel": 5.01,
            "Sodium": 2.28
        }
        self.selected_var = StringVar(value="None")  # Default value is "None"
        self.place_options()
        self.tube_electrons = []

    def place_options(self):
        """Place the Radiobuttons for selecting metals."""
        calcium = Radiobutton(self.subcanvas2, text="Calcium", variable=self.selected_var, value="Calcium", command=self.work_function) #change value to metal name
        calcium.place(x=20, y=10)

        copper = Radiobutton(self.subcanvas2, text="Copper", variable=self.selected_var, value="Copper", command=self.work_function)
        copper.place(x=20, y=40)

        iron = Radiobutton(self.subcanvas2, text="Iron", variable=self.selected_var, value="Iron", command=self.work_function)
        iron.place(x=20, y=70)

        nickel = Radiobutton(self.subcanvas2, text="Nickel", variable=self.selected_var, value="Nickel", command=self.work_function)
        nickel.place(x=20, y=100)

        sodium = Radiobutton(self.subcanvas2, text="Sodium", variable=self.selected_var, value="Sodium", command=self.work_function)
        sodium.place(x=20, y=130)

    def work_function(self):
        selected_metal = self.selected_var.get().title()  # Convert to title case
        if selected_metal in self.metal_work_functions:
            work_function = self.metal_work_functions[selected_metal] * (1.6 * (10 ** -19))
            print(f"Work Function for {selected_metal}: {work_function}")
            return work_function
        else:
            print(f"Metal '{selected_metal}' not found in work function dictionary.")
            return 0
        
    def return_work_function(self):
        return self.work_function()
    
    def calculate_photon_energy(self,wavelength):
        PLANCK = 6.63* (10**-34)
        LIGHT = 3* (10**8)

        energy = (PLANCK * LIGHT) / wavelength
        return energy
    

    def incident_energy(self):
        return self.calculate_photon_energy(self.return_wavelength())

    def stopping_potential(self):
        return 0
        #return self.voltage * (1.6*(10**-19))

    def resultant_kinetic_energy(self):
        return (self.incident_energy() - self.return_work_function()) - self.stopping_potential()
    

    def velocity(self):
        velocity = math.sqrt((2* self.resultant_kinetic_energy())/(9.11*(10**-31) ))
        print(velocity)
        return velocity

    def calculate_relative_speed(self):
        return (self.velocity() * (10**-6)) / 0.05

    def create_electron(self, x, y):
        """Create an electron particle."""
        radius = 2
        x2 = x + radius * 2
        y2 = y + radius * 2
        electron_id = self.subcanvas1.create_oval(x, y, x2, y2, fill="blue", outline="")
        self.tube_electrons.append(electron_id)

    def move_electrons(self):
        """Move electrons after they are emitted."""
        print("my guy")
        print(self.calculate_relative_speed) # returns an instance instead of a number
        if self.running:
            for electron in self.tube_electrons[:]:
                self.subcanvas1.move(electron,self.calculate_relative_speed() , 0)  # controls the speed PER ITERATION
                if self.subcanvas1.coords(electron):
                    x1, y1, x2, y2 = self.subcanvas1.coords(electron)
                    if x1 > 777:  # Remove if out of bounds
                        self.subcanvas1.delete(electron)
                        self.tube_electrons.remove(electron)
                
            self.subcanvas1.after(5000, self.move_electrons) # controls the speed
    

'''
class LinkedParticles(ElectronMotion):
    def __init__(self, root, subcanvas1, subcanvas2):
        super().__init__(root, subcanvas1, subcanvas2)
        self.root = root
        # Create a target shape (e.g., metal plate)
        self.target_shape =  self.subcanvas1.create_rectangle(777,280,782,480, fill = "grey", outline = "black", width = 2)

        self.second_particle = ElectronMotion(self.root,self.subcanvas1, self.subcanvas2)

        # Create the first particle motion
        self.first_particle = CreateSpectrum(root,subcanvas1, subcanvas2)
        self.first_particle.c1.target_shape = self.target_shape
        self.first_particle.c1.trigger_callback = self.trigger_second_particle

        # Add a button to start the first particle motion
        self.play = subcanvas1.create_oval(420,695,445,720, fill = "lightblue")
        self.step = subcanvas1.create_oval(460,695,485,720, fill = "lightblue")

        self.subcanvas1.tag_bind(self.play, "<Button-1>", self.pause_play_on_click)
        self.subcanvas1.tag_bind(self.step, "<Button-1>", self.step_on_click)
    
    '''
    def trigger_second_particle(self, coords):
        x, y = coords
        electron_start_x = self.subcanvas1.coords(self.target_shape)[2]  # Right edge of metal plate
        electron_start_y = (y + self.subcanvas1.coords(self.target_shape)[1]) / 2  # Center of photon collision

        # Create and move an electron
        self.second_particle.create_electron(electron_start_x, electron_start_y)
        self.second_particle.move_electrons()
    '''

    def pause_play_on_click(self,event):    
        if self.first_particle.c1.running:
            print("Pausing simulation")
            self.first_particle.c1.running = False  # Stop photon motion
            self.second_particle.running = False  # Stop electron motion
            self.play_event = False  # Stop creating new particles
        else:
            print("Resuming simulation")
            self.first_particle.c1.running = True  # Resume photon motion
            self.second_particle.running = True  # Resume electron motion
            self.play_event = True
            self.first_particle.c1.start()

    
    def trigger_second_particle(self, coords):
        x, y = coords
        self.second_particle.create_electron(x, y)  # Adjust electron start position
        self.second_particle.move_electrons()
    
        
    def step_on_click(self):
        pass
    
    






class Visualise(ElectronMotion):
    def __init__(self, root, subcanvas1, subcanvas2):
        super().__init__(root, subcanvas1, subcanvas2) 
        Button(self.subcanvas2, text = "A Level Notes", font=("Arial", 14, "bold"), command = self.a_level_notes)     
        self.root2 = Tk()              

    def a_level_notes(self):
        n1 = Notes(self.root, self.root2, self.subcanvas2)
        n1()

    def canvas_AspectRatio(self,root):
        root_height = root.winfo_screenheight()
        root_width = root.winfo_screenwidth()

        # Aspect ratios for each of the Sub-Canvases - REFERENCE
        SC1_width_ratio = 1.3
        SC2_width_ratio = 5.5   # The specific ratios will be decided during the Programming
        SC_height_ratio = 1.12

        subcanvas1_width = root_width //SC1_width_ratio
        subcanvas1_height = (root_height//SC_height_ratio)	

        subcanvas2_width = root_width //SC2_width_ratio
        subcanvas2_height = (root_height/SC_height_ratio)


        self.subcanvas1.config(width=subcanvas1_width, height=subcanvas1_height)
        self.subcanvas1.place(x = (root_width/100 ) , y= (root_height/21 ))

        self.subcanvas2.config(width=subcanvas2_width, height=subcanvas2_height)
        self.subcanvas2.place(x = (root_width/1.24 ) , y= (root_height/21 ))
        return subcanvas1_width, subcanvas1_height
    


    
    def draw_circuit(self,subcanvas): # Draws the Whole circuit for Subcanvas 1
        width,height = self.canvas_AspectRatio(subcanvas)
        
        #Discharge Tube
        subcanvas.create_oval(182,240, 217,520, outline = "black", width = 2)
        subcanvas.create_oval(800,240,835,520, outline = "black", width = 2)
        subcanvas.create_rectangle(200,240,820,240, outline = "black", width = 1)
        subcanvas.create_rectangle(200,520,820,520, outline = "black", width = 1)
        
        #  The wires of the circuit
        subcanvas.create_rectangle(70,380,230,382, fill = "black")
        subcanvas.create_rectangle(70,380,72,650, fill = "black")
        subcanvas.create_rectangle(70,650,968,652, fill = "black")
        subcanvas.create_rectangle(968,652,970,382, fill = "black")  
        subcanvas.create_rectangle(970,382,782,380, fill = "black")  

        # The metal plates
        subcanvas.create_rectangle(230,280,235,480, fill = "grey", outline = "black", width = 2)

        # The Battery
        subcanvas.create_rectangle(408,620,538,680, fill = "darkgoldenrod",outline = "black")
        subcanvas.create_rectangle(408,620,508,680, fill = "grey",outline = "black")
        subcanvas.create_rectangle(538,640,548,660, fill = "black",outline = "black")

        
        #The Lamp
        subcanvas.create_rectangle(580,50,700,60, fill = "darkgoldenrod", outline = "black", width = 2)
        subcanvas.create_polygon(580, 40, 590, 48, 555, 145, 500, 100, fill="black")

        #The Pause/play buttons
        subcanvas.create_polygon(468,701,468,715,480,708, fill = "black")
        subcanvas.create_line(466,701,466,715,fill = "black", width = 2)

        #Ammeter - (Just a DYNAMICALLY CHANGING LABEL)
        ammeter_label = Label(subcanvas, text= f"Ammeter: 0.000 A ", bg="white", font=("Arial", 18)).place(x=608, y=633)

    
    def update_ammeter(self):
        pass    



    def __call__(self):  # To Initialise the main tkinter window
        v1 = Visualise(self.root, self.subcanvas1, self.subcanvas2)

        self.root.title("Photoelectric Effect Simulator")
        self.root.state('zoomed')  # To ensure that the program always opens as a Full Screen and not a small window
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        Label(self.root, text="The Photoelectric Effect simulator", bg="gainsboro", font=("Arial", 18)).place(x=500, y=0)

        v1.canvas_AspectRatio(self.root)
        v1.draw_circuit(self.subcanvas1)
        v1.create_final_spectrum()
        #v1.run()





'''


class ElectronMotion(CreateSpectrum, CreateParticle):
    def __init__(self, root, subcanvas1, subcanvas2, tube_electrons):
        super().__init__(root, subcanvas1, subcanvas2, tube_electrons)
        self.get_wavelength = self.return_wavelength()
        self.calcium = 2.00
        self.copper = 4.70
        self.iron = 4,50
        self.nickel = 5.01
        self.sodium = 2.28

        self.tube_electrons = tube_electrons
        self.selected_var = StringVar(value="None")  # Default value is "None"
        self.inside_time = 50
    


    def place_options(self):
        # Create radiobuttons with the same variable and values representing the Metal names
        calcium = Radiobutton(self.subcanvas2, text="Calcium", variable=self.selected_var, value="Calcium", command = self.work_function)
        calcium.place(x=20,y=10)

        copper = Radiobutton(self.subcanvas2, text="Copper", variable=self.selected_var, value="Copper", command=self.work_function)
        copper.place(x=20,y=40)

        iron = Radiobutton(self.subcanvas2, text="Iron", variable=self.selected_var, value="Iron", command=self.work_function)
        iron.place(x=20,y=70)

        nickel = Radiobutton(self.subcanvas2, text="Nickel", variable=self.selected_var, value="Nickel", command=self.work_function)
        nickel.place(x=20,y=100)

        sodium = Radiobutton(self.subcanvas2, text="Sodium", variable=self.selected_var, value="Sodium", command=self.work_function)
        sodium.place(x=20,y=130)



    def check_metal(self):
        selection = self.selected_var.get()
        if selection != "None":
            return selection
        else:
            print("No option selected")

    def work_function(self,metal):
        joules =  metal * 1.6*(10**-19)
        return joules
    
    def kinetic_energy(self):
        return self.calculate_photon_energy(self.get_wavelength)

    def create_electron(self):
        radius = 1.5 
        x1 = 230  # Start just outside the left edge of the canvas
        y1 = random.randint(290, 420)
        x2 = x1 + radius * 2
        y2 = y1 + radius * 2
        coords = (y1,y2)

        # Draw the circle and return its ID
        circle_id = self.subcanvas1.create_oval(x1, y1, x2, y2, fill="black", outline="")
        self.tube_electrons.append(circle_id)
        self.subcanvas1.after(50, self.create_electron)  # Create a new electron every 50ms

        return coords
    
    def retur(self):
        print(self.wavelength)
        return self.get_wavelength


    def move(self):
        """Move electrons based on energy condition."""
        # Check the selected metal and get its work function
        metal_work_function = self.work_function(self.calcium)

        for circle_id in self.tube_electrons[:]:
            energy = self.calculate_photon_energy(self.get_wavelength)  # Get energy based on wavelength

            if energy > metal_work_function:
                self.subcanvas1.move(circle_id, 5, 0)

                x1, y1, x2, y2 = self.subcanvas1.coords(circle_id)
                if x2 > self.subcanvas1.winfo_width():  # If it moves out of the canvas
                    self.subcanvas1.delete(circle_id)  # Remove from canvas
                    self.tube_electrons.remove(circle_id)  # Remove from list
            else:
                # Electron doesn't move if energy is less than the work function
                pass

        # Ensure the method is called repeatedly
        self.subcanvas1.after(50, self.move)

    def run(self):
        #time = self.inside_time
        self.create_electron() 
        self.root.after(self.time, self.run) 


'''




'''
 def move(self):
        """Move electrons based on energy condition."""
        # Check if selected metal is chosen
        metal_work_function = self.work_function(self.calcium)

        for circle_id in self.tube_electrons[:]:
            energy = self.calculate_photon_energy(self.get_wavelength())  # Get energy based on wavelength
            if energy > metal_work_function:
                self.subcanvas1.move(circle_id, 5, 0)  # Move the electron by 5 pixels

                x1, y1, x2, y2 = self.subcanvas1.coords(circle_id)
                if x2 < 230:  # If the electron goes out of bounds
                    self.subcanvas1.delete(circle_id)
                    self.tube_electrons.remove(circle_id)  
            else:
                # Electron will not move if energy is less than the work function
                pass

        # Keep calling the move method every 50ms
        self.subcanvas1.after(50, self.move)
'''



def validate_colour(self,colour):
    try:
        self.subcanvas1.winfo_toplevel().call("winfo", "rgb", colour)
        return True
    except TclError:
        return False
    

#ElectronMotion class DRAFT

















