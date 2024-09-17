def count(n):
  if n> 20:
   return
  print(n) 
  count(n+1)

count(0)


def factoral(n):
  if n ==1 :
    return 1
  else:
    return n * factoral(n-1)
print(factoral(10))