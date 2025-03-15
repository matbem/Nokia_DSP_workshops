green = [ 2,-1]
blue  = [-1,-2]

dot_product = 0
for i in range(len(green)): # i = 0,..len(green)-1 
    dot_product += green[i] * blue[i]

print(dot_product)

