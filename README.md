# Tamagotchi Pugalenthi

A small Python pet simulator where you care for a few virtual companions, keep them alive, and try not to let them get too hungry, bored, or exhausted.

This project is simple, playful, and easy to run locally. It is built around the classic Tamagotchi idea: you choose a pet, manage its needs, and deal with random in-game events.

## What the game does

You start with three pets:

- Pika
- Mochi
- Blob

From the menu, you can:

- choose a pet
- feed it
- play with it
- put it to sleep
- heal it
- check its status
- save the game
- load the game
- view overall stats

Each pet has a few stats:

- Health
- Hunger
- Boredom
- Exhaustion

If any of them get too high or too low, your pet can get hurt. If health reaches zero, the pet dies and is gone for good.

## How to play

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

3. Use the menu to choose actions.

### Main menu options

- 1. Select a pet
- 2. Show statistics
- 3. Save game
- 4. Load game
- 5. Quit

When you choose a pet, you can do actions like feeding, playing, sleeping, healing, or checking the pet's status.

## Game mechanics

The pet gets affected by its actions and by random events:

- Feeding decreases hunger but can increase excitement.
- Playing reduces boredom and increases happiness-like energy.
- Sleeping lowers exhaustion and raises boredom a little.
- Healing restores health.
- Random events can give your pet a bonus or cause damage.
- Over time, hunger, boredom, and exhaustion increase automatically.

This keeps the game moving and means you need to keep checking in on your pets.

## Save system

The game automatically saves progress to `savegame.json`.

You can:

- save the game at any time from the menu
- load the previous save later

This makes it easy to keep playing without losing progress.

## Project files

- `main.py` — starts the game
- `game.py` — game logic and menu flow
- `tamagotchi.py` — pet behavior and stats
- `storage.py` — save/load logic
- `savegame.json` — stored game data

## Requirements

This project uses only Python's standard library, so there are no extra dependencies to install.

## Quick start

```bash
python main.py
```

Have fun raising your pets and trying to keep them alive as long as possible.
