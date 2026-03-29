try:
    from ex1.ArtifactCard import ArtifactCard
    from ex0.CreatureCard import CreatureCard
    from ex1.SpellCard import SpellCard
    from .Deck import Deck
except Exception as e:
    print(e)


def main() -> None:
    try:
        print("\nBuilding deck with different card types...")
        deck = Deck()
        bolt = SpellCard(
                "Lightning Bolt", 3, "rare",
                "Deal 3 damage to target")
        crystal = ArtifactCard(
                "Mana Crystal", 2, "rare",
                "Permanent: +1 mana per turn")
        dragon = CreatureCard(
            "Fire Dragon", 5, "rare", 1, 5,
            "Creature summoned to battlefield")
        deck.add_card(bolt)
        deck.add_card(crystal)
        deck.add_card(dragon)
        deck_state = deck.get_deck_stats()
        print(f"Deck stats: {deck_state}")
        print("\nDrawing and playing cards\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        card_result = card.play({})
        print(f"Play result: {card_result}\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        card_result = card.play({})
        print(f"Play result: {card_result}\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        card_result = card.play({})
        print(f"Play result: {card_result}\n")
        print("Polymorphism in action: Same interface", end=", ")
        print("different card behavior!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("=== Data Deck Builder ===")
    main()
