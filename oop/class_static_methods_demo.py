class Calculator:
    calculation_type = "Arithmetic Operations"
    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        return a*b

    @staticmethod
    def add(a, b):
        return a+b
    