alien0 = {"color": "", "points": 0, "speed": "", "x_position": 0, "y_position": 5}
for i in range(0,3):
	i += 1
	if i == 2:
		break
	else:
		spd = input("请告诉我你刚刚击败的alien的速度？\n")
		alien0["speed"] = str(spd)
		if str(spd) == "slow":
			alien0["add_x_position"] = 1
			alien0["points"] = 5
			alien0["color"] = "green"
		elif str(spd) == "medium":
			alien0["add_x_position"] = 2
			alien0["points"] = 8
			alien0["color"] = "blue"
		elif str(spd) == "fast":
			alien0["add_x_position"] = 3
			alien0["points"] = 10
			alien0["color"] = "gold"
		alien0["x_position"] += alien0["add_x_position"]
		print("The " + alien0["color"] + " alien you just killed, then you get " + str(
			alien0["points"]) + " points for your award!\n" + "Now it's at x_position " + str(
				alien0["x_position"]) + ".")
