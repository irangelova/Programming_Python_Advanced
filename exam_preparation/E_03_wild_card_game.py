def draw_cards(*first_card_data, **second_card_data):
    spell_cards = []
    monster_cards = []
    for card, type in first_card_data:
        if type == "monster":
            monster_cards.append(card)
        elif type == "spell":
            spell_cards.append(card)

    for card2, type2 in second_card_data.items():
        if type2 == "monster":
            monster_cards.append(card2)
        elif type2 == "spell":
            spell_cards.append(card2)

    monster_cards_sorted = sorted(monster_cards, reverse=True)
    spell_cards_sorted = sorted(spell_cards)
    result = []
    if monster_cards_sorted:
        result = ["Monster cards:"]
        for card_type in monster_cards_sorted:
            result.append(f"  ***{card_type}")
    if spell_cards_sorted:
        result.append("Spell cards:")
        for card_type2 in spell_cards_sorted:
            result.append(f"  $$${card_type2}")

    return "\n".join(result)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
