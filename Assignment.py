def move_rover(max_x, max_y, x, y, direction, instructions):
    directions = ["N", "E", "S", "W"]

    if direction not in directions:
        raise ValueError("Invalid initial direction")

    dir_index = directions.index(direction)

    for command in instructions:
        if command not in ["L", "R", "M"]:
            continue

        if command == "L":
            dir_index = (dir_index - 1) % 4
        elif command == "R":
            dir_index = (dir_index + 1) % 4
        elif command == "M":
            current_dir = directions[dir_index]

            new_x, new_y = x, y

            if current_dir == "N":
                new_y += 1
            elif current_dir == "E":
                new_x += 1
            elif current_dir == "S":
                new_y -= 1
            elif current_dir == "W":
                new_x -= 1

            if 0 <= new_x <= max_x and 0 <= new_y <= max_y:
                x, y = new_x, new_y

    return x, y, directions[dir_index]


def process_input():
    try:
        max_x, max_y = map(int, input().split())
    except ValueError:
        raise ValueError("Invalid plateau size input")

    rovers = []

    while True:
        try:
            position = input().strip()

            if not position:
                continue

            x, y, direction = position.split()
            x, y = int(x), int(y)

            instructions = input().strip()

            rovers.append((x, y, direction, instructions))

        except EOFError:
            break
        except ValueError:
            print("Invalid rover input, skipping...")
            continue

    return max_x, max_y, rovers


def main():
    try:
        max_x, max_y, rovers = process_input()

        results = []

        for rover in rovers:
            x, y, direction, instructions = rover

            final_x, final_y, final_dir = move_rover(
                max_x, max_y, x, y, direction, instructions
            )

            results.append(f"{final_x} {final_y} {final_dir}")

        for result in results:
            print(result)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()