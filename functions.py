import tkinter as tk 
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image

global df_python
global df_nodejs
global df_cpp
global df_html
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

    def _on_mousewheel(self, event):
        try:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        except:
            pass


#function to display python functions
def open_py(z):

    global root
    if root is None:
        root = tk.Tk()
    else:
        try:
            root.destroy()
        except:
            pass

        root = tk.Tk()
    
    frame = ScrollableFrame(root)
    buttons = {}
    functions = {}
    label = tk.Label(root, text = df_python['name'][z],  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)

        #ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

    l1 = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    #l1.place(x=10, y=20)
    l1.pack(anchor="w", padx =10, pady=10)



    max_width = 76
    desp_text = df_python['desp'][z]
    height = len(str(desp_text).split(".")) - 1

    width = len(str(desp_text))

    if width > max_width:
        width = max_width
        height += 1


    t_des = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_des.pack(anchor="w", fill="x", padx=15)
    t_des.insert(tk.END, desp_text)
    t_des.configure(state="disabled")
    frame.pack()

    l2 = tk.Label(frame.scrollable_frame, text= "Syntax: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l2.pack(anchor="w", pady=10, padx =10)


    syn_text = str(df_python['Syntax'][z])
    width = len(syn_text)
    height = 1
    t_syn = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_syn.pack( anchor="w", padx=15)
    t_syn.insert(tk.END, syn_text)
    t_syn.configure(state="disabled")

    l2 = tk.Label(frame.scrollable_frame, text= "Param Description: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l2.pack(anchor="w", pady=10, padx =10)

    t1 = str(df_python['Parameters'][z]).split("/")
    t2 =  str(df_python['param_description'][z]).split("/")

    for k in range(len(t1)):

        if t1[k] == 'nan' and t2[k] == 'nan':
            param_text = "no parameters"
        else:
            param_text = t1[k] + " - " + t2[k]
        width = len(param_text)
        height = len(param_text.split(".")) - 1
        if width > max_width:
            width = max_width
            height += 1


        t_param = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
        t_param.pack( anchor="w", padx=15)
        t_param.insert(tk.END, param_text)
        t_param.configure(state="disabled")

    l3 = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l3.pack(anchor="w", pady=10, padx =10)

    code = str(df_python['example_input'][z])
    height = len(code.split("\n"))
    width = len(max(code.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    t_code = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_code.pack( anchor="w", padx=15)
    t_code.insert(tk.END, code)
    t_code.configure(state="disabled")


    l4 = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    l4.pack(anchor="w", pady=10, padx =10)

    out = str(df_python['example_output'][z])
    height = len(out.split("\n"))

    width = len(max(out.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    t_out = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold", bg="black", fg="white")
    t_out.pack( anchor="w", padx=15)
    t_out.insert(tk.END, out)
    t_out.configure(state="disabled")

    padd = ttk.Label(frame.scrollable_frame)
    padd.pack()

    def close(event):
        root.destroy()
    root.bind("<Escape>", close)

    root.focus_force()
    root.resizable(width=False, height=False)
    root.title("python references")



#function to display Nodejs functions
def open_node(z):
    global root
    if root is None:
        root = tk.Tk()
    else:
        try:
            root.destroy()
        except:
            pass
        root = tk.Tk()
    
    
    frame = ScrollableFrame(root)
    buttons = {}
    functions = {}
    label = tk.Label(root, text = df_nodejs['name'][z],  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)

    l1 = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    #l1.place(x=10, y=20)
    l1.pack(anchor="w", padx =10, pady=10)



    max_width = 76
    desp_text = df_nodejs['desp'][z]

    dot = str(desp_text).split(".")
    en = str(desp_text).split("\n")
    height = len(dot) + len(en) - 2
 
    width = len(str(desp_text))

    if width > max_width:
        width = max_width
        if len(en) == 1:

            height += 1
        


    t_des = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_des.pack(anchor="w", fill="x", padx=15)
    t_des.insert(tk.END, desp_text)
    t_des.configure(state="disabled")
    frame.pack()

    l2 = tk.Label(frame.scrollable_frame, text= "Syntax: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l2.pack(anchor="w", pady=10, padx =10)


    syn_text = str(df_nodejs['Syntax'][z])
    width = len(syn_text)
    height = 1
    t_syn = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_syn.pack( anchor="w", padx=15)
    t_syn.insert(tk.END, syn_text)
    t_syn.configure(state="disabled")

    l2 = tk.Label(frame.scrollable_frame, text= "Param Description: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l2.pack(anchor="w", pady=10, padx =10)

    t1 = str(df_nodejs['Parameters'][z]).split("*")
    t2 =  str(df_nodejs['param_description'][z]).split("*")

    for k in range(len(t1)):

        if t1[k] == 'nan' and t2[k] == 'nan':
            param_text = "no parameters"
        else:
            param_text = t1[k] + " - " + t2[k]
        width = len(param_text)
        height = len(param_text.split(".")) - 1
        if width > max_width:
            width = max_width
            height += 1


        t_param = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
        t_param.pack( anchor="w", padx=15)
        t_param.insert(tk.END, param_text)
        t_param.configure(state="disabled")

    l3 = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l3.pack(anchor="w", pady=10, padx =10)

    code = str(df_nodejs['example_input'][z])
    height = len(code.split("\n"))
    width = len(max(code.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    t_code = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_code.pack( anchor="w", padx=15)
    t_code.insert(tk.END, code)
    t_code.configure(state="disabled")


    l4 = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    l4.pack(anchor="w", pady=10, padx =10)

    out = str(df_nodejs['example_output'][z])
    height = len(out.split("\n"))

    width = len(max(out.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    t_out = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold", bg="black", fg="white")
    t_out.pack( anchor="w", padx=15)
    t_out.insert(tk.END, out)
    t_out.configure(state="disabled")

    padd = ttk.Label(frame.scrollable_frame)
    padd.pack()
    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.focus_force()
    root.resizable(width=False, height=False)
    root.title("nodeJS references")


#function to display cpp functions
def open_cpp(z):
    global root
    if root is None:
        root = tk.Tk()
    else:
        try:
            root.destroy()
        except:
            pass
        root = tk.Tk()
    
    
    frame = ScrollableFrame(root)
    label = tk.Label(root, text = df_cpp['name'][z],  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)
    l1 = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l1.pack(anchor="w", padx =10, pady=10)



    max_width = 76
    desp_text = df_cpp['desp'][z]

    dot = str(desp_text).split(".")
    en = str(desp_text).split("\n")
    height = len(dot) + len(en) - 2
    
    width = len(str(desp_text))

    if width > max_width:
        width = max_width
        if len(en) == 1:

            height += 1
        


    t_des = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_des.pack(anchor="w", fill="x", padx=15)
    t_des.insert(tk.END, desp_text)
    t_des.configure(state="disabled")
    frame.pack()

    hf = tk.Label(frame.scrollable_frame, text= "Header file: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    hf.pack(anchor="w", pady=10, padx =10)
    height = 1
    width = len(str(df_cpp['module'][z])) + 1


    h_t = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    h_t.pack( anchor="w", padx=15)
    h_t.insert(tk.END, str(df_cpp['module'][z]))
    h_t.configure(state="disabled")
    


    l2 = tk.Label(frame.scrollable_frame, text= "Syntax: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l2.pack(anchor="w", pady=10, padx =10)


    syn_text = str(df_cpp['synx'][z])

    height = len(syn_text.split("\n"))
    width = len(max(syn_text.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    
    t_syn = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_syn.pack( anchor="w", padx=15)
    t_syn.insert(tk.END, syn_text)
    t_syn.configure(state="disabled")

    l2 = tk.Label(frame.scrollable_frame, text= "Param Description: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l2.pack(anchor="w", pady=10, padx =10)

    param_text = str(df_cpp['parameter'][z])
    height = len(param_text.split("\n"))
    width = len(max(param_text.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1
    

    t_param = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_param.pack( anchor="w", padx=15)
    t_param.insert(tk.END, param_text)
    t_param.configure(state="disabled")

    l3 = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l3.pack(anchor="w", pady=10, padx =10)

    code = str(df_cpp['example'][z])

    c1 = code.split("\t")
    c1 = "        ".join(c1)

    height = len(c1.split("\n"))
    width = len(max(c1.split("\n"), key=len))+1
   
    

    #if '\t' in max(code.split("\n")):
     #   width += 1

    if width > max_width:
            width = max_width
            height += 1
    
    t_code = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_code.pack( anchor="w", padx=15)
    t_code.insert(tk.END, code)
    t_code.configure(state="disabled")


    l4 = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    l4.pack(anchor="w", pady=10, padx =10)

    out = str(df_cpp['output'][z])
    height = len(out.split("\n"))

    width = len(max(out.split("\n"), key=len)) + 1

    if width > max_width:
            width = max_width
            height += 1

    t_out = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold", bg="black", fg="white")
    t_out.pack( anchor="w", padx=15)
    t_out.insert(tk.END, out)
    t_out.configure(state="disabled")

    padd = ttk.Label(frame.scrollable_frame)
    padd.pack()

    root.focus_force()
    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.resizable(width=False, height=False)
    root.title("Cpp references")


#function to display html tags
def open_html(z):
    path = "images/" + str(df_html['name'][z]).strip() +".png"
    global root
    if root is None:
        root = tk.Toplevel()
    else:
        try:
            root.destroy()
        except:
            pass
        root = tk.Toplevel()
    
    frame = ScrollableFrame(root)
    

   
    label = tk.Label(root, text = df_html['name'][z]+" tag",  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)
    

    l_t = tk.Label(frame.scrollable_frame, text= "Tag: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l_t.pack(anchor="w", pady=10, padx =10)


    tag = str(df_html['tag'][z])
    height = 1
    width = len(tag) + 1

    t_tag = tk.Text(frame.scrollable_frame, height=height, bd=1, width=width, font = "Courier 9 bold")
    t_tag.pack(anchor="w", padx=15)
    t_tag.insert(tk.END, tag)
    t_tag.configure(state="disabled")



    l1 = tk.Label(frame.scrollable_frame, text= "Definition: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    #l1.place(x=10, y=20)
    l1.pack(anchor="w", padx =10, pady=10)



    max_width = 76
    desp_text = df_html['desp'][z]
    en = str(desp_text).split("\n")
    height = len(en)
    
    width = len(max(en, key=len)) + 1
    if width> max_width:
        width = max_width
    for l in en:
        width_l = len(l)
        if width_l > max_width:
            height += 1
        


    t_des = tk.Text(frame.scrollable_frame, height=height+1, bd=1, width=width, font = "Courier 9 bold")
    t_des.pack(anchor="w", fill="x", padx=15)
    t_des.insert(tk.END, desp_text)
    t_des.configure(state="disabled")

    frame.pack()

    l3 = tk.Label(frame.scrollable_frame, text= "Example: ", font = "Verdana 13 bold", fg="#17609a", bd=5)
    l3.pack(anchor="w", pady=10, padx =10)

    code = str(df_html['example_input'][z])

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

    t_code = tk.Text(frame.scrollable_frame, height=height+1, bd=1, width=width, font = "Courier 9 bold")
    t_code.pack( anchor="w", padx=15)
    t_code.insert(tk.END, code)
    t_code.configure(state="disabled")


    l4 = tk.Label(frame.scrollable_frame, text= "Output: ", font = "Verdana 10 bold", fg="#17609a", bd=5)
    l4.pack(anchor="w", pady=10, padx =10)


    


    pic = Image.open(path)
    width, height = pic.size
    canvas = tk.Canvas(frame.scrollable_frame, width = width, height = height)  
    canvas.pack()
    img = ImageTk.PhotoImage(pic)
    canvas.create_image(5, 10, anchor=tk.NW, image=img)


    padd = ttk.Label(frame.scrollable_frame)
    padd.pack()

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
    
    root = tk.Tk()
    label = tk.Label(root, text = "Shortcuts",  font=("Calibri", 23, "bold"), fg="#17609a", bd=5).pack(pady=10)
    
    label = tk.Label(root, text = "Key Code",  font=("Calibri", 15, "bold"), fg="#17609a", bd=5)
    label.place(x=170, y=160)
    label = tk.Label(root, text = "Key",  font=("Calibri", 15, "bold"), fg="#17609a", bd=5)
    label.place(x=365, y=160)
    label = tk.Label(root, text = "Function",  font=("Calibri", 15, "bold"), fg="#17609a", bd=5)
    label.place(x=570, y=160)

    label = tk.Label(root, text = "<q>",  font=("Calibri", 12, "bold"))
    label.place(x=198, y=240)
    label = tk.Label(root, text = "<Escape>",  font=("Calibri", 12, "bold"))
    label.place(x=183, y=290)
    label = tk.Label(root, text = "<Left Arrow>",  font=("Calibri", 12, "bold"))
    label.place(x=173, y=340)

    button = ttk.Button(root, text="Q", width=8)
    button.place(x=360, y=240)
    button = ttk.Button(root, text="Esc", width=8)
    button.place(x=360, y=290)
    button = ttk.Button(root, text="<--", width=8)
    button.place(x=360, y=340)

    label = tk.Label(root, text = "Quit App, when in Main Menu",  font=("Calibri", 12))
    label.place(x=520, y=240)
    label = tk.Label(root, text = "Quit new Windows",  font=("Calibri", 12))
    label.place(x=545, y=290)
    label = tk.Label(root, text = "Back to Home",  font=("Calibri", 12))
    label.place(x=560, y=340)

    def close(event):
        root.destroy()
    root.bind("<Escape>", close)
    root.focus_force()
    root.geometry("800x600")
    root.title("Shortcuts")
    root.resizable(width=False, height=False)