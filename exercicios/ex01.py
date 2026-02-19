import matplotlib.pyplot as plt 

#Construa um gráfico de barras que compare a nota de popularidade de séries em 2025:
series = ['Stranger Things', 'It', 'Game of Thrones','Friends']
notas = [8.7, 9.8, 8.0,8.1]

plt.bar(series, notas)
plt.show()
plt.savefig('./exercicios/ex01.png')

#Construa um gráfico de barras que compare os celulares mais vendidos em 2026

#Ele limpa o grafico criando, para criar novos
plt.clf()

celulares = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
valor = [200000, 320000, 500000]

plt.bar(celulares, valor)
plt.show()
plt.savefig('./exercicios/ex02.png')