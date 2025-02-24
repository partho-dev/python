numbers = [1, 2, 3]
print(f"The output is {numbers}")
# Output [1, 2, 3]
print(*numbers)
# output 1 2 3


def greet(name, *args, **kwargs):
    print(f"Hello {name}")

    # Corrected: args is a tuple, and tuples don’t have `.count`, use `.len(args)` instead
    print(f"Total clothes: {len(args)}")  

    print(f"All args (clothes): {args}")  
    print(f"All kwargs (other info): {kwargs}")

# Calling the function with proper boolean syntax (True instead of true)
greet("Partho", "t-shirt", "pants", "Jackets", stay="4 days", food=True)
