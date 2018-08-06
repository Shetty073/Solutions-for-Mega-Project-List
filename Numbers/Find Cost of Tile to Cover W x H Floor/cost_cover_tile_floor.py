def cost_to_tile(w, h, c):
	cost = w * h * c
	return f"Total cost will be {cost}"
print(cost_to_tile(w=float(input("Width in floorplan: ")), h=float(input("Height in floorplan: ")), c=float(input("Enter the cost of a tile: "))))
