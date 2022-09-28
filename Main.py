for x in range(0,len(arr)):
  smallest = arr[x]
  for y in range(x+1,len(arr)):
    if(arr[x]>arr[y]):
      smallest = arr[y]
  arr[x], arr[smallest] = arr[smallest],arr[x]
