import tkinter as tk


class Page0View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, submit_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        self._submit_callback = submit_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """

        # self._label = tk.Label(self, text="Enter Your Name:")
        # self._label.grid(row=,column=0,padx=20)

        self._label = tk.Label(self, text="Player(s)")

        # my_data = self.set_form_data()

        self._label.grid(row=0,column=1,padx=20)

        self._entry_name = tk.Listbox(self)

        self._entry_name.grid(row=2,column=1)

        # self._button_refresh = tk.Button(self,
        #                          text="Refresh",
        #                          command=self._submit_callback)

        # self._button_refresh.grid(row=1, column=0, padx=10)

        # self._button_add = tk.Button(self,
        #                          text="Add")
        #
        # self._button_add.grid(row=1, column=1, padx=10)
        #
        # self._button_delete = tk.Button(self,
        #                           text="Delete")
        #
        # self._button_delete.grid(row=1, column=2, padx=10)
        #
        # self._button_update = tk.Button(self,
        #                                 text="Update")
        #
        # self._button_update.grid(row=1, column=3, padx=10)
        #
        # self._button_get_details = tk.Button(self,
        #                                      text="Get Details")
        #
        # self._button_get_details.grid(row=1, column=4, padx=10)

    def get_form_data(self):
        return { "name": self._entry_name.get() }

    def set_form_data(self, my_list):
        print('test')
        print(type(my_list))
        print(my_list)

        self._entry_name.delete(0, tk.END)

        self._entry_name.insert(len(my_list), tk.END)

        for i in my_list:
            info = '%s %s (%s)' % (i["first_name"], i["last_name"], i["member_num"])
            self._entry_name.insert(tk.END, info)