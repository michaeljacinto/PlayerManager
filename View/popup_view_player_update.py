import tkinter as tk
from tkinter import messagebox as tkMessageBox
import requests

class PlayerPopupViewUpdate(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback, player_index):
        """ Initialize the nav bar """

        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)
        self._close_popup_callback = close_popup_callback
        self._player_index = player_index
        self._create_widgets()

    def _create_widgets(self):

        player_data = self._get_player()

        self._label_first_name = tk.Label(self, text='First name:')
        self._label_first_name.grid(row=1, column=0, padx=20)
        self._entry_first_name = tk.Entry(self)
        self._entry_first_name.insert(0, player_data["first_name"])
        self._entry_first_name.grid(row=1,column=1,padx=10)

        self._label_last_name = tk.Label(self, text='Last name:')
        self._label_last_name.grid(row=2, column=0, padx=20)
        self._entry_last_name = tk.Entry(self)
        self._entry_last_name.insert(0, player_data["last_name"])
        self._entry_last_name.grid(row=2, column=1, padx=10)

        self._label_member_num = tk.Label(self, text='Member Number:')
        self._label_member_num.grid(row=3, column=0, padx=20)
        self._entry_member_num = tk.Entry(self)
        self._entry_member_num.insert(0, player_data["member_num"])
        self._entry_member_num.grid(row=3, column=1, padx=10)

        self._label_annual_salary = tk.Label(self, text='Annual Salary:')
        self._label_annual_salary.grid(row=4, column=0, padx=20)
        self._entry_annual_salary = tk.Entry(self)
        self._entry_annual_salary.insert(0, player_data["annual_salary"])
        self._entry_annual_salary.grid(row=4, column=1, padx=10)

        self._label_contract_years = tk.Label(self, text='Contract Years Length:')
        self._label_contract_years.grid(row=5, column=0, padx=20)
        self._entry_contract_years = tk.Entry(self)
        self._entry_contract_years.insert(0, player_data["contract_years_length"])
        self._entry_contract_years.grid(row=5, column=1, padx=10)

        self._label_last_team = tk.Label(self, text='Last team:')
        self._label_last_team.grid(row=6, column=0, padx=15)
        self._entry_last_team = tk.Entry(self)
        self._entry_last_team.insert(0, player_data["last_team"])
        self._entry_last_team.grid(row=6, column=1, padx=10)

        self._label_jersey_num = tk.Label(self, text='Jersey Number:')
        self._label_jersey_num.grid(row=7, column=0, padx=20)
        self._entry_jersey_num = tk.Entry(self)
        self._entry_jersey_num.insert(0, player_data["jersey_num"])
        self._entry_jersey_num.grid(row=7, column=1, padx=10)

        self._label_position = tk.Label(self, text='Position:')
        self._label_position.grid(row=8, column=0, padx=20)
        self._entry_position = tk.Entry(self)
        self._entry_position.insert(0, player_data["position"])
        self._entry_position.grid(row=8, column=1, padx=10)

        tk.Button(self,
                  text="Update Player",
                  command=self._send_json).grid(row=10,column=0,rowspan=5,padx=10,pady=5)

        tk.Button(self,
                  text="Cancel",
                  command=self._close_popup_callback).grid(row=10,column=1,rowspan=5,padx=10,pady=5)

    def _get_player(self):
        try:
            response = requests.get('http://127.0.0.1:5000/roster_manager/team_members/%d' % int(self._player_index))
            player_data = response.json()
            return player_data

        except Exception:
            pass

    def _send_json(self):

        player_data = self._get_player()

        flag = True

        try:
            annual_salary = int(self._entry_annual_salary.get())
            contract_years = int(self._entry_contract_years.get())
            jersey_num = int(self._entry_jersey_num.get())

        except Exception:
            flag = False

        if flag:
            player_json = {
                "first_name": self._entry_first_name.get(),
                "last_name": self._entry_last_name.get(),
                "member_num": self._entry_member_num.get(),
                "annual_salary": annual_salary,
                "contract_years_length": contract_years,
                "last_team": self._entry_last_team.get(),
                "type": "Player",
                "jersey_num": jersey_num,
                "position": self._entry_position.get()
            }

            print(player_json)

            response = requests.put('http://127.0.0.1:5000/roster_manager/team_members/%d' % player_data["id"], json=player_json)
            # json_response = response.json()
            print(response.content)
            tkMessageBox.askokcancel("Update Player", "Update player?")

            print(type(response.status_code))

            if response.status_code != 200:
                tkMessageBox.showerror("Error", response.content)
            else:
                tkMessageBox.showinfo("Success", "Player updated successfully.")

            self._close_popup_callback()

        else:
            tkMessageBox.showerror("Error", "Annual salary, contract years and jersey number must all be integers.")





