# text="Hello World!".lower().replace(" ","").replace("!","")
# p={i for i in text}
# print(p)
from collections import OrderedDict
text = "Hello World!"


a = OrderedDict.fromkeys([char.lower() for char in text if char.isalpha()])
print(a)
print(f"{{','.join(a.keys())}}")