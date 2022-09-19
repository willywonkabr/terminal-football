let TEAMS = {
  teamA: {name: 'Brazil', points: 0, goals_for: 0, goals_difference: 0, goals_against: 0,},
  teamB: {name: 'France', points: 0, goals_for: 0, goals_difference: 0, goals_against: 0,},
  teamC: {name: 'Israel', points: 0, goals_for: 0, goals_difference: 0, goals_against: 0,},
  teamD: {name: 'Angola', points: 0, goals_for: 0, goals_difference: 0, goals_against: 0,},
}
let MATCHES = [
// Turno 1
  // Rodada 1
  {home: TEAMS.teamA, goalsHome: 0, away: TEAMS.teamB, goalsAway: 0},
  {home: TEAMS.teamC, goalsHome: 0, away: TEAMS.teamD, goalsAway: 0},
  // Rodada 2
  {home: TEAMS.teamA, goalsHome: 0, away: TEAMS.teamC, goalsAway: 0},
  {home: TEAMS.teamB, goalsHome: 0, away: TEAMS.teamD, goalsAway: 0},
  // Rodada 3
  {home: TEAMS.teamA, goalsHome: 0, away: TEAMS.teamD, goalsAway: 0},
  {home: TEAMS.teamC, goalsHome: 0, away: TEAMS.teamB, goalsAway: 0},
// Turno 2
  // Rodada 4
  {away: TEAMS.teamA, goalsHome: 0, home: TEAMS.teamB, goalsAway: 0},
  {away: TEAMS.teamC, goalsHome: 0, home: TEAMS.teamD, goalsAway: 0},
  // Rodada 5
  {away: TEAMS.teamA, goalsHome: 0, home: TEAMS.teamC, goalsAway: 0},
  {away: TEAMS.teamB, goalsHome: 0, home: TEAMS.teamD, goalsAway: 0},
  // Rodada 6
  {away: TEAMS.teamA, goalsHome: 0, home: TEAMS.teamD, goalsAway: 0},
  {away: TEAMS.teamB, goalsHome: 0, home: TEAMS.teamC, goalsAway: 0},
]
function createGoals(max) {
  return Math.floor(Math.random() * max)
}
function matchScoreboard(match) {
  match.goalsHome = createGoals(4)
  match.goalsAway = createGoals(4)
}
function applyMatchesGoals(matches) {
  for (let match of matches) {
    matchScoreboard(match)
  }
}
function showMatch(match) {
  console.log(`${match.home.name}    ${match.goalsHome}  x  ${match.goalsAway}   ${match.away.name}`)
}
function matchesReport(matches) {
  let numMatch = 1
  let numWeek = 1
  let numRound = 1

  for (let match of matches) {
    if (numMatch % 6 === 1) {
      console.log(`\nRound ${numRound}`)
      numRound++
    }
    if (numMatch % 2 === 1) {
      console.log(`\nWeek ${numWeek}`)
      numWeek++
    }
    showMatch(match)
    numMatch++
  }
}
function sumPoints(matches) {
  for (let {home, away, goalsHome, goalsAway} of matches) {
    if (goalsHome > goalsAway) {
      home.points += 3
    } else if (goalsHome < goalsAway) {
      away.points += 3
    } else {
      home.points++
      away.points++
    }
    home.goals_for += goalsHome
    away.goals_for += goalsAway

    home.goals_against += goalsAway
    away.goals_against += goalsHome

    home.goals_difference += goalsHome - goalsAway
    away.goals_difference += goalsAway - goalsHome
  }
}
function standingTeams(teams) {
  let teamsList = Object.values(teams)

  teamsList.sort((team1, team2) => {
    if(team1.points !== team2.points) {
      return team2.points - team1.points
    }
    if(team2.goals_for !== team2.goals_for) {
      return team2.goals_for - team1.goals_for
    }
    if(team1.goals_difference !== team2.goals_difference) {
      return team2.goals_difference - team1.goals_difference
    }
    return team1.goals_against - team2.goals_against
  })
  return teamsList
}
function final(first, second) {
  let match = {away: first, goalsHome: 0, home: second, goalsAway: 0}

  matchScoreboard(match)
  showMatch(match)

  let champion = null

  if(match.goalsHome === match.goalsAway) {
    let penaltyHome = createGoals(6)
    let penaltyAway = createGoals(6)

    while(penaltyHome === penaltyAway) {
      penaltyHome += createGoals(2)
      penaltyAway += createGoals(2)
    }

    console.log('\nPenalties')
    console.log(`${match.home.name}     ${penaltyHome}  x  ${penaltyAway}     ${match.away.name}`)

    if(penaltyHome > penaltyAway) {
      champion = match.home
    } else {
      champion = match.away
    }
  } else {
    if(match.goalsHome > match.goalsAway) {
      champion = match.home
    } else {
      champion = match.away
    }    
  }
  console.log(`Champion ${champion.name}`)
}

applyMatchesGoals(MATCHES)
matchesReport(MATCHES)
sumPoints(MATCHES)
let standing = standingTeams(TEAMS)
console.table(standing)

let [first, second] = standing
final(first, second)
