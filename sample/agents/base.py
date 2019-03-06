"""Base Agent Module.

This module contains the class that is supossed to be the base
of any other agent created.

License:
"""

from insiders.random import RandomInsider


class BaseAgent():
    """A Basic Agent structure.

    This class is not intended to be instantiated, it is a model
    for more complex agents classes.

    Attributes:
        _cash: The ammount of money the agent have.
        _profit: The ammount of profit the agent have.
        actions: The agent's action vector.
        insiders: Objects that studies a unique stock, and inform the
        agent whether it should buy or not the stock

    """

    def __init__(self, actions, stocks, insider_type):
        """Initialize a Base Agent.

        Args:
            actions: The agent's action description. Can be 'all'.
                    or 'nowait'
            stocks: The stocks that the agents will be trading.
            insider_type: The type of the insiders. Can be 'random'.

        """
        self._cash = 0
        self._profit = 0
        self.actions = self._register_actions(actions)
        self.insiders = []
        insider_id = 0
        for stock in stocks:
            self.insiders.append(self._register_insider(insider_id,
                                                        insider_type, stock))
            insider_id += 1

    @property
    def cash(self):
        """Get or set the agent's cash."""
        return self._cash

    @cash.setter
    def cash(self, amt):
        self._cash = amt

    def cash_add(self, amt):
        """Add cash to the agent.

        Args:
            amt: The ammount to add.
        Raises:
            ValueError: Ammount must be positive!
                        If you want to subtract use cash_sub.

        """
        if amt < 0:
            raise ValueError("""Ammount must be positive!
                             If you want to subtract use cash_sub.""")
        self._cash += amt

    def cash_sub(self, amt):
        """Remove agent's cash.

        Args:
            amt: The ammount to remove.
        Raises:
            ValueError: Ammount must be positive!
                        If you want to add use cash_add.

        """
        if amt < 0:
            raise ValueError("""Ammount must be positive!
                             If you want to add use cash_add.""")
        self._cash -= amt

    def cash_zero(self):
        """Set agent's cash to zero."""
        self._cash = 0

    @property
    def profit(self):
        """Get or set the agent's profit."""
        return self._profit

    @profit.setter
    def profit(self, amt):
        self._profit = amt

    def profit_add(self, amt):
        """Add profit to the agent.

        Args:
            amt: The ammount to add.

        """
        self._profit += amt

    def profit_zero(self):
        """Set agent's profit to zero."""
        self._profit = 0

    def request_notifications(self):
        """Request notifications from insiders.

        Request for each insider the estimated direction of the stocks.

        Returns:
            A vector containing tuples of insider and stock direction.

        """
        notifications = []
        for insider in self.insiders:
            notifications.append((insider, insider.notify()))
        return notifications

    @classmethod
    def act(cls):
        """Blueprint for act function.

        This method must be overriden in the child class.

        Raises:
            NotImplementedError: Agent must implement act.

        """
        raise NotImplementedError("Agent must implement act.")

    @classmethod
    def _log(cls):
        """Blueprint for _log function.

        This method must be overriden in the child class.

        Raises:
            NotImplementedError: Agent must implement log.

        """
        raise NotImplementedError("Agent must implement log.")

    @classmethod
    def _register_actions(cls, actions):
        """Register the proper action vector.

        Register the proper action vector given a string description of
        the actions possibilities.

        Args:
            actions: The agent's actions keyword.
        Returns:
            The agent's actions vector. Can be 'all' or 'nowait'
        Raises:
            ValueError: Action must be 'all' or 'nowait'.

        """
        if actions == 'all':
            action_vec = ['buy', 'sell', 'wait']
        elif actions == 'nowait':
            action_vec = ['buy', 'sell']
        else:
            raise ValueError("Action must be 'all' or 'nowait'.")
        return action_vec

    @classmethod
    def _register_insider(cls, insider_id, insider_type, stock):
        """Register a new insider.

        Instantiate a new insider agent, given the arguments.

        Args:
            insider_id: The insider identifier.
            insider_type: The insider type.  Can be 'random'.
            stock: The stock that the insider will study.
        Returns:
            The insider object.
        Raises:
            ValueError: Insider must be 'random'.

        """
        if insider_type == 'random':
            insider = RandomInsider(insider_id, stock)
        else:
            raise ValueError("Insider must be 'random'.")
        return insider
