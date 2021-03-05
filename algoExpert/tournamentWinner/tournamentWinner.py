"""
https://www.algoexpert.io/questions/Tournament%20Winner
"""

competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

def tournamentWinner(competitions, results):
    
    total_scores = {}
    i = 0
    win_points = 3

    while i < len(results):
        for team in competitions:
            hometeam, awayteam = team[0], team[1]
            if results[i] == 0:
                total_scores[awayteam] = total_scores.get(awayteam, 0) + win_points
                total_scores[hometeam] = total_scores.get(hometeam, 0) + 0 

            else:
                total_scores[hometeam] = total_scores.get(hometeam, 0) + win_points
                total_scores[awayteam] = total_scores.get(awayteam, 0) + 0 

            i += 1
        print(total_scores)

print(tournamentWinner(competitions, results))
