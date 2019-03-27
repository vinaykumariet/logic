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
    j = j+li[i]

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


print(Findduplicate('Great responsibility'))


