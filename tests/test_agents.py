# pylint: skip-file

"""Test Agents Classes."""

import unittest
from .context import sample


class TestBaseAgent(unittest.TestCase):
    """Test base agent attributes and methods."""

    def test_init(self):
        """Test basic agent initialization properties."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertEqual(agent._cash, 0)
        self.assertEqual(agent._profit, 0)

    def test_init_actions(self):
        """Test basic agent initialization actions."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertEqual(agent.actions, ['buy', 'sell', 'wait'])
        agent2 = sample.BaseAgent('nowait', [], 'random')
        self.assertEqual(agent2.actions, ['buy', 'sell'])

    def test_init_insiders(self):
        """Test basic agent initialization insiders."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertEqual(len(agent.insiders), 0)
        agent2 = sample.BaseAgent('all', ['VALE3'], 'random')
        self.assertEqual(len(agent2.insiders), 1)
        self.assertEqual(agent2.insiders[0]._insider_id, 0)
        agent3 = sample.BaseAgent('all', ['VALE3', 'PETR3', 'ALPA3'], 'random')
        self.assertEqual(len(agent3.insiders), 3)
        self.assertEqual(agent3.insiders[0].insider_id, 0)
        self.assertEqual(agent3.insiders[1].insider_id, 1)
        self.assertEqual(agent3.insiders[2].insider_id, 2)

    def test_cash(self):
        """Test basic agent cash related functions."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertRaises(TypeError, agent.cash_sub, 'a')
        self.assertRaises(TypeError, agent.cash_add, 'a')
        self.assertEqual(agent.cash, 0)
        agent.cash = 20.00
        self.assertEqual(agent.cash, 20.00)
        agent.cash_add(30)
        self.assertEqual(agent.cash, 50.00)
        agent.cash_sub(10)
        self.assertEqual(agent.cash, 40.00)
        agent.cash_zero()
        self.assertEqual(agent.cash, 0)
        self.assertRaises(ValueError, agent.cash_sub, -10)
        self.assertRaises(ValueError, agent.cash_add, -7)

    def test_profit(self):
        """Test basic agent profit related functions."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertRaises(TypeError, agent.profit_add, 'a')
        self.assertEqual(agent.profit, 0)
        agent.profit = 20.00
        self.assertEqual(agent.profit, 20.00)
        agent.profit_add(30)
        self.assertEqual(agent.profit, 50.00)
        agent.profit_zero()
        self.assertEqual(agent.profit, 0)

    def test_act(self):
        """Test basic agent act function."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertRaises(NotImplementedError, agent.act)

    def test_log(self):
        """Test basic agent log function."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertRaises(NotImplementedError, agent._log)

    def test_register_actions(self):
        """Test basic agent register actions function."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertRaises(ValueError, agent._register_actions, ' ')
        self.assertEqual(agent._register_actions('all'),
                         ['buy', 'sell', 'wait'])
        self.assertEqual(agent._register_actions('nowait'), ['buy', 'sell'])

    def test_register_insider(self):
        """Test basic agent register insider function."""
        agent = sample.BaseAgent('all', [], 'random')
        self.assertRaises(ValueError,
                          agent._register_insider, 0, ' ', 'VALE3')

    def test_request_notifications(self):
        """Test basic agent request notifications function."""
        agent = sample.BaseAgent('all', ['VALE3', 'PETR3', 'ALPA3'], 'random')
        self.assertEqual(len(agent.request_notifications()), 3)
        agent2 = sample.BaseAgent('all', ['VALE3', 'PETR3'], 'random')
        self.assertEqual(len(agent2.request_notifications()), 2)


# class TestRandomAgent(unittest.TestCase):
#
#     def test_agent_init(self):
#         pass


if __name__ == "__main__":
    unittest.main()
