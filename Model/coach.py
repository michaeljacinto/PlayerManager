from sqlalchemy import Column, Integer, String
from abstract_team_member import AbstractTeamMember


class Coach(AbstractTeamMember):
    """ Coach class - Maintains the details of each coach """
    SPECIALIZATION_STR = "Specialization"
    FORMER_PLAYER_STR = "Former player"

    # __tablename__ = "coach"
    specialization = Column(String(100))
    is_former_player = Column(String(1))

    def __init__(self, first_name, last_name, member_num, annual_salary, contract_years_length, last_team, type,
                 specialization, is_former_player):
        """ Constructor- initializes attributes for the Coach class """

        super().__init__(first_name, last_name, member_num, annual_salary, contract_years_length, last_team, type)

        Coach._validate_input(Coach.SPECIALIZATION_STR, specialization)
        Coach._validate_string(Coach.SPECIALIZATION_STR, specialization)
        self.specialization = specialization

        Coach._validate_input(Coach.FORMER_PLAYER_STR, is_former_player)
        self.is_former_player = is_former_player

    def to_dict(self):
        """ Creates a dictionary from an instance of Coach """

        coach_dict = {}
        coach_dict['id'] = self.id
        coach_dict['first_name'] = self.first_name
        coach_dict['last_name'] = self.last_name
        coach_dict['member_num'] = self.member_num
        coach_dict['annual_salary'] = self.annual_salary
        coach_dict['contract_years_length'] = self.contract_years_length
        coach_dict['last_team'] = self.last_team
        coach_dict['type'] = self.type
        coach_dict['specialization'] = self.specialization

        if self.is_former_player == "1":
            coach_dict['is_former_player'] = True

        if self.is_former_player == "0":
            coach_dict['is_former_player'] = False

        return coach_dict

    def copy(self, object):
        """ Copies data from a TeamMember object to this TeamMember object """

        if isinstance(object, Coach):
            self.first_name = object.first_name
            self.last_name = object.last_name
            self.member_num = object.member_num
            self.annual_salary = object.annual_salary
            self.contract_years_length = object.contract_years_length
            self.last_team = object.last_team
            self.type = object.type
            self.specialization = object.specialization
            self.is_former_player = object.is_former_player

    def get_contract_details(self):
        """ Returns contract details of the coach """

        return 'This coach has a contract with the for $%d/year for %d years.' % \
               (self.annual_salary, self.contract_years_length)


    @staticmethod
    def _validate_string(display_name, input_value):
        """ Private method to validate the input value is a string type """

        if input_value != str(input_value):
            raise ValueError(display_name + " must be a string type")

    @staticmethod
    def _validate_input(display_name, input_value):
        """ Private helper to validate input values as not None or an empty string """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")