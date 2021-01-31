#**Number of Times Sorted array is rotated**
def inputArr():
    while True:
        try:
            list_arr=[int(x) for x in input('Enter an integer Array: ').split(" ")]
            print(list_arr)
            return list_arr
        except:
            print('Invalid input')

list_arr=inputArr()

def rotation():
    start=0
    size=len(list_arr)
    end=(size-1)
    while start<=end:
        mid=(start+end)//2
        #print(mid)
        prev=(mid+size-1)%size #Doing this to avoid negatives values
        next=(mid+1)%size
        #print(f"Previous is: {prev} and next is: {next}")
        if list_arr[mid]<list_arr[next] and list_arr[mid]<list_arr[prev]:
            #print("mid is",mid)
            return mid
        elif list_arr[start]<=list_arr[mid]:
            #print("Smaller")
            start=mid+1
        elif list_arr[end]<=list_arr[mid]:
            #print("bigger")
            end=mid-1


result=rotation()
print(f"The Array is rotated {result} times")