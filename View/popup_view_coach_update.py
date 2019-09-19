import tkinter as tk
from tkinter import messagebox as tkMessageBox
import requests


class CoachPopupViewUpdate(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback, coach_index):
        """ Initialize the nav bar """

        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)
        self._close_popup_callback = close_popup_callback
        self._coach_index = coach_index
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

    def _create_widgets(self):

        coach_data = self._get_coach()

        self._label_first_name = tk.Label(self, text='First name:')
        self._label_first_name.grid(row=1, column=0, padx=20)
        self._entry_first_name = tk.Entry(self)
        self._entry_first_name.insert(0, coach_data["first_name"])
        self._entry_first_name.grid(row=1,column=1,padx=10)

        self._label_last_name = tk.Label(self, text='Last name:')
        self._label_last_name.grid(row=2, column=0, padx=20)
        self._entry_last_name = tk.Entry(self)
        self._entry_last_name.insert(0, coach_data["last_name"])
        self._entry_last_name.grid(row=2, column=1, padx=10)

        self._label_member_num = tk.Label(self, text='Member Number:')
        self._label_member_num.grid(row=3, column=0, padx=20)
        self._entry_member_num = tk.Entry(self)
        self._entry_member_num.insert(0, coach_data["member_num"])
        self._entry_member_num.grid(row=3, column=1, padx=10)

        self._label_annual_salary = tk.Label(self, text='Annual Salary:')
        self._label_annual_salary.grid(row=4, column=0, padx=20)
        self._entry_annual_salary = tk.Entry(self)
        self._entry_annual_salary.insert(0, coach_data["annual_salary"])
        self._entry_annual_salary.grid(row=4, column=1, padx=10)

        self._label_contract_years = tk.Label(self, text='Contract Years Length:')
        self._label_contract_years.grid(row=5, column=0, padx=20)
        self._entry_contract_years = tk.Entry(self)
        self._entry_contract_years.insert(0, coach_data["contract_years_length"])
        self._entry_contract_years.grid(row=5, column=1, padx=10)

        self._label_last_team = tk.Label(self, text='Last team:')
        self._label_last_team.grid(row=6, column=0, padx=15)
        self._entry_last_team = tk.Entry(self)
        self._entry_last_team.insert(0, coach_data["last_team"])
        self._entry_last_team.grid(row=6, column=1, padx=10)

        self._label_specialization = tk.Label(self, text='Specialization:')
        self._label_specialization.grid(row=7, column=0, padx=20)
        self._entry_specialization = tk.Entry(self)
        self._entry_specialization.insert(0, coach_data["specialization"])
        self._entry_specialization.grid(row=7, column=1, padx=10)

        self._label_is_former_player = tk.Label(self, text='Former player? (y/n) *any other input will result in (n)')
        self._label_is_former_player.grid(row=8, column=0, padx=20)
        self._entry_is_former_player = tk.Entry(self)
        self._entry_is_former_player.insert(0, coach_data["is_former_player"])
        self._entry_is_former_player.grid(row=8, column=1, padx=10)

        tk.Button(self,
                  text="Update Coach",
                  command=self._send_json).grid(row=10,column=0,rowspan=5,padx=10,pady=5)

        tk.Button(self,
                  text="Cancel",
                  command=self._close_popup_callback).grid(row=10,column=1,rowspan=5,padx=10,pady=5)

    def _get_coach(self):
        try:
            response = requests.get('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(self._coach_index))
            coach_data = response.json()
            return coach_data

        except Exception:
            pass

    def _send_json(self):

        coach_data = self._get_coach()

        flag = True

        try:
            annual_salary = int(self._entry_annual_salary.get())
            contract_years = int(self._entry_contract_years.get())

            if self._entry_is_former_player.get() is 'y':
                self._entry_is_former_player = True
            else:
                self._entry_is_former_player = False

        except Exception:
            flag = False

        if flag:
            coach_json = {
                "first_name": self._entry_first_name.get(),
                "last_name": self._entry_last_name.get(),
                "member_num": self._entry_member_num.get(),
                "annual_salary": annual_salary,
                "contract_years_length": contract_years,
                "last_team": self._entry_last_team.get(),
                "type": "Coach",
                "specialization": self._entry_specialization.get(),
                "is_former_player": self._entry_is_former_player
            }

            print(coach_json)

            response = requests.put('http://127.0.0.1:5000/roster_manager/team_members/%d' % coach_data["id"], json=coach_json)
            # json_response = response.json()
            print(response.content)
            tkMessageBox.askokcancel("Coach Update", "Update coach?")

            print(type(response.status_code))

            if response.status_code != 200:
                tkMessageBox.showerror("Error", response.content)
            else:
                tkMessageBox.showinfo("Success", "Coach successfully updated.")

            self._close_popup_callback()

        else:
            tkMessageBox.showerror("Error", "Annual salary AND contract years must be integers.")





