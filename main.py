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


# factorial(5) factor 5 * 24 >120
#factorial(4) factor 4 * 6 >24
#factorial(3) factor 3 * 2 >6
#factorial(2) factor 2 *1 >2
#factorial(1) factor 1 *1 >1