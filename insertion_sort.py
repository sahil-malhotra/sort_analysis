import random
import time
import matplotlib.pyplot as plt

def insertion(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i>=0 and (value < list[i]):
            list[i+1] = list[i]
            list[i] = value
            i = i - 1



def mean(a):
    return sum(a) / len(a)

def test():
    graph_list_x = []


    find_all_list_y = []
    find_all_sorted_list_y = []
    find_all_worst_list_y = []

    random_lists = []
    sorted_list_y = []
    worst_list_y = []
    range_num = 2000

    # creating 15 random lists
    for one_list in range(15):
        random_lists.append([])
        for x in range(range_num):
            random_lists[one_list].append(random.randint(1, 1001))
        range_num += 2000
        graph_list_x.append(len(random_lists[one_list]))

        print(random_lists[one_list])

    # creating 15 random best sorted lists
    for one_item in range(15):
        sorted_list_y.append(sorted(random_lists[one_item]))

    # creating 15 random worst sorted lists
    for one_item in range(15):
        worst_list_y.append(sorted(random_lists[one_item], reverse=True))

    # Each list being tested 50 times and then calculating the average time taken for execution of each list (average case)
    for i in range(50):
        graph_list_y = []
        for one_item in range(15):
            pass_list = random_lists[one_item][:]
            start = time.clock()
            insertion(pass_list)
            elapsed = (time.clock() - start)
            print(pass_list)

            graph_list_y.append(elapsed)

        find_all_list_y.append(graph_list_y)


    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))

    # Each list being tested 50 times and then calculating the average time taken for execution of each list (best case)
    for i in range(50):
        graph_sorted_list_y = []
        for one_item in range(15):
            pass_list = sorted_list_y[one_item][:]
            start = time.clock()
            insertion(pass_list)
            elapsed = (time.clock() - start)
            print(pass_list)

            graph_sorted_list_y.append(elapsed)

        find_all_sorted_list_y.append(graph_sorted_list_y)


    final_sorted_avg_list_y = list(map(mean, zip(*find_all_sorted_list_y)))

    # Each list being tested 50 times and then calculating the average time taken for execution of each list (worst case)
    for i in range(50):
        graph_worst_list_y = []
        for one_item in range(15):
            pass_list = worst_list_y[one_item][:]
            start = time.clock()
            insertion(pass_list)
            elapsed = (time.clock() - start)
            print(pass_list)

            graph_worst_list_y.append(elapsed)

        find_all_worst_list_y.append(graph_worst_list_y)


    final_worst_avg_list_y = list(map(mean, zip(*find_all_worst_list_y)))

    # plotting the graph
    plt.xlabel('List Length')
    plt.ylabel('Time Taken')
    plt.plot(graph_list_x, final_avg_list_y, label='Average Case')
    plt.plot(graph_list_x, final_sorted_avg_list_y, label='Best Case')
    plt.plot(graph_list_x, final_worst_avg_list_y, label='Worst Case')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == '__main__':

    test()