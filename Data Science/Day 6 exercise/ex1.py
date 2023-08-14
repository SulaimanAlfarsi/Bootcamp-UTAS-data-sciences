# Read the number of test cases
T = int(input("Enter the number of test cases: "))

# Loop through each test case
for i in range(T):
    # Read inputs for each test case
    N = int(input("Enter the number of friends: "))
    X = int(input("Enter the cost of each burger: "))
    K = int(input("Enter the amount of money Chef has: "))

    # Calculate the total cost of buying burgers for all friends
    total_cost = N * X

    # Compare the total cost with Chef's money
    if total_cost <= K:
        print("YES")
    else:
        print("NO")
