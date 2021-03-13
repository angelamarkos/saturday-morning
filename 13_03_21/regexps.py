import re
string = '-this Them\t Absdfg*# This<tag1>1\t is 5jo a. 22<ta@#g1> [] \<test>\n That them *2 b1 string.'

'is' in string
print(string.find('is'))
print(string.index('is'))
match_instance = re.search('is', string)

print(re.search('[12][12]', string))
print(re.search('[*abc][12]', string))
print(re.search('[a-zA-Z]{4}', string))
print(re.search('[^a-zA-Z][a-zA-Z]{3,4}', string))
print(re.search('[a-zA-Z]*', string))

print(re.search('<[a-zA-Z][a-z0-9]+>', string))
print(re.search('<([a-zA-Z][a-z0-9])+>', string))
print(re.search('[\w]', string))
print(re.search('[a-zA-Z0-9_]', string))
print(re.search('[\W]', string))
print(re.search('[^a-zA-Z0-9_]', string))

print(re.search('[\d]', string))
print(re.search('[\D]', string))

print(re.search('[\s]', string))
print(re.search('[\S]', string))

print(re.search('\.', string))
print(re.search('\\\\', string))

print(re.search('^th[a-z]{2}\s', string))
print(re.search('string.$', string))
matched = re.search('([A-Z][a-z]{5})([*&^#])', string)

print(matched.group(0))
print(matched.group(1))
print(len(string))
print(re.search('.*', string))
print(re.search('-?this', string))

print(re.search('<.*>', string))
print(re.search('<\S+?>', string))

# * +
line_1 = '</tag_1> <tag_1>value <tage_2> dfds </tag_2> </tag_1>'

# print(re.search("<\w+>|</\w+>", line_1))

print(re.search('Th\w+?\d', string))
print(re.search('Th.+ ', string))

# ^ $ \A \Z
print(re.search('Th\w+? ', string, re.MULTILINE|re.IGNORECASE))

string = 'String \n asd \n'
string = """
Text 1
Text 2
"""

#
# # # print(re.findall("<\w+>|</\w+>", line_1))
# # print(list(re.finditer("<\w+>|</\w+>", line_1)))
# # print(list(re.split("<\w+>|</\w+>", line_1)))

text = """Return a list of all non-overlapping matches in the string.
If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.
    Empty matches are included in the result."""

print(re.findall('.+?\.', text, re.DOTALL))


