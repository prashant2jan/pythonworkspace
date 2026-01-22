squares = {x: x*x for x in range(1,11)}
print(squares)

squares = {x*x for x in range(1,11)}
print(squares)

squares = {x*x for x in range(1,11)}
print(sorted(squares))
print(sorted(squares, reverse=True))