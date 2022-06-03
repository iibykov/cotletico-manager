from random import sample
import json


class Event:
    def __init__(self, messages):
        self.messages = messages

    def print_message(self, **params):
        message = "".join(sample(self.messages, 1))
        for param in params:
            message = message.replace("{{{0}}}".format(param), params[param])
        print(message)


# Example
with open('../data/messages.json') as file:
    messages_dict = json.loads(file.read())

goal = Event(messages_dict["goal"])
corner = Event(messages_dict["corner"])
foul = Event(messages_dict["foul"])
yellow_card = Event(messages_dict["yellow_card"])
offside = Event(messages_dict["offside"])
penalty = Event(messages_dict["penalty"])
second_half = Event(messages_dict["second_half"])
full_time = Event(messages_dict["full_time"])
