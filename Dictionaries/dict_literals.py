dict_literals = {}
print(dict_literals)    # {}
dic = dict()
print(dic)              # {}
dic[(2,3)] = 10
dict_literals[(2,3)] = 10
print(dic)              # {(2, 3): 10}
print(dict_literals)    # {(2, 3): 10}
#They are more or less same , but dictionary literals are more readable and commonly used.
