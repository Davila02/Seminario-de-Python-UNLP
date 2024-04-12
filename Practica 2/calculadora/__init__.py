def generar_estructura(names,goals,goals_avoided,assists):
    players_stats = {}

    for name, goal, goal_a, assist in zip(names, goals, goals_avoided, assists):
        datos = (goal, goal_a, assist)
        players_stats[name] = datos

    return players_stats

def goleador(player_stats):
    max_player, cant_goals = max(player_stats.items(), key=lambda elem: elem[1][0])
    info = (max_player,cant_goals[0])
    return info