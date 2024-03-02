import argparse
import logging
import multiprocessing
from multiprocessing import Pool

import numpy
from rich.console import Console
from rich.live import Live
from rich.progress import track
from rich.table import Table

from cost_function import CostFunction
from game import Game
from game_consts import *
from player import Player
from shared_array import SharedArray

logger = logging.getLogger('logger')
logger.setLevel(logging.ERROR)
console = logging.StreamHandler()
logger.addHandler(console)

console = Console()


def log_one_game(game_number: int, cost_function, seed: int = None) -> None:
    game = Game(seed=seed)

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Player", style="dim", width=12)
    table.add_column("Jump 10", justify="center")
    table.add_column("H1 :arrow_down_small:", justify="right")
    table.add_column("H2 :arrow_down_small:", justify="right")
    table.add_column("H3 :arrow_up_small:", justify="right")
    table.add_column("H4 :arrow_up_small:", justify="right")

    console.rule(f"Starting game #{game_number}")

    with Live(table, refresh_per_second=100):  # update 4 times a second to feel fluid
        cards_left = Player.play_one_game(game, cost_function, table)

    console.print(f"Number of cards left in deck: {cards_left}")


def play_once(game_number: int, seed: int, cost_parameters: dict, arr_size: tuple[int, int]):
    g = Game(seed=seed)
    shared_arr = SharedArray(create=False, num_elements=arr_size)
    cost_function = CostFunction(shared_arr=shared_arr, row_in_arr=game_number, **cost_parameters)
    deck_size = Player.play_one_game(g, cost_function)
    return deck_size


def play_n_games(num_games: int, cost_parameters: dict = {}, with_progress_bar: bool = True,
                 seed: int = None, num_processes: int = None, spawn_child_prccesses: bool = True) -> list[int]:
    deck_sizes = []

    generator = range(num_games)
    if with_progress_bar:
        generator = track(generator, description="Playing ...")

    arr_size = [num_games, DECK_SIZE]
    shared_arr = SharedArray(create=True, num_elements=arr_size)

    try:
        if spawn_child_prccesses:
            if num_processes is None:
                num_processes = multiprocessing.cpu_count() // 2
            with Pool(num_processes) as p:
                params = [
                    [game_number, seed, cost_parameters, arr_size] for game_number in range(num_games)
                ]
                deck_sizes = p.starmap(play_once, params)
        else:
            for game_number in range(num_games):
                game_res = play_once(game_number, seed, cost_parameters, arr_size)
                deck_sizes.append(game_res)

        arr = numpy.array(deck_sizes)
        m, s = numpy.mean(arr), numpy.std(arr)
        if with_progress_bar:
            print(f"mean deck size is {m}, std is {s}")
    finally:
        # print(shared_arr.stats())
        del shared_arr

    return m, s, arr


def main() -> None:
    parser = argparse.ArgumentParser(description='Play "The Game"')
    parser.add_argument('--num-games', type=int, help='number of games to play', required=False)
    parser.add_argument('--print', action='store_const',
                        const="print", default="print", help='print a game to the console', required=False)
    parser.add_argument('--seed', action='store', type=int,
                        default=None, help='set a random seed for all the games', required=False)
    parser.add_argument('--num-processes', action='store', type=int,
                        default=None, help='number of child processes', required=False)
    parser.add_argument('--spawn', action=argparse.BooleanOptionalAction, required=False,
                        help='spawn child processes', default=True)

    parser.add_argument('--opt-param', action="append", required=False,
                        help='optimization parameters in the shape param=val')

    args = parser.parse_args()

    cost_parameters = {}
    for p in args.opt_param:
        param, val = p.split("=")
        cost_parameters[param] = float(val)

    print(f"optimization parameters: {cost_parameters}")

    if args.num_games is not None:
        play_n_games(args.num_games, cost_parameters=cost_parameters, with_progress_bar=True, seed=args.seed,
                     num_processes=args.num_processes, spawn_child_prccesses=args.spawn)
    else:
        shared_arr = SharedArray(create=True, num_elements=[1, DECK_SIZE])
        cf = CostFunction(shared_arr=shared_arr, )
        log_one_game(1, cf, seed=args.seed)
        print(cf.stats())


if __name__ == '__main__':
    main()
