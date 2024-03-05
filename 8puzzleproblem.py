
import heapq

class Puzzle:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __lt__(self, other):
        return self.cost < other.cost

    def goal_state(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.state == goal

    def possible_moves(self):
        moves = []
        i, j = self.find_zero()
        if i > 0:
            moves.append((-1, 0))  # Move the blank space up
        if i < 2:
            moves.append((1, 0))   # Move the blank space down
        if j > 0:
            moves.append((0, -1))  # Move the blank space left
        if j < 2:
            moves.append((0, 1))   # Move the blank space right
        return moves

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_child(self, move):
        new_state = [row[:] for row in self.state]
        i, j = self.find_zero()
        new_i = i + move[0]
        new_j = j + move[1]
        new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
        return Puzzle(new_state, self, move)

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    value = self.state[i][j]
                    goal_i, goal_j = (value - 1) // 3, (value - 1) % 3
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def print_solution(self):
        if self.parent:
            self.parent.print_solution()
        if self.move:
            print(f"Move the blank space {'Up' if self.move == (-1, 0) else 'Down' if self.move == (1, 0) else 'Left' if self.move == (0, -1) else 'Right'}")
        for row in self.state:
            print(row)
        print(f"Cost: {self.cost}")
        print()

def get_user_input():
    print("Enter the initial state of the 8-puzzle (use 0 to represent the blank space):")
    initial_state = []
    for i in range(3):
        row = input(f"Enter elements for row {i + 1} separated by space: ").strip().split()
        initial_state.append([int(num) for num in row])
    return initial_state

def solve_puzzle(initial_state):
    initial_node = Puzzle(initial_state)
    frontier = []
    heapq.heappush(frontier, initial_node)

    visited = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        visited.add(current_node)

        if current_node.goal_state():
            return current_node

        for move in current_node.possible_moves():
            child = current_node.generate_child(move)
            if child not in visited:
                child.cost = child.depth + child.manhattan_distance()
                heapq.heappush(frontier, child)

    return None

if __name__ == "__main__":
    initial_state = get_user_input()
    solution = solve_puzzle(initial_state)
    if solution:
        print("Solution found:")
        solution.print_solution()
    else:
        print("No solution found.")


