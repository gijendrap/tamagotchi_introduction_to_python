import random
from tamagotchi import Tamagotchi
import storage

def stats(pets):
    a = [p for p in pets if p.alive]
    d = [p for p in pets if not p.alive]
    print(f"\n=== Stats ===")
    print(f"Alive: {len(a)}  Dead: {len(d)}")
    if a:
        print(f"Avg Health:     {sum(p.hp for p in a) / len(a):.1f}")
        print(f"Avg Hunger:     {sum(p.hu for p in a) / len(a):.1f}")
        print(f"Avg Boredom:    {sum(p.bo for p in a) / len(a):.1f}")
        print(f"Avg Exhaustion: {sum(p.ex for p in a) / len(a):.1f}")
    print()

def event(pets):
    a = [p for p in pets if p.alive]
    if not a:
        return
    p = random.choice(a)
    r = random.randint(1, 5)
    if r == 1:
        print(f">> {p.n} got sick! -20 HP")
        p.hp = max(0, p.hp - 20)
    elif r == 2:
        print(f">> {p.n} found food! -15 hunger")
        p.hu = max(0, p.hu - 15)
    elif r == 3:
        print(f">> {p.n} got a health bonus! +10 HP")
        p.hp = min(100, p.hp + 10)
    elif r == 4:
        print(f">> {p.n} had a nightmare! +20 boredom")
        p.bo = min(100, p.bo + 20)
    else:
        print(f">> Nothing happened.")

    if p.hp <= 0:
        p.hp = 0
        p.alive = False
        print(f"{p.n} has died! RIP")

def tick(pets):
    for p in pets:
        if p.alive:
            p.hu += 3
            p.bo += 3
            p.ex += 2
            p._check()

def pick(pets):
    print("\nPets:")
    for i, p in enumerate(pets):
        s = "alive" if p.alive else "dead"
        print(f"  {i + 1}. {p.n} ({s})")
    try:
        c = int(input("Pick a pet (number): ")) - 1
        if c < 0 or c >= len(pets):
            print("Invalid choice.")
            return None
        return pets[c]
    except ValueError:
        print("Enter a number.")
        return None

def action(p):
    if not p.alive:
        print(f"{p.n} is dead, can't do anything.")
        return
    print(f"\nWhat do you want to do with {p.n}?")
    print("  1. Feed")
    print("  2. Play")
    print("  3. Sleep")
    print("  4. Heal")
    print("  5. Status")
    try:
        c = int(input("Choice: "))
    except ValueError:
        print("Invalid input.")
        return
    if c == 1:
        p.feed()
        print(f"You fed {p.n}.")
    elif c == 2:
        p.play()
        print(f"You played with {p.n}.")
    elif c == 3:
        p.sleep()
        print(f"{p.n} is sleeping.")
    elif c == 4:
        p.heal()
        print(f"You healed {p.n}.")
    elif c == 5:
        p.status()
    else:
        print("Invalid choice.")

def run():
    print("\n=== TAMAGOTCHI SIMULATOR ===\n")
    pets = [
        Tamagotchi("Pika"),
        Tamagotchi("Mochi"),
        Tamagotchi("Blob")
    ]

    while True:
        alive = any(p.alive for p in pets)
        if not alive:
            print("All your pets are dead. Game over.")
            break

        print("\n--- MENU ---")
        print("1. Select a pet")
        print("2. Show statistics")
        print("3. Save game")
        print("4. Load game")
        print("5. Quit")

        try:
            m = int(input("Choice: "))
        except ValueError:
            print("Enter a number.")
            continue

        if m == 1:
            p = pick(pets)
            if p:
                action(p)
                tick(pets)
                event(pets)
        elif m == 2:
            stats(pets)
        elif m == 3:
            storage.save(pets)
        elif m == 4:
            r = storage.load()
            if r:
                pets = r
        elif m == 5:
            print("Bye!")
            break
        else:
            print("Invalid option.")
