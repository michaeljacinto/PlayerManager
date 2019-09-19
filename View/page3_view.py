import tkinter as tk


class Page3View(tk.Frame):
    """ Page 3 """

    def __init__(self, parent, submit_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        self._submit_callback = submit_callback

        self._data = ["first_name", "last_name", "member_num", "annual_salary", "contract_years_length", "type"]

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 3 """

        self._entry_name = tk.Listbox(self)
        self._entry_name.grid(row=1,column=1)

        self._button = tk.Button(self,
                                 text="Refresh",
                                 command=self._submit_callback)
        self._button.grid(row=2,column=1,padx=20)

    def set_form_data(self, all):
        self._entry_name.delete(0, tk.END)
        for item in all:
            self._entry_name.insert(tk.END, "%d. %s %s (%s)" % (item['id'], item['first_name'], item['last_name'],
                                                          item['member_num']))





