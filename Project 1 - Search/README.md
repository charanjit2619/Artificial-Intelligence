# AI Solutions for 9-Piece Puzzle Game

This project contains a comprehensive Python implementation addressing various aspects of the classic 9-piece puzzle game. The project is structured into distinct parts, each focusing on a different algorithmic approach to solve the puzzle.

**Part A:** Generates all possible states of the puzzle. The code efficiently lists these states and provides a sample of 10 states for demonstration.

**Part B:** Implements a state transition function. Given the current state and an action (up, down, left, right), the function computes the resultant state.

**Part C:** Focuses on reaching a goal state where each row's numbers form multiples of three. The program uses random actions to achieve this, showcasing the unpredictability and limitations of random search strategies.

**Part D:** Employs Breadth-First Search (BFS) to systematically explore the state space and find the shortest path to a numerically ordered goal state. This part details the sequence of actions and states from initial to goal state, highlighting BFS's effectiveness in finding optimal solutions.

**Part E:** Applies Depth-First Search (DFS) to the same problem addressed in Part D. The differences in the number of moves and the paths taken between BFS and DFS are analyzed, providing insights into the strengths and weaknesses of each method.

**Part F:** Adjusts the goal state to require a clockwise arrangement of numbers around a central blank space, posing a new challenge and testing the flexibility of the implemented search strategies.

**Part G:** Introduces Uniform Cost Search (UCS) with two cost scenarios: uniform cost and varied costs for different moves. This part demonstrates the impact of cost considerations on search strategy and solution optimality.

Each part of the project is accompanied by detailed code and comments, making it easy to follow and understand the implemented algorithms and their applications in solving the 9-piece puzzle.
