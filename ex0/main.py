try:
    from .CreatureCard import CreatureCard
except Exception as e:
    print(e)


def main() -> None:
    try:
        fire_dragon_name = "Fire Dragon"
        fire_dragon = CreatureCard(
                fire_dragon_name, 5, "Legendary",
                1, 5, "Creature summoned to battlefield")
        print("=== DataDeck Card Foundation ===")
        print("\nTesting Abstract Base Class Design:\n")
        print("CreatureCard Info:")
        fire_dragon_info = fire_dragon.get_card_info()
        print(fire_dragon_info)
        print()
        print(f"Playing {fire_dragon.name} with {fire_dragon.mana} available")
        play_result = fire_dragon.play({})
        print(f"Play result: {play_result}\n")
        fire_dragon.attack_target("Goblin Warrior")
        print()
        fire_dragon.mana = 3
        print(f"Testing insufficient mana ({fire_dragon.mana} available)")
        print(f"Playable: {fire_dragon.is_playable(fire_dragon.mana)}")
        print()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
    print("Abstract pattern successfully demonstrated!")
