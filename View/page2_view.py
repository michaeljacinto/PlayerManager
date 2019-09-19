import tkinter as tk
import requests
from tkinter import messagebox as tkMessageBox


class Page2View(tk.Frame):
    """ Page 2 """

    def __init__(self, parent, submit_callback, page_popup_callback, page_popup_callback_update_coach):
        """ Initialize Page 2 """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._submit_callback = submit_callback
        self._page_popup_callback = page_popup_callback
        self._page_popup_callback_update_coach = page_popup_callback_update_coach
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 2 """

        self._label = tk.Label(self, text="Coach(es)")

        self._label.grid(row=1, column=2, padx=10)

        self._entry_name = tk.Listbox(self)

        self._entry_name.grid(row=2, column=1, rowspan=15, columnspan=3)

        self._button_add = tk.Button(self,
                                     text="ADD",
                                     command=self._page_popup_callback)
        self._button_add.grid(column=0, row=2, pady=3)

        self._button_delete = tk.Button(self,
                                        text="DELETE",
                                        fg="red",
                                        command=self._delete)
        self._button_delete.grid(column=0, row=3, pady=3)

        self._button_update = tk.Button(self,
                                        text="UPDATE",
                                        command=self._page_popup_callback_update_coach)
        self._button_update.grid(column=0, row=4, pady=3)

        self._button = tk.Button(self,
                                 text="REFRESH",
                                 command=self._submit_callback)

        self._button.grid(row=5, column=0, pady=3)

        self._button_get_details = tk.Button(self,
                                             text="GET DETAILS",
                                             command=self._get_details)
        self._button_get_details.grid(column=0, row=6, pady=3)

    def set_form_data(self, json):

        self._entry_name.delete(0, tk.END)
        for member in json:
            if member['type'] == "Coach":
                self._entry_name.insert(tk.END, '%d. %s %s (%s)' % (member['id'], member['first_name'],
                                                                    member['last_name'], member['member_num']))

    def update_index(self):
        try:
            index = self._entry_name.get(self._entry_name.curselection()[0])
            index_num = index.split('.')
            # response = requests.get('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(index_num[0]))
            # coach_data = response.json()
            return int(index_num[0])

        except Exception:
            tkMessageBox.showerror("Error", "You need to select a member.")

    def _get_details(self):

        index = self._entry_name.get(self._entry_name.curselection()[0])
        index_num = index.split('.')
        response = requests.get('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(index_num[0]))
        coach_data = response.json()

        if response.status_code == 200:
            tkMessageBox.showinfo("Details", "ID: %s\n"
                                             "Name: %s %s\n"
                                             "Member #:%s\n"
                                             "Annual Salary: %d\n"
                                             "Contract Length (Years): %d\n"
                                             "Last team: %s\n"
                                             "Type: Coach\n"
                                             "Specialization: %s\n"
                                             "Former Player: %s" % (coach_data["id"],coach_data["first_name"], coach_data["last_name"],
                                                                    coach_data["member_num"], coach_data["annual_salary"],
                                                                    coach_data["contract_years_length"],
                                                                    coach_data["last_team"], coach_data["specialization"], coach_data["is_former_player"]))

    def _delete(self):
        if tkMessageBox.askyesno('Delete Coach', 'Are you sure you want to delete this coach?'):
            index = self._entry_name.get(self._entry_name.curselection()[0])
            index_num = index.split('.')

            response = requests.delete('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(index_num[0]))
            if response.status_code == 200:
                tkMessageBox.showinfo("Success", "ID: %s has been deleted" % index_num[0])
                self._entry_name.delete(tk.ANCHOR)
            else:
                tkMessageBox.showerror("Error", response.content)

    def _update(self):
        pass
