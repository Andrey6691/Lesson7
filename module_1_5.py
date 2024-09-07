immutable_var=([1, 2, 3], 'apple', 'string', 2)
print(immutable_var)
#immutable_var[0]=5   Нельзя менять состав кортежа
#print(immutable_var)
immutable_var[0][2]=10
print(immutable_var)