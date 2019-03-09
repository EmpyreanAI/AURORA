"""Base Insider Module.

This module contains the class that is supossed to be the base
of any other insider created.

License:
"""

from simulator.stock import Stock

DEFAULT_DIRS = ('up', 'down')


class BaseInsider():
    """A Basic Insider structure.

    This class is not intended to be instantiated, it is a model
    for more complex insiders classes.

    Attributes:
        _insider_id: The identifier of the Insider.
        _stock_name: The name of the stock that the insider studies.
        _stock_wallet: The wallet containing Stocks objects.
        _directions: The tuple of possible stock directions

    """

    def __init__(self, insider_id, stock_name, dirs=DEFAULT_DIRS):
        """Initialize a Base Insider.

        Args:
            insider_id: The identifier of the Insider.
            stock_name: The name of the stock that the insider studies.
            dirs: The tuple of possible stock directions.
                  Default is 'up' and 'down'
        """
        self._insider_id = insider_id
        self._stock_name = stock_name
        self._stock_wallet = []
        self._directions = dirs

    @property
    def insider_id(self):
        """Get the insider id."""
        return self._insider_id

    @property
    def stock_name(self):
        """Get the insider stock name."""
        return self._stock_name

    @property
    def stock_wallet(self):
        """Get the insider stock wallet vector."""
        return self._stock_wallet

    def add_stock(self, stock):
        """Add a stock to the stock wallet.

        Stock needs to be an Stock object or
        will raise an value error.

        Args:
            stock: A Stock object instance.
        Raises:
            ValueError: Stock must be an instance of Stock class!

        """
        if isinstance(stock, Stock):
            self.stock_wallet.append(stock)
        else:
            raise ValueError("""Stock must be an instance of Stock class!""")

    def remove_stock(self):
        """Remove a stock from the stock wallet vector.

        Returns:
            The stock object being removed.

        """
        return self.stock_wallet.pop(0)

    def wallet_size(self):
        """Return the size of the wallet.

        Return:
            The ammount of stocks in the stock_wallet

        """
        return len(self.stock_wallet)

    def notify(self):
        """Notify the agent of the predicted direction.

        Return:
            The predicted direction of the stock, 'up' or 'down'.

        """
        return self.predict_direction()

    def predict_direction(self):
        """Blueprint for predict_direction function.

        This method must be overriden in the child class.

        Raises:
            NotImplementedError: Insider must implement predict direction.

        """
        raise NotImplementedError("Insider must implement predict direction.")

    @classmethod
    def _log(cls):
        """Blueprint for _log function.

        This method must be overriden in the child class.

        Raises:
            NotImplementedError: Insider must implement log.

        """
        raise NotImplementedError("Insider must implement log.")
