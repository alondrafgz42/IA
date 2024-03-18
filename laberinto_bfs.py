#L A B E R I N T O  B F S 

#Declaracion de librerias
import time
import psutil
from collections import deque

def solve_maze(maze, start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return True, path

        # Mark as visited
        if (x,y) != start:
            maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    if maze[nx][ny] != 'E':
                        maze[nx][ny] = '2'

    return False, []

if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['S', '0', '1', '1', '1', '1', '1', '1', '1', '0'],
        ['1', '0', '1', '1', '1', '1', '0', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '0', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '0', '0', '0', '1', '1', '1'],
        ['S', '0', '1', '0', '1', '1', '0', '1', '1', '1'],
        ['1', '0', '1', '0', '1', '1', '0', '1', '1', '1'],
        ['1', '0', '0', '0', '1', '1', 'E', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

    ]

    start = (1, 0)
    end = (8, 6)

    start_time = time.time()
    solved, path = solve_maze(maze, start, end)
    end_time = time.time()

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")

    tiempo = end_time - start_time
    print("\nTime taken to solve the maze: {:.6f} seconds".format(tiempo))

    memoria = psutil.virtual_memory()
    print("\nMemory usage statistics:")
    print("Total memory:", memoria.total, "bytes")
    print("Available memory:", memoria.available, "bytes")
    print("Memory used:", memoria.used, "bytes")
    print("Memory free:", memoria.free, "bytes")
    print("Memory usage percentage:", memoria.percent, "%")
