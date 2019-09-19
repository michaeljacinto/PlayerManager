import tkinter as tk


class BottomNavbarView(tk.Frame):
    """ Navigation Bar """

    def __init__(self, parent, quit_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        # self._add_callback = add_callback
        self._quit_callback = quit_callback
        self._create_widgets()

    def _create_widgets(self):
        self._button = tk.Button(self,
                           text="QUIT",
                           command=self._quit_callback)
        self._button.grid(column=1,row=1)
        # self._button.grid(column=2)

        # self._button_add = tk.Button(self,
        #                          text="ADD",
        #                          fg="blue",
        #                          command=self._add_callback)
        # self._button_add.grid(column=2,row=1)
        #
        # self._button_delete = tk.Button(self,
        #                              text="DELETE",
        #                              fg="red",
        #                              command=self._quit_callback)
        # self._button_delete.grid(column=3, row=1)
        #
        # self._button_update = tk.Button(self,
        #                              text="UPDATE",
        #                              fg="green",
        #                              command=self._quit_callback)
        # self._button_update.grid(column=4, row=1)
        #
        # self._button_get_details = tk.Button(self,
        #                              text="GET DETAILS",
        #                              command=self._quit_callback)
        # self._button_get_details.grid(column=5, row=1)