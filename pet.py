from animal import Animal


class Pet():
    def __init__(self, name, critter_instance):
        self.name = name
        self.animal_type = critter_instance

    def set_owner(self, name, phone):
        self.owner_name = name
        self.owner_number = phone

    def __str__(self):
        return f'This pets name is {self.name}. It has {self.animal_type.leg_num} legs and likes to say {self.animal_type.say_something()}!'