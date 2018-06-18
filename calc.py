num = int(input("Please enter number of things: "))
avg = 0
for i in range (num):
  score = int(input("Enter the stats here: "))
  avg = (avg + score)
print("Your average is: ", avg/num)
