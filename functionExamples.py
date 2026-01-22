def greet(name="World"):
    print(f"Hello {name}!")

def add(a, b=0, *rest, **kwargs):
    """Add a, b and any extra positional numbers. kwargs ignored."""
    total = a + b + sum(rest)
    print(f"Sum {total}")
    print(f"Kwargs {kwargs}")
    return total

print(greet())
print(greet("Prashant"))
add(1, 2, 3, 4, 5, key="value")