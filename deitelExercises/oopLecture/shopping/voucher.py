class BasketVoucher:
    def __init__(self, capacity):
        self.basket_list = []
        self.number_of_items = 0
        self.capacity = capacity

    def size(self):
        return self.capacity

    def add(self, item):
        if self.number_of_items != self.capacity:
            self.basket_list.append(item)
            self.number_of_items += 1
        if self.number_of_items == self.capacity:
            self.basket_list[self.capacity - 1] = item

    def get_item_in_index(self, index):
        return self.basket_list[index - 1]

    def get_list(self):
        return self.basket_list

    def pop(self):
        removed = self.basket_list[0]
        BasketVoucher.refill_after_pop(self)
        return removed

    def refill_after_pop(self):
        counter = 0
        while counter < (self.capacity - 1):
            self.basket_list[counter] = self.basket_list[counter + 1]
            counter += 1

    def __str__(self):
        to_be_returned = ""
        to_be_returned += "Capacity: " + str(self.capacity) + "\n"
        to_be_returned += "No of Items: " + str(self.number_of_items) + "\n"
        to_be_returned += "ITEMS: "
        for item in self.basket_list:
            to_be_returned += item + ", "
        return  to_be_returned

    def __eq__(self, obj):
        compared = BasketVoucher(obj)
        if compared.basket_list == self.basket_list:
            if compared.capacity == self.capacity:
                if compared.number_of_items == self.number_of_items:
                    return True
                return False
            return False
        return False
