class NumerosIgualesException (Exception):  # Extiende de Exception
    def __init__(self, m):
        self.m = m
