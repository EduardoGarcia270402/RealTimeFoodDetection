class UserProfile:
    def __init__(self):
        self.height = None
        self.weight = None
        self.target_weight = None
        self.type = None

        self.daily_calories = 0
        self.goal = None  # cut | maintain | gain

    def calculate_daily_calories(self):

        if None in (self.height, self.weight, self.target_weight, self.type):
            self.daily_calories = 0
            self.goal = None
            return

        base = 10 * self.weight + 6.25 * self.height - 125 + 5

        factor = {
            "normal": 1.2,
            "sport": 1.6,
            "fighter": 1.9
        }.get(self.type, 1.2)

        maintenance = base * factor

        if self.target_weight < self.weight:
            self.goal = "cut"
            self.daily_calories = maintenance * 0.8
        elif self.target_weight > self.weight:
            self.goal = "gain"
            self.daily_calories = maintenance * 1.15
        else:
            self.goal = "maintain"
            self.daily_calories = maintenance

        self.daily_calories = int(self.daily_calories)
