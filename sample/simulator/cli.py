
from argparse import ArgumentParser
from simulator.simulator import Simulator
from simulator.simulator import (DEFAULT_START_YEAR, DEFAULT_END_YEAR,
                                 DEFAULT_AGENT, DEFAULT_STOCK,
                                 DEFAULT_WINDOW_SIZE, DEFAULT_ACTIONS)


def get_simulator():

    parser = ArgumentParser(description='...')

    group = parser.add_argument_group('Simulator Setup')

    parser.add_argument('-sy', '--start-year', dest='start_year',
                        default=DEFAULT_START_YEAR,
                        choices=list(range(DEFAULT_START_YEAR,
                                           DEFAULT_END_YEAR)),
                        type=int, help='Select the first year of the data.')
    parser.add_argument('-ey', '--end-year', dest='end_year',
                        default=DEFAULT_END_YEAR,
                        choices=list(range(DEFAULT_START_YEAR,
                                           DEFAULT_END_YEAR)),
                        type=int, help='Select the last year of the data.')
    parser.add_argument('-a', '--agent', dest='agent',
                        choices=['random'], default=DEFAULT_AGENT,
                        type=str, help='Select the type of the agent to run in the simulator')
    parser.add_argument('-s', '--stock', dest='stock',
                        choices=['VALE3'], default=DEFAULT_STOCK,
                        type=str, help='Select the stock to make transactions')
    parser.add_argument('-ws', '--window_size', dest='window',
                        default=DEFAULT_WINDOW_SIZE,
                        type=int, help='Select the size of the window to learn from')
    parser.add_argument('-act', '--actions', dest='actions',
                        choices=['all', 'nowait'], default=DEFAULT_ACTIONS,
                        type=str, help='Select the desired action vector')

    args = parser.parse_args()

    simulator = Simulator(window_size=args.window,
                          actions=args.actions,
                          stock=args.stock,
                          agent=args.agent,
                          start_year=args.start_year,
                          end_year=args.end_year)

    return simulator
