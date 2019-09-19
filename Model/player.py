from sqlalchemy import Column, Integer, String
from abstract_team_member import AbstractTeamMember


class Player(AbstractTeamMember):
    """ Player class - Maintains the details of each player """
    JERSEY_NUM_INT = "Jersey number"
    POSITION_STR = "Position"

    # __tablename__ = "player"
    jersey_num = Column(Integer)
    position = Column(String(100))

    def __init__(self, first_name, last_name, member_num, annual_salary, contract_years_length, last_team, type,
                 jersey_num, position):
        """ Constructor- initializes attributes for the Player class """

        super().__init__(first_name, last_name, member_num, annual_salary, contract_years_length, last_team, type)

        Player._validate_input(Player.JERSEY_NUM_INT, jersey_num)
        Player._validate_int(Player.JERSEY_NUM_INT, jersey_num)
        self.jersey_num = jersey_num

        Player._validate_input(Player.POSITION_STR, position)
        Player._validate_string(Player.POSITION_STR, position)
        self.position = position

    def to_dict(self):
        """ Creates a dictionary from an instance of Player """

        player_dict = {}
        player_dict['id'] = self.id
        player_dict['first_name'] = self.first_name
        player_dict['last_name'] = self.last_name
        player_dict['member_num'] = self.member_num
        player_dict['annual_salary'] = self.annual_salary
        player_dict['contract_years_length'] = self.contract_years_length
        player_dict['last_team'] = self.last_team
        player_dict['type'] = self.type
        player_dict['jersey_num'] = self.jersey_num
        player_dict['position'] = self.position

        return player_dict

    def copy(self, object):
        """ Copies data from a Player object to this Player object """

        if isinstance(object, Player):
            self.first_name = object.first_name
            self.last_name = object.last_name
            self.member_num = object.member_num
            self.annual_salary = object.annual_salary
            self.contract_years_length = object.contract_years_length
            self.last_team = object.last_team
            self.type = object.type
            self.jersey_num = object.jersey_num
            self.position = object.position

    def get_contract_details(self):
        """ Returns the contract details of a player """

        return 'This player has a contract with the for $%d/year for %d years.' % \
               (self.annual_salary, self.contract_years_length)

    @staticmethod
    def _validate_input(display_name, input_value):
        """ Private helper to validate input values as not None or an empty string """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_int(display_name, input_value):
        """ Private method to validate the input value is a int type """

        if input_value != int(input_value):
            raise ValueError(display_name + " must be an integer type")

    @staticmethod
    def _validate_string(display_name, input_value):
        """ Private method to validate the input value is a string type """

        if input_value != str(input_value):
            raise ValueError(display_name + " must be a string type")