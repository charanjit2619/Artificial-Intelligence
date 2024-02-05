# AI-Optimized Robot Navigation: Solving a Grid-Based Puzzle with MDP

In this comprehensive AI project, I tackled the intricate problem of robotic navigation within a constrained grid environment, representing a puzzle with terminal rewards and obstacles. Utilizing the principles of Markov Decision Processes (MDP) and Value Iteration algorithm, I programmed a solution in Python that guides a virtual robot to its goal while avoiding game-over states.

The project's core is the development of an MDP class that defines the environment's states, actions, and rewards. The Value Iteration algorithm, executed over 100 iterations, calculates the optimal policy for the robot's movements, taking into account action costs and the direction faced by the robot. Special attention was given to the action model, which incorporates various costs and realistic constraints like blocked paths and impossible moves.

Through meticulous coding and testing, I incorporated conditions such as noise and discount factors, transitioning the problem from deterministic to probabilistic scenarios. This change highlighted the algorithm's robustness, where it successfully altered the robot's path based on the likelihood of achieving the best possible outcome.

By simulating different action outcomes and iterating to convergence, the robot demonstrated an ability to navigate effectively, reflecting real-world applications where AI must make strategic decisions in uncertain environments. The results underscore the potential of MDPs in AI to optimize decision-making processes, paving the way for smarter, more efficient robotic navigation systems.

This repository contains all the source code, alongside a detailed walkthrough of the methodology and conclusions drawn from the robot's performance under various simulation settings. It stands as a testament to the power of AI in solving complex, dynamic problems with multiple variables at play.
