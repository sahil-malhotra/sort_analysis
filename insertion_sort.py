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
    print(list)

def mean(a):
    return sum(a) / len(a)

def test():
    graph_list_x = []

    find_all_list_y = []

    random_lists = []
    range_num = 1000

    # creating 15 random lists with varying length like 1000, 2000.., till 15000.
    for one_list in range(15):
        random_lists.append([])
        for x in range(range_num):
            random_lists[one_list].append(random.randint(1, 1001))
        range_num += 1000
        graph_list_x.append(len(random_lists[one_list]))

        print(random_lists[one_list])

    # Each list being tested 50 times and then calculating the average time taken for execution of each list
    for i in range(50):
        graph_list_y = []
        for one_item in range(15):
            start = time.clock()
            insertion(random_lists[one_item])
            elapsed = (time.clock() - start)

            graph_list_y.append(elapsed)

        find_all_list_y.append(graph_list_y)


    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))

    # plotting the graph
    plt.xlabel('List Length')
    plt.ylabel('Time Taken')
    plt.plot(graph_list_x, final_avg_list_y)
    plt.grid()
    plt.show()

if __name__ == '__main__':

    test()