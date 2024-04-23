class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Create serial number generator with a start value"""
        self.start = start  # you can chain your equalities in python!
        self.current_num = self.start

    def generate(self):
        """Returns next number in generator to user"""
        self.current_num += 1
        return self.current_num - 1

    def reset(self):
        """Resets self.current_num back to original start value"""
        self.current_num = self.start
