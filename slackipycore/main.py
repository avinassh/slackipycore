import requests

from slackipy_exceptions import (AlreadyInTeam, InvalidInviteeEmail,
                                 InvalidAuthToken, AlreadyInvited,
                                 APIRequestError)


invite_api_url = "https://{team_name}.slack.com/api/users.admin.invite"
users_api_url = ("https://{team_name}.slack.com/api/users.list?"
                 "token={api_token}&presence=1")
team_api_url = "https://{team_name}.slack.com/api/team.info?token={api_token}"


def invite(team_name, api_token, invitee_email):
    url = invite_api_url.format(team_name=team_name)
    payload = {'email': invitee_email, 'token': api_token}
    r = requests.post(url, data=payload)

    _process_response(response=r)

    return True


def get_users(team_name, api_token):
    url = users_api_url.format(team_name=team_name, api_token=api_token)
    r = requests.get(url)
    response_data = _process_response(response=r)

    total_users = response_data['members']
    online_users = [m for m in total_users if m['presence'] == 'active']

    return (total_users, online_users)


def get_team_info(team_name, api_token):
    url = team_api_url.format(team_name=team_name, api_token=api_token)
    r = requests.get(url)
    response_data = _process_response(response=r)

    return response_data['team']


def _process_response(response):
    response_data = response.json()

    if not response.status_code == requests.codes.ok:
        raise APIRequestError

    if not response_data.get('ok'):
        _check_error(response_data['error'])

    return response_data


def _check_error(error):
    if error == 'invalid_auth':
        raise InvalidAuthToken
    if error == 'already_in_team':
        raise AlreadyInTeam
    if error == 'invalid_email':
        raise InvalidInviteeEmail
    if error == 'already_invited':
        raise AlreadyInvited
