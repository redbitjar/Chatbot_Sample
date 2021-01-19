from enum import Enum

class Action(Enum):
    WEBLINK = "webLink"
    MESSAGE = "message"
    PHONE = "phone"
    BLOCK = "block"

def action_navigate(action : Action) -> str:
    if not isinstance(action, Action):
        raise TypeError('action must be an instance of Action Enum')
    ret = ''
    if action == Action.WEBLINK:
        ret = "webLink"
    elif action == Action.MESSAGE:
        ret = "message"
    elif action == Action.PHONE:
        ret = "phone"
    elif action == Action.BLOCK:
        ret = "block"
    return ret