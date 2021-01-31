# Find an element in Nearly Sorted Array**
def isPresentNearlySorted(nums,key):
  start=0
  end=(len(nums)-1)
  while start<=end:
    mid=start+(end-start)//2
    if nums[mid]==key:
      return mid
    elif mid-1>0 and nums[mid-1]==key:
      return mid-1
    elif mid+1>=len(nums) and nums[mid+1]==key:
      return mid+1
    elif nums[mid]>key:
      end=mid-2
    else:
      start=mid+2
  return -1

isPresentNearlySorted([5,10,30,20,40],11)    