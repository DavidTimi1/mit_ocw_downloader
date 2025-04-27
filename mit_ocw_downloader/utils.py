import math

def escape(s):
    for old, new in [(":"," -"), ("?", "~q"), ("/", " or "), ("|", "-")]:
        s = s.replace(old, new)
    return s

def unitSize(size):
    pow = round(math.log10(size) / math.log10(1024))

    if pow < 1: 
        return f"{size} B"
    
    if pow == 2:
        return f"{int((size / 1024) * 100)/100} KB"
    
    if pow == 3:
        return f"{int((size / 1024 ** 2) * 100)/100} MB"
    
    return f"{int((size / 1024 ** 3) * 100)/100} GB"