# likes = ["cake","apple","banna","noodles"]
# likes.remove("apple")
# print(likes)
my_coustomers = ["董卓","吕布","吕不韦"]
# costomers = costomer for customer in my_coustomers
for costomer in my_coustomers:
	print(costomer+"，期望与您共进晚餐。")

unpresented_costomers = "吕不韦"
print("\n"+unpresented_costomers)
print(my_coustomers.remove(unpresented_costomers))
for costomer in my_coustomers:
	print(costomer+"，再次期望与您共进晚餐。")

ultra_costomers = ["chen ming","dai shijie","wang wei"]
my_coustomers.insert(0,ultra_costomers[0])
my_coustomers.insert(2,ultra_costomers[1])
my_coustomers.append(ultra_costomers[-1])
print(my_coustomers)
print("\n我们找到了一张更大的餐桌，现在我们可以邀请更多人了，比如，emmmmm ~\n\t")
for costomer in ultra_costomers:
	print(costomer.title()+"，非常期望与您共进晚餐，too ~")

print("\nSorry, it's out of my thought, we can't have you all dinner actually, for the first time I hear that I was very sad. ")
for i in range(0,3):
	my_coustomers.pop(i)
for costomer in my_coustomers:
	print(costomer.title()+"：\n\t您好，您依然在我们邀请共进晚餐的队列，欢迎您的莅临！\n")

del my_coustomers[0]
del my_coustomers[0] 
print(my_coustomers)