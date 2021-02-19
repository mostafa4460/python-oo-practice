"""Python serial number generator."""

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

    def __init__(self, start = 100):
        """ Creates a Serial Number Generator with a given start number (default start = 100) """
        self.start = start
        self.serial_num = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.serial_num + 1}>"

    def generate(self):
        """ Returns the serial number, then increments it by 1 """
        self.serial_num += 1
        return self.serial_num - 1

    def reset(self):
        """ Resets the serial number back to the original start """
        self.serial_num = self.start