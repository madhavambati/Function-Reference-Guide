from functions import *
from search import *
from search import AutocompleteEntry
from search import NO_RESULTS_MESSAGE
from tkinter import messagebox


# There is a pcontainer frame in which a parent frame resides
# All the subpages are present at the botoon of the parent page in the container page
# There are 4 subpages indicating different technologies 

# main app class
class tkinterApp(tk.Tk): 
	
	
	def __init__(self, *args, **kwargs): 
		
		
		tk.Tk.__init__(self, *args, **kwargs) 
		
		# container frame intialisation
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# dict to store sub-pages
		self.frames = {}
		
		for F in (Home_Page, Cpp_Page, Python_Page, Node_Page, Html_Page):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		
		self.show_frame(Home_Page)
		self.bind("<Left>", lambda e:self.show_frame(Home_Page, "LEFT"))
	
	# Funtion to show frames
	def show_frame(self, cont, event=None): 
		frame = self.frames[cont]
		frame.tkraise()

	# quit function with warning message
	def quit(self, event=None):
		warning_msgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
		if warning_msgBox == 'yes':
			self.destroy()
		else:
			pass


#class for Homepage, this includes all the buttons and widgets in the homepage
class Home_Page(tk.Frame): 
	def __init__(self, parent, controller): 
		
		tk.Frame.__init__(self, parent)
		heading_label = tk.Label(self, text ="Function Reference Guide", font=("Calibri", 30, 'bold'), fg="#17609a", bd=5) 
		heading_label.pack(pady=20, ipadx=50)
		home_label = tk.Label(self, text ="HOME", font=("Calibri", 20, 'bold'), fg="#17609a", bd=5) 
		home_label.pack(pady=40)

		Cpp_button = ttk.Button(self
			, text ="C++",  cursor="hand2",
		command = lambda : controller.show_frame(Cpp_Page), width=20)
		Cpp_button.place(x=340, y=200)

		
		python_button = ttk.Button(self, text ="Python",  cursor="hand2",
		command = lambda : controller.show_frame(Python_Page), width=20) 
		python_button.place(x=340, y=250)

		nodejs_button = ttk.Button(self, text ="NodeJS",  cursor="hand2",
		command = lambda : controller.show_frame(Node_Page), width=20) 
		nodejs_button.place(x=340, y=300)

		html_button = ttk.Button(self, text ="Html",  cursor="hand2",
		command = lambda : controller.show_frame(Html_Page), width=20) 
		html_button.place(x=340, y=350)

		shortcuts_button = ttk.Button(self, text ="Shortcuts",  cursor="hand2",
		command = key_bindings, width=10) 
		shortcuts_button.place(x=370, y=550)


		
#class for cpp tab, this includes search bar and all the buttons representing respective functions
class Cpp_Page(tk.Frame): 
	
	def __init__(self, parent, controller):

 
		
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="C++",  font="Calibri 25 bold", fg="#17609a", bd=5) 
		label.pack(pady=10)

		# code for making scrollable frame
		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		#Home button to navigate back to home
		home_button = ttk.Button(self.canvas, text ="Home",  cursor="hand2",
							command = lambda : controller.show_frame(Home_Page)) 
		home_button.place(x=30)

		# Search field on the top right corner
		self.entry = AutocompleteEntry(self.canvas)
		# search contents
		cpp_names = df_cpp['name'].tolist()
		cpp_names.append('CPP')

		
		self.build(entries=cpp_names, case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)

		# To display search icon
		pic = Image.open("images/search.png")
		self.img_icon = ImageTk.PhotoImage(pic)
		self.icon_image = tk.Label(self.canvas, image=self.img_icon)
		self.icon_image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)
		

		buttons = {}   # dict for storing different function buttons
		names = df_cpp['name'].unique() # name of the functions
		
		for z in range(len(df_cpp['name'])):
			buttons[df_cpp['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2", text=df_cpp['name'][z], command = lambda z=z: open_cpp(z))
			buttons[df_cpp['name'][z]].pack(pady=10, padx=325)
 
 	# Function to build search functionality
	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"],
        )


#class for python tab, this includes search bar and all the buttons representing respective functions
class Python_Page(tk.Frame): 
	def __init__(self, parent, controller, text=None, des=None,event=None):

 
		tk.Frame.__init__(self, parent) 
		label = tk.Label(self, text ="Python",  font=("Calibri", 25, "bold"), fg="#17609a", bd=5) 
		label.pack(pady=10)

		# code for making scrollable frame
		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		#Home button to navigate back to home
		home_button = ttk.Button(self.canvas, text ="Home", cursor="hand2",
							command = lambda : controller.show_frame(Home_Page)) 
		home_button.place(x=30)

		# Search field on the top right corner
		self.entry = AutocompleteEntry(self.canvas)
		# search contents
		python_names = df_python['name'].tolist()
		python_names.append('PYTHON')

		
		selection = self.build(entries = python_names, case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)

		# To display search icon
		pic = Image.open("images/search.png")
		self.icon_img = ImageTk.PhotoImage(pic)
		self.icon_image = tk.Label(self.canvas, image=self.icon_img)
		self.icon_image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)
		
		buttons = {}  #dict for storing different function buttons
		names = df_python['name'].unique() # name of the functions

		for z in range(len(df_python['name'])):
			buttons[df_python['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2",text=df_python['name'][z], command = lambda z=z: open_py(z))
			buttons[df_python['name'][z]].pack(pady=10, padx=325)

	# Function to build search functionality
	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"])
	

#class for NodeJs tab, this includes search bar and all the buttons representing respective functions
class Node_Page(tk.Frame): 
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent) 
		

		label = tk.Label(self, text ="NodeJS",  font=("Calibri", 25, "bold"), fg="#17609a", bd=5) 
		label.pack(pady=10)

		# code for making scrollable frame
		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		
		#Home button to navigate back to home
		home_button = ttk.Button(self.canvas, text ="Home", cursor="hand2",
							command = lambda : controller.show_frame(Home_Page)) 
		home_button.place(x=30)

		# search contents
		nodejs_names = df_nodejs['name'].tolist()
		nodejs_names.append('NODEJS')

		# Search field on the top right corner
		self.entry = AutocompleteEntry(self.canvas)
		selection = self.build(entries=nodejs_names,case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)

		# To display search icon
		pic = Image.open("images/search.png")
		self.icon_img = ImageTk.PhotoImage(pic)
		self.icon_image = tk.Label(self.canvas, image=self.icon_img)
		self.icon_image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)

		buttons = {} #dict for storing different function buttons
		names = df_nodejs['name'].unique() # name of the functions
		
		for z in range(len(df_nodejs['name'])):
			buttons[df_nodejs['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2", text=df_nodejs['name'][z], command = lambda z=z: open_node(z))
			buttons[df_nodejs['name'][z]].pack(pady=10, padx=315)
	
	# Function to build search functionality
	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )
			

#class for Html tab, this includes search bar and all the buttons representing respective tags
class Html_Page(tk.Frame): 
	def __init__(self, parent, controller): 

		tk.Frame.__init__(self, parent) 
		
		label = tk.Label(self, text ="Html",  font=("Calibri", 25, "bold"), fg="#17609a", bd=5) 
		label.pack(pady=10)
		# code for making scrollable frame
		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief='ridge')
		self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = ttk.Frame(self.canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")
		#Home button to navigate back to home
		home_page = ttk.Button(self.canvas, text ="Home", cursor="hand2",
							command = lambda : controller.show_frame(Home_Page)) 
		home_page.place(x=30)

		# search contents
		html_names = df_html['name'].tolist()
		html_names.append('HTML')

		# Search field on the top right corner
		self.entry = AutocompleteEntry(self.canvas)
		selection = self.build(entries=html_names, 
			case_sensitive=False, no_results_message=NO_RESULTS_MESSAGE)
		self.entry.pack(anchor="ne", ipadx=5, side=tk.RIGHT, expand = False, pady=3)
		
		# To display search icon
		pic = Image.open("images/search.png")
		self.icon_img = ImageTk.PhotoImage(pic)
		self.icon_image = tk.Label(self.canvas, image=self.icon_img)
		self.icon_image.pack(anchor="ne", ipadx=3, side=tk.RIGHT)

		buttons = {} #dict for storing different function buttons
		names = df_html['name'].unique() # name of the functions
		
		for z in range(len(df_html['name'])):
			buttons[df_html['name'][z]] = ttk.Button(self.scrollable_frame, cursor="hand2", text=df_html['name'][z], command = lambda z=z: open_html(z))
			buttons[df_html['name'][z]].pack(pady=10, padx=360)

	# Function to build search functionality
	def build(self, *args, **kwargs):
		self.entry.build(
            kwargs["entries"],
            kwargs["case_sensitive"],
            kwargs["no_results_message"]
        )
			
# App initialization
app = tkinterApp()
# keybinding for quiting app
app.bind("<q>", app.quit)
app.geometry('800x600')
app.resizable(width=False, height=False)
app.title('app')
app.mainloop() 

