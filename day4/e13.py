# import random
# l='''Chris Harry K
# Siddartha Kommu
# Mayank Pathak
# Balaji Pappala
# Sumanth Kumar Valluru
# Japa Harish
# Lakshmi Sahithi Vanga
# G.VANI
# Indukuru Sravani
# Sirneni Pavan Sai
# Suman Kumar Ghorai
# Yugesh Karoti
# chundi vishnu priya
# Sri Sanjana Indugula
# G Santosh Kumar
# GANGIREDLA KARTHIK
# Venkata Naidu Punnana
# pedapalli suresh
# Prathamesh Pahune
# Venkata Krishna kolli
# Ram Mishra'''
# v=[i for i in l.split('\n')]
# endpoint=2
# for(startpoint in range(1,))

# import random

# # Sample list of names
# names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# # Get two random indices in order
# indices = sorted(random.sample(range(len(names)), 2))
# print(indices)

# # Extract names with ordered indices
# selected_names = [(i, names[i]) for i in indices]

# #print(selected_names)
import random

names = [
    'Chris Harry K', 'Siddartha Kommu', 'Mayank Pathak', 'Balaji Pappala',
    'Sumanth Kumar Valluru', 'Japa Harish', 'Lakshmi Sahithi Vanga', 'G.VANI',
    'Indukuru Sravani', 'Sirneni Pavan Sai', 'Suman Kumar Ghorai', 'Yugesh Karoti',
    'Chundi Vishnu Priya', 'Sri Sanjana Indugula', 'G Santosh Kumar', 'Gangiredla Karthik',
    'Venkata Naidu Punnana', 'Pedapalli Suresh', 'Prathamesh Pahune', 'Venkata Krishna Kolli',
    'Ram Mishra'
]

def get_random_groups(names_list, group_size=2):
    """Shuffles names and groups them into pairs."""
    random.shuffle(names_list) 
    groups = [names_list[i:i + group_size] for i in range(0, len(names_list), group_size)]
    #print(groups)
    return groups
random_groups = get_random_groups(names)
for i, group in enumerate(random_groups,1):
    print(f"Group {i}: {group}")
