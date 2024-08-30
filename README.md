
# Auto Clicker

This is a Python-based auto clicker designed specifically for the Cookie Clicker game. The script automatically clicks the screen at a high rate and performs additional clicks at specific coordinates at regular intervals.

## Features

- Continuous clicking with a customizable delay.
- Special clicks at designated coordinates every 30 seconds.
- Simple start/stop mechanism using the spacebar.
- Display of current mouse position in a small, movable window.

## Installation

### Prerequisites

- Python 3.x
- Install the necessary Python packages:
  ```bash
  pip install pyautogui pynput
  ```

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/robertusaph/auto-clicker.git
   cd auto-clicker
   ```

2. Run the script:
   ```bash
   python auto-clicker.py
   ```

3. Press the spacebar to start or stop the auto clicker.

### Customization

- **Click Delay**: Adjust the `delay` variable to change the speed of continuous clicking.
- **Special Click Interval**: Modify the `special_click_interval` variable to change how often the special clicks occur.
- **Special Click Coordinates**: The script clicks at a series of hardcoded coordinates. Adjust these as needed for your game setup.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
