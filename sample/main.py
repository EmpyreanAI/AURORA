from simulator.simulator import Simulator

if __name__ == '__main__':
    try:
        Simulator().run()
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
