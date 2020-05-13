# pop and append from right or left O(1)
from collections import deque

class TicketQueue:
    def __init__(self):
        # self.lst = []
        self.deque = deque()

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Yeti")
        Yeti has been added to the queue the queue is: deque(['Yeti'])
        >>> queue.add_person("Bridget")
        Bridget has been added to the queue the queue is: deque(['Yeti', 'Bridget'])
        """
        # self.lst.append(name)  # => O(1)
        self.deque.append(name)
        print(f"{name} has been added to the queue the queue is: {self.deque}")

    def service_person(self):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Yeti")
        Yeti has been added to the queue the queue is: deque(['Yeti'])
        >>> queue.add_person("Bridget")
        Bridget has been added to the queue the queue is: deque(['Yeti', 'Bridget'])
        >>> queue.service_person()
        Yeti has been serviced
        """
        # serviced = self.lst.pop(0)  # => O(1)
        serviced = self.deque.popleft()  # => O(1)
        print(f"{serviced} has been serviced")

    def bypass_queue(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Yeti")
        Yeti has been added to the queue the queue is: deque(['Yeti'])
        >>> queue.add_person("Bridget")
        Bridget has been added to the queue the queue is: deque(['Yeti', 'Bridget'])
        >>> queue.bypass_queue("LJ")
        LJ has bypassed the queue it is now: deque(['LJ', 'Yeti', 'Bridget'])

        """
        # self.lst = name + self.lst # => O(n)
        self.deque.appendleft(name) # => O(n)
        print(f"{name} has bypassed the queue it is now: {self.deque}")