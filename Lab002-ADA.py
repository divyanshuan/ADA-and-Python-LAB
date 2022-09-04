# Implement Merge Sort Algorithm with all the necessary functions.

def mergeSort(array):
    if len(array) > 1:
        #  T is the point where the array is divided into two subarrays
        T = len(array)//2
        Left = array[:T]
        Right= array[T:]
        # Sort the two halves
        mergeSort(Left)
        mergeSort(Right)

        i = j = k = 0

        ''' Until we reach either end of either Left or Right pick larger values among
            elements Left and Right and place them in the correct position at A[m..p] '''
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

        ''' When we run out of elements in either Left or Right then 
            pick up the remaining elements and put in A[m..p] '''
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    array = [9, 8, 22, 14, 19, 11, 5, 32, 52, 41]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)