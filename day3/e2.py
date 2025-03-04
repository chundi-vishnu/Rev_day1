users=[("Alice",25,"New York"),("Bob",17,"Los Angles"),("Charlie",30,"Chicago")]
user_dict={users[i][0]:users[i][1] for i in range(len(users)) if users[i][1]>18}
print(user_dict)