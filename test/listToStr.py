import re

#

# str = ','.join(str(item) for inneritem in list for item in inneritem)

# keywords = ('[', ']')
# restr = re.sub('|'.join(keywords), '', '[[10, 20], [39, 182], [61, 90]]')


s = '[]'
str = '[[10, 20], [39, 182], [61, 90]]'
a = re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', str, re.S)
restr = ",".join(a)
print(restr)
