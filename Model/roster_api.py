from flask import Flask, request
from team_roster_manager import TeamRoster
from abstract_team_member import AbstractTeamMember
from player import Player
from coach import Coach
import json

app = Flask(__name__)

TEAM_ROSTER_DB = 'team_members.sqlite'

roster_mgr = TeamRoster(TEAM_ROSTER_DB)


@app.route('/roster_manager/team_members', methods=['POST'])
def add():
    """ Add a team member to the Team Roster """

    content = request.json

    try:
        if content['type'] == "Player":
            try:
                player = Player(content['first_name'], content['last_name'], content['member_num'],
                                content['annual_salary'], content['contract_years_length'],
                                content['last_team'], content['type'], content['jersey_num'], content['position'])

                player_id = roster_mgr.add(player)

                response = app.response_class(
                    response='Team member has been assigned ID: %d' % player_id,
                    status=200
                )

                return response

            except KeyError as err:

                response = app.response_class(
                    response='Team member object is invalid. Entities with \'Player\' as their type '
                             'must have %s inputted.' % err,
                    status=400
                )

                return response

            except ValueError as err:
                response = app.response_class(
                    response='Team member object is invalid. %s' % err,
                    status=400
                )

                return response

        elif content['type'] == "Coach":

            try:
                coach = Coach(content['first_name'], content['last_name'], content['member_num'],
                              content['annual_salary'], content['contract_years_length'],
                              content['last_team'], content['type'],content['specialization'],
                              content['is_former_player'])

                coach_id = roster_mgr.add(coach)

                response = app.response_class(
                    response='Team member has been assigned ID: %d' % coach_id,
                    status=200
                )

                return response

            except KeyError as err:
                response = app.response_class(
                    response='Team member object is invalid. Entities with \'Coach\' as their type '
                              'must have %s inputted.' % err,
                    status=400
                )
                return response

            except ValueError as err:
                response = app.response_class(
                    response='Team member object is invalid. %s' % err,
                    status=400
                )

                return response

        else:
            response = app.response_class(
                response='Invalid team member type. The only \'type\' currently implemented are \'Player\' and '
                         '\'Coach\'',
                status=400
            )

            return response

    # exception that catches if a "type" key isn't inputted
    except KeyError as err:
        response = app.response_class(
            response='%s must be inputted' % err,
            status=400
        )

        return response


@app.route('/roster_manager/team_members/<int:team_member_id>', methods=['GET'])
def get(team_member_id):
    """ Get a team member based on their ID from the Team Roster """

    if team_member_id <= 0:
        response = app.response_class(
            status=400
        )
        return response

    try:
        team_member = roster_mgr.get(team_member_id)

        response = app.response_class(
            status=200,
            response=json.dumps(team_member.to_dict()),
            mimetype='application/json'
        )

        return response

    except (AttributeError, UnboundLocalError):
        response = app.response_class(
            response='Team member with ID: %d does not exist' % team_member_id,
            status=404
        )

        return response


@app.route('/roster_manager/team_members/all', methods=['GET'])
def get_all():
    """ Get all team members from the Team Roster """

    team_members = roster_mgr.get_all()

    team_member_list = []

    for member in team_members:
        team_member_list.append(member.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(team_member_list),
        mimetype='application/json'
    )

    return response


@app.route('/roster_manager/team_members/all/<type>', methods=['GET'])
def get_all_by_type(type):
    """ Get all team members from the Team Roster based on type """

    try:
        team_roster_list = roster_mgr.get_all_by_type(type)
        response = app.response_class(
                status=200,
                response=json.dumps(team_roster_list),
                mimetype='application/json'
            )
        return response

    except ValueError as err:
        response = app.response_class(
            # response='Member type: \'%s\' is invalid.' % type,
            response=str(err),
            status=400,
        )

    return response


@app.route('/roster_manager/team_members/<int:team_member_id>', methods=['PUT'])
def update(team_member_id):
    """ Update a team member from the Team Roster by ID """

    content = request.json

    try:
        if content["type"] == 'Player':
            member = Player(content['first_name'], content['last_name'], content['member_num'],
                            content['annual_salary'], content['contract_years_length'],
                            content['last_team'], 'Player', content['jersey_num'], content['position'])

            # roster_mgr.update(player)

        if content["type"] == 'Coach':
            member = Coach(content['first_name'], content['last_name'], content['member_num'],
                          content['annual_salary'], content['contract_years_length'],
                          content['last_team'], 'Coach', content['specialization'], content['is_former_player'])

        member.id = team_member_id
        roster_mgr.update(member)

        response = app.response_class(
            status=200
        )

        return response


    except KeyError as err:
        response = app.response_class(
            response='Team member object is invalid. Team member with ID: %d has type: \'%s\'. %s must be inputted.' %
                     (team_member_id, roster_mgr.get(team_member_id).type, err),
            status=400
        )

        return response

    except ValueError as err:
        response = app.response_class(
            response=str(err),
            status=400
        )

        return response

    except (AttributeError, UnboundLocalError) as err:
        response = app.response_class(
            response='Team member with an ID: %d does not exist. %s' % (team_member_id, err),
            status=404
        )

        return response


@app.route('/roster_manager/team_members/<int:team_member_id>', methods=['DELETE'])
def delete(team_member_id):
    """ Delete team member from the Team Roster by ID """

    try:
        roster_mgr.delete(team_member_id)
        response = app.response_class(
            status=200
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )

    return response


if __name__ == "__main__":
    app.run()
