def firstoccur(list_arr,key):
  start=0
  size=len(list_arr)
  end=size-1
  ls=-1
  while start<=end:
    mid=(start+end)//2
    if key==list_arr[mid]:
      ls=mid
      end=mid-1
    elif key<list_arr[mid]:
      end=mid-1
    elif key>list_arr[mid]:
      start=mid+1
  return ls

def lastoccur(list_arr,key):
  start=0
  end=(len(list_arr)-1)
  fs=-1
  while start<=end:
    mid=(start+end)//2
    if key==list_arr[mid]:
      fs=mid
      start=mid+1
    elif key<list_arr[mid]:
      end=mid-1
    elif key>list_arr[mid]:
      start=mid+1
  return fs

def count(result_First,result_Last):
  count_occur=result_Last-result_First+1
  return count_occur

while True:
  try:
    list_arr= [int(x) for x in input("Please enter your array: ").split(" ")] 
    print("Your input array is: ", list_arr)
    key=int(input("Please enter a value to search: "))
    print("your input is",key)
    break
  except:
    print("Please Enter a valid Input")
#print("while loop existed")
result_First=firstoccur(list_arr,key)
if result_First !=-1:
  print(f'The First occurence index for the number:{key} is at "{result_First}"')
else:
  print(f'Number:"{key}" is not present in the array')

result_Last=lastoccur(list_arr,key)
if result_Last!=-1:
  print(f'The Last occurence index for the number:{key} is at "{result_Last}"')
else:
  print(f'Number:"{key}" is not present in the array')

print(f'The count of the occurences of the number: {key} is:"{count(result_First,result_Last)}"')