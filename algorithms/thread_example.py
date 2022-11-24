from threading import Thread


def ceva_functie(start, stop):
    index = start
    while index < stop:
        print(index)
        index += 1


thread = Thread(target=ceva_functie, args=(50, 100))
thread2 = Thread(target=ceva_functie, args=(0, 50))
thread.start()
thread2.start()

thread.join()
thread2.join()