# Vehicle Routing Problem (VRP) Mathematical Formulations

This repository presents the mathematical formulations of the Capacitated Vehicle Routing Problem (CVRP). The CVRP is a classic combinatorial optimization problem that involves delivering goods to customers using a fleet of vehicles while minimizing transportation costs.

## Problem Description

The CVRP can be represented mathematically as follows:

**Parameters:**
- `n`: Number of customers (excluding the depot).
- `p`: Number of vehicles.
- `c[i][j]`: Cost or distance between customer `i` and customer `j`.
- `d[i]`: Demand of customer `i`.
- `Q[v]`: Vehicle 'v` capacity.

**Decision Variables:**
- `x[i][j][v]`: Binary variable indicating whether vehicle `v` travels from customer `i` to customer `j`.

## Mathematical Formulations

### Objective Function

Minimize the total distance traveled by all vehicles:

$$
\min \sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{v=1}^{p} c_{ij} \cdot x_{ijv}
$$


### Constraints

1. **Each customer must be visited by exactly one vehicle (excluding the depot):**

$$
\sum_{j=1}^{n} \sum_{v=1}^{n} x_{ijv} = 1, \quad \forall i \in \{1, \ldots, n\}
$$


2. **Flow conservation at each customer (excluding the depot):**

$$
\sum_{j=1}^{n} \sum_{v=1}^{n} x_{ijv} - \sum_{j=1}^{n} \sum_{v=1}^{n} x_{jiv} = 0, \quad \forall i \in \{1, \ldots, n\}
$$


3. **Vehicle load constraints (individual capacities for each vehicle):**

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} d_i \cdot x_{ijv} \leq Q_v, \quad \forall v \in \{1, \ldots, n\}
$$


In the third constraint, \(Q_v\) represents the capacity of vehicle \(v\). You would need to specify these individual vehicle capacities in your problem instance data.

## Usage

To use this mathematical model for solving the CVRP, you can implement it in an optimization library like PuLP and provide your own data to find optimal routes.

## Contributing

Contributions to this project by improving the mathematical model or adding new features are welcome. Pull requests and discussions are encouraged.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
