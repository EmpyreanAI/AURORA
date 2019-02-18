
from argparse import ArgumentParser
from simulator.stockmarket import StockMarket
from agents.random import RandomAgent

DEFAULT_WINDOW_SIZE = 10
DEFAULT_START_YEAR = 2017
DEFAULT_END_YEAR = 2018
DEFAULT_STOCK = ['VALE3', 'VALE3', 'VALE3']

DEFAULT_AGENT = 'random'
DEFAULT_ACTIONS = 'all'



def get_simulator():

    parser = ArgumentParser(description='...')

    group = parser.add_argument_group('Stock Market Setup')

    group.add_argument('-sy', '--start-year', dest='start_year',
                        default=DEFAULT_START_YEAR,
                        choices=list(range(DEFAULT_START_YEAR,
                                           DEFAULT_END_YEAR)),
                        type=int, help='Select the first year of the data.')
    group.add_argument('-ey', '--end-year', dest='end_year',
                        default=DEFAULT_END_YEAR,
                        choices=list(range(DEFAULT_START_YEAR,
                                           DEFAULT_END_YEAR)),
                        type=int, help='Select the last year of the data.')
    group.add_argument('-ws', '--window_size', dest='window',
                        default=DEFAULT_WINDOW_SIZE,
                        type=int, help='Select the size of the window to learn from')

    group = parser.add_argument_group('Agent Setup')

    group.add_argument('-a', '--agent', dest='agent',
                        choices=['random'], default=DEFAULT_AGENT,
                        type=str, help='Select the type of the agent to run in the simulator')
    group.add_argument('-act', '--actions', dest='actions',
                        choices=['all', 'nowait'], default=DEFAULT_ACTIONS,
                        type=str, help='Select the desired action vector')
    group.add_argument('-s', '--stock', dest='stock', default=DEFAULT_STOCK,
                        type=list, help='Select the stock to make transactions')

    args = parser.parse_args()

    agent = register_agent(args)

    simulator = register_market(args, agent)

    return simulator

def register_agent(args):
    if args.agent == 'random':
        return RandomAgent(args.actions, args.stock)
    else:
        raise ValueError("Agent must be 'random'.")

def register_market(args, agent):
    return StockMarket(agent=agent,
                       window_size=args.window,
                       start_year=args.start_year,
                       end_year=args.end_year)
