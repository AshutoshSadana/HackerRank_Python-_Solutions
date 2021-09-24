if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #making a list
    tarr=list(arr)
    #sorting the list to and getting the max element
    tarr.sort()
    max1 = tarr[-1]
    #reverse the sorted list
    tarr.reverse()
    #comparing with the next element to find second highest
    for i in tarr:
        if i!=max1:
            result = i
            print(result)
            break