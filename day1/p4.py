#1
score1= {"Nexon": 85, "Harrier": 92, "Altroz": 88}
a=max(score1,key=score1.get)
max_value=score1[a]
print(a,max_value)