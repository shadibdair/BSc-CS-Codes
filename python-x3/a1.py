class Creature:
    def __init__(self, race, life, weapon_name, weapon_power):
        # Validate the types of the inputs.
        if not isinstance(race, str) or not isinstance(life, (int, float)) or not isinstance(weapon_name, str) or not isinstance(weapon_power, int):
            raise TypeError("Invalid type for one of the parameters")
        # Validate the values of life and weapon power
        if life < 0 or weapon_power <= 0:
            raise ValueError("Life must be non-negative and weapon power must be positive")
        
        # Initialize instance variables.
        self.race = race
        self.life = life
        self.weapon_name = weapon_name
        self.weapon_power = weapon_power

    def get_race(self):
        # Return the creature's race
        return self.race

    def get_life(self):
        # Return the creature's current life
        return self.life

    def is_alive(self):
        # Check if the creature is alive (life > 5.0)
        return self.life > 5.0

    def hit(self, other):
        # Perform a hit on another creature
        if not self.is_alive() or not other.is_alive():
            # If either creature is not alive, abort the hit
            return
        self.life -= 5.0  # Deduct life for making a hit
        hit_power = self.weapon_power + self.life / 4  # Calculate hit power
        other.absorb(hit_power)  # The other creature absorbs the hit

    def absorb(self, hit_power):
        # Absorb a hit and reduce life accordingly
        self.life -= hit_power

    def __lt__(self, other):
        # Less than comparison based on weapon power
        return self.weapon_power < other.weapon_power

    def __eq__(self, other):
        # Equality comparison based on weapon power
        return self.weapon_power == other.weapon_power

    def __add__(self, other):
        # Combine two creatures to create a new one
        if not self.is_alive() or not other.is_alive():
            # If either creature is not alive, return None
            return None
        stronger, weaker = (self, other) if self > other else (other, self)
        new_race = stronger.race + "-" + weaker.race  # Combine races
        new_life = self.life + other.life  # Sum of lives
        new_weapon_name = stronger.weapon_name  # Weapon name from the stronger creature
        new_weapon_power = stronger.weapon_power  # Weapon power from the stronger creature
        return Creature(new_race, new_life, new_weapon_name, new_weapon_power)

    def __str__(self):
        # String representation of the creature
        return f"Race: {self.race}, Life: {self.life}, Weapon: {self.weapon_name} (Power: {self.weapon_power})"

# Example usage
c1 = Creature("elf", 50, "M-16", 10)
c2 = Creature("hobbit", 6.0, "Glock", 4)
print(c1 > c2)  # Test 1: Compare creatures based on weapon power
c3 = c1 + c2  # Test 2: Combine creatures to create a new one
print(c3)  # Display the new creature
print(c1)  # Test 3: Display creature c1
print(c2)  # Test 4: Display creature c2
c1.hit(c2)  # Test 5: c1 hits c2
print(c1.get_race(), c1.get_life(), c1.is_alive())  # Display c1's status
print(c2.get_race(), c2.get_life(), c2.is_alive())  # Display c2's status
c2.hit(c1)  # Test 6: c2 hits c1
print(c1.get_race(), c1.get_life(), c1.is_alive())  # Display c1's status again
print(c2.get_race(), c2.get_life(), c2.is_alive())  # Display c2's status again
