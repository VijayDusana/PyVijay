z=int(input("Enter The Number To Check"))
flag = False



if z > 1:
   for l in range(2,z):
       reminder=z%l
       if reminder == 0:
          flag = True
          break

if flag == True:
    print(z,"is not a Prime Number")
else:
    print(z,"is a prime number")
