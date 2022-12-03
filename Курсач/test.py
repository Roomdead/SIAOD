import random
from tkinter import *


def quickSort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr) - 1)]
        low = [item for item in arr if item[1] < x[1]]
        eq = [item for item in arr if item[1] == x[1]]
        hi = [item for item in arr if item[1] > x[1]]
        arr = quickSort(hi) + eq + quickSort(low)
    return arr

def clicked():
    g = int(igor.get())
    t = int(tries.get())
    results = []
    for i in range(t):
        results.append(random.randint(1, g))
    lbl_results = Label(window, text=results, font=("Arial Bold", 20))
    lbl_results.grid(column=3, row=3)
    maximums = []
    for res in results:
        if not maximums.count([res]):
            maximums.append([res])
    for el in maximums:
        el.append(results.count(el[0]))
    maximums = quickSort(maximums)
    lbl_answer = Label(window, text="Ебашим в ето " + str(maximums[0][0]), font=("Arial Bold", 20))
    lbl_answer.grid(column=3, row=4)

window = Tk()
window.title("Ща зарандомим")
window.geometry('400x250')
lbl_igor = Label(window, text="Скока игор?")
lbl_tries = Label(window, text="Скока попыток?")
btn = Button(window, text="Рандомим", command=clicked)

igor = Entry(window, width=10)
tries = Entry(window, width=10)

lbl_igor.grid(column=0, row=0)
igor.grid(column=0, row=1)
lbl_tries.grid(column=1, row=0)
tries.grid(column=1, row=1)
btn.grid(column=3, row=2)



window.mainloop()
