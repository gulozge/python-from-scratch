def madlib(name, place, adjective, emotion, animal, verb, friend):
    madlibs = f"""One day, {name} went to the {place}.
               It was a {adjective} day, and {name} was feeling {emotion}.
               Suddenly, a {animal} came and {verb} on the ground. 
               {name} was very {emotion}and ran to {place} to tell {friend}.
               They both decided to {verb} together. It was a fun day!"""

    return madlibs


name = input("Enter a name: ")
place = input("Enter a place (e.g., park, school): ")
adjective = input("Enter an adjective (e.g., big, beautiful): ")
emotion = input("Enter an emotion (e.g., happy, sad): ")
animal = input("Enter an animal (e.g., dog, cat): ")
verb = input("Enter a verb (e.g., run, jump): ")
friend = input("Enter a friend's name: ")
print(madlib(name, place, adjective, emotion, animal, verb, friend))
