def reverse(string):
    print(string)
    print(len(string))
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))

def sortf(str):
  k=str
  li = []
  x = len(k)
  for i in range (0,x):
    li.append(k[i])
  for i in range(0,x):
    for j in range(0,x):
        if li[i]<li[j]:
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
  j= " ".join(li)
  # for i in range(0,x):
  #   j+= li[i]

  return j  




# Python program to check whether two strings are  
# anagrams of each other  
  
# function to check whether two strings are anagram  
# of each other  
def areAnagram(str1, str2):  
    # Get lengths of both strings  
    n1 = len(str1)  
    n2 = len(str2)  
  
    # If lenght of both strings is not same, then  
    # they cannot be anagram  
    if n1 != n2:  
        return 0
  
    # Sort both strings  
    str1 = sortf(str1) 
    str2 = sortf(str2) 
  
    # Compare sorted strings  
    for i in range(0, n1):  
        if str1[i] != str2[i]:  
            return 0
  
    return 1
  
  
# Driver program to test the above function  
str1 = "test"
str2 = "tste"
# if areAnagram(str1, str2):  
#     print ("The two strings are anagram of each other") 
# else:  
#     print ("The two strings are not anagram of each other") 
  
# This code is contributed by Bhavya Jain  






# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   #print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       #print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1




var ="gg.f.fk"

i=0
temp=""
while i < len(var):
    if var[i] not in temp:
        temp+=var[i]
        # if var[i]=='.':
        #     print(f"{var[i]} :{var.count(var[i])}")
    i+=1


# def check(n):
#     dictd={}
#     for i in n:
#         if i in dictd:
#             dictd[i]+=1

#         else:
#             dictd[i]=1
    
#     return  dictd      

# print(check('vin.ay'))

# sotting string
k="laiopb"
li = []
x = len(k)
for i in range (0,x):
    li.append(k[i])

#print("List is : ",li)


for i in range(0,x):
    for j in range(0,x):
        if li[i]<li[j]:
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
j=""

for i in range(0,x):
    j+= li[i]

#print("After sorting String is : ",j)


#find the first non-repeating character in given string




def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

# print(first_non_repeating_character('abcdef'))
#print(first_non_repeating_character('abcabcdef'))
# print(first_non_repeating_character('aabbcc'))


# function to check string is  
# palindrome or not  
def isPalindrome(str): 
  
    # Run loop from 0 to len/2  
    for i in range(0, len(str)//2):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  
# main function 
s = "5624"
ans = isPalindrome(s) 
  
# if (ans): 
#     print("Yes") 
# else: 
#     print("No")


# find duplicate from strin


def Findduplicate(n):
  duplicate_char=[]
  for i in range(0,len(n)):
    
    for j in range(i+1,len(n)):
      if n[i]== n[j]  and n[i] not in duplicate_char:
        duplicate_char.append(n[i])


  return duplicate_char  


# print(Findduplicate('Great responsibility'))


