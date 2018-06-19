class HeartRateCalculator():

	def __init__(self,age):
		self.age = age

    def max_heart_rate(self):
        return (220 - self.age)

    def min_target_heart_rate(self):
        return (self.max_heart_rate() * 0.5)

    def max_target_heart_rate(self):
        return (self.max_heart_rate() * 0.85)
