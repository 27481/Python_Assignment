import sys

# Get the current recursion limit
current_limit = sys.getrecursionlimit()
print("Current recursion limit:", current_limit)

# Set a new recursion limit (e.g., 5000)
new_limit = 1000000000
sys.setrecursionlimit(new_limit)

# Verify the updated recursion limit
updated_limit = sys.getrecursionlimit()
print("Updated recursion limit:", updated_limit)



def bhupender_jogi():
    return bhupender_jogi()

# Call the infinite recursive function
bhupender_jogi()


