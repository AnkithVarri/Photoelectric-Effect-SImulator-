from tkinter import *
from tkinter import messagebox


class Notes:
    def __init__(self, parent_window):
        # Create a new Toplevel window
        self.window = Toplevel(parent_window)
        self.window.title("A-Level Notes")
        self.window.geometry("800x600")  # Set window size
        self.window.configure(bg="#f8f9fa")  # Background color

    def display_notes(self):
        # Create a frame for the text widget
        frame = Frame(self.window, bg="#ffffff", bd=2, relief="groove")
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Create the text widget
        text_widget = Text( frame,wrap="word",font=("Georgia", 14), bg="#ffffff",fg="#333333",highlightthickness=0, padx=10, pady=10 )
        text_widget.pack(expand=True, fill="both")
        
        # Insert the content into the Text widget
        content = """    
        A Level Notes:

        Key Definitions for the Quantum Chapter:
         - The Photoelectric Effect: A phenomenon (discovered by Albert Einstein), where when light with enough energy is incident on a Metal's surface, Electrons are emitted from the metal's surface.
         - Ionisation: The Process of removing an electron from an atom or molecule, resulting in an electrically charged molecule called an ion
         - Work Function -  The minimum energy required for a Photon to “knock off” an electron of a metal’s surface. Each metal has a different work function.  

                Equation for Work function is:    Work Function = Planck’s constant * Threshold frequency.    Energy measured in Joules (J)

         - Planck’s constant : A universal Physics Constant, with value (6.63 * 10^-34)  Js
         - Threshold Frequency - The minimum frequency required to knock off an electron.  Frequency measured in Hertz (Hz)
         - Stopping Potential - A variable in the photoelectric effect. Where the value of the battery’s negative Potential Difference (pd) is high enough. At this Pd value, it is enough to prevent electrons from leaving the metal’s surface (with a fixed incident energy from a specific photon), therefore “stopping” the photoelectric effect. Stopping potential measured in Volts (V)
         - Photon Intensity - The amount of photons “making contact” with the metal’s surface per second. The higher the photon intensity, the more photons that make contact with the metal surface per second.  No units for intensity.
         - Photon Energy - The amount of energy in 1 photon.  A higher Photon energy does not mean a higher photon intensity and vice versa.  Photon Energy measured in Joules (J)
         - A Photocell - A glass cylinder connected to 2 metal plates on either end. The light shines through the glass cylinder and hits one of the metal plates. Then electrons will be emitted from the metal plate and they will travel to the other metal plate. If the electrons reach the other metal plate, then they will travel through the wires (as current).
         - Ek(max) - If a light photon has “too much energy”, then once the photon knocks off the electron, the remaining energy of the photon is transferred the electron as Kinetic Energy. Therefore causing the electron to move in Space. It’s called Ek(max) since it’s the max possible Kinetic Energy that an electron can have, when a specific photon energy is incident on a Metal’s surface (of a specific metal).
         - Equation for this is:  Ek(max) = Total Incident Energy - The metal’s Work Function


        Key Points to remember:
         - As you increase the Intensity, the speed of the electrons inside the Dscharge tube IS NOT AFFECTED, instead more photons will be released off of the plate (assuming that the photons have enoug henergy in the first place).
         - The gradient of a frequency against Intensity Graph is equal to the Planck's constant. No matter how high the energy of the light is, the gradient will always equal the Planck's constant.
         - The Pd of the Battery can also be used to accelerate and decelerate the electrons, which is due to the stronger/weaker electric field within the discharge Tube.
         - Common applications of the Photoelectric effect are Neon Lights (The lights used in Pubs and Barbershops)
        

        Common Applications of the Photoelectric Effect:
         - Neon Lights: Used in advertising signs, they rely on ionisation and light emission.
         - Photomultiplier Tubes: Used in scientific instruments for detecting low levels of light.
         - Solar Panels: Convert light into electricity using the photoelectric effect.
         - Automatic Doors & Light Sensors: Many devices use photoelectric sensors to detect light changes.
         
        
        Experimental Observations and Graphical Analysis:
            Graph of Maximum Kinetic Energy vs. Frequency:
             - The graph is a straight line with equation:
             - The x-intercept (where ) corresponds to the threshold frequency .
             - The y-intercept is , the work function.
             - The gradient is Planck’s constant .
             - The graph is independent of light intensity.

            Graph of Current vs. Voltage (Potenial Difference)
                - The graph is a straight line with the same gradient as the E_k (max) vs. frequency graph, since:


        Key Experimental Setup for Demonstrating the Photoelectric Effect:
            Apparatus:
             - A vacuum photocell
             - A metal plate (e.g., zinc or sodium)
             - A source of monochromatic light (e.g., UV lamp)
             - A variable power supply to adjust stopping potential
             - An ammeter to measure photoelectric current

            Observations:
             - Photoelectrons are only emitted if the light frequency is above the threshold frequency.
             - Increasing the intensity of the light (while keeping frequency constant) increases the number of emitted electrons but does not affect their energy.
             - Increasing the frequency of incident light increases the kinetic energy of emitted electrons.

        """

        # Insert the content into the Text widget
        text_widget.insert("1.0", content)

        # Format the indentation and text alignment, when writing long bullet points
        text_widget.tag_config("paragraph",spacing1=5,spacing3=10, lmargin1=20, lmargin2=80)

        # Style general text
        text_widget.tag_config("header", font=("Georgia", 16, "bold"), foreground="#0056b3") # Similar to HTML/CSS kinda
        text_widget.tag_config("paragraph", spacing3=10)

      
        # Make the Text widget read-only
        text_widget.config(state="disabled")
