import pulp

# Example data
num_customers = 3
num_vehicles = 2
vehicle_capacities = [10, 4]  # Capacities of the two vehicles
depot_index = 0
distances = [
    [0, 2, 3, 1],  # Distance matrix (including the depot)
    [2, 0, 4, 2],
    [3, 4, 0, 3],
    [1, 2, 3, 0]
]
demands = [0, 3, 4, 2]  # Demands for depot and customers

# Create the LP problem
cvrp_problem = pulp.LpProblem("CVRP", pulp.LpMinimize)

# Decision variables
x = {}
for i in range(num_customers + 1):  # +1 for depot
    for j in range(num_customers + 1):  # +1 for depot
        for v in range(num_vehicles):
            x[i, j, v] = pulp.LpVariable(f"x_{i}_{j}_{v}", cat=pulp.LpBinary)



# Objective function
cvrp_problem += pulp.lpSum(distances[i][j] * x[i, j, v] for i in range(num_customers + 1) for j in range(num_customers + 1) for v in range(num_vehicles))

# Constraints
# Each customer must be visited by exactly one vehicle (excluding the depot)
for i in range(1, num_customers + 1):  # Start from 1 to skip the depot
    cvrp_problem += pulp.lpSum(x[i, j, v] for j in range(num_customers + 1) for v in range(num_vehicles)) == 1

# Flow conservation at each customer (excluding the depot)
for j in range(1, num_customers + 1):  # Start from 1 to skip the depot
    cvrp_problem += pulp.lpSum(x[i, j, v] for i in range(num_customers + 1) for v in range(num_vehicles)) - \
                    pulp.lpSum(x[j, i, v] for i in range(num_customers + 1) for v in range(num_vehicles)) == 0

# Vehicle load constraints (individual capacities)
for v in range(num_vehicles):
    cvrp_problem += pulp.lpSum(demands[i] * x[i, j, v] for i in range(num_customers + 1) for j in range(num_customers + 1)) <= vehicle_capacities[v]


# Solve the problem
cvrp_problem.solve()

# Process the solution and print the results
if pulp.LpStatus[cvrp_problem.status] == "Optimal":
    print("Optimal Routes:")
    for v in range(num_vehicles):
        route = [i for i in range(num_customers + 1) if any(pulp.value(x[i, j, v]) == 1 for j in range(num_customers + 1))]
        print(f"Vehicle {v}: {route}")
else:
    print("No feasible solution.")
