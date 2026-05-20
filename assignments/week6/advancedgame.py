# --- Constants ---
MAX_INVENTORY_SIZE = 5
STARTING_ROOM = "beach"
WIN_ITEM = "flare"
WIN_ROOM = "beach"

# --- Game State ---
inventory = []
current_room = STARTING_ROOM
player_health = 3

# --- World Data ---
rooms = {
    "beach": {
        "description": "You are on a sandy beach. The sun is hot and the sea stretches endlessly. A rescue plane might pass overhead...",
        "items": [
            {"name": "coconut", "type": "food",    "description": "A fresh coconut. Could restore some energy."},
            {"name": "rope",    "type": "tool",    "description": "A sturdy rope. Useful for many things."},
        ]
    },
    "jungle": {
        "description": "You push through dense jungle. Strange sounds surround you.",
        "items": [
            {"name": "medkit",  "type": "healing", "description": "A first aid kit. Restores full health."},
            {"name": "map",     "type": "tool",    "description": "A hand-drawn map of the island."},
            {"name": "berries", "type": "food",    "description": "Wild berries. Hopefully not poisonous..."},
        ]
    },
    "cave": {
        "description": "A dark, damp cave. Something glints in the corner.",
        "items": [
            {"name": "torch",   "type": "tool",    "description": "Lights up dark places."},
            {"name": "flare",   "type": "tool",    "description": "An emergency signal flare. This could save you!"},
            {"name": "knife",   "type": "tool",    "description": "A rusty knife. Better than nothing."},
        ]
    }
}

# --- Functions ---

def show_inventory():
    """Display all items currently in the player's inventory."""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print(f"Inventory ({len(inventory)}/{MAX_INVENTORY_SIZE}):")
        for item in inventory:
            print(f"  - {item['name'].capitalize()} ({item['type']})")


def show_room_items():
    """Display the current room's description and all items in it."""
    room = rooms[current_room]
    print(f"\n{room['description']}")

    if not room["items"]:
        print("There are no items here.")
    else:
        print("You can see:")
        for item in room["items"]:
            print(f"  - {item['name'].capitalize()} ({item['type']})")


def pick_up(item_name):
    """Pick up a named item from the room and add it to inventory."""
    room_items = rooms[current_room]["items"]

    for item in room_items:
        if item["name"] == item_name:

            if len(inventory) >= MAX_INVENTORY_SIZE:
                print(f"Your inventory is full! Drop something first. ({MAX_INVENTORY_SIZE}/{MAX_INVENTORY_SIZE})")
                return

            inventory.append(item)
            room_items.remove(item)
            print(f"You picked up the {item['name'].capitalize()}.")
            return

    print(f"There is no '{item_name}' here.")


def drop(item_name):
    """Drop a named item from inventory back into the current room."""
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            print(f"You dropped the {item['name'].capitalize()}.")
            return

    print(f"You don't have '{item_name}' in your inventory.")


def examine(item_name):
    """Examine an item — it must be in your inventory or in the current room."""
    # Check inventory first
    for item in inventory:
        if item["name"] == item_name:
            print(f"{item['name'].capitalize()}: {item['description']}")
            return

    # Then check the room
    for item in rooms[current_room]["items"]:
        if item["name"] == item_name:
            print(f"{item['name'].capitalize()}: {item['description']}")
            return

    print(f"You can't see any '{item_name}' here.")


def use(item_name):
    """Use an item from inventory. Effect depends on item type."""
    global player_health, current_room

    for item in inventory:
        if item["name"] == item_name:

            # --- Win condition ---
            if item["name"] == WIN_ITEM and current_room == WIN_ROOM:
                print("You fire the flare into the sky. A distant plane turns toward the island...")
                print("🚁 A rescue helicopter arrives! YOU ARE SAVED! 🎉")
                print("\nYou win! Thanks for playing.")
                quit()

            # --- Food items restore health ---
            elif item["type"] == "food":
                if item["name"] == "berries":
                    player_health -= 1
                    print(f"You eat the berries. They taste bitter... something feels wrong. ❤️ Health: {player_health}/3")
                    inventory.remove(item)
                    if player_health <= 0:
                        print("You collapse. Game over. 💀")
                        quit()
                else:
                    if player_health < 3:
                        player_health = min(player_health + 1, 3)
                        print(f"You eat the {item['name'].capitalize()}. You feel a bit better. ❤️ Health: {player_health}/3")
                        inventory.remove(item)
                    else:
                        print("You are already at full health!")

            # --- Healing items ---
            elif item["type"] == "healing":
                player_health = 3
                print(f"You use the {item['name'].capitalize()}. Health fully restored! ❤️ Health: {player_health}/3")
                inventory.remove(item)

            # --- Room navigation items ---
            elif item["name"] == "map":
                print("The map shows three areas: Beach, Jungle, and Cave.")
                print("Use 'go beach', 'go jungle', or 'go cave' to move between them.")

            elif item["name"] == "torch":
                print("You hold up the torch. The cave walls glitter around you.")

            elif item["name"] == "rope":
                print("You swing the rope around. Not sure what to tie it to yet.")

            elif item["name"] == "knife":
                print("You slash at some nearby vines. Feels good, but not immediately useful.")

            # --- Flare in wrong room ---
            elif item["name"] == "flare":
                print("You need to be on the beach to signal a rescue plane!")

            else:
                print(f"You use the {item['name'].capitalize()}, but nothing happens.")

            return

    print(f"You don't have '{item_name}' in your inventory.")


def go(room_name):
    """Move the player to a different room."""
    global current_room

    if room_name in rooms:
        current_room = room_name
        print(f"\nYou head to the {room_name.capitalize()}.")
        show_room_items()
    else:
        print(f"You can't go to '{room_name}'. Try: beach, jungle, or cave.")


# --- Game Loop ---

def game_loop():
    """Main game loop: read commands and call the right function."""
    print("===========================================")
    print("   🏝️  STRANDED — A Survival Text Game  🏝️")
    print("===========================================")
    print("You wake up on a beach after a shipwreck.")
    print("Find a way to signal for rescue before it's too late.")
    print(f"❤️  Health: {player_health}/3")
    print("\nType 'help' for a list of commands.")
    show_room_items()

    while True:
        command = input("\n> ").strip().lower()

        match command.split():
            case ["help"]:
                print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [room], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                use(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["go", room_name]:
                go(room_name)
            case ["quit"]:
                print("You give up and wait for the tide. Goodbye! 🌊")
                break
            case _:
                print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    game_loop()
