class Battle:
    def __init__(self, good_army, bad_army):
        # Validate the armies
        if not all(isinstance(creature, (Creature, GoodCreature)) for creature in good_army):
            raise TypeError("good_army must contain only Creature or GoodCreature instances")
        if not all(isinstance(creature, (Creature, BadCreature)) for creature in bad_army):
            raise TypeError("bad_army must contain only Creature or BadCreature instances")
        
        self.good_army = good_army
        self.bad_army = bad_army

    def dual_fight(self, good_index, bad_index):
        rounds = 0
        good_creature = self.good_army[good_index]
        bad_creature = self.bad_army[bad_index]
        
        # Continue the duel until one of them is not alive
        while good_creature.is_alive() and bad_creature.is_alive():
            # Bad creature hits first
            bad_creature.hit(good_creature)
            # If the good creature is still alive, it hits back
            if good_creature.is_alive():
                good_creature.hit(bad_creature)
            rounds += 1
        
        return rounds

# Example usage
g1 = Creature("elf", 50, "M-16", 10)
g2 = GoodCreature("dwarf", 25.5, "knife", 2)
b1 = Creature("Ork", 25.5, "knife", 2)
b2 = BadCreature("Ork", 60.0, "poison", 4, 3)
b = Battle([g1, g2], [b1, b2])
print(b.dual_fight(0,0))  # Expected output: 1
