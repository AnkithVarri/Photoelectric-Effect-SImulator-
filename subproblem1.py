from tkinter import *
from tkinter import ttk
import math
import time


from subproblem1 import *
from subproblem2 import *
from subproblem3 import *
from subproblem4 import *



class CreateSpectrum:
    def __init__(self, root, subcanvas1, subcanvas2, callback=None):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.subcanvas2 = subcanvas2
        self.callback = callback

        self.time = 50
        self.wavelength= 380

        self.wavelength_label = Label(self.subcanvas1, text="Wavelength: 380 nm", bg="white", width=20)
        self.wavelength_label.place(x=835, y=185)

        self.intensity_label = Label(self.subcanvas1, text="Intensity: 0%", bg="white", width=20)
        self.intensity_label.place(x=830, y=12)
        
        self.intensity_slider = Scale(self.subcanvas1, from_=1, to=100, length=300, orient="horizontal", command=self.update_intensity_label)
        self.intensity_slider.place(x=750, y=30)
        self.intensity_slider.set(50)

        self.wavelength_slider = Scale(self.subcanvas1, from_= 380, to=750, length=300, orient="horizontal", command=self.update_wavelength_label)
        self.wavelength_slider.place(x=750, y=135)

        self.c1 = CreateParticle(self.root,self.subcanvas1, get_colour_method=self.get_colour)


    def get_current_color(self, event = None):
        color_value = self.wavelength_slider.get()
        hex_color = "#{:02x}{:02x}{:02x}".format(color_value, color_value, color_value)
        return hex_color

        
    def get_rgb_from_position(self, position):
        positioncalc = position * 255
        r, g, b = 0, 0, 0

        if position < 0:
            return None, None, None
        
        elif position < (70 / 370):
            r = 255 * (70 - positioncalc) / 70
            g = 0
            b = 255

        elif position < (120 / 370) and position > (70 / 370):
            r = 0
            g = 255 * (positioncalc - 70) / 50
            b = 255

        elif position < (190 / 370) and position > (120 / 370):
            r = 0
            g = 255
            b = 255 * (190 - positioncalc) / 70

        elif position < (220 / 370) and position > (190 / 370):
            r = 255 * (positioncalc - 190) / 30
            g = 255
            b = 0

        elif position < (370 / 370) and position > (220 / 370):
            r = 255
            g = 255 * (370 - positioncalc) / 150
            b = 0

        elif position > (370 / 370):
            return None, None, None
        
        if r == None or g == None or b == None:
            return r, g, b
        else:
            r = int(r)
            g = int(g)
            b = int(b)

        return r, g, b
    
    

    def get_colour(self, value=None):
        if value is None:
            value = self.wavelength_slider.get()

        if value < 380:
            value = 380
        elif value > 750:
            value = 750

        r, g, b = 0, 0, 0

        if value <= 380:
            r = 115
            g = 115
            b = 115

        elif value > 380 and value < 451:
            r = 255 * (450 - value) / 70
            g = 0
            b = 255

        elif value > 450 and value < 501:
            r = 0
            g = 255 * (value - 450) / 50
            b = 255

        elif value > 500 and value < 571:
            r = 0
            g = 255
            b = 255 * (570 - value) / 70

        elif value > 570 and value < 601:
            r = 255 * (value - 570) / 30
            g = 255
            b = 0

        elif value > 600 and value < 750:
            r = 255
            g = 255 * (750 - value) / 150
            b = 0

        elif value >= 750:
            r = 45
            g = 45
            b = 45

        r = max(0, min(255, int(r)))
        g = max(0, min(255, int(g)))
        b = max(0, min(255, int(b)))
        #print(f"#{int(r):02x}{int(g):02x}{int(b):02x}")

        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"
    
    def update_time(self, value):
        self.time = max(1, int(value))  # Update the internal time
        return self.time


    def update_intensity_label(self, value):
        self.time = max(1, int(value))  # Update the internal time
        self.intensity_label.config(text=f"Intensity: {value}%")
        self.c1.update_time(value)  # Update the photon speed


    def update_wavelength_label(self,value):                                                      
        wavelength = int(value)  # Convert slider value to an integer wavelength
        color = self.get_colour(wavelength)  
        self.wavelength_label.config( text=f"Wavelength: {wavelength} nm", bg=color ) # Retrieve the wavelength/intensity INFO from THESE VARIABLES

        
    def update_electron_speed(self):
        if hasattr(self, 'volt'):
            self.volt.update_electron_motion()

            
    def create_colour_spectrum(self):   #To create 1 line , representing each rgb combination of the light spectrum
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
        # Create the color spectrum
        self.create_colour_spectrum()







class ElectronMotion:

    '''
    The class responsible for the Electron Motion
    Contains the Physics calculations, which use the values retrieved from the CreateSpectrum class
    '''
    def __init__(self, root, subcanvas1, subcanvas2, graph=None, spectrum=None):
        self.root = root
        self.subcanvas1 = subcanvas1
        self.subcanvas2 = subcanvas2
        if spectrum is None:
            self.first_particle = CreateSpectrum(root, subcanvas1, subcanvas2)
        else:
            self.first_particle = spectrum

        self.create_particle = self.first_particle.c1
        self.first_particle.volt = self

        self.battery_slider = Scale(self.subcanvas1, from_=-8.0, to=8.0, length=300, orient="horizontal", resolution=0.1, command=self.update_electron_motion)
        self.battery_slider.place(x=390, y=580)

        self.metal_work_functions = {"Calcium": 2.00, "Copper": 4.70, "Iron": 4.50, "Nickel": 5.01, "Sodium": 2.28}
        self.selected_var = StringVar(value="None")

        #self.place_options()
        self.tube_electrons = []
        self.place_options()

        self.wave = 380
        self.volt = 0
        
        self.running1 = True

        self.current = 0.0
        self.electron_density = 1e15  # Example: Adjust this
        self.wire_cross_sectional_area = 1e-6  # Example: Adjust this
        self.ammeter_label = Label(self.subcanvas1, text=f"Ammeter: 0 A ", bg="white", font=("Arial", 18))
        self.ammeter_label.place(x=608, y=633)

        self.graph = graph

    def calculate_current(self):
        velocity = self.velocity()
        #print(velocity)
        if velocity < 300000:
            velocity  = 0
            print("ok")
       
        self.current = self.electron_density * 1.6e-19 * velocity * self.wire_cross_sectional_area if velocity > 0 else 0.0  # Current also depends upon electron density and cross sectional area of the Wire
        return self.current

    def update_current(self):
        self.current = self.calculate_current()
        self.ammeter_label.config(text=f"Ammeter: {self.current:.2e} A")

   
    def place_options(self):
        '''Place the Mwtal options on the subcanvas 2'''
        metals = ["Calcium", "Copper", "Iron", "Nickel", "Sodium"]
        for i, metal in enumerate(metals):
            Radiobutton(self.subcanvas2, text=metal, variable=self.selected_var, value=metal, command=self.on_metal_selected).place(x=20, y=10 + i * 30)

    def on_metal_selected(self):
        pass

    def work_function(self):
        '''calculate the work function, using the metal values'''
        selected_metal = self.selected_var.get().title()
        return self.metal_work_functions.get(selected_metal, 0) * 1.6e-19
    
    def calculate_photon_energy(self, wavelength):
        'calculates photon energy'
        PLANCK = 6.63e-34
        LIGHT = 3e8
        return (PLANCK * LIGHT) / (wavelength * 1e-9)

    def incident_energy(self):
        '''return the calculated photon energy'''
        print(self.first_particle.wavelength_slider.get())
        return self.calculate_photon_energy(self.first_particle.wavelength_slider.get())

    def update_electron_motion(self, event=None):
        self.stopping_potential()
        self.move_electrons()

    def stopping_potential(self, event=None):
        '''calculate the stopping potential in Joules'''
        self.volt = self.battery_slider.get()
        print(self.volt)
        return self.volt * 1.6e-19

    def resultant_kinetic_energy(self):
        '''uses the resultant kinetic energy formula to calculate the resultant kinetic energy'''
        kinetic_energy = (self.incident_energy() - self.work_function()) + self.stopping_potential()
        return max(0, kinetic_energy)

    def velocity(self):
        kinetic_energy = self.resultant_kinetic_energy()
        #print(kinetic_energy, "ENERGYYY22222222222222222222")
        mass_of_electron = 9.11e-31
        return math.sqrt(2 * kinetic_energy / mass_of_electron) if kinetic_energy > 0 else 0
        

    def calculate_relative_speed(self):
        '''scales down the speed to a speed that ysers can see in the simulator'''
        velocity = self.velocity()
        #print(velocity, "VELOCITYYY222222222222222222")
        return int(velocity * 1e-6 * 8)

    def create_electron(self, x, y):
        '''creates an electron'''
        radius = 2
        x2 = x + radius * 2
        y2 = y + radius * 2
        electron_id = self.subcanvas1.create_oval(x, y, x2, y2, fill="blue", outline="")
        self.tube_electrons.append(electron_id)

    def move_electrons(self):
        '''Moves the electron in the defined pattern
          Also updates the Ammeter
          '''
        if not self.create_particle.running:
            return
        relative_speed = self.calculate_relative_speed()
        for electron in self.tube_electrons[:]:
            self.subcanvas1.move(electron, relative_speed, 0)
            coords = self.subcanvas1.coords(electron)
            if coords and coords[0] > 777:
                # Retrieve kinetic energy and frequency
                kinetic_energy = self.resultant_kinetic_energy()
                frequency = (3e8 / self.first_particle.wavelength_slider.get())  # c / λ
                #self.graph.add_Ek_point(frequency, kinetic_energy)
                #self.graph.add_IV_point(self.volt, self.current)

                self.subcanvas1.delete(electron)
                self.tube_electrons.remove(electron)
                #self.update_current()
        if not self.create_particle.running: # To prevent a "laggy" motion
            print("yessss")
            self.subcanvas1.after(50, self.move_electrons)

















class Graph:
    def __init__(self, root, subcanvas):
        self.root = root
        self.subcanvas = subcanvas

        self.frequency_data = []
        self.kinetic_energy_data = []
        self.current_data = []
        self.voltage_data = []

        self.large_window = None
        self.fig_large, self.ax_large, self.canvas_large = None, None, None
        self.line = None
        self.pop_up = None

        self.graph_type = StringVar(value="kinetic")

        Radiobutton(self.subcanvas, text="Kinetic Energy vs. Frequency", variable=self.graph_type, value="kinetic").place(x=10, y=200)
        Radiobutton(self.subcanvas, text="Current vs Voltage", variable=self.graph_type, value="voltage").place(x=10, y=230)
       
        self.graph_open = False
        #self.open_graph()

    def add_Ek_point(self, frequency, kinetic_energy):
        self.frequency_data.append(frequency)
        self.kinetic_energy_data.append(kinetic_energy)
        self.update_graph()

    def add_IV_point(self, voltage, current):
        self.voltage_data.append(voltage)
        self.current_data.append(current)
        self.update_graph()

    def open_graph(self):
        """Opens the graph window if it's not already open."""
        if not self.graph_open:
            self.graph_open = True
            self.create_graph_window()

    def create_graph_window(self):
        """Creates the graph window and sets up the plot with hardcoded axis limits."""
        self.large_window = Toplevel(self.root)
        self.large_window.title("Enlarged Graph")
        self.large_window.geometry("400x400")

        self.fig_large =    plt.Figure(figsize=(10, 8), dpi=100)
        self.ax_large = self.fig_large.add_subplot(111)

        self.canvas_large = FigureCanvasTkAgg(self.fig_large, master=self.large_window)
        self.canvas_large.get_tk_widget().pack(fill=BOTH, expand=True)

        self.pop_up = self.ax_large.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points", bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.8), arrowprops=dict(arrowstyle="->"))
        self.pop_up.set_visible(False)

        self.fig_large.canvas.mpl_connect("motion_notify_event", self.hover)

        self.ax_large.set_xlim(self.get_x_limits())
        self.ax_large.set_ylim(self.get_y_limits())

        self.update_graph()

        self.large_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.graph_open = False
        self.large_window.destroy()
        self.large_window = None
        self.fig_large, self.ax_large, self.canvas_large = None, None, None
        self.line = None

    def get_x_limits(self):
        graph_type = self.graph_type.get()
        if graph_type == "kinetic":
            return (0, 1e6)
        elif graph_type == "voltage":
            return (-10, 10)
        else:
            return (0, 1)

    def get_y_limits(self):
        graph_type = self.graph_type.get()
        if graph_type == "kinetic":
            return (0, 0.5e-17)
        elif graph_type == "voltage":
            return (0, 0.001)
        else:
            return (0, 1)


    def update_graph(self, event=None):
        if self.graph_open and self.ax_large:
            if self.graph_type.get() == "kinetic":
                self.line, = self.ax_large.plot(self.frequency_data, self.kinetic_energy_data, color='g', marker='o', label="Data Points")
                self.ax_large.set_xlabel("Frequency (Hz)")
                self.ax_large.set_ylabel("Kinetic Energy (J)")
                self.ax_large.set_title("Photoelectric Effect: Kinetic Energy vs. Frequency")
            elif self.graph_type.get() == "voltage":
                self.line, = self.ax_large.plot(self.voltage_data, self.current_data, color='r', marker='o', label="Data Points")
                self.ax_large.set_xlabel("Voltage (V)")
                self.ax_large.set_ylabel("Current (A)")
                self.ax_large.set_title("Current vs. Voltage")
            else:
                self.line, = self.ax_large.plot([0], [0], color='g', marker='o', label="Data Points")

            self.ax_large.set_xlim(self.get_x_limits())
            self.ax_large.set_ylim(self.get_y_limits())

            self.canvas_large.draw()

    def hover(self, event):
        if event.inaxes == self.ax_large and self.line and self.line.get_xdata().size > 0:
            xdata = self.line.get_xdata()
            ydata = self.line.get_ydata()

            for i in range(len(xdata)):
                if abs(event.xdata - xdata[i]) < (xdata.max() - xdata.min()) * 0.02 and abs(event.ydata - ydata[i]) < (ydata.max() - ydata.min()) * 0.05:
                    self.pop_up.xy = (xdata[i], ydata[i])
                    self.pop_up.set_text(f"({xdata[i]:.2e}, {ydata[i]:.2e})")
                    self.pop_up.set_visible(True)
                    self.fig_large.canvas.draw_idle()
                    return  # Exit after finding the closest point

        self.pop_up.set_visible(False)
        self.fig_large.canvas.draw_idle()

















class LinkedParticles(ElectronMotion):
    def __init__(self, root, subcanvas1, subcanvas2, graph=None):
        super().__init__(root, subcanvas1, subcanvas2, graph)
        self.create_particle.trigger_callback = self.trigger_second_particle
        self.root = root
        self.second_particle = ElectronMotion(root, subcanvas1, subcanvas2, graph, spectrum=self.first_particle)
        
        self.play = subcanvas1.create_oval(420, 695, 445, 720, fill="lightblue")
        self.subcanvas1.tag_bind(self.play, "<Button-1>", self.pause_play_on_click)
        

    def pause_play_on_click(self,event):    
        if self.first_particle.c1.running:
            print("Pausing simulation")
            self.first_particle.c1.running = False  # Stop photon motion
            self.second_particle.running1 = False  # Stop electron motion
            self.play_event = False  # Stop creating new particles
        else:
            print("Resuming simulation")
            self.first_particle.c1.running = True  # Resume photon motion
            self.second_particle.running1 = True  # Resume electron motion
            self.play_event = True
            self.first_particle.c1.start()

    
    def trigger_second_particle(self, coords):
        x, y = coords
        self.second_particle.create_electron(x, y)  # Adjust electron start position
        self.second_particle.move_electrons()


    








class Visualise(LinkedParticles):
    def __init__(self, root, subcanvas1, subcanvas2,graph = None):
        super().__init__(root, subcanvas1, subcanvas2,graph)
        #self.notes_button = Button(self.subcanvas2, text="A Level Notes", font=("Arial", 14, "bold"), command=self.a_level_notes) # An Instance of the Notes class. The Notes are accesed through the Visualie class
        #self.notes_button.place(x=115, y=5)

        self.inactivity_time = 120
        self.countdown_seconds = 3
        self.inactivity_timer = None
        self.is_countdown_running = False
        self.last_activity_time = time.time() * 1000  # Initialize here!
        self.activity_delay = 500  # 500 milliseconds delay

        self.start_inactivity_timer()

        self.root.bind("<Motion>", self.reset_inactivity_timer)
        self.root.bind("<Button-1>", self.reset_inactivity_timer)

    def a_level_notes(self):
        n1 = Notes(self.root)
        n1.display_notes()

    def canvas_AspectRatio(self, root):
        root_height = root.winfo_screenheight()
        root_width = root.winfo_screenwidth()

        SC1_width_ratio = 1.3
        SC2_width_ratio = 5.5
        SC_height_ratio = 1.12

        subcanvas1_width = root_width // SC1_width_ratio
        subcanvas1_height = (root_height // SC_height_ratio)
        subcanvas2_width = root_width // SC2_width_ratio
        subcanvas2_height = (root_height / SC_height_ratio)

        self.subcanvas1.config(width=subcanvas1_width, height=subcanvas1_height)
        self.subcanvas1.place(x=(root_width / 100), y=(root_height / 21))
        self.subcanvas2.config(width=subcanvas2_width, height=subcanvas2_height)
        self.subcanvas2.place(x=(root_width / 1.24), y=(root_height / 21))

        return subcanvas1_width, subcanvas1_height

    def draw_circuit(self, subcanvas):

        width, height = self.canvas_AspectRatio(subcanvas)

        subcanvas.create_oval(182, 240, 217, 520, outline="black", width=2)
        subcanvas.create_oval(800, 240, 835, 520, outline="black", width=2)

        subcanvas.create_rectangle(200, 240, 820, 240, outline="black", width=1)
        subcanvas.create_rectangle(200, 520, 820, 520, outline="black", width=1)

        subcanvas.create_rectangle(70, 380, 230, 382, fill="black")
        subcanvas.create_rectangle(70, 380, 72, 650, fill="black")
        subcanvas.create_rectangle(70, 650, 968, 652, fill="black")
        subcanvas.create_rectangle(968, 652, 970, 382, fill="black")
        subcanvas.create_rectangle(970, 382, 782, 380, fill="black")

        subcanvas.create_rectangle(230,280,235,480, fill = "grey", outline = "black", width = 2)
        subcanvas.create_rectangle(408, 620, 538, 680, fill="darkgoldenrod", outline="black")

        subcanvas.create_rectangle(408, 620, 508, 680, fill="grey", outline="black")
        subcanvas.create_rectangle(538, 640, 548, 660, fill="black", outline="black")

        subcanvas.create_rectangle(580, 50, 700, 60, fill="darkgoldenrod", outline="black", width=2)
        subcanvas.create_polygon(580, 40, 590, 48, 555, 145, 500, 100, fill="black")

    def start_inactivity_timer(self):
        if self.inactivity_timer:
            self.root.after_cancel(self.inactivity_timer)
        print("STARTING")
        self.inactivity_timer = self.root.after(self.inactivity_time * 1000, self.trigger_final_countdown)

    def reset_inactivity_timer(self, event=None):
        current_time = time.time() * 1000
        if current_time - self.last_activity_time > self.activity_delay:
            self.last_activity_time = current_time
            if self.is_countdown_running:
                self.is_countdown_running = False
            self.start_inactivity_timer()



    def trigger_final_countdown(self):
        print("executing")
        if not self.is_countdown_running:
            self.is_countdown_running = True
            self.display_finalcountdown()

    def display_finalcountdown(self):
        '''Starts the Final countdown: 3...2....1.... SHUTDOWN

        recursively calls the update_countdown() method
        '''
        
        if not self.root.winfo_exists():
            return

        def update_countdown(seconds):
            if not self.root.winfo_exists():
                return
            if seconds > 0:
                self.root.after(1000, update_countdown, seconds - 1)
            else:
                self.close_application()
        update_countdown(self.countdown_seconds)

    def close_application(self):
        if self.root.winfo_exists():
            print("Closing the application due to inactivity.")
            self.root.destroy()

    def __call__(self):
        self.root.title("Photoelectric Effect Simulator")
        self.root.state('zoomed')
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        Label(self.root, text="The Photoelectric Effect simulator", bg="gainsboro", font=("Arial", 18)).place(x=500, y=0)

        self.canvas_AspectRatio(self.root)
        self.draw_circuit(self.subcanvas1)
        self.first_particle.create_final_spectrum()
