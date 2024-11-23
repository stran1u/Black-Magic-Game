import random
import time

class BlackMagicBook:
    def __init__(self):
        self.spells = {
            "Necromancy": ["Raise the dead", "Summon a shade", "Unleash the curse of decay"],
            "Curses": ["Hex of misfortune", "Curse of endless night", "Rotting curse"],
            "Dark Enchantment": ["Bind the soul", "Charm the heart", "Control the mind"],
            "Forbidden Arts": ["Summon the demon", "Blood ritual", "Open the portal of darkness"]
        }

    def cast_spell(self, spell_type):
        if spell_type not in self.spells:
            print("You cannot wield such power!")
            return
        spell = random.choice(self.spells[spell_type])
        print(f"Chanting the ancient words... '{spell}'...")

        time.sleep(2)
        print(f"The spell '{spell}' has been cast successfully!")
        time.sleep(1)
        self._reaction(spell)

    def _reaction(self, spell):
        reactions = [
            "A chilling breeze sweeps through the room.",
            "You hear whispers from the abyss.",
            "The air grows thick with the scent of decay.",
            "A shadow moves in the corner of your eye."
        ]
        print(random.choice(reactions))
        print("You feel the weight of the dark forces around you.")

def main():
    print("Welcome to the Dark Magic Book!")
    time.sleep(1)
    print("Choose your path in the dark arts...")

    book = BlackMagicBook()
    while True:
        print("\nAvailable spells:")
        print("1. Necromancy")
        print("2. Curses")
        print("3. Dark Enchantment")
        print("4. Forbidden Arts")
        print("5. Exit the dark realm")

        choice = input("\nChoose an option: ")

        if choice == '1':
            book.cast_spell("Necromancy")
        elif choice == '2':
            book.cast_spell("Curses")
        elif choice == '3':
            book.cast_spell("Dark Enchantment")
        elif choice == '4':
            book.cast_spell("Forbidden Arts")
        elif choice == '5':
            print("You have turned away from the path of darkness. Farewell.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
