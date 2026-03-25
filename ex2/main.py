from ex2.EliteCard import EliteCard


def main() -> None:
    print()
    elit_card = EliteCard("Arcane Warrior", 3, "elit", "melle")
    print("EliteCard capabilites:")
    print(f"- Card: {elit_card.card}")
    print(f"- Combatable: {elit_card.combatable}")
    print(f"- Magical: {elit_card.magical}")
    print()
    print("Playing Arcane Warrior (EliteCard):\n")
    print("Combat phase:")
    attack_result = elit_card.attack("Enemy")
    print(f"Attack result: {attack_result}")
    defense_result = elit_card.defend(10)
    print(f"Deffense result: {defense_result}")
    print()
    print("Magic phase:")
    spell_cast = elit_card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_cast}")
    channel_cast = elit_card.channel_mana(3)
    print(f"Mana channel: {channel_cast}")
    print("\nMultiple interface implemenatio successful!")


if __name__ == "__main__":
    print("=== DataDeck Ability System ===")
    main()
