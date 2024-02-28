from datetime import date

class User:
    def __init__(self,id,first_name,second_Name,age,group):
        self.id = id
        self.first_name = first_name
        self.second_name = second_Name
        self.age = age
        self.group= group

    def calculate_age(self,birth_year):
        curr_year = date.today().year
        accual_age = birth_year - curr_year
        if accual_age < 18:
            return f"niepelnoletni: {accual_age}"
        elif accual_age > 18:
            return f"pelnoletni: {accual_age}"

    