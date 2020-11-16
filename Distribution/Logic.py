import random


class Even:
    def __init__(self, a, b, accuracy, number_count):
        self.a = a
        self.b = b
        self.exp_value_theor = self.culc_exp_value_theor()
        self.exp_value = 0
        self.dispersion = 0
        self.number_count = number_count
        self.aim = 0
        self.accuracy = accuracy
        self.sequence = []
        self.error_message = ''

    def distribute(self):
        result = []
        try:
            exp_value = 0
            dispersion = 0
            while True:
                random_array = [random.random() for i in range(self.number_count)]
                even_array = self.get_even_array(random_array)
                exp_value = self.culc_exp_value(even_array)
                dispersion = self.culc_dispersion(even_array, exp_value)
                aim = abs(exp_value - (self.a + self.b) / 2)
                if not self.culc_accuracy(exp_value, self.exp_value_theor, dispersion, ((self.b - self.a) ** 2) / 12):
                    result = even_array
                    self.exp_value = exp_value
                    self.dispersion = dispersion
                    self.aim = aim
                    break
        except Exception:
            self.error_message = "Error"
            return False
        self.sequence = result
        return True

    def culc_accuracy(self, m, m1, d, d1):
        return (not self.epsilon(m, m1)) or (not self.epsilon(d, d1))

    def get_even_array(self, random_array):
        return [(self.b - self.a) * i + self.a for i in random_array]

    def culc_exp_value(self, array):
        return sum(array) / len(array)

    def get_exp_value(self):
        return self.culc_exp_value(self.sequence)

    def culc_exp_value_theor(self):
        return (self.a + self.b) / 2

    def culc_dispersion(self, array, exp_value):
        return sum([(i - exp_value) ** 2 for i in array]) / len(array)

    def epsilon(self, m, mr):
        return abs(m - mr) <= self.accuracy
