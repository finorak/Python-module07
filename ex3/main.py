try:
    from ex3.AggressiveStrategy import AgressiveStrategy
except Exception as e:
    print(e)
try:
    from ex3.FantasyCardFactory import FantasyCardFactory
except Exception as e:
    print(e)
try:
    from ex3.GameEngine import GameEngine
except Exception as e:
    print(e)


def main() -> None:
    print()
    try:
        factory = FantasyCardFactory()
        factory_name = factory.get_factory_name()
        print("Factory:", factory_name)
        strategy = AgressiveStrategy()
        strategy_name = strategy.get_strategy_name()
        print("Strategy:", strategy_name)
        factory.card_factory.create_creature("dragon")
        factory.card_factory.create_creature("goblin")
        factory.card_factory.create_spell("fireball")
        factory.card_factory.create_artifact("mana_ring")
        available_types = factory.get_availables_types()
        print(f"Available types: {available_types}\n")
        print("Simulating aggressive turn...")
        hand = ["Fire Dragon (5)", "Goblin Warrior (2)", "Lightning Bolt"]
        print("Hand:", hand)
        battlefield: list[str] = []
        print("\nTurn execution:")
        print("Strategy:", strategy_name)
        strategy.execute_turn(hand, battlefield)
        game = GameEngine()
        report = game.get_engine_status()
        print("Game Report:")
        print(report)
        print()
        print("Abstract Factory + Strategy Pattern", end=": ")
        print("Maximum flexibility")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")
    main()
