
from argparse import ArgumentParser
from .stockmarket import StockMarket
from .brokerage import Brokerage
from agents.random import RandomAgent

DEFAULT_WINDOW_SIZE = 10
DEFAULT_START_YEAR = 2004
DEFAULT_END_YEAR = 2018
DEFAULT_STOCK = ['VALE3', 'PETR3', 'ALPA3']

DEFAULT_AGENT = 'random'
DEFAULT_ACTIONS = 'all'
DEFAULT_INSIDER = 'random'

DEFAULT_FEE = 0


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
                       default=DEFAULT_WINDOW_SIZE, type=int,
                       help='Select the size of the window to learn from')

    group = parser.add_argument_group('Agent Setup')

    group.add_argument('-a', '--agent', dest='agent',
                       choices=['random'], default=DEFAULT_AGENT, type=str,
                       help="""Select the type of the agent
                       to run in the simulator""")
    group.add_argument('-A', '--actions', dest='actions',
                       choices=['all', 'nowait'], default=DEFAULT_ACTIONS,
                       type=str, help='Select the desired action vector')
    group.add_argument('-s', '--stock', dest='stock', default=DEFAULT_STOCK,
                       type=list, help='Select the stock to make transactions')
    group.add_argument('-i', '--insider', dest='insider',
                       default=DEFAULT_INSIDER, type=str, choices=['random'],
                       help='Select the type of the insider')

    group = parser.add_argument_group('Brokerage Setup')
    group.add_argument('-f', '--fee', dest='fee',
                       default=DEFAULT_FEE, type=int,
                       help="""Select the ammount of the transactions fee""")

    args = parser.parse_args()
    market = register_market(args)
    brokerage = register_brokerage(market, args.fee)
    agent = register_agent("J.Bond", brokerage, args)
    brokerage.register_agent(agent)

    return agent, brokerage


def register_agent(agent_id, brokerage, args):
    if args.agent == 'random':
        agent = RandomAgent(agent_id, brokerage, args.actions,
                            args.stock, args.insider)
    else:
        raise ValueError("Agent must be 'random'.")

    return agent


def register_brokerage(market, fee):
    return Brokerage(market, fee)


def register_market(args):
    return StockMarket(window_size=args.window,
                       start_year=args.start_year,
                       end_year=args.end_year)
