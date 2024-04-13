from ass5 import *

# Part 1
c1 = Creature("elf", 50, "M-16", 10)
c2 = Creature("hobbit", 6.0, "Glock", 4)
print(c1 > c2)  # Test 1
c3 = c1 + c2
print(c3)  # Test 2
print(c1)  # Test 3
print(c2)  # Test 4
c1.hit(c2)
print(c1.get_race(), c1.get_life(), c1.is_alive())  # Test 5
print(c2.get_race(), c2.get_life(), c2.is_alive())  # Test 6
c2.hit(c1)
print(c1.get_race(), c1.get_life(), c1.is_alive())  # Test 7
print(c2.get_race(), c2.get_life(), c2.is_alive())  # Test 8

# Part 2
g1 = GoodCreature("dwarf", 25.5, "knife", 2)
c2 = Creature("hobbit", 60.0, "Glock", 4)
g1.hit(c2)
print(g1.get_race(), g1.get_life(), g1.is_alive())  # Test 9
print(c2.get_race(), c2.get_life(), c2.is_alive())  # Test 10

# Part 3
c1 = Creature("dwarf", 25.5, "knife", 2)
b2 = BadCreature("Ork", 60.0, "poison", 4, 3)
c1.hit(b2)
print(c1.get_race(), c1.get_life(), c1.is_alive())  # Test 11
print(b2.get_race(), b2.get_life(), b2.is_alive())  # Test 12

# Part 4
g1 = Creature("elf", 50, "M-16", 10)
g2 = GoodCreature("dwarf", 25.5, "knife", 2)
b1 = Creature("Ork", 25.5, "knife", 2)
b2 = BadCreature("Ork", 60.0, "poison", 4, 3)
b = Battle([g1, g2], [b1, b2])
print(b.dual_fight(0,0))  # Test 13

# Part 5
g1 = Creature("elf", 50, "M-16", 10)
g2 = GoodCreature("dwarf", 25.5, "knife", 2)
b1 = Creature("Ork", 25.5, "knife", 2)
b2 = BadCreature("Ork", 60.0, "poison", 4, 3)
tb = TotalBattle([g1, g2], [b1, b2], False)
print(tb.fight())  # Test 14

