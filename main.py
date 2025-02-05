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
]

# Possible item drops
items = [
    {"name": "Health Potion", "type": "potion", "effect": "restore", "value": 30},
    {"name": "Iron Sword", "type": "weapon", "effect": "attack", "value": 5},
    {"name": "Steel Armor", "type": "armor", "effect": "defense", "value": 3},
]

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
