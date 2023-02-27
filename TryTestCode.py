my_state = "illinois"
total = my_state.count("l") + my_state.find("i") + len(my_state) + my_state.index("o")
print(total)
#--------------------------------------------------------------
s1 = "abc"
s2 = "abcdef"
print(s1.__contains__(s2))
#--------------------------------------------------------------
L1 = []
L1.append([1,[2,3],4])
L1.extend([7,8,9])
print(L1[0][1][1] + L1[2])