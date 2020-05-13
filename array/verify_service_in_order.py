import unittest


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Check if we're serving orders first-come, first-served
    '''
    create a pointer for each array
    iterate across served orders
    compare current served order with pointers at the start of each of the other lists
    if the value matches one of the pointers move that pointer for that list forward
    if neither list has a pointer at the served order's current val pointer return false
    '''
    takeout_pointer = 0
    dinein_pointer = 0
    take_n = len(take_out_orders)
    dine_n = len(dine_in_orders)

    if take_n + dine_n != len(served_orders):
        return False

    for order in served_orders:
        if take_n > 0 and order == take_out_orders[takeout_pointer]:
            takeout_pointer += 1
            take_n -= 1
        elif dine_n > 0 and order == dine_in_orders[dinein_pointer]:
            dinein_pointer += 1
            dine_n -= 1
        else:
            return False

    return True


# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)


unittest.main(verbosity=2)