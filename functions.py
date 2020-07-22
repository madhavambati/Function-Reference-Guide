import tkinter as tk 
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image

global df_python # for python dataframe
global df_nodejs # for nodejs dataframe
global df_cpp    # for cpp dataframe
global df_html   # for html dataframe
global root

root = None
# accessing all function data from Database
df_python = pd.read_csv("database/python.csv", sep=',', encoding='cp1252')
df_nodejs = pd.read_csv("database/nodeJS.csv", sep=',', encoding='cp1252')
df_cpp = pd.read_csv("database/cpp.csv", sep=',')
df_html = pd.read_csv("database/html.csv", sep=',', encoding='cp1252')

# scrollable frame class
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=640, height=480, bd=0, highlightthickness=0, relief='ridge')
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, height=640,width=480)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # binding scrollbar to the frame
    def _on_mousewheel(self, event):
        try:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        except:
            pass


#function to display python functions
def open_py(z):

    # code block to restrict multiple windows from opening
    # if the root is none a new page is created else old page is destroyed and a new page is created 
    global root
    if root is None:
        root = tk.Tk()
    else:
        try:
            root.destroy()
        except:
            pass

        root = tk.Tk() # new frame
    
    frame = ScrollableFrame(root) # scrollable frame is made out of normal frame
    function_label = tk.Label(root, text = df_python['name'][z],  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)

    definition_label = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    definition_label.pack(anchor="w", padx =10, pady=10)

    max_width = 76 # max width for text, used to prevent text from going out of frame 
    desp_text = df_python['desp'][z] # text in description heading
    height = len(str(desp_text).split(".")) - 1
    width = len(str(desp_text))
    if width > max_width:
        width = max_width
        height += 1

    desp_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    desp_textbox.pack(anchor="w", fill="x", padx=15)
    desp_textbox.insert(tk.END, desp_text)
    desp_textbox.configure(state="disabled")
    frame.pack()

    syntax_label = tk.Label(frame.scrollable_frame, text= "Syntax: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    syntax_label.pack(anchor="w", pady=10, padx =10)

    syn_text = str(df_python['Syntax'][z])
    width = len(syn_text)
    height = 1
    syntax_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    syntax_textbox.pack( anchor="w", padx=15)
    syntax_textbox.insert(tk.END, syn_text)
    syntax_textbox.configure(state="disabled")

    param_label = tk.Label(frame.scrollable_frame, text= "Param Description: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    param_label.pack(anchor="w", pady=10, padx =10)

    t1 = str(df_python['Parameters'][z]).split("/")   # for parameters 
    t2 =  str(df_python['param_description'][z]).split("/") # for description of each param

    for k in range(len(t1)):    # for handing nan values in the description
        if t1[k] == 'nan' and t2[k] == 'nan':
            param_text = "no parameters"
        else:
            param_text = t1[k] + " - " + t2[k]
        width = len(param_text)
        height = len(param_text.split(".")) - 1
        if width > max_width:
            width = max_width
            height += 1

        param_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
        param_textbox.pack( anchor="w", padx=15)
        param_textbox.insert(tk.END, param_text)
        param_textbox.configure(state="disabled")

    examaple_label = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    examaple_label.pack(anchor="w", pady=10, padx =10)

    code = str(df_python['example_input'][z])  # variable for stroing example code
    height = len(code.split("\n"))
    width = len(max(code.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    example_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    example_textbox.pack( anchor="w", padx=15)
    example_textbox.insert(tk.END, code)
    example_textbox.configure(state="disabled")


    output_label = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    output_label.pack(anchor="w", pady=10, padx =10)

    out = str(df_python['example_output'][z]) # variable for storing output of the example
    height = len(out.split("\n"))
    width = len(max(out.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    output_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold", bg="black", fg="white")
    output_textbox.pack( anchor="w", padx=15)
    output_textbox.insert(tk.END, out)
    output_textbox.configure(state="disabled")

    # dummy label to introduce padding at the end of the frame
    padding = ttk.Label(frame.scrollable_frame)
    padding.pack()

    # close function and escape keybinding for the frame
    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.focus_force()
    root.resizable(width=False, height=False)
    root.title("python references")



#function to display Nodejs functions
def open_node(z):

    # code block to restrict multiple windows from opening
    # if the root is none a new page is created else old page is destroyed and a new page is created 
    global root
    if root is None:
        root = tk.Tk()
    else:
        try:
            root.destroy()
        except:
            pass
        root = tk.Tk() # new frame
    
    
    frame = ScrollableFrame(root) # scrollable frame is made out of normal frame
    function_label = tk.Label(root, text = df_nodejs['name'][z],  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)

    desp_label = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    desp_label.pack(anchor="w", padx =10, pady=10)
    
    # code block for controlling height and width of the textbox
    max_width = 76 # max width for text, used to prevent text from going out of frame 
    desp_text = df_nodejs['desp'][z]

    dot = str(desp_text).split(".") # to detect end of sentences
    en = str(desp_text).split("\n") # to detect end of lines
    height = len(dot) + len(en) - 2
    width = len(str(desp_text))

    if width > max_width:
        width = max_width
        if len(en) == 1:
            height += 1

    desp_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    desp_textbox.pack(anchor="w", fill="x", padx=15)
    desp_textbox.insert(tk.END, desp_text)
    desp_textbox.configure(state="disabled")
    frame.pack()

    syntax_label = tk.Label(frame.scrollable_frame, text= "Syntax: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    syntax_label.pack(anchor="w", pady=10, padx =10)

    syn_text = str(df_nodejs['Syntax'][z])
    width = len(syn_text)
    height = 1
    syntax_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    syntax_textbox.pack( anchor="w", padx=15)
    syntax_textbox.insert(tk.END, syn_text)
    syntax_textbox.configure(state="disabled")

    param_label = tk.Label(frame.scrollable_frame, text= "Param Description: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    param_label.pack(anchor="w", pady=10, padx =10)

    t1 = str(df_nodejs['Parameters'][z]).split("*")         # spliting parameters and their respective descriptions
    t2 =  str(df_nodejs['param_description'][z]).split("*") 

    for k in range(len(t1)):

        if t1[k] == 'nan' and t2[k] == 'nan':   # to handing nan data in the csv file
            param_text = "no parameters"
        else:
            param_text = t1[k] + " - " + t2[k]
        width = len(param_text)
        height = len(param_text.split(".")) - 1
        if width > max_width:
            width = max_width
            height += 1


        param_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
        param_textbox.pack( anchor="w", padx=15)
        param_textbox.insert(tk.END, param_text)
        param_textbox.configure(state="disabled")

    examaple_label = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    examaple_label.pack(anchor="w", pady=10, padx =10)

    code = str(df_nodejs['example_input'][z]) # variable to store example code
    height = len(code.split("\n"))
    width = len(max(code.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    example_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    example_textbox.pack( anchor="w", padx=15)
    example_textbox.insert(tk.END, code)
    example_textbox.configure(state="disabled")

    output_label = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    output_label.pack(anchor="w", pady=10, padx =10)

    out = str(df_nodejs['example_output'][z]) #variable for storing example output
    height = len(out.split("\n"))
    width = len(max(out.split("\n"), key=len)) + 1
    if width > max_width:
            width = max_width
            height += 1

    output_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold", bg="black", fg="white")
    output_textbox.pack( anchor="w", padx=15)
    output_textbox.insert(tk.END, out)
    output_textbox.configure(state="disabled")

    # dummy label to introduce padding at the end of the frame
    padding = ttk.Label(frame.scrollable_frame)
    padding.pack()

    # close function and escape keybinding for the frame
    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.focus_force()
    root.resizable(width=False, height=False)
    root.title("nodeJS references")


#function to display cpp functions
def open_cpp(z):

    # code block to restrict multiple windows from opening
    # if the root is none a new page is created else old page is destroyed and a new page is created 
    global root
    if root is None:
        root = tk.Tk()
    else:
        try:
            root.destroy()
        except:
            pass
        root = tk.Tk() # new frame

    frame = ScrollableFrame(root) # scrollable frame is made out of normal frame
    
    function_label = tk.Label(root, text = df_cpp['name'][z],  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)
    
    desp_label = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    desp_label.pack(anchor="w", padx =10, pady=10)

    # code block for controlling height and width of the textbox
    max_width = 76 # max width for text, used to prevent text from going out of frame 
    desp_text = df_cpp['desp'][z]

    dot = str(desp_text).split(".") # to detect end of sentences 
    en = str(desp_text).split("\n") # to detect end of lines
    height = len(dot) + len(en) - 2
    width = len(str(desp_text))
    if width > max_width:
        width = max_width
        if len(en) == 1:
            height += 1

    desp_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    desp_textbox.pack(anchor="w", fill="x", padx=15)
    desp_textbox.insert(tk.END, desp_text)
    desp_textbox.configure(state="disabled")
    frame.pack()

    header_label = tk.Label(frame.scrollable_frame, text= "Header file: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    header_label.pack(anchor="w", pady=10, padx =10)
    height = 1
    
    width = len(str(df_cpp['module'][z])) + 1
    header_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    header_textbox.pack( anchor="w", padx=15)
    header_textbox.insert(tk.END, str(df_cpp['module'][z]))
    header_textbox.configure(state="disabled")

    syntax_label = tk.Label(frame.scrollable_frame, text= "Syntax: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    syntax_label.pack(anchor="w", pady=10, padx =10)

    syn_text = str(df_cpp['synx'][z])  # variable for storing syntax text
    height = len(syn_text.split("\n"))
    width = len(max(syn_text.split("\n"), key=len)) + 1

    if width > max_width:
        width = max_width
        height += 1

    syntax_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    syntax_textbox.pack( anchor="w", padx=15)
    syntax_textbox.insert(tk.END, syn_text)
    syntax_textbox.configure(state="disabled")

    param_label = tk.Label(frame.scrollable_frame, text= "Param Description: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    param_label.pack(anchor="w", pady=10, padx =10)

    param_text = str(df_cpp['parameter'][z])
    height = len(param_text.split("\n"))
    width = len(max(param_text.split("\n"), key=len)) + 1
    if width > max_width:
        width = max_width
        height += 1

    param_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    param_textbox.pack( anchor="w", padx=15)
    param_textbox.insert(tk.END, param_text)
    param_textbox.configure(state="disabled")

    examaple_label = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    examaple_label.pack(anchor="w", pady=10, padx =10)

    # for handling height and width of the code/example textbox
    code = str(df_cpp['example'][z])
    c1 = code.split("\t")
    c1 = "        ".join(c1)
    height = len(c1.split("\n"))
    width = len(max(c1.split("\n"), key=len))+1
    if width > max_width:
        width = max_width
        height += 1
    
    example_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    example_textbox.pack( anchor="w", padx=15)
    example_textbox.insert(tk.END, code)
    example_textbox.configure(state="disabled")

    output_label = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    output_label.pack(anchor="w", pady=10, padx =10)

    out = str(df_cpp['output'][z]) # variable to store ouput of the example
    height = len(out.split("\n"))
    width = len(max(out.split("\n"), key=len)) + 1
    if width > max_width:
        width = max_width
        height += 1

    output_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold", bg="black", fg="white")
    output_textbox.pack( anchor="w", padx=15)
    output_textbox.insert(tk.END, out)
    output_textbox.configure(state="disabled")

    # dummy label to introduce padding at the end of the frame
    padding = ttk.Label(frame.scrollable_frame)
    padding.pack()

    # close function and escape keybinding for the frame
    def close(event):
        root.destroy()

    root.focus_force()
    root.bind("<Escape>", close)
    root.resizable(width=False, height=False)
    root.title("Cpp references")


#function to display html tags
def open_html(z):

    path = "images/" + str(df_html['name'][z]).strip() +".png"
    # code block to restrict multiple windows from opening
    # if the root is none a new page is created else old page is destroyed and a new page is created 
    global root
    if root is None:
        root = tk.Toplevel()
    else:
        try:
            root.destroy()
        except:
            pass
        root = tk.Toplevel() # new frame
    
    frame = ScrollableFrame(root) # scrollable frame is made out of normal frame

    tag_label_name = tk.Label(root, text = df_html['name'][z]+" tag",  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)

    tag_label = tk.Label(frame.scrollable_frame, text= "Tag: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    tag_label.pack(anchor="w", pady=10, padx =10)

    tag = str(df_html['tag'][z])
    height = 1
    width = len(tag) + 1

    tag_textbox = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    tag_textbox.pack(anchor="w", padx=15)
    tag_textbox.insert(tk.END, tag)
    tag_textbox.configure(state="disabled")

    desp_label = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    desp_label.pack(anchor="w", padx =10, pady=10)

    # code block for controlling height and width of the textbox
    max_width = 76 # max width for text, used to prevent text from going out of frame 
    desp_text = df_html['desp'][z]
    en = str(desp_text).split("\n")  # to detect end of the line
    height = len(en)
    width = len(max(en, key=len)) + 1
    if width> max_width:
        width = max_width
    for l in en:
        width_l = len(l)
        if width_l > max_width:
            height += 1

    desp_textbox = tk.Text(frame.scrollable_frame, height=height+1, bd=1, width=width, font = "Courier 9 bold")
    desp_textbox.pack(anchor="w", fill="x", padx=15)
    desp_textbox.insert(tk.END, desp_text)
    desp_textbox.configure(state="disabled")
    frame.pack()

    examaple_label = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    examaple_label.pack(anchor="w", pady=10, padx =10)

    code = str(df_html['example_input'][z])  #variable to store example 
    c1 = code.split("\t")
    c1 = "        ".join(c1)
    height = len(c1.split("\n"))
    width = len(max(c1.split("\n"), key=len))+1
    if width > max_width:
        width = max_width
    for l in c1.split("\n"):
        width_l = len(l)
        if width_l > max_width:
            height += 1

    example_textbox = tk.Text(frame.scrollable_frame, height=height+1, bd=1, width=width, font = "Courier 9 bold")
    example_textbox.pack( anchor="w", padx=15)
    example_textbox.insert(tk.END, code)
    example_textbox.configure(state="disabled")

    output_label = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    output_label.pack(anchor="w", pady=10, padx =10)

    # HTML cant be rendered in the tkinter frame
    # To show example output for each tag, images of the html pages
    # are taken and displayed under ouput heading 

    pic = Image.open(path) # output picture stored in "images/" folder
    width, height = pic.size
    canvas = tk.Canvas(frame.scrollable_frame, width = width, height = height)  
    canvas.pack()
    img = ImageTk.PhotoImage(pic)
    canvas.create_image(5, 10, anchor=tk.NW, image=img)

    # dummy label to introduce padding at the end of the frame
    padding = ttk.Label(frame.scrollable_frame)
    padding.pack()

    # close function and escape keybinding for the frame
    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.focus_force()
    root.resizable(width=False, height=False)

    try:
        root.mainloop()
        root.title("Html references")
    except:
        pass


# keybindings page construction
def key_bindings():
    
    root = tk.Tk() # new frame
    main_label = tk.Label(root, text = "Shortcuts",  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)
    
    heading_label = tk.Label(root, text = "Key Code",  font=("Calibri", 15, "bold"), fg="#17609a", bd=5)
    heading_label.place(x=170, y=160)
    heading_label = tk.Label(root, text = "Key",  font=("Calibri", 15, "bold"), fg="#17609a", bd=5)
    heading_label.place(x=365, y=160)
    heading_label = tk.Label(root, text = "Function",  font=("Calibri", 15, "bold"), fg="#17609a", bd=5)
    heading_label.place(x=570, y=160)

    keys_label = tk.Label(root, text = "<q>",  font=("Calibri", 12, "bold"))
    keys_label.place(x=198, y=240)
    keys_label = tk.Label(root, text = "<Escape>",  font=("Calibri", 12, "bold"))
    keys_label.place(x=183, y=290)
    keys_label = tk.Label(root, text = "<Left Arrow>",  font=("Calibri", 12, "bold"))
    keys_label.place(x=173, y=340)

    key_bindings_button = ttk.Button(root, text="Q", width=8)
    key_bindings_button.place(x=360, y=240)
    key_bindings_button = ttk.Button(root, text="Esc", width=8)
    key_bindings_button.place(x=360, y=290)
    key_bindings_button = ttk.Button(root, text="<--", width=8)
    key_bindings_button.place(x=360, y=340)

    instructions_label = tk.Label(root, text = "Quit App, when in Main Menu",  font=("Calibri", 12))
    instructions_label.place(x=520, y=240)
    instructions_label = tk.Label(root, text = "Quit new Windows",  font=("Calibri", 12))
    instructions_label.place(x=545, y=290)
    instructions_label = tk.Label(root, text = "Back to Home",  font=("Calibri", 12))
    instructions_label.place(x=560, y=340)

    # close function and escape keybinding for the frame
    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.focus_force()
    root.geometry("800x600")
    root.title("Shortcuts")
    root.resizable(width=False, height=False)