from random import sample
# import json


class Event:
    def __init__(self, messages):
        self.messages = messages

    def print_message(self, **params):
        message = "".join(sample(self.messages, 1))
        for param in params:
            message = message.replace("{{{0}}}".format(param), params[param])
        print(message)


# Example
# with open('../data/messages.json') as file:
#     messages_dict = json.loads(file.read())
#
# goal = Event(messages_dict["goal"])
# goal.print_message(time="12", team="Spain", player="Raul")
