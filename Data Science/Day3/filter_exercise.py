#Use Filter/lambda to find a list of words including substring ‘cat’

#Example a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]

#Result = ['cat', 'wildcat', 'thundercat']

#Hint use: re.compile(pattern, flags=0) , you need to import re

import re

a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo","acat"]

p = re.compile(".*cat")


newList = list(filter(p.match,a))
print(newList)

print("________________________________________________________________ \n")

newList = list(filter(lambda v : re.match(".*cat",v),a))
print(newList)

print("________________________________________________________________ \n")

length = list(map(lambda a: len(a),newList))
print(length)