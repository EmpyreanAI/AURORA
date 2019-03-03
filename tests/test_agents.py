import unittest
from .context import sample
# from sample. import
# import agents.random

class TestBaseAgent(unittest.TestCase):

    def test_agent_init(self):
        agent = sample.BaseAgent('all', [])
        self.assertEqual(agent.cash,0)
        self.assertEqual(agent.profit,0)
        self.assertEqual(agent.actions,['buy', 'sell', 'wait'])
        self.assertEqual(agent.cash,0)


class TestRandomAgent(unittest.TestCase):

    def test_agent_init(self):
        pass

if __name__ == "__main__":
    unittest.main()
