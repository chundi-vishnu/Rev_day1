l='''Chris Harry K
Siddartha Kommu
Mayank Pathak
Balaji Pappala
Sumanth Kumar Valluru
Japa Harish
Lakshmi Sahithi Vanga
G.VANI
Indukuru Sravani
Sirneni Pavan Sai
Suman Kumar Ghorai
Yugesh Karoti
chundi vishnu priya
Sri Sanjana Indugula
G Santosh Kumar
GANGIREDLA KARTHIK
Venkata Naidu Punnana
pedapalli suresh
Prathamesh Pahune
Venkata Krishna kolli
Ram Mishra'''
v=[i for i in l.split('\n')]
dict={k:v[k-1] for k in range(1,len(v)+1)}
print(dict)