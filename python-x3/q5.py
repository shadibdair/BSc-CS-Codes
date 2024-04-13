## Part 5
class TotalBattle(Battle):
    def __init__(self, good_army, bad_army, formation):
        super().__init__(good_army, bad_army)
        if formation:
            self.good_army = sorted(good_army, key=lambda creature: creature.weapon_power)
            self.bad_army = sorted(bad_army, key=lambda creature: creature.weapon_power)

    def fight(self):
        total_rounds = 0
        while any(creature.is_alive() for creature in self.good_army) and any(creature.is_alive() for creature in self.bad_army):
            # Find the first alive creature in each army
            good_fighter = next((creature for creature in self.good_army if creature.is_alive()), None)
            bad_fighter = next((creature for creature in self.bad_army if creature.is_alive()), None)
            
            if good_fighter is None or bad_fighter is None:
                break  # One of the armies has no more living creatures
            
            # Conduct a duel between the selected fighters
            rounds = self.dual_fight(self.good_army.index(good_fighter), self.bad_army.index(bad_fighter))
            total_rounds += rounds
        
        # Determine the outcome
        if any(creature.is_alive() for creature in self.good_army) and not any(creature.is_alive() for creature in self.bad_army):
            outcome = "Good guys won"
        elif not any(creature.is_alive() for creature in self.good_army) and any(creature.is_alive() for creature in self.bad_army):
            outcome = "Evil won"
        else:
            outcome = "Draw"
        
        return (total_rounds, outcome)

# Example usage
g1 = Creature("elf", 50, "M-16", 10)
g2 = GoodCreature("dwarf", 25.5, "knife", 2)
b1 = Creature("Ork", 25.5, "knife", 2)
b2 = BadCreature("Ork", 60.0, "poison", 4, 3)
tb = TotalBattle([g1, g2], [b1, b2], False)
print(tb.fight())  # Expected output: (5, 'Evil won')