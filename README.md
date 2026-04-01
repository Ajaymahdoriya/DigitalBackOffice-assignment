# Digital Back Office - Rover Navigation System

## Overview

This project implements a rover navigation system that controls robotic rovers on a rectangular plateau. The rovers can move in four cardinal directions (North, East, South, West) and follow a series of instructions to navigate the terrain without leaving the plateau boundaries.

## Features

- **Multi-Rover Support**: Control multiple rovers on the same plateau
- **Directional Movement**: Navigate in all four cardinal directions (N, E, S, W)
- **Command Processing**: Support for turn left (L), turn right (R), and move forward (M) commands
- **Boundary Protection**: Rovers automatically prevent boundary violations
- **Error Handling**: Robust input validation and error handling

## How It Works

### Rover Movement

Each rover operates within a rectangular plateau defined by maximum X and Y coordinates (0 to max_x, 0 to max_y).

**Available Commands:**
- `L` - Turn 90° left
- `R` - Turn 90° right
- `M` - Move forward one unit in the current direction

**Directions:**
- `N` - North (increases Y)
- `E` - East (increases X)
- `S` - South (decreases Y)
- `W` - West (decreases X)

### Example Scenario

```
Plateau size: 5 × 5
Rover 1: Start at (1, 2) facing North
Instructions: LMLMLMLMM
Final position: (1, 3) facing North

Rover 2: Start at (3, 3) facing East
Instructions: MMRMMRMRRM
Final position: (5, 1) facing East
```

## Usage

### Running the Program

```bash
python Assignment.py
```

### Input Format

1. **First Line**: Plateau dimensions
   ```
   5 5
   ```

2. **For Each Rover**:
   - Position and direction line: `x y direction`
   - Instructions line: `commands` (e.g., LMLMLMLMM)

### Example Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Output

Each rover's final position and direction:
```
1 3 N
5 1 E
```

## Functions

### `move_rover(max_x, max_y, x, y, direction, instructions)`
Moves a single rover based on provided commands.

**Parameters:**
- `max_x`: Maximum X coordinate of the plateau
- `max_y`: Maximum Y coordinate of the plateau
- `x`: Initial X coordinate
- `y`: Initial Y coordinate
- `direction`: Initial direction (N, E, S, W)
- `instructions`: String of commands (L, R, M)

**Returns:**
- Tuple: `(final_x, final_y, final_direction)`

### `process_input()`
Reads input from standard input and parses plateau size and rover data.

**Returns:**
- Tuple: `(max_x, max_y, rovers)` where rovers is a list of tuples

### `main()`
Main entry point that orchestrates input processing and rover movement calculations.

## Error Handling

- Invalid plateau dimensions will raise a `ValueError`
- Invalid rover positions are logged and skipped
- Invalid commands are silently skipped
- All exceptions are caught and reported with descriptive messages

## Implementation Details

- **Boundary Checking**: Before moving, the system checks if the new position is within plateau bounds
- **Direction Cycling**: Turning left/right uses modulo arithmetic to cycle through directions
- **Input Parsing**: Uses try-except blocks to gracefully handle invalid inputs
- **Rover Independence**: Each rover's path is calculated independently

## Notes

- Rovers cannot move outside the plateau boundaries
- Multiple rovers can occupy the same position
- The plateau's origin (0, 0) is at the bottom-left corner
- Invalid commands in the instruction string are ignored

## Requirements

- Python 3.x


