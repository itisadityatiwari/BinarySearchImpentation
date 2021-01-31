#***Find the floor of an element in a rotated sorted array***
def findFloor(nums,key):
  start=0
  end=(len(nums)-1)
  res=-1
  while start<=end:
    mid=start+(end-start)//2
    if nums[mid]==key:
      return mid
    elif key > nums[mid]:
        res=mid
        start=mid+1
    elif key<nums[mid]:
        end =mid-1
  return res

findFloor([5,10,20,30,40],31) 