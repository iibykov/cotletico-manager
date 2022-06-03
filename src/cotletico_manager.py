import random
import json
import player
import team
import match
import schedule

group_schedule = schedule.Schedule.schedule_from_json('../data/schedule.json')
teams = team.Team.teams_from_json('../data/players.json')
print(len(teams))

# host_team = match.Match.ideal_squad(teams[6], '6-2-2')[0]
# host_bad_positions = match.Match.ideal_squad(teams[6], '6-2-2')[1]
# print(*[(pl.name, pl.surname, pl.position, pl.rating) for pl in host_team], sep='\n')
# print(host_bad_positions)

exhibition_match = group_schedule.play_match(2, teams)
print(exhibition_match)
