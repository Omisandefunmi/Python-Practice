import unittest
from . import voucher


class VoucherTest(unittest.TestCase):

    def test_that_voucher_has_basket_voucher(self):
        basket = voucher.BasketVoucher(3)
        self.assertIsNotNone(basket)

    def test_that_voucher_has_list(self):
        basket = voucher.BasketVoucher(3)
        self.assertEqual([], basket.get_list())

    def test_that_voucher_has_size(self):
        basket = voucher.BasketVoucher(3)

        self.assertEqual(3, basket.capacity)

    def test_that_voucher_can_add(self):
        basket = voucher.BasketVoucher(3)
        basket.add("yam")

        self.assertEqual(1, basket.number_of_items)

    def test_that_items_in_voucher_can_be_queried(self):
        basket = voucher.BasketVoucher(3)
        basket.add("yam")

        self.assertEqual("yam", basket.getItemInIndex(1))

    def test_that_multiple_items_can_be_added(self):
        basket = voucher.BasketVoucher(3)
        basket.add("rice")
        basket.add("beans")
        basket.add("oil")

        expected = ['rice', 'beans', 'oil']
        self.assertEqual(expected, basket.get_list())

    def test_that_items_cannot_exceed_capacity(self):
        basket = voucher.BasketVoucher(3)
        basket.add("rice")
        basket.add("beans")
        basket.add("oil")
        basket.add("granola")
        basket.add("cider")

        expected = ['rice', 'beans', 'oil']
        self.assertEqual(expected, basket.get_list())

    def test_that_pop_removes_first_item(self):
        basket = voucher.BasketVoucher(3)
        basket.add("rice")
        basket.add("beans")
        basket.add("oil")
        self.assertEqual("rice", basket.pop())
        self.assertEqual("beans", basket.get_item_in_index(1))

    def test_that_item_overwrite_last_item_when_capacity_is_full(self):
        basket = voucher.BasketVoucher(3)
        basket.add("rice")
        basket.add("beans")
        basket.add("oil")
        basket.add("granola")
        basket.add("nuts")
        basket.add("parfait")

        expected = ['rice', 'beans', 'parfait']
        self.assertEqual(expected, basket.get_list())
        print(basket)
