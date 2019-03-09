# pylint: skip-file

import unittest
from .context import sample


class TestBaseInsiders(unittest.TestCase):
    """."""

    def test_init(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertEqual(sample.DEFAULT_DIRS, ('up', 'down'))
        self.assertEqual(insider._insider_id, 0)
        self.assertEqual(insider._stock_name, 'VALE3')
        self.assertEqual(insider._stock_wallet, [])
        self.assertEqual(len(insider._stock_wallet), 0)
        self.assertEqual(insider._directions, ('up', 'down'))

    def test_insider_id(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertEqual(insider.insider_id, 0)
        self.assertNotEqual(insider.insider_id, 1)

    def test_stock(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertEqual(insider.stock_name, 'VALE3')

    def test_stock_wallet(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertEqual(insider.stock_wallet, [])
        self.assertEqual(len(insider.stock_wallet), 0)
        self.assertEqual(insider.stock_wallet, [])
        self.assertEqual(insider.wallet_size(), 0)
        self.assertRaises(ValueError, insider.add_stock, 12.34)
        self.assertRaises(ValueError, insider.add_stock, 'a')
        self.assertRaises(ValueError, insider.add_stock, True)
        insider.add_stock(sample.Stock('VALE3', 12.34, "01-01-1997"))
        self.assertEqual(insider.stock_wallet[0].name, 'VALE3')
        self.assertEqual(insider.wallet_size(), 1)
        insider.remove_stock()
        self.assertEqual(insider.wallet_size(), 0)

    def test_notify(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertRaises(NotImplementedError, insider.notify)

    def test_log(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertRaises(NotImplementedError, insider._log)

    def test_directions(self):
        """."""
        insider = sample.BaseInsider(0, 'VALE3', sample.DEFAULT_DIRS)
        self.assertRaises(NotImplementedError, insider.predict_direction)
