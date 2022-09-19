import random
TEAMS = {
    'teamA': {'name': "Brazil",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0,},
    'teamB': {'name': "France",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0,},
    'teamC': {'name': "Israel",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0,},
    'teamD': {'name': "Angola",'points': 0,'goals_for': 0,'goals_difference': 0,'goals_against': 0,},
}

MATCHES = [
# Turno 1
    # Rodada 1
    {'home': TEAMS['teamA'], 'goalsHome': 0, 'away': TEAMS['teamB'], 'goalsAway': 0},
    {'home': TEAMS['teamC'], 'goalsHome': 0, 'away': TEAMS['teamD'], 'goalsAway': 0},
    # Rodada 2
    {'home': TEAMS['teamA'], 'goalsHome': 0, 'away': TEAMS['teamC'], 'goalsAway': 0},
    {'home': TEAMS['teamB'], 'goalsHome': 0, 'away': TEAMS['teamD'], 'goalsAway': 0},
    # Rodada 3
    {'home': TEAMS['teamA'], 'goalsHome': 0, 'away': TEAMS['teamD'], 'goalsAway': 0},
    {'home': TEAMS['teamC'], 'goalsHome': 0, 'away': TEAMS['teamB'], 'goalsAway': 0},
# Turno 2
    # Rodada 4
    {'home': TEAMS['teamA'], 'goalsHome': 0, 'away': TEAMS['teamB'], 'goalsAway': 0},
    {'home': TEAMS['teamC'], 'goalsHome': 0, 'away': TEAMS['teamD'], 'goalsAway': 0},
    # Rodada 5
    {'home': TEAMS['teamA'], 'goalsHome': 0, 'away': TEAMS['teamC'], 'goalsAway': 0},
    {'home': TEAMS['teamB'], 'goalsHome': 0, 'away': TEAMS['teamD'], 'goalsAway': 0},
    # Rodada 6
    {'home': TEAMS['teamA'], 'goalsHome': 0, 'away': TEAMS['teamD'], 'goalsAway': 0},
    {'home': TEAMS['teamC'], 'goalsHome': 0, 'away': TEAMS['teamB'], 'goalsAway': 0},
]
def createGoals():
    return random.randint(0,3) 
def matchScoreboard(match):
    match['goalsHome'] = createGoals()
    match['goalsAway'] = createGoals()
def applyMatchesGoals(matches):
    for match in matches:
        matchScoreboard(match)
def showMatch(match):
    print(f"{match['home']['name']} {match['goalsHome']} X {match['goalsAway']} {match['away']['name']}")
def matchesReport(matches):
    numMatch = 1
    numWeek = 1
    numRound = 1

    for match in matches:
        if (numMatch % 6) == 1:
            print(f"\nRound {numRound}")
            numRound += 1
        if (numMatch % 2) == 1:
            print(f"\nWeek {numWeek}")
            numWeek += 1
        showMatch(match)
        numMatch += 1
def sumPoints(matches):
    for match in matches:
        if match['goalsHome'] > match['goalsAway']:
            match['home']['points'] += 3
        elif match['goalsHome'] < match['goalsAway']:
            match['away']['points'] += 3
        else:
            match['home']['points'] += 1
            match['away']['points'] += 1

        match['home']['goals_for'] += match['goalsHome']
        match['away']['goals_for'] += match['goalsAway']

        match['home']['goals_difference'] += match['goalsHome'] - match['goalsAway']
        match['away']['goals_difference'] += match['goalsAway'] - match['goalsHome']

        match['home']['goals_against'] += match['goalsAway']
        match['away']['goals_against'] += match['goalsHome']
def standingTeams():
    teamsList = list(TEAMS.values()) 
    teamsList = sorted(teamsList, key = lambda team: (team['points'], team['goals_for'], team['goals_difference'], team['goals_against']), reverse = True)
    # print("\n",sorted(teamsList, key = lambda team: (team['points'], team['goals_for'], team['goals_difference'], team['goals_against']), reverse = True))
    # Print the names of the columns.
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('name', 'points', 'goals_for', 'goals_difference', 'goals_against'))
 
    # print each data item.
    for key, value in teamsList:
        name, points, goals_for, goals_difference, goals_against = value
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(name, points, goals_for, goals_difference, goals_against))
    return teamsList
def final(first, second):
    match = {'home': first, 'goalsHome': 0, 'away': second, 'goalsAway': 0}
    
    matchScoreboard(match)
    print("\n")
    showMatch(match)

    champion = None

    if match['goalsHome'] == match['goalsAway']:
        penaltyHome = random.randint(0,5)
        penaltyAway = random.randint(0,5)
    
        while penaltyHome == penaltyAway:
            penaltyHome += random.randint(0,2)
            penaltyAway += random.randint(0,2)

        print("\nPenalties")
        print(f"{match['home']['name']} {penaltyHome} x {penaltyAway} {match['away']['name']}")

        if penaltyHome > penaltyAway:
            champion = match['home']
        else:
            champion = match['away']
    else:
        if match['goalsHome'] > match['goalsAway']:
            champion = match['home']
        else:
            champion = match['away']
    print(f"Champion {champion['name']}")
applyMatchesGoals(MATCHES)
matchesReport(MATCHES)
sumPoints(MATCHES)
standing = standingTeams()

first, second = standing[0], standing[1]
final(first, second)
