""" . """

def structure(names, goals, goals_avoided, assists):
    """ Genera un diccionario de tupla utilizando como clave un nombre """
    statistics = {}
    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        statistics[name] = {"goals": goal, "goals_avoided": goal_avoided, "assists": assist}
    return statistics

def scorer(statistics):
    """ Devuelve el nombre y cantidad de goles del jugador con mas goles """
    max_name = max(statistics, key=lambda name: statistics[name]["goals"])
    return max_name, statistics[max_name]["goals"]

def most_influential(statistics):
    """ Devuelve el nombre del jugador con mejor promedio """ 
    return max(statistics, key=lambda name: statistics[name]["goals"] * 1.5 + statistics[name]["goals_avoided"] * 1.25 + statistics[name]["assists"])

def weighted_average(statistics):
    """ Devuelve el promedio de goles del equipo """
    return sum(valor["goals"] for valor in statistics.values()) / 25

def average_scorer(statistics):
    """ Devuelve el promedio del jugador con mas cantidad de goles """
    return scorer(statistics)[1] / 25
