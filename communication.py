import json


def packet(inJSON):
    '''Factory function to convert JSON packets to communication objects.

    Returns None if the type is not recognised'''
    strType = json.loads(inJSON)["PacketType"]
    match strType:
        case "message":
            final = Message()
            final.json = inJSON
            return final
        case "command":
            final = Command()
            final.json = inJSON
            return final
        case "login":
            final = LoginRequest()
            final.json = inJSON
            return final
        case "signup":
            final = SignupRequest()
            final.json = inJSON
            return final
        case "system":
            final = System()
            final.json = inJSON
            return final
        case "ChannelChange":
            final = ChannelChange()
            final.json = inJSON
            return final
        case "FederationRequest":
            final = FederationRequest()
            final.json = inJSON
            return final
        case "notification":
            final = Notification()
            final.json = inJSON
            return final
        case "UserList":
            final = UserList()
            final.json = inJSON
            return final
        case "CommandList":
            final = CommandList()
            final.json = inJSON
            return final
        case _:  # If the packet type is not recognised, return None
            return None


class Message():
    def __init__(self):
        self.username = ""
        self.text = ""
        self.isDM = False

    def json_get(self):
        return json.dumps({"PacketType": "message", "username": self.username, "message": self.text, "isDM": self.isDM})

    def json_set(self, inJSON):
        self.username = json.loads(inJSON)["username"]
        self.text = json.loads(inJSON)["message"]
        self.isDM = json.loads(inJSON)["isDM"]
    json = property(json_get, json_set)


class System():
    def __init__(self):
        self.text = ""

    def json_get(self):
        return json.dumps({"PacketType": "system", "message": self.text})

    def json_set(self, inJSON):
        self.text = json.loads(inJSON)["message"]
    json = property(json_get, json_set)


class Command():
    def __init__(self):
        self.name = ""
        self.args = []

    def json_get(self):
        return json.dumps({"PacketType": "command", "name": self.name, "args": self.args})

    def json_set(self, inJSON):
        self.name = json.loads(inJSON)["name"]
        self.args = json.loads(inJSON)["args"]
    json = property(json_get, json_set)


class LoginRequest():
    def __init__(self):
        self.username = ""
        self.password = ""

    def json_get(self):
        return json.dumps({"PacketType": "login", "username": self.username, "password": self.password})

    def json_set(self, inJSON):
        self.username = json.loads(inJSON)["username"]
        self.password = json.loads(inJSON)["password"]
    json = property(json_get, json_set)


class SignupRequest():
    def __init__(self):
        self.username = ""
        self.password = ""

    def json_get(self):
        return json.dumps({"PacketType": "signup", "username": self.username, "password": self.password})

    def json_set(self, inJSON):
        self.username = json.loads(inJSON)["username"]
        self.password = json.loads(inJSON)["password"]
    json = property(json_get, json_set)


class FederationRequest():
    def __init__(self):
        self.username = ""
        self.channel = ""

    def json_get(self):
        return json.dumps({"PacketType": "FederationRequest", "username": self.username, "channel": self.channel})

    def json_set(self, inJSON):
        self.username = json.loads(inJSON)["username"]
        self.channel = json.loads(inJSON)["channel"]
    json = property(json_get, json_set)


class Result():
    def __init__(self):
        self.result = False
        self.reason = ""

    def json_get(self):
        return json.dumps({"PacketType": "result", "result": self.result, "reason": self.reason})

    def json_set(self, inJSON):
        self.result = json.loads(inJSON)["result"]
        self.reason = json.loads(inJSON)["reason"]

    json = property(json_get, json_set)


class ChannelChange():
    def __init__(self):
        self.channel = ""

    def json_get(self):
        return json.dumps({"PacketType": "ChannelChange", "channel": self.channel})

    def json_set(self, inJSON):
        self.channel = json.loads(inJSON)["channel"]
    json = property(json_get, json_set)


class Notification():
    def __init__(self):
        self.type = ""
        self.location = ""

    def json_get(self):
        return json.dumps({"PacketType": "notification", "type": self.type, "location": self.location})

    def json_set(self, inJSON):
        self.type = json.loads(inJSON)["type"]
        self.location = json.loads(inJSON)["location"]
    json = property(json_get, json_set)

class UserList():
    def __init__(self):
        self.channelList = []
        self.serverList = []

    def json_get(self):
        return json.dumps({"PacketType": "UserList", "channelList": self.channelList, "serverList": self.serverList})

    def json_set(self, inJSON):
        self.channelList = json.loads(inJSON)["channelList"]
        self.serverList = json.loads(inJSON)["serverList"]
    json = property(json_get, json_set)

class CommandList():
    def __init__(self):
        self.commandList = []

    def json_get(self):
        return json.dumps({"PacketType": "CommandList", "commandList": self.commandList})

    def json_set(self, inJSON):
        self.commandList = json.loads(inJSON)["commandList"]
    json = property(json_get, json_set)

