dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

for i in dic2:
    dic1[i] = dic2[i]
for i in dic3:
    dic1[i] = dic3[i]
print(dic1)
