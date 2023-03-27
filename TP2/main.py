import Patisserie as myPatisserie
import pickle as pkl
import re


My_gateau1 = myPatisserie.Patisserie(45, 'BIY' )


print(My_gateau1.get_categorie())
My_gateau1.set_categorie('Ton chien')
print(My_gateau1.get_categorie())




'''with open('gat1.pkl', 'wb') as f:
    pkl.dump(My_gateau1, f)
with open('gat1.pkl', 'rb') as f:
    My_gateau2 = pkl.load(f)'''
'''
print(My_gateau1.get_categorie())
print(My_gateau2.get_categorie())
my_gateau_temp = My_gateau1 + My_gateau2
print(my_gateau_temp)'''