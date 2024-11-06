
# Minesweeper Game Project
<a src="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow"></a>

## Overview
This Minesweeper game is a desktop application developed using Python and PyQt5. The project is structured using the Model-View-Controller (MVC) software architecture pattern, which organizes the game into separate modules for handling data (Model), user interface (View), and input logic (Controller). This approach improves maintainability and enables easier future enhancements.

## 1. Software Architecture Pattern: MVC
**Justification:** The MVC pattern is well-suited for this game because it separates the game's logic, display, and user interaction, making it easier to manage and update. Each component in MVC serves a distinct role:
- **Model:** Manages game data, including the board layout, mines, and cell states.
- **View:** Manages the graphical user interface (GUI), displaying the board and its current state.
- **Controller:** Handles user inputs, updates the Model, and refreshes the View as needed.

## 2. Design Patterns

### 2.1 Creational Patterns
- **Factory Method Pattern:**
  - **Purpose:** To create buttons representing cells in the game dynamically.
  - **Implementation:** The `GameFactory` class creates cells based on the grid layout and assigns them as either mines or empty cells. By using a factory to create the buttons, we ensure flexibility if we need to change cell types in the future.

- **Singleton Pattern:**
  - **Purpose:** Ensures a single instance of the `GameFactory` class, maintaining a consistent game state across the application.
  - **Implementation:** The `GameFactory` class acts as a singleton in this structure, initialized once with the game configuration. This approach avoids potential issues with multiple instances managing separate game states.

### 2.2 Structural Patterns
- **Decorator Pattern:**
  - **Purpose:** Adds functionality to buttons to handle cell states, including flagging or revealing the cell.
  - **Implementation:** The `StyleState` class uses different methods (e.g., `_empty_cell`, `_mine_cell`, `_open_cell`) to dynamically modify button styles based on the cell state. This class acts as a decorator by changing the appearance and behavior of buttons without altering the `QPushButton` class itself.

- **Facade Pattern:**
  - **Purpose:** Simplifies interaction with complex methods for board setup and information display.
  - **Implementation:** The `Utils` class provides helper methods like `make_playground`, `make_info`, and `open_empty_cell`, abstracting complex processes of board generation and cell state updates. This facade simplifies interactions within the game setup.

### 2.3 Behavioral Patterns
- **Observer Pattern:**
  - **Purpose:** Monitors cell states to detect game-ending conditions.
  - **Implementation:** The main game loop observes changes in the flag count and mines detected, allowing the game to end when all mines are correctly flagged. The `check_win` function tracks flagged cells and updates the game status accordingly.

- **Command Pattern:**
  - **Purpose:** Handles different user interactions, such as left and right clicks on cells.
  - **Implementation:** The `handle_right_click` method in `GameFactory` acts as a command handler, executing different commands based on user input (e.g., toggling a flag with a right-click and revealing cells with a left-click).

## 3. UML Diagrams
Include the following UML diagrams for clarity:
- **Class Diagram:** Illustrate relationships between `GameFactory`, `MainWindow`, `Utils`, and `StyleState`. Show dependencies between `GameFactory` (Controller) and the View elements (buttons) as well as the Model (Utils).
- **Sequence Diagram:** Depict interactions when a cell is clicked, showing steps from `MainWindow` to `GameFactory`, updating the cell state, and refreshing the View.
- **State Diagram:** Illustrate the cell states (hidden, flagged, revealed, mine) and transitions based on user actions.

## 4. Usage Instructions
- Run the `main.py` file to start the Minesweeper game.
- Use left-click to reveal a cell and right-click to flag or unflag a cell.
- The game displays a flag counter to track flags placed. When the correct number of mines is flagged, the game declares a win.

## 5. Assumptions and Limitations
- **Assumptions:** The board size and number of mines are defined at the beginning and do not change mid-game.
- **Limitations:** The game currently supports only one difficulty level, with no support for custom configurations. All icons and graphics need to be available in the `assets/images` directory.

This structured approach in documentation captures each design aspect, improving both comprehension and future maintenance.
- https://github.com/barcek2281 Zhunis Ayanat
- https://github.com/Butternut01 Bayadiov Asanali
- https://github.com/Zufar-zfr Zufar Abdulvagap
