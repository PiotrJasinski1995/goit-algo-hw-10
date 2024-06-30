import pulp

# Initializing the model
model = pulp.LpProblem("Maximize_Products", pulp.LpMaximize)

# Defining variables
A = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer') # Quantity of Lemonade
B = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer') # Quantity of Fruit Juice

# Objective function (Profit maximization)
model += A + B, "Profit"

# Adding constraints
model += 2 * A + B <= 100 # Constraint for water
model += A <= 50 # Constraints for sugar
model += A <= 30 # Constraint for lemon juice
model += 2 * B <= 40 # Constraints for fruit puree

# Solving the model
model.solve()

# Displaying the results
print("Produce lemonade:", A.varValue)
print("Produce fruit juice:", B.varValue)
