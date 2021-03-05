"""
https://www.algoexpert.io/questions/Tournament%20Winner
"""

competitions = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
results = [0, 1, 1]


def calculate_scores(competitions, results):
    total_scores = {}
    win_points = 3

    for i, team in enumerate(competitions):
        hometeam, awayteam = team[0], team[1]
        if results[i] == 0:
            total_scores[awayteam] = total_scores.get(awayteam, 0) + win_points
            total_scores[hometeam] = total_scores.get(hometeam, 0) + 0

        else:
            total_scores[hometeam] = total_scores.get(hometeam, 0) + win_points
            total_scores[awayteam] = total_scores.get(awayteam, 0) + 0
    return total_scores


def tournamentWinner(competitions, results):
    total_scores = calculate_scores(competitions, results)
    winner = ""
    max_score_so_far = 0

    for team, score in total_scores.items():
        if score > max_score_so_far:
            max_score_so_far = score
            winner = team
    return winner


print(tournamentWinner(competitions, results))
