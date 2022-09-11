# implementatioon of Quick short

def partation(mylist, low, high):
    i = low-1
    pivot = mylist[high]  # taking a pivot for compare i.e. rightmost
    for j in range(low, high):
        if mylist[j] <= pivot:
            i += 1
            # if vale is less than pivot it wiil remain at the same point
            #  and low pointer move forward
            mylist[i], mylist[j] = mylist[j], mylist[i]
            # if value is greater swipe with the high
        mylist[i+1], mylist[high] = mylist[high], mylist[i+1]
        # swap with the greater element
        return i+1


def quick_short(mylist, low, high):
    # taking pivot element and arranging smaller than pivot on left
    # greter than pivot on right
    if low < high:
        part = partation(mylist, low, high)
        # getting partition
        quick_short(mylist, low, part-1)
        # recursevly calling on the left part
        quick_short(mylist, part, high)
        # recursevly calling on the right part


if __name__ == '__main__':
    mylist = [2, 4, 9, 6,8, 5]
    print(f"Unshorted arry is {mylist}")
    # printing unshorted arry
    size= len(mylist)-1
    #as index startb from 0
    quick_short(mylist, 0,size)
    print(f"Shorted arry is {mylist}")

    
