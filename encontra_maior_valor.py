import datetime
import matplotlib.pyplot as plt

def encontrar_maior_valor(dataset):
    start = datetime.datetime.now()
    with open(dataset+'.csv') as myfile:
        data = myfile.read().split('\n')[:-1]
    maior_num = 0
    for i in data:
        if int(i) > maior_num:
            maior_num = int(i)
    end = datetime.datetime.now()
    timedif = end - start
    maiores_valores.append(maior_num)
    file = open('resposta-'+dataset+'.txt','w') 
    file.write(str(maior_num)+'\n')
    file.write(str(timedif.total_seconds() * 1000)) 
    file.close() 

def plot_grafico(maiores_valores):
    plt.plot(['a', 'b', 'c', 'd', 'e'], maiores_valores, color='lightblue', linewidth=3)
    plt.xlim('a', 'e')
    plt.ylim(900000, 10000000)
    plt.show()

maiores_valores =[]
a = 'dataset-2-a'
b = 'dataset-2-b'
c = 'dataset-2-c'
d = 'dataset-2-d'
e = 'dataset-2-e'

print(encontrar_maior_valor(a))
print(encontrar_maior_valor(b))
print(encontrar_maior_valor(c))
print(encontrar_maior_valor(d))
print(encontrar_maior_valor(e))
plot_grafico(maiores_valores)
