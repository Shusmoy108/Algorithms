#l=low, h=high, x=searchitem, k=jumpvariant
def linearsearch(arr,l,h,x):
    for i in range (l,h):
        if(arr[i]==x):
            return i
    return -1
def binarysearch(arr,l,h,x):
    m= int((h+l)/2)
    if(h<=l):
         return -1
    if(arr[m]==x):
        return m
    if(arr[m]>x):
        return binarysearch(arr,m-1,l,x)
    if(arr[m]<x):
        return binarysearch(arr,h,m+1,x)
   
def jumpsearch(arr,l,h,k,x):
    y= l+k
    if y>h:
        return linearsearch(arr,l,h,x)
    if arr[y]<x:
        return jumpsearch(arr,y,h,k,x)
    if(arr[y]>x):
        return linearsearch(arr,l,y,x)
    if(arr[y]==x):
        return y
    
def interpolationsearch(arr,lo,hi,x):
    y= lo + int( (x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo]))
    if(hi<lo):
         return -1
    if arr[y]<x:
        return interpolationsearch(arr,y+1,hi,x)
    if(arr[y]>x):
        return interpolationsearch(arr,lo,y-1,x)
    if(arr[y]==x):
        return y
def exponentialsearch(arr,lo,hi,x):
    y=1
    while(arr[y]<x and y<=hi):
        y=y*2;
    if(y>hi):
        return -1
    return binarysearch(arr,y/2,y,x)
    
arr =[10, 20, 30, 50,80,100, 120,130, 170,200]        
x = 120; 
n = len(arr); 
#result = linearsearch(arr, x)
result = exponentialsearch(arr,0,n-1,x)
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 

