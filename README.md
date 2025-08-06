
# Endless Runner Game

A 2D endless runner game built with Python and Pygame where players dodge incoming enemies while running.

## Features

- Classic endless runner gameplay
- Player character with running animation
- Random enemy generation
- Score tracking system
- Increasing difficulty as game progresses
- Simple one-button control scheme

## Requirements

- Python 3.9+
- Pygame library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cherund/runner.git
   cd runner
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Controls:
   - **Space Bar**: Jump to avoid enemies
   - **ESC**: Quit game

3. Game Rules:
   - Avoid incoming enemies by jumping over them
   - Score increases the longer you survive
   - Game speed increases over time
   - Game ends when you collide with an enemy



## Code Overview

### main.py
- Handles game initialization and main loop
- Manages game states (running, game over)
- Controls game speed and difficulty progression
- Handles score display and updates

### Player_Enemies.py
- `Player` class:
  - Handles player movement and jumping physics
  - Manages animation states
  - Collision detection with enemies

- `Enemy` class:
  - Controls enemy movement and spawning
  - Manages different enemy types
  - Handles off-screen removal

## Customization

You can easily modify:
- Game speed parameters in `main.py`
- Player jump height in `Player_Enemies.py`
- Enemy spawn rates and types
- Visual styles by replacing assets

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## Acknowledgments

- Inspired by classic endless runner games
- Thanks to Pygame community for excellent resources

