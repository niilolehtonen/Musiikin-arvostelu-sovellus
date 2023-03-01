import re
def regex_check(x):
    if re.search("[^ ]+",x) == None:
        return False