import json
from datetime import datetime
from collections import Counter

date_now = datetime.now().strftime('%d/%b/%Y')

with open('../data/group_stage.json') as file:
    groups = json.load(file)

with open('../data/match_results.json') as file:
    match_results = json.load(file)

with open('../data/group.json') as file:
    g_name = json.load(file)


class Match:
    goals_a = 0  # added goals_a
    goals_b = 0  # added goals_b

    def __init__(self, stadium, date, team_a, team_b):  # added team_a, team_b, group
        self.events = {team_a: {'y_card': 0, 'r_card': 0}, team_b: {'y_card': 0, 'r_card': 0}}  # added events
        self.stadium = stadium
        self.date = date
        self.team_a = team_a
        self.team_b = team_b

    def add_event(self, event, team):
        self.events[team][event] += 1


def points(gd):  # argument is goals difference
    """counts the amount of points for the result generator function"""
    return (gd and (2, -1)[gd < 0]) + 1


def result_generator(match):  # argument is an instance of the "Match" class
    """generates the dict 'match_results' with data for the ranking of teams in the group stage"""
    m_number = match_number(match.team_a, match.team_b)
    match_results[m_number][match.team_a]['goals_for'] = match.goals_a  # add df to match_results dict
    match_results[m_number][match.team_b]['goals_for'] = match.goals_b  # add df to match_results dict
    match_results[m_number][match.team_a]['goals_against'] = match.goals_b  # add da to match_results dict
    match_results[m_number][match.team_b]['goals_against'] = match.goals_a  # add da to match_results dict
    match_results[m_number]['events'][match.team_a] = match.events[match.team_a]  # add events in the match_result dict
    match_results[m_number]['events'][match.team_b] = match.events[match.team_b]  # add events in the match_result dict
    goals_a = int(match.goals_a)
    goals_b = int(match.goals_b)
    goals_dif = goals_a - goals_b
    match_results[m_number][match.team_a]['points'] += points(goals_dif)  # add points to match_results dict
    match_results[m_number][match.team_b]['points'] += points(-goals_dif)  # add points to match_results dict
    match_results[m_number][match.team_a]['goal_dif'] = \
        match_results[m_number][match.team_a]['goals_for'] - match_results[m_number][match.team_a]['goals_against']
    match_results[m_number][match.team_b]['goal_dif'] = \
        match_results[m_number][match.team_b]['goals_for'] - match_results[m_number][match.team_b]['goals_against']


def match_number(team_a, team_b):
    """determines the number of the match by the names of the teams"""
    for k, v in match_results.items():
        if team_a in [*v.keys()] and team_b in [*v.keys()]:
            return k


def group_name(team_name):
    """Returns group name by team name"""
    for k, v in g_name.items():
        for i in v:
            if team_name in i:
                return k


def ranking_of_two(team_a, team_b, match_ab):
    if match_results[match_ab][team_a]['points'] > match_results[match_ab][team_b]['points']:
        return [team_a, team_b]
    else:
        return [team_b, team_a]


def ranking_of_three(team_a, team_b, team_c, match_ab, match_ac, match_bc):
    res_1 = {team_a: match_results[match_ab][team_a],
             team_b: match_results[match_ab][team_b],
             team_c: match_results[match_ac][team_c]}
    res_2 = {team_a: match_results[match_ac][team_a],
             team_b: match_results[match_bc][team_b],
             team_c: match_results[match_bc][team_c]}
    criteria_a = Counter()
    criteria_b = Counter()
    criteria_c = Counter()
    for v, k in res_1.items():
        if v == team_a:
            criteria_a.update(k)
            criteria_a.update(res_2[v])
        elif v == team_b:
            criteria_b.update(k)
            criteria_b.update(res_2[v])
        elif v == team_c:
            criteria_c.update(k)
            criteria_c.update(res_2[v])
    total_res = [[team_a, criteria_a['points'], criteria_a['goal_dif'], criteria_a['goals_for']],
                 [team_b, criteria_b['points'], criteria_b['goal_dif'], criteria_b['goals_for']],
                 [team_c, criteria_c['points'], criteria_c['goal_dif'], criteria_c['goals_for']]]
    total_res.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    if total_res[0][1:] == total_res[1][1:] \
            or total_res[0][1:] == total_res[2][1:] \
            or total_res[1][1:] == total_res[2][1:]:
        return False
    else:
        return [total_res[0][0], total_res[1][0], total_res[2][0]]


def fair_play(team_a, team_b, match_num):
    fair_a = [match_results[match_num]['events'][team_a]['y_card'],
              match_results[match_num]['events'][team_a]['r_card']]
    fair_b = [match_results[match_num]['events'][team_b]['y_card'],
              match_results[match_num]['events'][team_b]['r_card']]
    if fair_a == fair_b:
        return False
    else:
        fair_res = sorted([[team_a, *fair_a], [team_b, *fair_b]], key=lambda x: (-x[2], -x[1]), reverse=True)
        return [fair_res[0][0], fair_res[1][0]]


def fair_play_for_three(team_a, team_b, team_c, match_ab, match_ac, match_bc):
    res_1 = {team_a: [match_results[match_ab]['events'][team_a]['y_card'],
                      match_results[match_ab]['events'][team_a]['r_card']],
             team_b: [match_results[match_ab]['events'][team_b]['y_card'],
                      match_results[match_ab]['events'][team_b]['r_card']],
             team_c: [match_results[match_ac]['events'][team_c]['y_card'],
                      match_results[match_ac]['events'][team_c]['r_card']]}
    res_2 = {team_a: [match_results[match_ac]['events'][team_a]['y_card'],
                      match_results[match_ac]['events'][team_a]['r_card']],
             team_b: [match_results[match_bc]['events'][team_b]['y_card'],
                      match_results[match_bc]['events'][team_b]['r_card']],
             team_c: [match_results[match_bc]['events'][team_c]['y_card'],
                      match_results[match_bc]['events'][team_c]['r_card']]}
    fair_a = Counter()
    fair_b = Counter()
    fair_c = Counter()
    for v, k in res_1.items():
        if v == team_a:
            fair_a.update(k)
            fair_a.update(res_2[v])
        elif v == team_b:
            fair_b.update(k)
            fair_b.update(res_2[v])
        elif v == team_c:
            fair_c.update(k)
            fair_c.update(res_2[v])
    total_res = [[team_a, fair_a], [team_b, fair_b], [team_c, fair_c]]
    total_res.sort(key=lambda x: (-x[1]), reverse=True)
    if fair_a == fair_b == fair_c:
        return False
    elif total_res[0][1] == total_res[1][1] or total_res[1][1] == total_res[2][1]:
        if total_res[0][1] == total_res[1][1]:
            return [total_res[2][0], total_res[0][0], total_res[1][0], 'draw1']
        else:
            return [total_res[0][0], total_res[1][0], total_res[2][0], 'draw2']
    else:
        return [total_res[0][0], total_res[1][0], total_res[2][0]]


def update_status(criteria):  # Criteria is the name of the group
    """shows the ranking in the group stage"""
    res = [[k] + [j for j in v.values()] for k, v in groups[criteria].items()]
    res.sort(key=lambda x: (-x[8], -x[7], -x[5]))
    team_a, team_b, team_c, team_d = [i[0] for i in res]
    f, s, t, fo = [[i[8], i[7], i[5]] for i in res]  # points, goal difference and goal for
    match_ab, match_ac = match_number(team_a, team_b), match_number(team_a, team_c)
    match_ad, match_bc = match_number(team_a, team_d), match_number(team_b, team_c)
    match_bd, match_cd = match_number(team_b, team_d), match_number(team_c, team_d)
    if f == s or s == t or t == fo:
        tuple_bool = f == s, s == t, t == fo
        if tuple_bool.count(True) == 3:  # four teams have the same number of points
            return f'The places of the teams {team_a}, {team_b}, {team_c} and {team_d} ' \
                   f'in the Group {criteria} will be determined by drawing of lots by FIFA'
        elif tuple_bool.count(True) == 2:  # three teams or two pairs have the same number of points
            if tuple_bool.index(False) == 0:  # teams b, c, d have the same number of points
                r_three = ranking_of_three(team_b, team_c, team_d, match_bc, match_bd, match_cd)
                if r_three is False:
                    fair_bcd = fair_play_for_three(team_b, team_c, team_d, match_bc, match_bd, match_cd)
                    if fair_bcd is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {team_a}\n' \
                               f'second, third and fourth places between teams {team_b}, {team_c} and {team_d} ' \
                               f'will be determined by drawing of lots by FIFA'
                    elif len(fair_bcd) == 3:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {team_a}\nsecond place - {fair_bcd[0]}\n" \
                               f"third place - {fair_bcd[1]}\nfourth place - {fair_bcd[2]}\n"
                    elif fair_bcd[-1] == 'draw1':
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {team_a}\nSecond place - {fair_bcd[0]}\n' \
                               f'second and third places between teams {fair_bcd[1]} and {fair_bcd[2]} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'fourth place - {fair_bcd[0]}'
                    else:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {team_a}\nSecond place - {fair_bcd[0]}\n' \
                               f'third and fourth places between teams {fair_bcd[1]} and {fair_bcd[2]} ' \
                               f'will be determined by drawing of lots by FIFA'
                else:
                    return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                           f"first place - {team_a}\nsecond place - {r_three[0]}\n" \
                           f"third place - {r_three[1]}\nfourth place - {r_three[2]}\n"
            elif tuple_bool.index(False) == 2:  # teams a, b, c have the same number of points
                r_three = ranking_of_three(team_a, team_b, team_c, match_ab, match_ac, match_bc)
                if r_three is False:
                    fair_abc = fair_play_for_three(team_a, team_b, team_c, match_ab, match_ac, match_bc)
                    if fair_abc is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first, second and third places between teams {team_a}, {team_b} and {team_c} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'fourth place - {team_d}'
                    elif len(fair_abc) == 3:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {fair_abc[0]}\nsecond place - {fair_abc[1]}\n" \
                               f"third place - {fair_abc[2]}\nfourth place - {team_d}\n"
                    elif fair_abc[-1] == 'draw1':
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first and second places between teams {fair_abc[1]} and {fair_abc[2]} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'third place - {fair_abc[0]}\nFourth place - {team_d}'
                    else:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {fair_abc[0]}\n' \
                               f'second and third places between teams {fair_abc[1]} and {fair_abc[2]} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'fourth place - {team_d}'
                else:
                    return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                           f"first place - {r_three[0]}\nsecond place - {r_three[1]}\n" \
                           f"third place - {r_three[2]}\nfourth place - {team_d}\n"
            else:  # teams a, b as well as teams c, d have the same number of points
                if match_results[match_ab][team_a]['points'] == match_results[match_ab][team_b]['points'] \
                        and match_results[match_cd][team_c]['points'] == match_results[match_cd][team_d]['points']:
                    fair_ab = fair_play(team_a, team_b, match_ab)
                    fair_cd = fair_play(team_c, team_d, match_cd)
                    if fair_ab is False and fair_cd is False:
                        return f'The places of the teams {team_a}, {team_b}, {team_c} and {team_d} ' \
                               f'in the Group {criteria} will be determined by drawing of lots by FIFA'
                    elif fair_ab is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first and second places between teams {team_a} and {team_b} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'third place - {fair_cd[0]}\nFourth place - {fair_cd[1]}'
                    elif fair_cd is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {fair_ab[0]}\nSecond place - {fair_ab[1]}\n' \
                               f'third and fourth places between teams {team_c} and {team_d} ' \
                               f'will be determined by drawing of lots by FIFA'
                    else:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {fair_ab[0]}\nsecond place - {fair_ab[1]}\n" \
                               f"third place - {fair_cd[0]}\nfourth place - {fair_cd[1]}"
                elif match_results[match_ab][team_a]['points'] == match_results[match_ab][team_b]['points']:
                    fair_ab = fair_play(team_a, team_b, match_ab)
                    r_two_cd = ranking_of_two(team_c, team_d, match_cd)
                    if fair_ab is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first and second places between teams {team_a} and {team_b} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'third place - {r_two_cd[0]}\nFourth place - {r_two_cd[1]}'
                    else:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {fair_ab[0]}\nsecond place - {fair_ab[1]}\n" \
                               f"third place - {r_two_cd[0]}\nfourth place - {r_two_cd[1]}"
                elif match_results[match_cd][team_c]['points'] == match_results[match_cd][team_d]['points']:
                    fair_cd = fair_play(team_c, team_d, match_cd)
                    r_two_ab = ranking_of_two(team_a, team_b, match_ab)
                    if fair_cd is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {r_two_ab[0]}\nSecond place - {r_two_ab[1]}\n' \
                               f'third and fourth places between teams {team_c} and {team_d} ' \
                               f'will be determined by drawing of lots by FIFA'
                    else:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {r_two_ab[0]}\nsecond place - {r_two_ab[1]}\n" \
                               f"third place - {fair_cd[0]}\nfourth place - {fair_cd[1]}"

                else:
                    r_two_ab = ranking_of_two(team_a, team_b, match_ab)
                    r_two_cd = ranking_of_two(team_c, team_d, match_cd)
                    return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                           f"first place - {r_two_ab[0]}\nsecond place - {r_two_ab[1]}\n" \
                           f"third place - {r_two_cd[0]}\nfourth place - {r_two_cd[1]}"
        else:  # two teams have the same number of points
            if tuple_bool.index(True) == 0:
                if match_results[match_ab][team_a]['points'] == match_results[match_ab][team_b]['points']:
                    fair_ab = fair_play(team_a, team_b, match_ab)
                    if fair_ab is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first and second places between teams {team_a} and {team_b} will be ' \
                               f'determined by drawing of lots by FIFA\n' \
                               f'third place - {team_c}\nFourth place - {team_d}'
                    else:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {fair_ab[0]}\nsecond place - {fair_ab[1]}\n" \
                               f"third place - {team_c}\nfourth place - {team_d}"
                else:
                    r_two_ab = ranking_of_two(team_a, team_b, match_ab)
                    return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                           f"first place - {r_two_ab[0]}\nsecond place - {r_two_ab[1]}\n" \
                           f"third place - {team_c}\nfourth place - {team_d}"
            elif tuple_bool.index(True) == 1:
                if match_results[match_bc][team_b]['points'] == match_results[match_bc][team_c]['points']:
                    fair_bc = fair_play(team_b, team_c, match_bc)
                    if fair_bc is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {team_a}\n' \
                               f'second and third places between teams {team_c} and {team_d} ' \
                               f'will be determined by drawing of lots by FIFA\n' \
                               f'third place - {team_d}'
                    else:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {team_a}\nsecond place - {fair_bc[0]}\n" \
                               f"third place - {fair_bc[1]}\nfourth place - {team_d}"
                else:
                    r_two_bc = ranking_of_two(team_b, team_c, match_bc)
                    return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                           f"first place - {team_a}\nsecond place - {r_two_bc[0]}\n" \
                           f"third place - {r_two_bc[1]}\nfourth place - {team_d}"
            else:  # tuple_bool.index(True) == 2
                if match_results[match_cd][team_c]['points'] == match_results[match_cd][team_d]['points']:
                    fair_cd = fair_play(team_c, team_d, match_cd)
                    if fair_cd is False:
                        return f'The ranking of teams in the Group {criteria} as of {date_now}:\n' \
                               f'first place - {team_a}\nSecond place - {team_b}\n' \
                               f'third and fourth places beetwen teams {team_c} and {team_d} ' \
                               f'will be determined by drawing of lots by FIFA'
                    else:
                        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                               f"first place - {team_a}\nsecond place - {team_b}\n" \
                               f"third place - {fair_cd[0]}\nfourth place - {fair_cd[1]}"
                else:
                    r_two_cd = ranking_of_two(team_c, team_d, match_cd)
                    return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
                           f"first place - {team_a}\nsecond place - {team_b}\n" \
                           f"third place - {r_two_cd[0]}\nfourth place - {r_two_cd[1]}"
    else:
        return f"The ranking of teams in the Group {criteria} as of {date_now}:\n" \
               f"first place - {team_a}\nsecond place - {team_b}\n" \
               f"third place - {team_c}\nfourth place - {team_d}"


class Group:
    @staticmethod
    def team_position(team_name):
        """shows the team's current position in the group"""
        return update_status(group_name(team_name))


# экземпляры класса 'Match'
match_2 = Match('Al Thumama Stadium', '21/11/22', 'Senegal', 'Netherlands')
match_1 = Match('Al Bayt Stadium', '21/11/22', 'Qatar', 'Ecuador')
match_18 = Match('Al Thumama Stadium', '25/11/22', 'Senegal', 'Qatar')
match_19 = Match('Khalifa International Stadium', '25/11/22', 'Netherlands', 'Ecuador')
match_35 = Match('Khalifa International Stadium', '29/11/22', 'Senegal', 'Ecuador')
match_36 = Match('Al Bayt Stadium', '29/11/22', 'Netherlands', 'Qatar')

# вносим кол-во голов и events в экземпляры класса 'Match'
match_1.goals_a = 1
match_1.goals_b = 1
match_1.add_event('r_card', 'Qatar')

match_2.goals_a = 1
match_2.goals_b = 1
match_2.add_event('y_card', 'Senegal')
match_2.add_event('y_card', 'Senegal')
match_2.add_event('r_card', 'Netherlands')

match_18.goals_a = 1
match_18.goals_b = 1
match_18.add_event('r_card', 'Senegal')
match_18.add_event('r_card', 'Qatar')

match_19.goals_a = 1
match_19.goals_b = 1
match_19.add_event('y_card', 'Netherlands')
match_19.add_event('r_card', 'Ecuador')

match_35.goals_a = 1
match_35.goals_b = 1
match_35.add_event('y_card', 'Ecuador')

match_36.goals_a = 1
match_36.goals_b = 1
match_36.add_event('y_card', 'Netherlands')
match_36.add_event('y_card', 'Qatar')

# с помощью функции "result_generator" обновляем dict "match_results"
result_generator(match_1)
result_generator(match_2)
result_generator(match_18)
result_generator(match_19)
result_generator(match_35)
result_generator(match_36)
