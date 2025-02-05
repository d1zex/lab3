def solve(numheads, numlegs):
    r = (numlegs // 2) - numheads
    c = numheads - r
    
    if c < 0 or r < 0:
        return "No solution"
    
    return c, r

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")