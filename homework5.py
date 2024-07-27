immutable_var = ("s",True,6,12)
print(immutable_var)
#immutable_var[3]=200
#print(immutable_var)
#Кортеж не поддерживает обращение по элементам,
#но это позволяет повысить производительность, безопасность и сэкономить память
mutable_list = ['super',False,[222,333,444]]
print(mutable_list)
mutable_list[0] = 'lucker'
print(mutable_list)