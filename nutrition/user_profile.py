class UserProfile:
    def __init__(self):
        self.height = None
        self.weight = None
        self.type = None
        self.daily_calories = 0

    def calculate_daily_calories(self):
        # Harris-Benedict simplificado (edad promedio)
        base = 10*self.weight + 6.25*self.height - 125 + 5

        factor = {
            "normal": 1.2,
            "sport": 1.6,
            "fighter": 1.9
        }.get(self.type, 1.2)

        self.daily_calories = base * factor
