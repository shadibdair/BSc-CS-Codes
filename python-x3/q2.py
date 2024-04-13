class GoodCreature(Creature):
    def get_race(self):
        return "good " + super().get_race()

    def hit(self, other):
        if not self.is_alive() or not other.is_alive():
            return
        self.life -= 5.0
        hit_power = self.weapon_power + self.life / 2  # Modified formula for GoodCreature
        other.absorb(hit_power)

# דוגמאות הרצה
g1 = GoodCreature("dwarf", 25.5, "knife", 2)
c2 = Creature("hobbit", 60.0, "Glock", 4)
g1.hit(c2)
print(g1.get_race(), g1.get_life(), g1.is_alive())  # good dwarf 20.5 True
print(c2.get_race(), c2.get_life(), c2.is_alive())  # hobbit 47.75 True
