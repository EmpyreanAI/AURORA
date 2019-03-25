import simulator.cli as Cli

def _log(msg):
    print("[Main] {}".format(msg))

if __name__ == '__main__':
    try:
        AGENT, MARKET = Cli.get_simulator()
        AGENT.cash_add(1000.00)
        AGENT.log_cash()
        MARKET.proxy().run()
        AGENT._brokerage.proxy().please_pass_the_day()
        AGENT.log_profit()
        AGENT.log_cash()
        _log("Simulation Completed")
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
