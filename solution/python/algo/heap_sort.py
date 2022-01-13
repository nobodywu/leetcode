'''
代码来源：
https://www.runoob.com/python3/python-heap-sort.html

关于为什么最后一个非叶子节点是 n//2 -1
./heap_sort.md
'''


def heapify(arr, size, i):
    largest = i
    l = 2 * i + 1     # 左子节点序号 2 * i + 1
    r = 2 * i + 2     # 右子节点序号 2 * i + 2

    if l < size and arr[i] < arr[l]:
        # 左子节点存在，并且大于当前节点
        largest = l

    if r < size and arr[largest] < arr[r]:
        # 右子节点存在，并且大于当前节点
        largest = r

    if largest != i:
        # 当前节点比子节点小，交换后需要重新调整
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def heapSort(arr):
    size = len(arr)

    # 建一个大顶堆，从最后一个非叶子节点（size//2-1）开始
    for i in range(size//2-1, -1, -1):
        heapify(arr, size, i)

    # 交换根节点和末尾节点，并重新调整堆
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        # 交换后的size为i，最大的放在了最后边，因此size逐渐变小，被放在后边的不参与heapify
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print(arr)

    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # 大顶堆为[6, 5, 5, 3, 2, 4, 3, 2, 1]，不是从大到小的顺序
    heapSort(arr)
    print(arr)
