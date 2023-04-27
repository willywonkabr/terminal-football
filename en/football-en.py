from random import randint
TEAMS = {
    'team_a': {'name': "Brazil",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0},
    'team_b': {'name': "France",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0},
    'team_c': {'name': "Israel",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0},
    'team_d': {'name': "Angola",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0},
}

MATCHES = [
# Turno 1
    # Rodada 1
    {'home': TEAMS['team_a'], 'goals_home': 0, 'away': TEAMS['team_b'], 'goals_away': 0},
    {'home': TEAMS['team_c'], 'goals_home': 0, 'away': TEAMS['team_d'], 'goals_away': 0},
    # Rodada 2
    {'home': TEAMS['team_a'], 'goals_home': 0, 'away': TEAMS['team_c'], 'goals_away': 0},
    {'home': TEAMS['team_b'], 'goals_home': 0, 'away': TEAMS['team_d'], 'goals_away': 0},
    # Rodada 3
    {'home': TEAMS['team_a'], 'goals_home': 0, 'away': TEAMS['team_d'], 'goals_away': 0},
    {'home': TEAMS['team_c'], 'goals_home': 0, 'away': TEAMS['team_b'], 'goals_away': 0},
# Turno 2
    # Rodada 4
    {'home': TEAMS['team_a'], 'goals_home': 0, 'away': TEAMS['team_b'], 'goals_away': 0},
    {'home': TEAMS['team_c'], 'goals_home': 0, 'away': TEAMS['team_d'], 'goals_away': 0},
    # Rodada 5
    {'home': TEAMS['team_a'], 'goals_home': 0, 'away': TEAMS['team_c'], 'goals_away': 0},
    {'home': TEAMS['team_b'], 'goals_home': 0, 'away': TEAMS['team_d'], 'goals_away': 0},
    # Rodada 6
    {'home': TEAMS['team_a'], 'goals_home': 0, 'away': TEAMS['team_d'], 'goals_away': 0},
    {'home': TEAMS['team_c'], 'goals_home': 0, 'away': TEAMS['team_b'], 'goals_away': 0},
]
def create_goals():
    return randint(0,3) 
def match_scoreboard(match):
    match['goals_home'] = create_goals()
    match['goals_away'] = create_goals()
def apply_matches_goals(matches):
    for match in matches:
        match_scoreboard(match)
def show_match(match):
    print(f"{match['home']['name']} {match['goals_home']} X {match['goals_away']} {match['away']['name']}")
def matches_report(matches):
    num_match = 1
    num_week = 1
    num_round = 1

    for match in matches:
        if (num_match % 6) == 1:
            print(f"\nRound {num_round}")
            num_round += 1
        if (num_match % 2) == 1:
            print(f"\nWeek {num_week}")
            num_week += 1
        show_match(match)
        num_match += 1
def sum_points(matches):
    for match in matches:
        if match['goals_home'] > match['goals_away']:
            match['home']['points'] += 3
        elif match['goals_home'] < match['goals_away']:
            match['away']['points'] += 3
        else:
            match['home']['points'] += 1
            match['away']['points'] += 1

        match['home']['goals_for'] += match['goals_home']
        match['away']['goals_for'] += match['goals_away']

        match['home']['goals_difference'] += match['goals_home'] - match['goals_away']
        match['away']['goals_difference'] += match['goals_away'] - match['goals_home']

        match['home']['goals_against'] += match['goals_away']
        match['away']['goals_against'] += match['goals_home']
def standing_teams():
    teams_list = list(TEAMS.values()) 
    teams_list = sorted(teams_list, key = lambda team: (team['points'], team['goals_for'], team['goals_difference'], team['goals_against']), reverse = True)
    print("\n", sorted(teams_list, key = lambda team: (team['points'], team['goals_for'], team['goals_difference'], team['goals_against']), reverse = True))
    return teams_list
def final(first, second):
    match = {'home': first, 'goals_home': 0, 'away': second, 'goals_away': 0}
    
    match_scoreboard(match)
    print("\n")
    show_match(match)

    champion = None

    if match['goals_home'] == match['goals_away']:
        penalty_home = randint(0,5)
        penalty_away = randint(0,5)
    
        while penalty_home == penalty_away:
            penalty_home += randint(0,2)
            penalty_away += randint(0,2)

        print("\nPenalties")
        print(f"{match['home']['name']} {penalty_home} x {penalty_away} {match['away']['name']}")

        if penalty_home > penalty_away:
            champion = match['home']
        else:
            champion = match['away']
    else:
        if match['goals_home'] > match['goals_away']:
            champion = match['home']
        else:
            champion = match['away']
    print(f"Champion {champion['name']}")
apply_matches_goals(MATCHES)
matches_report(MATCHES)
sum_points(MATCHES)
standing = standing_teams()

first, second = standing[0], standing[1]
final(first, second)
