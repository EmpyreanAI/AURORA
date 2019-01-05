import simulator.cli as Cli

if __name__ == '__main__':
    try:
        simulator = Cli.get_simulator()
        simulator.run()
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
