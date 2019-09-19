from sqlalchemy import Column, Integer, String
from base import Base


class AbstractTeamMember(Base):

    """ Abstract Team Member class - Maintains the details of each team member """

    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    member_num = Column(String(100), nullable=False)
    annual_salary = Column(Integer, nullable=False)
    contract_years_length = Column(Integer, nullable=False)
    last_team = Column(String(100), nullable=False)
    type = Column(String(10), nullable=False)

    MEMBER_ID_INT = "Member ID"
    FIRST_NAME_STR = "First name"
    LAST_NAME_STR = "Last name"
    MEMBER_NUM_STR = "Member number"
    ANNUAL_SALARY_INT = "Annual salary"
    CONTRACT_YEARS_INT = "Contract years"
    LAST_TEAM_STR = "Last team"
    MEMBER_TYPE_STR = "Type"

    def __init__(self, first_name, last_name, member_num, annual_salary, contract_years_length, last_team, type):
        """ Constructor - initializes attributes for the AbstractTeamMember class """

        AbstractTeamMember._validate_input(AbstractTeamMember.FIRST_NAME_STR, first_name)
        AbstractTeamMember._validate_string(AbstractTeamMember.FIRST_NAME_STR, first_name)
        self.first_name = first_name

        AbstractTeamMember._validate_input(AbstractTeamMember.LAST_NAME_STR, last_name)
        AbstractTeamMember._validate_string(AbstractTeamMember.LAST_NAME_STR, last_name)
        self.last_name = last_name

        AbstractTeamMember._validate_input(AbstractTeamMember.MEMBER_NUM_STR, member_num)
        AbstractTeamMember._validate_string(AbstractTeamMember.MEMBER_NUM_STR, member_num)
        self.member_num = member_num

        AbstractTeamMember._validate_input(AbstractTeamMember.ANNUAL_SALARY_INT, annual_salary)
        AbstractTeamMember._validate_int(AbstractTeamMember.ANNUAL_SALARY_INT, annual_salary)
        self.annual_salary = annual_salary

        AbstractTeamMember._validate_input(AbstractTeamMember.CONTRACT_YEARS_INT, contract_years_length)
        AbstractTeamMember._validate_int(AbstractTeamMember.CONTRACT_YEARS_INT, contract_years_length)
        self.contract_years_length = contract_years_length

        AbstractTeamMember._validate_input(AbstractTeamMember.LAST_TEAM_STR, last_team)
        AbstractTeamMember._validate_string(AbstractTeamMember.LAST_TEAM_STR, last_team)
        self.last_team = last_team

        AbstractTeamMember._validate_input(AbstractTeamMember.MEMBER_TYPE_STR, type)
        AbstractTeamMember._validate_string(AbstractTeamMember.MEMBER_TYPE_STR, type)
        self.type = type

    def to_dict(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_contract_details(self):
        raise NotImplementedError("Subclass must implement abstract method")

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

    @staticmethod
    def _validate_input(display_name, input_value):
        """ Private helper to validate input values as not None or an empty string """

        if input_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if input_value == "":
            raise ValueError(display_name + " cannot be empty.")
