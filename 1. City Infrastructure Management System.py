# task 1

class Vehicle:
    def __init__(self, reg_number, type, owner):
        self.reg_number = reg_number
        self.type = type
        self.owner = owner


    def update_owner(self, new_owner):
        self.owner = new_owner

    

vehicles = []

vehicle1 = Vehicle("001", "car", "Tom Sawyer")
vehicles.append(vehicle1)

vehicle2 = Vehicle("002", "truck", "Bob Cane")
vehicles.append(vehicle2)

print(f"vehicle1 owner is: {vehicle1.owner}.")

vehicle1.update_owner("Timmy Sawyer")

print(f"vehicle1 owner has bee updated to: {vehicle1.owner}.")



# Task 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        self.participant_count = 0

    def add_participant(self, new_participant):
        self.participants.append(new_participant)
        self.participant_count += 1

    
    def get_participant_count(self, event_name):
        return event_name.participant_count
    

event1 = Event("party", "11.22.2023")

event1.add_participant("Tom Jones")
event1.add_participant("Tim Curry")

print(f"event1 has {event1.get_participant_count(event1)} participants.")
print(f"Those participants are {event1.participants}.")

#I am using the class method here but it feels that it would be easier to just call event1.participant_count as is shown below.

print(f"event1 has {event1.participant_count} participants.")







