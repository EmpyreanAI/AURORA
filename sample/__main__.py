import simulator.cli as Cli

def _log(msg):
    print("[Main] {}".format(msg))

if __name__ == '__main__':
    try:
        AGENT, BROKERAGE = Cli.get_simulator()
        AGENT.cash_add(1000.00)
        AGENT.log_cash()
        BROKERAGE.run()
        AGENT.log_profit()
        AGENT.log_cash()
        _log("Simulation Completed")
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
