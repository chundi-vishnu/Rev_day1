import re 
def extract_dates(text): 
    pattern = r"\b\d{4}-\d{2}-\d{2}\b" 
    return re.findall(pattern, text) 
text = "The event is scheduled for 2023-10-15 and 2023-11-20." 
dates = extract_dates(text) 
print(dates) 