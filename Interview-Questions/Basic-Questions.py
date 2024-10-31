# --------------------------------------------------------------------------------------------------------------------------------------#
# General Questions
# Level-1 Questions
# problem 1:
i = 1
while i <= 10:
    print(i)
    i +=1

# problem 2:
n = int(input("enter the number :" ))
i = 0
while i <= n:
    print(i)
    i= i+1

# problem 3:
n = int(input("enter a number starting point: "))
a = int(input("enter a number stoping point: "))
while n >=a:
    print(n)
    n -= 1

# problem 4:
number = 3
sum_of_num = 0
i = 0
while i<= number:
    sum_of_num +=i
    i +=1
print(sum_of_num)

# problem 5:
number = 3
sum_of_num = 0
i = 0
while i<= number:
    a = i*i
    sum_of_num += a
    i +=1
print(sum_of_num)

# problem 6:
num_1 = int(input("enter the number: "))
i = 0
while i <= num_1:
    if i % 2 == 0:
        print(i)
    i += 1

# problem 7:
num_1 = int(input("enter the number: "))
sum_of_even, i = 0,0
while i <= num_1:
    if i % 2 == 0:
        print(i)
        sum_of_even +=i
    i += 1
print(f"sum of the even numbers are: {sum_of_even}")

# problem 8:
num_1 = int(input("enter the number: "))
count,sum_of_even, i = 0,0,0
while count < num_1:
    if i % 2 == 0:
        print(i)
        sum_of_even +=i
        count += 1
    i += 1
print(f"sum of the even numbers are: {sum_of_even}")

# Level-2
# problem 9 Sum of digits of a given number:
num_1 = list(input("enter the number: "))
i = 0
sum_1 =0
for i in range(len(num_1)):
    sum_1 += int(num_1[i])
print(sum_1)

# OR
# problem 9 Sum of digits of a given number:
num_1 = input("enter the number: ")
sum_1 =0
for i in range(len(num_1)):
    sum_1 = sum_1 +int(num_1) % 10
    num_1 = int(num_1)// 10
print(sum_1)

# problem 10 Sum of square of digits of a given number:
num_1 = list(input("enter the number: "))
i = 0
sum_1 =0
for i in range(len(num_1)):
    sum_1 += int(num_1[i]) * int(num_1[i])
print(sum_1)

# OR
# problem 9 Sum of digits of a given number:
num_1 = input("enter the number: ")
sum_1 =0
for i in range(len(num_1)):
    digit_1 = int(num_1) % 10
    sum_1 = sum_1 +(digit_1*digit_1)
    num_1 = int(num_1)// 10
print(sum_1)

# problem 11 a given number is armstrong or not:
num_1 = int(input("enter the no for armstrong or not?"))
original_no = num_1
i = 0
a = 0
armstrong_check = 0
while num_1>0:
    digit_1 = num_1 % 10
    cube_ofnum = digit_1**3
    armstrong_check += cube_ofnum
    num_1 = num_1//10
if armstrong_check == original_no:
    print("yes")
else:
    print("no")

# problem 12 a product of given num:
num_1 = 123
product = 1
while num_1 > 0:
    Digit_ = int(num_1) % 10
    product = product * Digit_
    num_1 = int(num_1) // 10
print(product)

# problem 13 sum of even and product of odd:
num_1 =  int(input("enter the no "))
sum_, prod_ = 0,1
while num_1>0:
    digit_ = num_1 % 10
    if digit_ % 2 == 0:
        sum_ += digit_
    else:
        prod_ *= digit_
    num_1 = num_1 // 10
print(f"sum : {sum_} and product: {prod_}")

# problem 13 reverse a number:
num_1 =  int(input("enter the no "))
while num_1>0:
    digit_ = num_1%10
    print(digit_, end='')
    num_1 = num_1//10

# problem 14 reverse a string:
string_1 =  input("enter the no ")
index = len(string_1)-1
reverse_ = ""
while index>=0:
    reverse_ += string_1[index]
    index -=1
print(reverse_)

# problem 15 palindrome a number:
num_1 =  int(input("enter the no "))
number_1=num_1
rev = 0
while num_1 > 0:
    digit_ = num_1 %10
    rev = rev*10 + digit_
    num_1 = num_1//10
if rev == number_1:
    print("yes")
else:
    print("no")
# OR 
string_1 = "tenet"
index = len(string_1) - 1
reverse =""
while index>=0:
    reverse += string_1[index]
    index -=1
if reverse == string_1:
    print("yes")
else:
    print("no")

# problem 16 prime number:
num_1 =  int(input("enter the no "))
i = 1
count = 0
while i <=num_1:
    if num_1%i==0:
       count += 1
    i +=1
if count == 2:
    print(f"{num_1} is prime no")

# problem 17 factorial of number:
num_1 = int(input("Enter the number: "))
i = 0
factorial_ = 1
while i<num_1:
    digit_ = num_1 -i
    factorial_ *= digit_
    i +=1
if num_1 == 0:
    print(1)
else:
    print(factorial_)

# problem 18 fibonacci series:
num_1 = int(input("Enter the number"))
a, b, c = 0,1,0
while c <= num_1:
    print(c)
    a = b
    b = c
    c = a+b

# problem 18 sum of elements of a list:
input_number = input("Enter an integer: ")
digit_list = list(input_number)
sum_of_list = 0
for i in digit_list:
    sum_of_list += int(i)
print("Sum of numbers:", sum_of_list)

# problem 18 sum of elements of a list:
input_number = list(input("Enter an integer: "))
odd_of_list = 0
even_of_list = 0
for i in input_number:
    if int(i) % 2 == 0:
        even_of_list +=1 
    else:
        odd_of_list +=1
print(even_of_list)
print(odd_of_list)

# problem 19 frequency of elements in a list:
input_number = list(input("Enter an integer: "))
element_count = {}
for element in input_number:
    if element in element_count:
        element_count[element] +=1
    else:
        element_count[element] = 1
for element in element_count:
    count = element_count[element]
    print(f"{element}: {count}")

# problem 19 reverse a list:
input_number = list(input("Enter an integer: "))
reverse_list = []
index = len(input_number)-1
while index >= 0:
    reverse_list.append(input_number[index])
    index -=1
print(reverse_list)

# problem 20 inserting at a list:
input_list = list(input("Enter an integer: "))
index_to_insert= int(input("index"))
value_= input("value")
index_1 = 0
new_list = []
while index_1 < len(input_list):
    if index_1 == index_to_insert:
        new_list.append(value_)
    new_list.append(input_list[index_1])
    index_1 +=1
print(new_list)




# --------------------------------------------------------------------------------------------------------------------------------------#
# Course Questions
# # problem 1:
# Minimum Number
number= list((input("enter")))
target = 3
i = 0
minimum = int(number[0])
for i in range(len(number)-1):
    if int(number[i])<minimum:
        minimum = int(number[i])
    i +=1
print(minimum)

# # problem 2:
# Minimum Number in 2d array
number= [
    [2,8,3],
    [3,4,5],
    [6,7,8]
]
minimum = number[0][0]
for i in number:
    for j in i:
        if j <minimum:
            minimum = j
print(minimum)

# # problem 3:
# Count even number of digits
number= [1,22,333,4444,55555,666666]
count_ofintegers = 0
for i in number:
    count = 0
    while i>0:
        i = i//10
        count +=1
    if count%2==0:
        count_ofintegers += 1
print(count_ofintegers)
# # or
strings= ['a','bb','ccc','dddd','eeeee','ffffff']
count_ofintegers = 0
for i in strings:
    length = len(i)
    if length%2==0:
        count_ofintegers += 1
print(count_ofintegers)

# # problem 4:
# Reverse of a number
number = 123456789
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print(reversed_number)
# # or
string = "abcdefghi"
reversed_string = ""
index = len(string) - 1  # Start from the last character
while index >= 0:
    reversed_string += string[index]
    index -= 1
print(reversed_string)


# More General Questions
# --------------------------------------------------------------------------------------------------------------------------------------#
# Problem 1:
num_1, num_2 ,num_3 = input("Gave me 3 numbers: ").split(",")
average = (int(num_1)+int(num_2)+int(num_3))/3  
print(average)

# Problem 2:
name = input("enter your name : ")
print(name[::-1])

# Problem 3:
name, character = input("Enter name and character: ").split(",")
print(f"length of the character is {len(name)}")
print(f"Character Count is : {name.lower().count(character.lower())}")

# Problem 4:
import random
b = random.randint(0,9)
print(b)
a = int(input("give me a number:"))
if a == b:
    print("you won")
if a > b:
    print("too high")
else:
    print("too low")

# Problem 5:
name = input("name:")
age = int(input("Age:"))
if name[0].lower() == "a" and age > 10:
    print("you can watch Coco Movie")
else:
    print("sorry, you cannot watch Coco")

# Problem 6:
number = int(input("Enter a number for sum: :"))
i = 1
total = 0 
while i <=number: 
    total= total + i
    i = i+1
print(total)

# problem 7:
number = input("Enter a Number: ")
total = 0
i = 0
while i <len(number):
    total = total + int(number[i])
    i = i + 1
print(total)

# Problem 8:
name = input("Enter your name :")
i = 0
temp = ""
while i < len(name):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp = name[i]
    i = i+1

# Problem 9:
# Problem 4 extension:
import random
b = random.randint(0,10)
guess_game = False
i = 0
while not guess_game:
    a = int(input("give me a number:"))
    if a == b:
        i = i+1
        print(f"you won, you guessed in {i} times")
        continue
    if a > b:
        i = i+1
        print("too high")
        continue
    if a < b :
        i = i+1
        print("too low")
        continue

# # problem 10:
def is_even(x):
    return x%2==0

# problem 11:
def Greater(x,y):
    if x>y:
        return x 
    return y
a,b = input("enter: ").split(" ")
print(Greater(a,b))

# problem 12:
def Greater(x,y,z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return x 
    return z
a,b,c = input("enter: ").split(" ")
print(Greater(a,b,c))

# Problem 13:
def is_palindrome(string):
    new_string = ""
    count = len(string)
    while count>0:
            new_string = new_string + string[count - 1]
            count = count - 1
    return string == new_string
name = input("enter the name:")
print(is_palindrome(name))

# Problem 14:
def Fibonacci_series(num):
    a,b = 0,1  
    i = 1
    print(a,end = " ")
    print(b,end = " ")
    while i <= int(num)-2:
        c = a+b
        print(c,end = " ")
        a = b
        b = c
        i += 1
x= input("Enter a number: ")
Fibonacci_series(x)


# Problem 15:
def square_list(given_list):
  square_list1 = []
  for i in given_list:
    square_list1.append(int(i) * int(i))
  return square_list1
user_input_list= list(input("enter the list :").split(" "))
print(square_list(user_input_list))


# Problem 16:
def reverse_list(given_list):
  reverse_list1 = []
  for i in range(len(given_list)):
    a = given_list.pop()
    reverse_list1.append(a)
  return reverse_list1
user_input_list= list(input("enter the list :"))
print(reverse_list(user_input_list))


# Problem 17:
def reverse_list(given_list):
  reverse_list1 = []
  for i in given_list:
    reverse_list1.append(i[::-1])
  return reverse_list1
user_input_list= list(input("enter the list :").split(","))
print(reverse_list(user_input_list))


# Problem 18:
def odd_even_list(given_list):
  even_list = []
  odd_list = []
  combined_list = []
  for i in given_list:
    if int(i)%2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)  
  combined_list.append(odd_list)
  combined_list.append(even_list)
  return combined_list
user_input_list= list(input("enter the list :").split(","))
print(odd_even_list(user_input_list))


# Problem 19:
def Filter_same_elements(given_list_1, given_list_2):
  same_list = []
  for a in given_list_1:
    for b in given_list_2:
      if b == a:
        same_list.append(a)
  return same_list
user_input_list_1= list(input("enter the list :").split(","))
user_input_list_2= list(input("enter the list :").split(","))
print(Filter_same_elements(user_input_list_1, user_input_list_2))


# Problem 20:
def cubeFinder(num):
    i, CubeDic = 1,{}
    while i <= num:
        CubeDic[i] = i**3
        i+=1
    print(CubeDic)
User_num = int(input("Enter the Number: "))
cubeFinder(User_num)


# Word Counter:
def CharCount(s):
    CounterofChar = {}
    for c in s:
        CounterofChar[c] = s.count(c)
    return CounterofChar
String_1 = input("Enter: ")
print(CharCount(String_1))

# Prime Numbers
# This one has less comparisons
num_1 = int(input("Enter the Number: "))
i = 1
factors = 0
while i <=(num_1**0.5):
    if num_1 % i == 0:
       factors += 1
    i += 1
if factors>1:
    print("Not Prime")
else:
    print("Prime")
    
# Count Digits:
num = 12345679
digit = 0
count = 0
while num >0:
    digit = num%10
    num = num // 10
    count+=1
print(count)

#  Reverse a number:
num =  1234567
reversednum, digit,  = 0,0
while(num>0):
    digit = num%10
    reversednum = reversednum * 10 + digit
    print("digit",digit)
    num = num // 10
print("reversednum",reversednum)

# check palindrome:
stringOne = "122222222221"
reversedString = ""
lengthOfstring = len(stringOne)
while lengthOfstring>0:
    reversedString += stringOne[lengthOfstring-1]
    lengthOfstring -= 1
if(stringOne == reversedString):
    print(reversedString)

# all divisors:
num = 1234567
i,counter = 1,1
while i <= num:
    if num % i == 0:
        counter +=1
        print("divisor",i)
    i += 1
print(counter)

# prime_or_not:
num = 1234567
i,counter = 1,1
while i <= num:
    if num % i == 0:
        counter +=1
        print("divisor",i)
    i += 1
print(counter)

# frequency of elements:
arrayOne = ["2","2","3","3","3","7","7","7","7","11","12","11","11","11","11","11","11","11","11","11"]
hashmap = {}
i,maxcount,lowcount,elementofmaxcount,elementoflowcount = 0,0,0,"",""
lengthOfarray = len(arrayOne)-1
while i<lengthOfarray:
    if arrayOne[i] in hashmap:
        hashmap[arrayOne[i]] +=1
    else:
        hashmap[arrayOne[i]] = 1
    i += 1
for arrayOne[i] in hashmap:
    count = hashmap[arrayOne[i]]
    if maxcount < count:
        maxcount = count
        elementofmaxcount = arrayOne[i]
    elif lowcount<count:
        lowcount = count
        elementoflowcount = arrayOne[i]
print(f"{elementofmaxcount}:{maxcount}\n{elementoflowcount}:{lowcount}")

# -----------------------------------------------------------------------------------------------
# Problem 1 Leetcode 217:
# Contains Duplicate 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Problem 3:
# is palindrome by two pointers:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        while l<r:
            while l < r and not self.alpnum(s[l]):
                l = l+1                
            while r>l and not self.alpnum(s[r]):
                r = r-1
            if s[l].lower() != s[r].lower():
                return False
            l , r = l+1, r-1
        return True
    def alpnum(self, c):
        return (ord("A") <= ord(c) <=ord("Z")or
        (ord("a") <= ord(c) <=ord("z"))or 
        (ord("0") <= ord(c) <=ord("9")))

# Problem 6:
# swiping the elements of an array
arr = [1,2,3,4,5]
i = 0
index1 = 0
index2 = 2
for i in arr:
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp 
print(arr)

# Problem 7:
# max elements of an array
arr = [1,2,3,4,5]
i = 0
max_element = 0
while i <len(arr):
    if max_element < arr[i]:
        max_element = arr[i]
    i +=1
print(max_element)

# Problem 8:
# reverse of an array
arr = [1,2,3,4,5]
left_pointer = 0
right_pointer = len(arr)-1
while left_pointer <= right_pointer:
    arr[left_pointer], arr[right_pointer] = arr[right_pointer],arr[left_pointer]
    left_pointer +=1
    right_pointer -=1
print(arr)

# Problem 9:
# Contains not Duplicate in a sorted array
arr = [1,1,2,2,3,4,4,5,5]
l, r = 0,1
while l < len(arr) and r < len(arr):
    if arr[l] != arr[r]:
        one_time = arr[l]
        print(one_time)
        break
    l= l + 2
    r= r + 2