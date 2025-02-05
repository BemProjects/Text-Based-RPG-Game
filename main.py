import random

# Define player stats
player = {
    "name": "Hero",
    "level": 1,
    "xp": 0,
    "xp_to_level": 10,
    "health": 100,
    "max_health": 100,
    "attack": 10,
    "defense": 5,
    "inventory": [],
    "equipped": {"weapon": None, "armor": None}
}

# Base monster stats
base_monsters = [
    {"name": "Goblin", "level": 1, "health": 30, "attack": 5, "defense": 2, "xp": 5},
    {"name": "Orc", "level": 2, "health": 50, "attack": 8, "defense": 3, "xp": 8},
    {"name": "Troll", "level": 3, "health": 80, "attack": 12, "defense": 5, "xp": 12},
    {"name": "Bandit", "level": 4, "health": 90, "attack": 14, "defense": 6, "xp": 14},
    {"name": "Skeleton Warrior", "level": 5, "health": 100, "attack": 16, "defense": 7, "xp": 16},
    {"name": "Dark Mage", "level": 6, "health": 110, "attack": 18, "defense": 8, "xp": 18},
    {"name": "Werewolf", "level": 7, "health": 120, "attack": 20, "defense": 9, "xp": 20},
    {"name": "Shadow Knight", "level": 8, "health": 130, "attack": 22, "defense": 10, "xp": 22},
    {"name": "Fire Drake", "level": 9, "health": 150, "attack": 24, "defense": 12, "xp": 24},
    {"name": "Ice Golem", "level": 10, "health": 160, "attack": 26, "defense": 13, "xp": 26},
    {"name": "Necromancer", "level": 11, "health": 170, "attack": 28, "defense": 14, "xp": 28},
    {"name": "Vampire Lord", "level": 12, "health": 180, "attack": 30, "defense": 15, "xp": 30},
    {"name": "Demon Hound", "level": 13, "health": 200, "attack": 32, "defense": 16, "xp": 32},
    {"name": "Wraith", "level": 14, "health": 210, "attack": 34, "defense": 17, "xp": 34},
    {"name": "Fallen Angel", "level": 15, "health": 220, "attack": 36, "defense": 18, "xp": 36},
    {"name": "Infernal Behemoth", "level": 16, "health": 250, "attack": 38, "defense": 20, "xp": 38},
    {"name": "Titan", "level": 17, "health": 280, "attack": 40, "defense": 22, "xp": 40},
    {"name": "Celestial Dragon", "level": 18, "health": 300, "attack": 42, "defense": 24, "xp": 42},
    {"name": "Abyssal Horror", "level": 19, "health": 350, "attack": 45, "defense": 26, "xp": 45},
    {"name": "Dark Overlord", "level": 20, "health": 400, "attack": 50, "defense": 30, "xp": 50}
]

# Possible item drops
items = [
    {"name": "Health Potion", "type": "potion", "effect": "restore", "value": 30},
    {"name": "Iron Sword", "type": "weapon", "effect": "attack", "value": 5},
    {"name": "Steel Armor", "type": "armor", "effect": "defense", "value": 3},
]

rare_items = [
    {"name": "Sword of the Abyss", "type": "weapon", "effect": "attack", "value": 10, "level": 15},
    {"name": "Shield of Eternity", "type": "armor", "effect": "defense", "value": 8, "level": 16},
    {"name": "Dagger of Shadows", "type": "weapon", "effect": "attack", "value": 12, "level": 17},
    {"name": "Armor of the Fallen", "type": "armor", "effect": "defense", "value": 10, "level": 18},
    {"name": "Ring of the Void", "type": "weapon", "effect": "attack", "value": 15, "level": 19},
    {"name": "Amulet of the Ancients", "type": "armor", "effect": "defense", "value": 12, "level": 20},
    {"name": "Bow of the Celestial Hunt", "type": "weapon", "effect": "attack", "value": 14, "level": 18},
    {"name": "Helm of the Infernal King", "type": "armor", "effect": "defense", "value": 14, "level": 19},
    {"name": "Gauntlets of Titan Strength", "type": "weapon", "effect": "attack", "value": 10, "level": 17},
    {"name": "Boots of the Phantom", "type": "armor", "effect": "defense", "value": 6, "level": 15},
    {"name": "Staff of the Dark Mage", "type": "weapon", "effect": "attack", "value": 16, "level": 18},
    {"name": "Cursed Blade of the Wraith", "type": "weapon", "effect": "attack", "value": 18, "level": 20},
    {"name": "Cloak of the Shadow Knight", "type": "armor", "effect": "defense", "value": 9, "level": 16},
    {"name": "Bracers of the Vampire Lord", "type": "armor", "effect": "defense", "value": 11, "level": 19},
    {"name": "Pendant of the Demon Hound", "type": "weapon", "effect": "attack", "value": 13, "level": 18},
    {"name": "Crown of the Abyssal Horror", "type": "armor", "effect": "defense", "value": 15, "level": 20},
    {"name": "Hammer of the Titan", "type": "weapon", "effect": "attack", "value": 11, "level": 17},
    {"name": "Orb of Celestial Power", "type": "weapon", "effect": "attack", "value": 14, "level": 19},
    {"name": "Wings of the Fallen Angel", "type": "armor", "effect": "defense", "value": 16, "level": 20},
    {"name": "Sword of the Dark Overlord", "type": "weapon", "effect": "attack", "value": 20, "level": 20}
]

def drop_rare_item(monster):
    if monster["level"] >= 15 and random.random() < 0.2:  # 20% chance for rare item drop from level 15+ monsters
        return random.choice([item for item in rare_items if item["level"] <= monster["level"]])
    return None

def scale_monsters():
    """Increase monster stats based on player's level."""
    return [
        {
            "name": monster["name"],
            "level": monster["level"] + player["level"] // 2,
            "health": monster["health"] + player["level"] * 10,
            "attack": monster["attack"] + player["level"],
            "defense": monster["defense"] + player["level"] // 2,
            "xp": monster["xp"] + player["level"] * 2
        }
        for monster in base_monsters
    ]

def level_up():
    """Levels up the player without restoring health."""
    if player["xp"] >= player["xp_to_level"]:
        player["level"] += 1
        player["xp"] -= player["xp_to_level"]
        player["xp_to_level"] += 10
        player["attack"] += 2
        player["defense"] += 1
        print(f"\n🎉 You leveled up to Level {player['level']}! 🎉")
        print(f"Stats increased! Attack: {player['attack']}, Defense: {player['defense']}\n")

def find_item():
    """Randomly finds an item after defeating a monster (30% chance)."""
    if random.random() < 0.3:
        item = random.choice(items)
        player["inventory"].append(item)
        print(f"🛡️ You found a {item['name']}! ({item['type'].capitalize()} - {item['effect'].capitalize()} +{item['value']})")

def attack_monster(monster):
    """Handles combat between player and monster."""
    print(f"\n⚔️ You engage a {monster['name']} (Lv {monster['level']})! ⚔️")
    monster_health = monster["health"]

    while monster_health > 0 and player["health"] > 0:
        damage_to_monster = max(0, player["attack"] - monster["defense"])
        monster_health -= damage_to_monster
        print(f"You hit the {monster['name']} for {damage_to_monster} damage! ({monster_health} HP left)")

        if monster_health > 0:
            damage_to_player = max(0, monster["attack"] - player["defense"])
            player["health"] -= damage_to_player
            print(f"The {monster['name']} hits you for {damage_to_player} damage! ({player['health']} HP left)")

    if player["health"] > 0:
        print(f"🏆 You defeated the {monster['name']}! 🏆")
        player["xp"] += monster["xp"]
        print(f"🎖️ Gained {monster['xp']} XP! (Total XP: {player['xp']}/{player['xp_to_level']})")
        level_up()
        find_item()
    else:
        print("💀 You were defeated! Game over.")

def use_item():
    """Allows the player to use an item from the inventory."""
    if not player["inventory"]:
        print("🛑 You have no items!")
        return

    print("\n👜 Inventory:")
    for i, item in enumerate(player["inventory"], 1):
        print(f"{i}. {item['name']} ({item['effect'].capitalize()} +{item['value']})")

    choice = input("Choose an item to use (or press Enter to cancel): ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(player["inventory"]):
            item = player["inventory"].pop(index)
            if item["type"] == "potion":
                player["health"] = min(player["max_health"], player["health"] + item["value"])
                print(f"✅ Used {item['name']}! Health restored to {player['health']}.")
            elif item["type"] in ["weapon", "armor"]:
                equip_item(item)
        else:
            print("Invalid choice.")
    else:
        print("Cancelled.")

def equip_item(item):
    """Equips a weapon or armor for stat boosts."""
    if item["type"] == "weapon":
        player["attack"] += item["value"]
        if player["equipped"]["weapon"]:
            print(f"🔄 Replaced {player['equipped']['weapon']['name']} with {item['name']}!")
        player["equipped"]["weapon"] = item
    elif item["type"] == "armor":
        player["defense"] += item["value"]
        if player["equipped"]["armor"]:
            print(f"🔄 Replaced {player['equipped']['armor']['name']} with {item['name']}!")
        player["equipped"]["armor"] = item

    print(f"✅ Equipped {item['name']}! {item['effect'].capitalize()} increased by {item['value']}.")

def choose_monster():
    """Allows player to select which monster to fight."""
    monsters = scale_monsters()
    print("\n🦇 Available Monsters:")
    for i, monster in enumerate(monsters, 1):
        print(f"{i}. {monster['name']} (Lv {monster['level']}) - HP: {monster['health']}, ATK: {monster['attack']}, DEF: {monster['defense']}")

    choice = input("Choose a monster to fight (or press Enter to cancel): ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(monsters):
            attack_monster(monsters[index])
        else:
            print("Invalid choice.")
    else:
        print("Cancelled.")

def game_loop():
    """Main game loop allowing player to fight monsters, check stats, or exit."""
    while player["health"] > 0:
        print("\n===== ⚔️ Adventure Menu ⚔️ =====")
        print("1. Fight a Monster")
        print("2. Check Stats")
        print("3. Use an Item")
        print("4. Exit Game")

        choice = input("Choose an action: ")

        if choice == "1":
            choose_monster()
        elif choice == "2":
            print(f"\n📊 Stats: Lv {player['level']} XP: {player['xp']}/{player['xp_to_level']} HP: {player['health']}/{player['max_health']} ATK: {player['attack']} DEF: {player['defense']}")
            print(f"Equipped: {player['equipped']}")
            print(f"Inventory: {[item['name'] for item in player['inventory']]}")
        elif choice == "3":
            use_item()
        elif choice == "4":
            print("👋 Thanks for playing!")
            break
        else:
            print("Invalid choice.")

# Start the game
print("\n🛡️ Welcome to the Monster Battler Game! 🛡️")
game_loop()
