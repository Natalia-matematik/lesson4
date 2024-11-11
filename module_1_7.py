immutable_var=(1975, 1979, 'Sun', 'Moon')
print(immutable_var)
print('кортеж это неизменяемые объекты',immutable_var)
mutable_list=["hare", "wolf", "fox", "bear", 4]
print(mutable_list)
mutable_list[0]=1975
mutable_list[3]=2007
mutable_list[4]='elephant'
mutable_list.append('animals')
mutable_list.extend(['predators',3])
mutable_list.remove(1975)
print(mutable_list)
print('elephant' in mutable_list)
print(1979 not in mutable_list)
print('predators' not in mutable_list)