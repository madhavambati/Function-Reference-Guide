from functions import *


__all__ = ["AutocompleteEntry"]
NO_RESULTS_MESSAGE = "No results found"


# To open the search result
def search_key(key, entries):

    if entries[-1] == "CPP":

        try:
            idx = df_cpp['name'].tolist().index(key)
            open_cpp(idx)
        except:
            pass
        
    if entries[-1] == "PYTHON":
        
        try:
            idx = df_python['name'].tolist().index(key)
            open_py(idx)
        except:
            pass
        
    if entries[-1] == "NODEJS":
        try:

            idx = df_nodejs['name'].tolist().index(key)
            open_node(idx)
        except:
            pass

    if entries[-1] == "HTML":
        try:
            idx = df_html['name'].tolist().index(key)
            open_html(idx)
        except:
            pass

# class for Search results
# initiating doesnt start the class, build the class after initiating
#build function is down below
class AutocompleteEntry(tk.Frame, object):
    
    LISTBOX_HEIGHT = 5
    LISTBOX_WIDTH = 25
    ENTRY_WIDTH = 25

    def __init__(self, *args, **kwargs):
        
        super(AutocompleteEntry, self).__init__(*args, **kwargs)
        self.text = tk.StringVar()
        self.entry = ttk.Entry(
            self,
            textvariable=self.text,validate="focusout",
            width=self.ENTRY_WIDTH
        )



        self.entry.bind_all("<Escape>", lambda event:event.widget.focus_set())
        self.listbox = tk.Listbox(
            self,
            height=self.LISTBOX_HEIGHT,
            width=self.LISTBOX_WIDTH, cursor="hand2",
        )


    def build(
              self,
              entries,
              max_entries=5,
              case_sensitive=False,
              no_results_message=NO_RESULTS_MESSAGE
            ):
        
        if not case_sensitive:
            entries = [entry.lower() for entry in entries]

        self._case_sensitive = case_sensitive
        self._entries = entries
        self._no_results_message = no_results_message
        self._listbox_height = max_entries

        self.entry.bind("<KeyRelease>", self._update_autocomplete)
        self.entry.focus()
        self.entry.grid(column=0, row=0)

        self.listbox.bind("<<ListboxSelect>>", self._select_entry)
        self.listbox.grid(column=0, row=1)
        self.listbox.grid_forget()
        
        
        

    def _update_autocomplete(self, event):
       
        self.listbox.delete(0, tk.END)
        self.listbox["height"] = self._listbox_height

        text = self.text.get()
        if not self._case_sensitive:
            text = text.lower()
        if not text:
            self.listbox.grid_forget()
        else:
            for entry in self._entries:
                if text in entry.strip():
                    self.listbox.insert(tk.END, entry)

        listbox_size = self.listbox.size()
        if not listbox_size:
            if self._no_results_message is None:
                self.listbox.grid_forget()
            else:
                try:
                    self.listbox.insert(
                        tk.END,
                        self._no_results_message.format(text)
                    )
                except UnicodeEncodeError:
                    self.listbox.insert(
                        tk.END,
                        self._no_results_message.format(
                            text.encode("utf-8")
                        )
                    )
                if listbox_size <= self.listbox["height"]:
                    # In case there's less entries than the maximum
                    # amount of entries allowed, resize the listbox.
                    self.listbox["height"] = listbox_size
                self.listbox.grid()
        else:
            if listbox_size <= self.listbox["height"]:
                self.listbox["height"] = listbox_size
            self.listbox.grid()

    def _select_entry(self, event):
        
        widget = event.widget

        try:
            value = widget.get(int(widget.curselection()[0]))
            search_key(value, self._entries)
            self.text.set(value)
        except:
            print("went to except")


        
        
        
        
