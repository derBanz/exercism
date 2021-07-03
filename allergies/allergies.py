class Allergies:

    def __init__(self, score):
        self.score=format(score,"0b")[-8::]
        allergens=["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        self.allergen=[]
        for i in range(len(self.score)):
            if int(self.score[::-1][i]):
                self.allergen.append(allergens[i])

        print(self.allergen)

    def allergic_to(self, item):
        return item in self.allergen

    @property
    def lst(self):
        return self.allergen