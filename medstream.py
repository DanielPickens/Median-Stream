from bisect import insort_right

def findMedian(arr):
    """Using bisect (sorted list)"""
    sorted_list = [arr[0]]
    output = [arr[0]]
    for i, v in enumerate(arr[1:], start=2):
        insort_right(sorted_list, v)
        index = i // 2
        output.append(
            sorted_list[index]
            if i % 2
            else sum(sorted_list[index - 1 : index + 1]) // 2
        )
    return output
