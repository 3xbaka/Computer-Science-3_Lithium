#classes for plants and zombies
print("Welcome to Plants vs Zombies")
print("the zombie is on lane 20, the peashooter is on lane 1, and the snow pea is on lane 2")
print("The zombie will walk 1 lane per turn, and the zombie will attack the plant if its on the same lane, the plants have unlimited range and will start shooting as it sees the zombie")
print("The snow pea has a special ability to freeze the zombie for 3 turns, and the zombie will not move during that time")
print("The game will end if the zombie reaches lane 1, or if the zombie dies, or if all plants die")
print("the peashooter has 100 health and does 15 damage, the snow pea has 100 health and does 20 damage, the zombie has 200 health and does 10 damage")
class Plant:
    def __init__(self, name, health, damage, special_ability, lane):
        self.name = name
        self.health = health
        self.damage = damage
        self.special_ability = special_ability
        self.lane = lane

    def attack(self, zombie):
        zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount


class Zombie:
    def __init__(self, name, health, damage, walkspeed, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.walkspeed = walkspeed
        self.distance = distance

    def move(self):
        self.distance -= self.walkspeed

    def attack(self, plant):
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount

#variables amnd stuff
Peashooter = Plant("Peashooter", 100, 15, None, 1)
SnowPea = Plant("SnowPea", 100, 20, "Freeze", 2)
Zombie = Zombie("Zombie", 200, 10, 1, 20)
winning_lane = 1
freeze_turns = 0
freeze_cooldown = 0
winner = None

#Game loop
while True:
    print("TURNING")
    ability_used = False

    if Zombie.distance <= winning_lane:
        winner = "Loss"
        print("Zombie reached lane 1")
        break

    if Zombie.health <= 0:
        winner = "Win"
        print("Zombie is dead")
        break
    for plant in (Peashooter, SnowPea):
        if plant.health > 0:
            print(plant.name + " is shooting at the zombie")
            plant.attack(Zombie)
            if (plant.special_ability == "Freeze" and freeze_turns == 0
                    and freeze_cooldown == 0):
                freeze_turns = 3
                freeze_cooldown = 5
                ability_used = True
                print("SnowPea cast Freeze")
    if Zombie.health <= 0:
        winner = "Win"
        print("Zombie is dead")
        break
    if Zombie.distance == Peashooter.lane and Peashooter.health > 0:
        print("Zombie is attacking the Peashooter")
        Zombie.attack(Peashooter)
    elif Zombie.distance == SnowPea.lane and SnowPea.health > 0:
        print("Zombie is attacking the SnowPea")
        Zombie.attack(SnowPea)

    print("Zombie health:", Zombie.health)

    if Peashooter.health <= 0 and SnowPea.health <= 0:
        winner = "Loss"
        print("All plants are dead")
        break

    if freeze_turns > 0:
        freeze_turns -= 1
        print("Zombie is frozen")
    else:
        Zombie.move()
        print("Zombie walks by 1 to", Zombie.distance)

    if freeze_cooldown > 0 and not ability_used:
        freeze_cooldown -= 1
#win or lose boiiiiii
if winner == "Win":
    print("YOU JUST LCUKY")
elif winner == "Loss":
    print("THE JUDGES AWAIT YOUR POOR PERFORMANCE")

 
    