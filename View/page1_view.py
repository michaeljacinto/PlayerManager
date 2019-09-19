import tkinter as tk
import requests
from tkinter import messagebox as tkMessageBox



class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, get_all, get, get_coach, get_player, delete, add, update, view_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        # self._submit_callback = submit_callback
        # self._page_popup_callback = page_popup_callback
        # self._page_popup_callback_update = page_popup_callback_update
        self._which_members = tk.IntVar()

        self._get_all = get_all
        self._get = get
        self._get_coach = get_coach
        self._get_player = get_player
        self._delete = delete
        self._add = add
        self._update = update
        self._view_callback = view_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """

        tk.Label(self,
                text="Select Type:").grid(row=0, column=0)

        self._which_members = tk.IntVar()

        tk.Radiobutton(self,
                    text="All",
                    variable=self._which_members,
                    command=self._switch_list,
                    value=0).grid(row=0, column=1)

        tk.Radiobutton(self,
                    text="Coach",
                    variable=self._which_members,
                    command=self._switch_list,
                    value=1).grid(row=0, column=2)

        tk.Radiobutton(self,
                    text="Player",
                    variable=self._which_members,
                    command=self._switch_list,
                    value=2).grid(row=0, column=3)



        self._label = tk.Label(self, text="Members:")
        self._label.grid(row=1, column=2)

        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self._listbox = tk.Listbox(self, yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self._listbox.yview)
        self._listbox.grid(row=2, columnspan=3, sticky=tk.W+tk.E, padx=10)
        self._scrollbar.grid(row=2, column=3, sticky=tk.N+tk.S+tk.W)

        self._refresh(self._get_all())

        tk.Button(self,
                text="View",
                command=self._view
                ).grid(row=3, column=1, sticky=tk.W+tk.E)

        tk.Button(self,
                text="Update",
                command=self._update).grid(row=3, column=2, sticky=tk.W+tk.E)

        tk.Button(self,
                text="Add",
                command=self._add_popup_callback).grid(row=4, column=1, sticky=tk.W+tk.E)

        tk.Button(self,
                text="Delete",
                command=self._delete).grid(row=4, column=2, sticky=tk.W+tk.E)


    def _switch_list(self):
        selection = self._which_members.get()
        if selection == 0:
            self._refresh(self._get_all())

        elif selection == 1:
            self._refresh(self._get_coach())

        elif selection == 2:
            self._refresh(self._get_player())

    def set_form_data(self, json):
        self._entry_name.delete(0, tk.END)

        for member in json:
            if member['type'] == "Player":
                self._entry_name.insert(tk.END, '%d. %s %s (%s)' % (member['id'], member['first_name'],
                                                                    member['last_name'], member['member_num']))

    def update_index(self):
        try:
            index = self._entry_name.get(self._entry_name.curselection()[0])
            index_num = index.split('.')
            return int(index_num[0])

        except Exception:
            tkMessageBox.showerror("Error", 'You need to select a member.')

    def _delete(self):

        if tkMessageBox.askyesno('Delete Player', 'Are you sure you want to delete this player?'):
            index = self._entry_name.get(self._entry_name.curselection()[0])
            index_num = index.split('.')

            response = requests.delete('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(index_num[0]))

            if response.status_code == 200:
                tkMessageBox.showinfo("Success", "ID: %s has been deleted" % index_num[0])
                self._entry_name.delete(tk.ANCHOR)
            else:
                tkMessageBox.showerror("Error", response.content)

    def _get_details(self):

        index = self._entry_name.get(self._entry_name.curselection()[0])
        index_num = index.split('.')
        response = requests.get('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(index_num[0]))
        player_data = response.json()

        if response.status_code == 200:
            tkMessageBox.showinfo("Details", "ID: %s\n"
                                             "Name: %s %s\n"
                                             "Member #:%s\n"
                                             "Annual Salary: %d\n"
                                             "Contract Length (Years): %d\n"
                                             "Last team: %s\n"
                                             "Type: Player\n"
                                             "Jersey #: %d\n"
                                             "Position: %s" % (player_data["id"], player_data["first_name"], player_data["last_name"],
                                                               player_data["member_num"], player_data["annual_salary"],
                                                               player_data["contract_years_length"], player_data["last_team"]
                                                               , player_data["jersey_num"], player_data["position"]))

        else:
            tkMessageBox.showerror("Error", "You need to select something.")