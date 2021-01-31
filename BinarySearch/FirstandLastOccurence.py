#For First Occurence First And Last Occurence using Binary Search*
def binary(list_arr,number):
    size=len(list_arr)
    start = 0
    end = size-1
    res=-1
    #ls=-1
    while start<=end:
        mid = start+((end-start)//2)
        #to avoid int overflow we can use mid=start+(end-start//2)
        print('mid is: ',mid)
        #print(list_arr[mid])
        if number == list_arr[mid]:
          res=mid
          end=mid-1 #For Last occurence change this line to start=mid+1
        elif number < list_arr[mid]:
            end = mid-1
            #print('end',end)
        else:
            start=mid+1
    return res
while True:
  try:
    list_arr= [int(x) for x in input("Please enter your array: ").split(" ")] 
    print("Your input array is: ", list_arr)
    number=int(input("Please enter a value to search: "))
    print("your input is",number)
    break
  except:
    print("Invalid Input")
#print("while loop existed")
result=binary(list_arr,number)
if result !=-1:
  print(f'The index for the number:"{number}" is at {result}')
else:
  print(f'Number:"{number}" is not present in the array')
