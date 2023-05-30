#1
import logging
class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def add(self, a, b):
        result = a + b
        self.logger.info(f" {a} + {b} = {result}")
        return result
    def minus(self, a, b):
        result = a - b
        self.logger.info(f" {a} - {b} = {result}")
        return result
    def mnog(self, a, b):
        result = a * b
        self.logger.info(f" {a} * {b} = {result}")
        return result
    def dilen(self, a, b):
        result = a / b
        if b == 0:
            try:
                a / b
            except ValueError:
                raise ValueError("error")
        else:
            self.logger.info(f" {a} / {b} = {result}")
        return result
calc = Calculator()
calc.add(1,3)
calc.mnog(1,5)
calc.minus(1,5)
calc.dilen(1,5)