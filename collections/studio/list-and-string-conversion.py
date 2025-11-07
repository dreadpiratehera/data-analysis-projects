proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), 
# semicolons (;) or just spaces.

protoProtoList = [proto_list1, proto_list2, proto_list3, proto_list4]
CommaCount = 0
SemicolonCount = 0
SpaceCount = 0
CommaSpaceCount = 0
for comma in protoProtoList:
    CommaCount += 1
    if ',' in comma:
        print("The characters are separated by commas in proto_list" + str(CommaCount))
for semicolon in protoProtoList:
    SemicolonCount += 1
    if ';' in semicolon:
        print("THe characters are separated by semicolons in proto_list" + str(SemicolonCount))
for spaces in protoProtoList:
    SpaceCount += 1
    if ' ' in spaces:
        print("THe characters are separated by spaces in proto_list" + str(SpaceCount))


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, 
# and then join the array into a new comma separated string.

CommaArray = proto_list1.split(',')
CommaArray.reverse()
CommaString = ','.join(CommaArray)
print(CommaString)


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the 
# entries, and then join the array into a new comma separated string.

SemicolonArray = proto_list2.split(';')
SemicolonArray.sort()
SemicolonString = ";".join(SemicolonArray)
print(SemicolonString)



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize 
# the entries, and then join the array into a new space separated string.

SpaceArray = proto_list3.split(' ')
SpaceArray.sort(reverse=True)
SpaceString = " ".join(SpaceArray)
print(SpaceString)



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the 
# same result as part “b”, making sure that the extra spaces are NOT part of the final string.

CommaSpaceArray = proto_list4.split(', ')
CommaSpaceArray.reverse()
CommaSpaceString = ",".join(CommaSpaceArray)
print(CommaSpaceString)
