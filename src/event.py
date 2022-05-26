from random import sample


class Event:
    def __init__(self, time):
        self.time = time

    def print_message(self, messages, params):
        message = "".join(sample(messages, 1))
        for param in params:
            message = message.replace("{{{0}}}".format(param), params[param])
        print(message)


class Goal(Event):
    messages = [
        "{time}' The ball finds its way to {player} ({team}) after a confusing situation inside the goalmouth. He finds some space and easily knocks the ball in with his body and alters the score.",
        "{time}' Goal! {player} ({team}) was in the right place at the right time to get to the rebound inside the box and gleefully rifles the ball low inside the left post.",
        "{time}' {player} ({team}) receives a killer pass on the edge of the box and controls the ball with a great first touch to fire it beyond the helpless goalkeeper.",
        "{time}' {player} ({team}) scores as he latches on to a pass on the edge of the box and unleashes a perfect strike that goes behind the goalkeeper.",
        "{time}' {player} ({team}) meets the corner and displays his eye for goal as he coolly plants a header from close range into the left side of the goal.",
        "{time}' Goal! {player} ({team}) unleashes a first-time shot from inside the box and beats the goalkeeper into the bottom left corner."
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class YellowCard(Event):
    messages = [
        "{time}' {player} ({team}) is shown a yellow card by the referee for making a challenge on his opponent, but he looks angry with the decision.",
        "{time}' Booking. {player} ({team}) receives a caution from the referee.",
        "{time}' {player} ({team}) gets a yellow card after the final whistle for unsporting behaviour.",
        "{time}' {player} ({team}) receives a yellow card for chasing the referee and shouting at him.",
        "{time}' Today's referee rightly decides to book {player} ({team}) for his harsh tackle.",
        "{time}' {player} ({team}) can't expect anything else than a yellow card for his hard tackle. And a yellow it is. Referee didn't think twice about pulling it out of his pocket.",
        "{time}' Yellow card. {player} ({team}) goes into the book for a bad tackle on his opponent.",
        "{time}' {player} ({team}) has tested the patience of referee and goes into the book for a previous late challenge.",
        "{time}' {player} ({team}) is rightly booked by the referee because it could not have been anything other than a yellow card."
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class RedCard(Event):
    messages = [
        "{time}' {player} ({team}) makes a horrific tackle on his opponent and is shown a straight red card by the referee!",
        "{time}' RED card! {player} ({team}) can’t believe it as the referee orders him from the pitch following the VAR review.",
        "{time}' {player} ({team}) makes an ugly challenge on his opponent and receives a red card from the referee!",
        "{time}' RED CARD! {player} ({team}) makes a bad challenge and receives a second yellow card from the referee. He can have an early bath.",
        "{time}' A card of the red variety is shown to {player} ({team}). He has been sent off."
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class Corner(Event):
    messages = [
        "{time}' The ball is off of the pitch and it's a goal kick for ({team}).",
        "{time}' ({team}) have a chance to score from a corner kick, but the ball is cleared by a defender.",
        "{time}' Corner kick. {player} ({team}) is ready to send the ball into the box.",
        "{time}' {player} ({team}) goes over to take a corner kick after one of the defenders makes a good clearance.",
        "{time}' ({team}) take the corner, but their hopes of scoring a goal end with a nice clearance by the defence.",
        "{time}' ({team}) have a corner.",
        "{time}' ({team}) take the corner, but their hopes of scoring a goal end with a nice clearance by the defence. The ball goes behind for a corner. ({team}) will have an opportunity to threaten the opposition's goal.",
        "{time}' {player} ({team}) sends a wonderful cross from the corner kick. However, the defence works perfectly to clear the ball and avert the threat.",
        "{time}' {player} ({team}) rolls the ball short to a teammate from the corner instead of sending a cross into the box.",
        "{time}' ({team}) failed to take advantage of the corner as the opposition's defence was alert and averted the threat.",
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class Offside(Event):
    messages = [
        "{time}' {player} ({team}) is caught offside after the linesman raises his flag.",
        "{time}' One of the players from ({team}) times his run too early and the referee blows his whistle for offside.",
        "{time}' {player} ({team}) finds himself behind the opposition's defence, but the game is stopped for offside.",
        "{time}' {player} ({team}) finds himself in an offside position and the referee stops play after the linesman raises his flag.",
        "{time}' {player} ({team}) almost finds himself in a very promising position, but he is flagged offside by the linesman.",
        "{time}' {player} ({team}) is forced to stop his forward run after being caught in an offside position by the linesman."
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class Substitution(Event):
    messages = [
        "{time}' {new_player} ({team}) joins the action as a substitute, replacing {old_player}.",
        "{time}' It's time for a substitution. {new_player} ({team}) comes on in place of {old_player}.",
        "{time}' Here is a change. {old_player} is going off and the coach gives the last tactical orders to {new_player} ({team}).",
        "{time}' Coach has decided to substitute {old_player} and he is replaced by {new_player} ({team}).",
        "{time}' Coach decides to make a substitution. {old_player} will be replaced by {new_player} ({team}).",
        "{time}' Substitution. {old_player} is replaced by {new_player} ({team}).",
    ]

    def __init__(self, time, team, new_player, old_player):
        super().__init__(time)
        self.team = team
        self.new_player = new_player
        self.old_player = old_player
        self.print_message(self.messages, {"time": time, "team": team, "new_player": new_player, "old_player": old_player})


class Foul(Event):
    messages = [
        "{time}' The game is interrupted. {player} ({team}) has violated the rules in the battle for the ball. No protests or gestures are being made as he is quite aware of what he did.",
        "{time}' {player} ({team}) was trying to get to the ball but clattered into the legs of the opponent as well. Referee blows his whistle for an infringement.",
        "{time}' {player} ({team1}) makes an overly-aggressive challenge and referee blows his whistle for a foul.",
        "{time}' {player} ({team}) is penalised for a foul. Referee had a clear view and blows his whistle.",
        "{time}' {player} ({team}) jumps into a tackle and referee blows his whistle for a foul.",
        "{time}' {player} ({team}) plays in a hopeful cross, but it doesn't find its way to any of the attacking players. The ball is off of the pitch and it's a goal kick."
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class Penalty(Event):
    messages = [
        "{time}' {player} ({team}) is going to take the penalty!"
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class Injury(Event):
    messages = [
        "{time}' {player} ({team}) requires medical treatment, so the referee stops play and signals for the physio to come onto the pitch.",
        "{time}' The game is interrupted now, {player} ({team}) picks up a knock and the physio has to come on.",
        "{time}' The game is interrupted. {player} ({team}) suffers a horrific injury!",
        "{time}' {player} ({team}) is down injured and the referee stops play so that he can receive medical treatment."
    ]

    def __init__(self, time, team, player):
        super().__init__(time)
        self.team = team
        self.player = player
        self.print_message(self.messages, {"time": time, "team": team, "player": player})


class KickOff(Event):
    messages = [
        "{time}' The referee blows his whistle and we are underway."
    ]

    def __init__(self, time):
        super().__init__(time)
        self.print_message(self.messages, {"time": time})


class Break(Event):
    messages = [
        "{time}' The referee blows his whistle to end the first half and the players are now heading to their respective dressing rooms."
    ]

    def __init__(self, time):
        super().__init__(time)
        self.print_message(self.messages, {"time": time})


class SecondHalf(Event):
    messages = [
        "{time}' Referee blows his whistle to start the second half."
    ]

    def __init__(self, time):
        super().__init__(time)
        self.print_message(self.messages, {"time": time})


class FullTime(Event):
    messages = [
        "{time}' Referee is looking at his watch and immediately ends this match."
    ]

    def __init__(self, time):
        super().__init__(time)
        self.print_message(self.messages, {"time": time})
