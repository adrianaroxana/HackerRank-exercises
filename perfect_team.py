
skills = "pppmmbbcccczzzpppmmmbbbbzzpp"
my_list = []
a = skills.count("p")
my_list.append(a)
b = skills.count("m")
my_list.append(b)
c = skills.count("c")
my_list.append(c)
d = skills.count("b")
my_list.append(d)
e = skills.count("z")
my_list.append(e)
print(my_list)
print("The number of teams that can be formed is: ", min(my_list))
