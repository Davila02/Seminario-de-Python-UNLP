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

def calcular_promedio_ponderado(player_stats):
    promedio_jugadores = []
    for player, stats in player_stats.items():
        promedio_ponderado = (player, (stats[0] * 1.5) + (stats[1] * 1.25) + stats[2])
        promedio_jugadores.append(promedio_ponderado)
    return promedio_jugadores

def mas_influyente(player_stats):
    return max(calcular_promedio_ponderado(player_stats), key=lambda elem:elem[1])[0]

def promedio_goles(goals):
    return sum(goals)/25

def promedio_goleador(goals):
    return goals/25