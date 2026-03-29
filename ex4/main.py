try:
    from ex4.TournamentCard import TournamentCard
    from ex4.TournamentPlatform import TournamentPlatform
except Exception as e:
    print(e)


def main() -> None:
    print("\nRegistering Tournament Cards...\n")
    try:
        fire_dragon = TournamentCard(
                "Fire Dragon", 2,
                "rare", "dragon_001", 1200)
        fire_dragon_info = fire_dragon.get_card_info()
        for key in fire_dragon_info:
            print(f"- {key}: {fire_dragon_info[key]}")
        print()
        ice_wizard = TournamentCard(
                "Ice Wizard", 2,
                "rare", "wizard_001", 1150)
        ice_wizard_info = ice_wizard.get_card_info()
        for key in ice_wizard_info:
            print(f"- {key}: {ice_wizard_info[key]}")
        print("\nCreating tournament match...")
        tournament = TournamentPlatform()
        tournament.register_card(fire_dragon)
        tournament.register_card(ice_wizard)
        match_result = tournament.create_match("dragon_001", "wizard_001")

        print("\nTournament Leaderboard:")
        leaderboard = tournament.get_leaderboard()
        index = 0
        for card in leaderboard:
            print(f"{index + 1}. {card.name}", end=" : ")
            print(f"Rating: {card.rating} ({card.win}-{card.losse})")
        print(f"\nMatch result: {match_result}")
        print("\nPltaform Report:")
        report = tournament.generate_tournament_report()
        print(report)
    except Exception as e:
        print(e)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstrct patterns working together harmoniously!")


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")
    main()
