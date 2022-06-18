import unittest
from . import account


class AccountTest(unittest.TestCase):

    def test_that_account_can_be_created(self):
        account1 = account.Account("Tolani", "0000")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_none(self):
        account1 = account.Account("Tolani", "0000")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_can_deposit(self):
        account1 = account.Account("Tolani", "0000")
        account1.deposit(1000)

        self.assertEqual(1000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("Tolani", "0000")
        account1.deposit(500)

        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(500, account1.balance)

    def test_that_account_can_withdraw(self):
        account1 = account.Account("lolo", "0000")
        account1.deposit(4000)

        self.assertEqual(4000, account1.balance)

        account1.withdraw(2000, "0000")

        self.assertEqual(2000, account1.balance)

    def test_that_account_cannot_withdraw_if_pin_incorrect(self):
        account1 = account.Account("lolo", "0000")
        account1.deposit(4000)

        self.assertRaises(AssertionError, account1.withdraw, 2000, "1111")
        self.assertEqual(4000, account1.balance)

    def test_that_account_cannot_withdraw_amount_higher_than_balance(self):
        account1 = account.Account("lola", "0000")
        account1.deposit(4000)

        self.assertRaises(ValueError, account1.withdraw, 5000, "0000")
        self.assertEqual(4000, account1.balance)

    def test_that_account_can_transfer(self):
        account1 = account.Account("lola", "0000")
        account2 = account.Account("wale", "1111")
        account1.deposit(4000)
        account1.transfer(3000, account2, "0000")

        self.assertEqual(1000, account1.balance)

    if __name__ == '__main__':
        unittest.main()
