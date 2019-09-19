import tkinter as tk
from top_navbar_view import TopNavbarView
# from page0_view import Page0View
from page1_view import Page1View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from popup_view_player import PlayerPopupView
from popup_view_coach import CoachPopupView
from popup_view_player_update import PlayerPopupViewUpdate
from popup_view_coach_update import CoachPopupViewUpdate
# from popup_view import PopupView
# from GUI_add import PopupView
import requests

class MainAppController(tk.Frame):
    """ Main Application for Roster GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

        self._page1 = Page1View(self,
                                self._get_all_api,
                                self._get_team_member,
                                self._get_coach_api,
                                self._get_player_api,
                                self._delete_member_api,
                                self._add_member_to_api,
                                self._update_member_to_api,
                                self._view_popup_callback)

    def _add_popup_callback(self):
        self._popup_win = tk.Toplevel()
        self._popup = AddPopupView(self._popup_win, self._close_popup_callback, self._add_member_to_api)

    def _add_member_to_api(self):
        member_json = self._popup.get_member_entry()
        requests.post(url='http://127.0.0.1:5000/roster_manager/team_members', json=member_json)
        self._page1._switch_list()

    def _view_popup_callback(self, json):
        self._popup_win = tk.Toplevel()
        self._view_win = ViewPopUp(self._popup_win, self._close_popup_call_back, json)


    def _update_member_to_api(self):
        member_json = self._popup._get_member_entry()
        id = member_json["id"]
        print(member_json)
        requests.put("http://127.0.0.1:5000/roster_manager/team_members/{}".format(id), json=member_json)
        self._page1._switch_list()

    def _get_team_member(self, id:int):
        return requests.get("http://127.0.0.1:5000/roster_manager/team_members/{}".format(id)).json()

    def _get_all_api(self):
        return requests.get("http://127.0.0.1:5000/roster_manager/team_members/all").json()

    def _get_player_api(self):
        return requests.get("http://127.0.0.1:5000/roster_manager/team_members/Player").json()

    def _get_coach_api(self):
        return requests.get("http://127.0.0.1:5000/roster_manager/team_members/Coach").json()

    #delete
    def _delete_member_api(self, id:int):
        requests.delete("http://127.0.0.1:5000/roster_manager/team_members/{}".format(id))

    def _close_popup_callback(self):
        self._popup_win.destroy()

    def _quit_callback(self):
        self.quit()


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()