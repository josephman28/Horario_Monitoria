# Para correr el codigo es necesario instalar networkx y matplotlib

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
E = nx.Graph()
C = nx.Graph()

file_g = open("hor_graf.txt","r")
file_e = open("hor_ecu.txt","r")
file_c = open("hor_cal3.txt","r")

linea_g = file_g.readlines()
linea_e = file_e.readlines()
linea_c = file_c.readlines()

def agregar_v(grafo,x):
    grafo.add_node(x)


def agregar_a(grafo,x,y):
    grafo.add_edge(x,y)


def Horario(grafo, linea):

    cont=0
    estudiantes = len(linea)

    estu = []
    for i in range(estudiantes):
        estu.append(i)
        estu[i]= linea[i].split("\n")
        estu[i]= estu[i][0].split(".")

    y= estu[0]
    for j in range (1, estudiantes):
        x = estu[j]
        for i in y:
            agregar_v(grafo, i)
            for e in x:
                if i == e:
                    agregar_a(grafo, i, cont)
                    cont+=1

    hor_fin = ''
    maxim = 0

    for i in range (len(y)):
        n = y[i]
        x = grafo.degree(n)
        #
        #
        if (x > maxim):
            maxim = x
            hor_fin = n
            #print(hor_fin)

    if hor_fin[0] == "1":
        hor1 = hor_fin[len(hor_fin)-1:]
        hor_fin = hor_fin[1:(len(hor_fin)-1)]

        hor_fin = "Lunes " + hor_fin
        hor_fin = hor_fin + "-" + hor1


    elif hor_fin[0] == "2":
        hor1 = hor_fin[len(hor_fin)-1:]
        hor_fin = hor_fin[1:(len(hor_fin)-1)]

        hor_fin = "Martes " + hor_fin
        hor_fin = hor_fin + "-" + hor1

    elif hor_fin[0] == "3":
        hor1 = hor_fin[len(hor_fin)-1:]
        hor_fin = hor_fin[1:(len(hor_fin)-1)]

        hor_fin = "Miercoles " + hor_fin
        hor_fin = hor_fin + "-" + hor1

    elif hor_fin[0] == "4":
        hor1 = hor_fin[len(hor_fin)-1:]
        hor_fin = hor_fin[1:(len(hor_fin)-1)]


        hor_fin = "Jueves " + hor_fin
        hor_fin = hor_fin + "-" + hor1

    elif hor_fin[0] == "5":
        hor1 = hor_fin[len(hor_fin)-1:]
        hor_fin = hor_fin[1:(len(hor_fin)-1)]

        hor_fin = "Viernes " + hor_fin
        hor_fin = hor_fin + "-" + hor1


    if grafo == G:
        print("El mejor horario para la monitoria de {} es: ".format("Grafos"), hor_fin)
    elif grafo == E:
        print("El mejor horario para la monitoria de {} es: ".format("Ecuaciones"), hor_fin)
    else:
        print("El mejor horario para la monitoria de {} es: ".format("Calculo 3"), hor_fin)

print("Grafos (rosa): ")
Horario(G, linea_g)
nx.draw(G,with_labels=True,node_color="pink")


print("Ecuaciones (verde): ")
Horario(E, linea_e)
nx.draw(E,with_labels=True,node_color="lightgreen")


print("Cálculo (azul):")
Horario(C, linea_c)
nx.draw(C,with_labels=True)

plt.draw()
plt.show()
