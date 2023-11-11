# Python program to merge two sorted arrays/
def mergeArrays(arr1, arr2, n1, n2, arr3):
    i = 0
    j = 0
    k = 0

    # traverse the arr1 and insert its element in arr3
    
    while(i < n1+n2):
        if j < n1 and arr1[j] <= arr2[k] : 
            arr3[i] = arr1[j]
            j += 1
        elif k < n2 and arr2[k] < arr1[j] :
            arr3[i] = arr2[k]
            k += 1
        i+=1


# Driver code
if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    n1 = len(arr1)
    print("Array n1 : ")
    for i in range(n1) :
            print(arr1[i], end=" ")

    print()
    arr2 = [2, 4, 6, 8]
    n2 = len(arr2)
    print("Array n2 : ")
    for i in range(n2) :
            print(arr2[i], end=" ")

    print()
    arr3 = [0 for i in range(n1+n2)]
    mergeArrays(arr1, arr2, n1, n2, arr3)

    print("Array after merging")
    for i in range(n1 + n2):
        print(arr3[i], end=" ")

# This code is contributed by Tapesh(tapeshdua420)
