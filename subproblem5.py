from tkinter import *
from tkinter import messagebox






#A PERFECT TEMPLATE




class Notes:
    def __init__ (self,root, root2,subcanvas2 ):
        self.root = root
        self.root2 = root2
        self.subcanvas2 = subcanvas2
    
    def display_notes(self):
        frame = Frame(self.root2, bg="#ffffff", bd=2, relief="groove")
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        text_widget = Text(frame, wrap="word", font=("Georgia", 14), bg="#ffffff", fg="#333333", highlightthickness=0, padx=10, pady=10)
        text_widget.pack(expand=True, fill="both")
        
        # Add content to the Text widget
        content = """
        Welcome to our simulator leaflet!

        Here are some useful sections:
        - Learn about the [Photoelectric Effect].
        - Explore the [Simulator Settings].
        - Check out the [Results Analysis].

        Click on any link to navigate within the simulator.
        """

        # Insert the content into the Text widget
        text_widget.insert("1.0", content)

        # Configure tags for simulator links
        text_widget.tag_add("photoelectric", "3.14", "3.32")  # Text range for "Photoelectric Effect"
        text_widget.tag_add("settings", "4.12", "4.29")       # Text range for "Simulator Settings"
        text_widget.tag_add("analysis", "5.12", "5.28")       # Text range for "Results Analysis"

        # Bind hyperlinks to simulator actions
        text_widget.tag_bind("photoelectric", "<Button-1>", lambda e: self.show_message("Navigating to Photoelectric Effect section..."))
        text_widget.tag_bind("settings", "<Button-1>", lambda e: self.show_message("Opening Simulator Settings..."))
        text_widget.tag_bind("analysis", "<Button-1>", lambda e: self.show_message("Loading Results Analysis..."))

        # Style hyperlinks
        text_widget.tag_config("photoelectric", foreground="#0056b3", underline=True)
        text_widget.tag_config("settings", foreground="#0056b3", underline=True)
        text_widget.tag_config("analysis", foreground="#0056b3", underline=True)

        # Style general text
        text_widget.tag_config("header", font=("Georgia", 16, "bold"), foreground="#0056b3")
        text_widget.tag_config("paragraph", spacing3=10)

        # Format the text
        text_widget.tag_add("header", "1.0", "1.27")  # Tag for the header
        text_widget.tag_add("paragraph", "2.0", "end")

        # Make the Text widget read-only
        text_widget.config(state="disabled")
        
    def show_message(self,message):
        """Display a message box with the given message."""
        messagebox.showinfo("Simulator Action", message)


    def __call__(self):
        n1 = Notes(self.root, self.root2, self.subcanvas2)
        #self.root2.title("Photoelectric Effect Simulator")
        self.root2.state('zoomed')  # To ensure that the program always opens as a Full Screen and not a small window
        self.root2.configure(bg="white")
        self.root2.resizable(False, False)
        Label(self.root, text="The Photoelectric Effect simulator", bg="gainsboro", font=("Arial", 18)).place(x=500, y=0)
        self.root2.mainloop()

# Create the main Tkinter window


