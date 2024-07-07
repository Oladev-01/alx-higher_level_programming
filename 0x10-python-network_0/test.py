#!/usr/bin/python3
def find_peak(list):
    if list is None or len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    low, high = 0, len(list) - 1
    while low < high:
        mid = (low + high) // 2
        print(f"mid is {mid}\tlow is {low}\thigh is {high}")
        if list[mid] < list[mid + 1]:
            low = mid+1
            print(f"low was here and it is now {low}")

        else:
            high = mid
            print(f"high was here and it is {high}")
    return list[low]

if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

