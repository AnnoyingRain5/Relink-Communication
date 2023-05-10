import json


def packet(inJSON):
    strType = json.loads(inJSON)["PacketType"]
    match strType:
        case "message":
            final = message()
            final.json = inJSON
            return final
        case "command":
            final = command()
            final.json = inJSON
            return final
        case "login":
            final = loginRequest()
            final.json = inJSON
            return final
        case "signup":
            final = signupRequest()
            final.json = inJSON
            return final
        case "system":
            final = system()
            final.json = inJSON
            return final
        case "ChannelChange":
            final = channelChange()
            final.json = inJSON
            return final
        case "notification":
            final = notification()
            final.json = inJSON
            return final
        case _:  # If the packet type is not recognised, return None
            return None


class message():
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


class system():
    def __init__(self):
        self.text = ""

    def json_get(self):
        return json.dumps({"PacketType": "system", "message": self.text})

    def json_set(self, inJSON):
        self.text = json.loads(inJSON)["message"]
    json = property(json_get, json_set)


class command():
    def json_get(self):
        return json.dumps({"PacketType": "command", "name": self.name, "args": self.args})

    def json_set(self, inJSON):
        self.name = json.loads(inJSON)["name"]
        self.args = json.loads(inJSON)["args"]
    json = property(json_get, json_set)


class loginRequest():
    def __init__(self):
        self.username = ""
        self.password = ""

    def json_get(self):
        return json.dumps({"PacketType": "login", "username": self.username, "password": self.password})

    def json_set(self, inJSON):
        self.username = json.loads(inJSON)["username"]
        self.password = json.loads(inJSON)["password"]
    json = property(json_get, json_set)


class signupRequest():
    def __init__(self):
        self.username = ""
        self.password = ""

    def json_get(self):
        return json.dumps({"PacketType": "signup", "username": self.username, "password": self.password})

    def json_set(self, inJSON):
        self.username = json.loads(inJSON)["username"]
        self.password = json.loads(inJSON)["password"]
    json = property(json_get, json_set)


class result():
    def __init__(self):
        self.result = False
        self.reason = ""

    def json_get(self):
        return json.dumps({"PacketType": "result", "result": self.result, "reason": self.reason})

    def json_set(self, inJSON):
        self.result = json.loads(inJSON)["result"]
        self.reason = json.loads(inJSON)["reason"]

    json = property(json_get, json_set)


class channelChange():
    def __init__(self):
        self.channel = ""

    def json_get(self):
        return json.dumps({"PacketType": "ChannelChange", "channel": self.channel})

    def json_set(self, inJSON):
        self.channel = json.loads(inJSON)["channel"]
    json = property(json_get, json_set)


class notification():
    def __init__(self):
        self.type = ""
        self.location = ""

    def json_get(self):
        return json.dumps({"PacketType": "notification", "type": self.type, "location": self.location})

    def json_set(self, inJSON):
        self.type = json.loads(inJSON)["type"]
        self.location = json.loads(inJSON)["location"]
    json = property(json_get, json_set)
