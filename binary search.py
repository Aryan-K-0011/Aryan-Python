#binary search
def binary_search(arr,low,high,x):
    if high>=low:
        mid=(high+low)
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1
arr=[2,45,65,7,4]
x=5
result=binary_search(arr,0,len(arr)-1,x)
if result !=-1:
    print("Present",str(result))
else:
    print("Not present")
    
