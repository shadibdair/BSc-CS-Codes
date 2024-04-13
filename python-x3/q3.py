class BadCreature(Creature):
    def __init__(self, race, life, weapon_name, weapon_power, shield_power):
        super().__init__(race, life, weapon_name, weapon_power)
        if not isinstance(shield_power, int) or shield_power < 0:
            raise TypeError("Shield power must be a non-negative integer")
        self.shield_power = shield_power

    def absorb(self, hit_power):
        # Adjust the hit power by the shield power before subtracting from life
        effective_hit_power = max(hit_power - self.shield_power, 0)  # Ensure it does not go negative
        self.life -= effective_hit_power

# Example usage
c1 = Creature("dwarf", 25.5, "knife", 2)
b2 = BadCreature("Ork", 60.0, "poison", 4, 3)
c1.hit(b2)
print(c1.get_race(), c1.get_life(), c1.is_alive())  # dwarf 20.5 True
print(b2.get_race(), b2.get_life(), b2.is_alive())  # Ork 55.875 True
