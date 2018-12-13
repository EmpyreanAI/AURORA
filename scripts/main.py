from simulator import Simulator

if __name__ == '__main__':
  try:
    Simulator.run()
    # import pdb; pdb.set_trace()
  except KeyboardInterrupt:
    print('\n\nInterrupted execution\n')
