# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.arista import Arista


def buildear(dicc): #O(n^2)
    adys = []
    for i in dicc:
        for j in dicc:
            if dicc[i][j] > 0:
                adys.append(Arista().set_data(i, j, dicc[i][j]))
    return adys







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
