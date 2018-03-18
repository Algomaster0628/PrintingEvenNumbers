numbers = [] #stores numbers in list
for values in range(0,1000):#checks for divisibility by 3 and 5
  if values % 3 == 0 or values % 5 == 0 :
    values=int(values)
    numbers.append(values)
print(numbers)
print(sum(numbers)) #prints the sum of numbers
