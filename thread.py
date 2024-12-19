from time import sleep
from threading import Thread

def funcao1():
    for i in range(1,11):
        print("executando funcao 1")
        sleep(1)
        if i == 10:
            break


def funcao2():
    for i in range(1,11):
        print("executando funcao 2")
        sleep(0.8)
        if i == 10:
            break

t1 = Thread(target=funcao1)
t1.start()

t2 = Thread(target=funcao2)
t2.start()

funcao2()

