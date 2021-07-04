"""
Set task:
* A class to create a list of allergens based on an "allergy score".
* A function to return whether a specific allergen is on the allergy list of the Object.
* A function to return the full list of allergens of the Object.
Method:
* The score gets formated into a binary representation, where the last eight characters are sliced and saved in reverse order.
* Each character gets checked. A "1" in a specific position indicates an allergy to the allergen of the same index.
Example:
* A = Allergies(47) (-> 101111 -> 111101)
* A.allergic_to("peanuts") -> True
* A.lst -> ["eggs", "peanuts", "shellfish", "strawberries", "chocolate"]
"""

class Allergies:

    def __init__(self, score): 
        score=format(score,"0b")[-8::][::-1] 
        print(score)
        allergens=["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        self.allergen=[]
        for i in range(len(score)):
            if int(score[i]): 
                self.allergen.append(allergens[i])

    def allergic_to(self, item): 
        return item in self.allergen

    @property
    def lst(self): 
        return self.allergen