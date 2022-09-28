n = int(input())
arr=[]

for x in range(0,n):
    a = int(input())
    arr.append(a)

for x in range(0,len(arr)):
  smallest = arr[x]
  for y in range(x+1,len(arr)):
    if(arr[x]>arr[y]):
      smallest = y
      arr[x], arr[smallest] = arr[smallest],arr[x]

print(arr)
