from utils import *
import math


def get_chooser(depth):
    def temp(this_game_map: np.ndarray):
        return choose(this_game_map, depth)

    return temp


def choose(this_game_map: np.ndarray, depth):
    best_score = -math.inf
    best_choice = None
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    alpha = -math.inf
    beta = math.inf
    for point in choices:
        this_game_map[point] = 1
        this_score = minmax_dfs(-this_game_map, depth - 1, -beta, -alpha)
        this_score = -this_score
        this_game_map[point] = 0
        if this_score > best_score:
            best_score = this_score
            best_choice = point
        alpha = max(alpha, best_score)
    return best_choice


def minmax_dfs(this_game_map: np.ndarray, depth, alpha, beta):
    score = get_two_side_score(this_game_map)
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    if depth == 0:
        return score
    for point in choices:
        this_game_map[point] = 1
        this_score = minmax_dfs(-this_game_map, depth - 1, -beta, -alpha)
        this_score = -this_score
        this_game_map[point] = 0
        score = max(this_score, score)

        if score > beta:
            break
        alpha = max(alpha, score)

    return score
