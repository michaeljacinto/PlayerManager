from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base


from abstract_team_member import AbstractTeamMember
from player import Player
from coach import Coach
import json
import os


class TeamRoster:
    """ Team Roster class - Maintains the details of each team """
    DB_FILENAME_STR = "Database filename"

    def __init__(self, db_filename):
        """ Constructor - initializes attributes for the TeamRoster class """

        TeamRoster._validate_input_str(TeamRoster.DB_FILENAME_STR, db_filename)

        engine = create_engine('sqlite:///' + db_filename)
        self._db_session = sessionmaker(bind=engine)

    def add(self, team_member):
        """ Adds a member to the team roster """

        TeamRoster._validate_team_member('Team Member', team_member)

        session = self._db_session()

        existing_team_member = session.query(AbstractTeamMember).filter(AbstractTeamMember.member_num ==
                                                                        team_member.member_num).first()

        if existing_team_member is None:
            session.add(team_member)
            session.commit()
        else:
            session.close()
            raise ValueError("Team member already exists")

        team_member_id = team_member.id

        session.close()

        return team_member_id

    def get(self, id):
        """ Returns the member in the team roster by ID """

        TeamRoster._validate_input_int('ID', id)

        session = self._db_session()

        existing_team_member = session.query(AbstractTeamMember).filter(AbstractTeamMember.id == id).first()

        team_member = ''

        if existing_team_member not in [None, '']:
            if existing_team_member.type == "Player":
                team_member = session.query(Player).filter(Player.id == existing_team_member.id).first()

            if existing_team_member.type == "Coach":
                team_member = session.query(Coach).filter(Coach.id == existing_team_member.id).first()

        else:
            session.close()
            raise ValueError("Team member cannot be found")

        session.close()

        return team_member

    def get_all(self):
        """ Retrieves the entire roster in the team """

        session = self._db_session()

        players = session.query(Player).filter((Player.jersey_num != "null") and (Player.position != "null")).all()
        coaches = session.query(Coach).filter((Coach.specialization != "null") and (Coach.is_former_player != "null")).all()

        team_list = players + coaches

        session.close()

        return team_list

    def get_all_by_type(self, type):
        """ Returns all team members by the type """

        TeamRoster._validate_input_str('Type', type)

        type_list = []

        session = self._db_session()

        roster_list = self.get_all()

        for team_member in roster_list:
            if team_member.type == type:
                type_list.append(team_member.to_dict())

        session.close()

        if len(type_list) > 0:
            return type_list
        else:
            return []

    def update(self, team_member):
        """ Updates a team member """

        TeamRoster._validate_team_member('Team Member', team_member)

        session = self._db_session()

        if team_member.type == "Player":
            existing_team_member = session.query(Player).filter(Player.id == team_member.id).first()

        elif team_member.type == "Coach":
            existing_team_member = session.query(Coach).filter(Coach.id == team_member.id).first()

        else:
            raise ValueError("Type %s has not been implemented." % team_member.type)

        if team_member.type == existing_team_member.type:
            existing_team_member.copy(team_member)

        else:
            raise ValueError("The existing team member does not have the same type as the updating team member.")

        session.commit()
        session.close()

    def delete(self, id):
        """ Removes a member from the team roster """

        TeamRoster._validate_input_int('ID', id)

        session = self._db_session()

        existing_team_member = session.query(AbstractTeamMember).filter(AbstractTeamMember.id == id).first()

        if existing_team_member is None:
            raise ValueError("Team member object does not exist.")

        session.delete(existing_team_member)
        session.commit()
        session.close()

        return existing_team_member

    @staticmethod
    def _validate_input_str(display_name, input_value):
        """ Private method to validate the input value is a string type """

        if input_value != str(input_value):
            raise ValueError(display_name + " must be a string type")

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_input_int(display_name, input_value):
        """ Private method to validate the input value is a string type """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")

        if input_value != int(input_value):
            raise ValueError(display_name + " must be an integer type")

    @staticmethod
    def _validate_team_member(display_name, input_value):
        """ Private helper to validate input values as not None or an empty string """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")

if __name__ == '__main__':
    unittest.main()