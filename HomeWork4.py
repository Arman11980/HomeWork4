immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
immutable_var[1][1] = 200 # кортеж менять нельзя-это закон
print(immutable_var)
Mutable_list = [1, 2,'a','b', 'Modifiet']
Mutable_list[0][0] = 8 # тот же закон
print(Mutable_list)