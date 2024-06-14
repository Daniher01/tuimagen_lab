import random

class RutGenerator:
    def __init__(self):
        self.generated_ruts = set()

    def generate_unique_rut(self):
        while True:
            random_num = random.randint(100000000, 999999999)
            rut = f'SR_{random_num}'
            if rut not in self.generated_ruts:
                self.generated_ruts.add(rut)
                return rut