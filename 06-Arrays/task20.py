ar = [12, 6, 4, 9, 10]
def star(ar):
  for i in range(len(ar)):
      k = ar[i]
      print("")
      for j in range(k):
          print("*", end=" ")
          i+=1
  print("")
print(star(ar))


