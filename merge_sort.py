import random
import time
import matplotlib.pyplot as plt


def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


def mean(a):
    return sum(a) / len(a)

def test():
    graph_list_x = []

    find_all_list_y = []

    random_lists = []
    range_num = 2000

    # creating 15 random lists with varying length like 1000, 2000.., till 15000.
    for one_list in range(15):
        random_lists.append([])
        for x in range(range_num):
            random_lists[one_list].append(random.randint(1, 1001))
        range_num += 2000
        graph_list_x.append(len(random_lists[one_list]))

        print(random_lists[one_list])

    # Each list being tested 50 times and then calculating the average time taken for execution of each list
    for i in range(50):
        graph_list_y = []
        for one_item in range(15):
            start = time.clock()
            merge_sort(random_lists[one_item])
            elapsed = (time.clock() - start)

            graph_list_y.append(elapsed)

        find_all_list_y.append(graph_list_y)
        print(graph_list_y)

    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))

    # plotting the graph
    plt.xlabel('List Length')
    plt.ylabel('Time Taken')
    plt.plot(graph_list_x, final_avg_list_y)
    plt.grid()
    plt.show()

if __name__ == '__main__':

    test()