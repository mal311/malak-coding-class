class robot:
    #class static attribute
    species = "robot"

    #instance attribute
    def __init__ (self, nm, h):
        self.name = nm
        self.origin = h


bot = robot("bot", "china")

print("bot is a ",bot.species)
print()


print(f"{bot.name} is from {bot.origin}")
