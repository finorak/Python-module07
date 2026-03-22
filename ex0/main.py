from ex0 import CreatureCard


if __name__ == "__main__":
    fire_dragon_name = "Fire Dragon"
    fire_dragon = CreatureCard(fire_dragon_name, 5, "Legendary", 7, 5)
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    fire_dragon_info = fire_dragon.get_card_info()
    print(fire_dragon_info)
    print("Abstract pattern successfully demonstrated!")
