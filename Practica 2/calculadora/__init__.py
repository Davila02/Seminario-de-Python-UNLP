def generar_estructura(names,goals,goals_avoided,assists):
    players_stats = {}

    for name, goal, goal_a, assist in zip(names, goals, goals_avoided, assists):
        datos = (goal, goal_a, assist)
        players_stats[name] = datos

    return players_stats

