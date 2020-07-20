from functions import *
from search import AutocompleteEntry
from search import NO_RESULTS_MESSAGE
from search import *


class tkinterApp(tk.Tk): 
	
	
	def __init__(self, *args, **kwargs): 
		
		
		tk.Tk.__init__(self, *args, **kwargs) 
		
		
		container = tk.Frame(self)

		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		
		self.frames = {}
		
		for F in (StartPage, Page1, Page2, Page3, Page4):
			


			frame = F(container, self)
		
		
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		
		self.show_frame(StartPage)
		self.bind("<Left>", lambda e:self.show_frame(StartPage, "LEFT"))
	
	def show_frame(self, cont, event=None): 
		frame = self.frames[cont]
		frame.tkraise()

	def quit(self, event=None):
		self.destroy()



class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text ="Function Reference Guide", font=("Calibri", 30, 'bold'), fg="#17609a", bd=5) 
		label.pack(pady=20, ipadx=50)
		label = tk.Label(self, text ="HOME", font=("Calibri", 20, 'bold'), fg="#17609a", bd=5) 
		
		label.pack(pady=40)


		

		button1 = ttk.Button(self
			, text ="C++",  cursor="hand2",
		command = lambda : controller.show_frame(Page1), width=20)
		button1.place(x=340, y=200)

		
		button2 = ttk.Button(self, text ="Python",  cursor="hand2",
		command = lambda : controller.show_frame(Page2), width=20) 
		button2.place(x=340, y=250)

		button3 = ttk.Button(self, text ="NodeJS",  cursor="hand2",
		command = lambda : controller.show_frame(Page3), width=20) 
		button3.place(x=340, y=300)

		button4 = ttk.Button(self, text ="Html",  cursor="hand2",
		command = lambda : controller.show_frame(Page4), width=20) 
		button4.place(x=340, y=350)

		button4 = ttk.Button(self, text ="Shortcuts",  cursor="hand2",
		command = key_bindings, width=10) 
		button4.place(x=370, y=550)


		

class Page1(tk.Frame): 
	
	def __init__(self, parent, controller):

 
		
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="C++",  font="Calibri 25 bold", fg="#17609a", bd=5) 
		label.pack(pady=10)

		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		home = ttk.Button(self.canvas, text ="Home",  cursor="hand2",
							command = lambda : controller.show_frame(StartPage)) 
		home.place(x=30)
		self.entry = AutocompleteEntry(self.canvas)

		cpp_names = df_cpp['name'].tolist()
		cpp_names.append('CPP')

		
		self.build(entries=cpp_names, case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)

		pic = Image.open("images/search.png")
		width, height = pic.size
		self.img = ImageTk.PhotoImage(pic)
		self.image = tk.Label(self.canvas, image=self.img)
		self.image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)
		

		buttons = {}
		functions = {}
		names = df_cpp['name'].unique()
		


		for z in range(len(df_cpp['name'])):

			buttons[df_cpp['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2", text=df_cpp['name'][z], command = lambda z=z: open_cpp(z))
			buttons[df_cpp['name'][z]].pack(pady=10, padx=325)

	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"],
        )
	def _on_mousewheel(self, event):
		print(event.widget)

		if "page1" in str(event.widget):
			if event.num == 4 or event.delta == 120:
				self.canvas.yview_scroll(-1, "units")
			elif event.num == 5 or event.delta == -120:
				self.canvas.yview_scroll(1, "units")


class Page2(tk.Frame): 
	def __init__(self, parent, controller, text=None, des=None,event=None):

 
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="Python",  font=("Calibri", 25, "bold"), fg="#17609a", bd=5) 
		label.pack(pady=10)

		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		home = ttk.Button(self.canvas, text ="Home", cursor="hand2",
							command = lambda : controller.show_frame(StartPage)) 
		home.place(x=30)
		self.entry = AutocompleteEntry(self.canvas)

		python_names = df_python['name'].tolist()
		python_names.append('PYTHON')

		pic = Image.open("images/search.png")
		width, height = pic.size
		
		
		selection = self.build(entries = python_names, case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)

		self.img = ImageTk.PhotoImage(pic)
		self.image = tk.Label(self.canvas, image=self.img)
		self.image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)
		
		
		buttons = {}
		functions = {}
		names = df_python['name'].unique()
		

		
		for z in range(len(df_python['name'])):
			
			
			buttons[df_python['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2",text=df_python['name'][z], command = lambda z=z: open_py(z))

			buttons[df_python['name'][z]].pack(pady=10, padx=325)

	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"])
	

		


class Page3(tk.Frame): 
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent) 
		

		label = tk.Label(self, text ="NodeJS",  font=("Calibri", 25, "bold"), fg="#17609a", bd=5) 
		label.pack(pady=10)

		

		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		home = ttk.Button(self.canvas, text ="Home", cursor="hand2",
							command = lambda : controller.show_frame(StartPage)) 
		home.place(x=30)


		nodejs_names = df_nodejs['name'].tolist()
		nodejs_names.append('NODEJS')

		self.entry = AutocompleteEntry(self.canvas)
		selection = self.build(entries=nodejs_names,case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)
		
		pic = Image.open("images/search.png")
		width, height = pic.size
		self.img = ImageTk.PhotoImage(pic)
		self.image = tk.Label(self.canvas, image=self.img)
		self.image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)

		buttons = {}
		functions = {}
		names = df_nodejs['name'].unique()
		


		for z in range(len(df_nodejs['name'])):
			
			
			buttons[df_nodejs['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2", text=df_nodejs['name'][z], command = lambda z=z: open_node(z))
			buttons[df_nodejs['name'][z]].pack(pady=10, padx=315)
	
	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )
			


class Page4(tk.Frame): 
	def __init__(self, parent, controller): 

		tk.Frame.__init__(self, parent) 
		
		label = tk.Label(self, text ="Html",  font=("Calibri", 25, "bold"), fg="#17609a", bd=5) 
		label.pack(pady=10)

		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		home = ttk.Button(self.canvas, text ="Home", cursor="hand2",
							command = lambda : controller.show_frame(StartPage)) 
		home.place(x=30)


		html_names = df_html['name'].tolist()
		html_names.append('HTML')

		self.entry = AutocompleteEntry(self.canvas)
		selection = self.build(entries=html_names, 

			case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)
		

		pic = Image.open("images/search.png")
		width, height = pic.size
		self.img = ImageTk.PhotoImage(pic)
		self.image = tk.Label(self.canvas, image=self.img)
		self.image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)

		buttons = {}
		functions = {}
		names = df_html['name'].unique()
		


		for z in range(len(df_html['name'])):
			
			
			buttons[df_html['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2", text=df_html['name'][z], command = lambda z=z: open_html(z))
			buttons[df_html['name'][z]].pack(pady=10, padx=360)

	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )
			

app = tkinterApp()
app.bind("<q>", app.quit)
app.geometry('800x600')
app.resizable(width=False, height=False)
app.title('app')
app.mainloop() 

