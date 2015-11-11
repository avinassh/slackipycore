# Slackipy Core

`slackipycore` helps you invite users to your Slack team/channel using Python. `slackipycore` is meant for advanced users and is written for [`slackipy`](https://github.com/avinassh/slackipy).

## Need A Web Version?

Check my project [`slackipy`](https://github.com/avinassh/slackipy).


## Requirements

`slackipycore` is Python 3 only library.

## Installation 

    pip install slackipycore

## Usage

    >>> from slackipycore import invite
    >>> from slackipycore import AlreadyInTeam
    >>>

## API Reference

`invite`
----------

Description: Invites `email` to the Slack team. Returns `True` if successful or raises one of the exceptions.

**Parameters:**

| Name       | Type      | Required | Description                         
| ---------- | --------- | -------- | -----------
| `team_id`  | string | Yes | Slack team id or subdomain
| `api_token`  | string | Yes | Slack API Token (of admin)
| `invitee_email`  | string | Yes | Email to which invite to be sent

`get_team_info`
--------------

Description: Returns a dictionary which contains team name, id, team images etc 

**Parameters:**

| Name       | Type      | Required | Description                         
| ---------- | --------- | -------- | -----------
| `team_id`  | string | Yes | Slack team id or subdomain
| `api_token`  | string | Yes | Slack API Token (of admin)


`get_users`
--------------

Description: Returns a tuple containing two lists, a list containing info of all users and another list of currently online users.

**Parameters:**

| Name       | Type      | Required | Description                         
| ---------- | --------- | -------- | -----------
| `team_id`  | string | Yes | Slack team id or subdomain
| `api_token`  | string | Yes | Slack API Token (of admin)
  

## Exceptions

- `AlreadyInTeam`
- `InvalidInviteeEmail`
- `InvalidAuthToken`
- `AlreadyInvited`
- `APIRequestError`

## License

The mighty MIT license. Please check `LICENSE` for more details.