SORU 1

https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma
With List Comprehension Solution:
Write a program that returns a list of all the numbers from 1 to an integer argument. But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.
fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"] 

CEVAP 1

number = int(input("give me a number: "))
liste = list(range(1,number+1))
n=[]
for i in liste:
    if i % 3 ==0 and i % 5 == 0:
        n.append("FizzBuzz")
    elif i % 3 == 0:
        n.append("Fizz")
    elif i % 5 == 0:
        n.append("Buzz")
    else:
        n.append(i)
print(n)

CEVAP 2
def fizz_buzz(number):
    liste = list(range(1,number+1))
    n=[]
    for i in liste:
        if i % 3 ==0 and i % 5 == 0:
            n.append("FizzBuzz")
        elif i % 3 == 0:
            n.append("Fizz")
        elif i % 5 == 0:
            n.append("Buzz")
        else:
            n.append(i)
    print(n)

fizz_buzz(15)

CEVAP 3
def fiz_buzz(maximum):
    lst = list(range(1, maximum+1))
    print(lst)
    for i in lst:
        if i % 15 == 0:
            lst[lst.index(i)] = "FizzBuzz"
            elif i % 5 == 0:
                lst[lst.index(i)] = "Buzz"
            elif i % 3 == 0:
                lst[lst.index(i)] = "Fizz"
    return lst
print(fizz_buzz(4))

CEVAP 4
def fizz_buzz(num):
    return ["fizzBuzz" if not n%15 else
        "Buzz" if not n%5 else
        "Fizz" if not n%3 ense
        n for n in range(1, num+1)]
print(fizz_buzz(4))


SORU 2

https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma
An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
is_isogram("Algorism") ➞ True
is_isogram("PasSword") ➞ False
# Not case sensitive.
is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.

CEVAP 1
word = list(input("give me a word: ").upper())
for i in word:
    if word.count(i)>1:
        print(False)
        break
    else:
        print(True)
        break
CEVAP 2
def tekrareden(number):
    word = list((number).upper())
    for i in word:
        if word.count(i)>1:
            print(False)
            break
        else:
            print(True)
            break
tekrareden("ALİ")

CEVAP 3
def is_isogram(txt):
    return len(txt) == len(set(txt.lower()))
print(is_isogram("consecutive"))

CEVAP 4
def is_isogram(txt):
    t=[]
    for i in txt.lower():
        if i not in t:
            t.append(i)
    return t == txt.lower()
print(is_isogram("consecutive"))

SORU 3

https://edabit.com/challenge/fmQ9QvPBWL7N9hSkq
Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.
unstretch("ppoeemm") ➞ "poem"
unstretch("wiiiinnnnd") ➞ "wind"
unstretch("ttiiitllleeee") ➞ "title"
unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"
Final strings won't include words with double letters (e.g. "passing", "lottery").

CEVAP 1
def unstretch(word):
    c = word[0]
    for i in range(1, len(word)):
        if word[i] != c[-1]:
            c += word[i]
    return c
print(unstretch("ttiiiitllllleeeee"))


SORU 4

https://edabit.com/challenge/6CGomPbu3dK536PH2
Create a function that takes in a list and returns a list of the accumulating sum.
accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
# [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
accumulating_list([1, 5, 7]) ➞ [1, 6, 13]
accumulating_list([1, 0, 1, 0, 1]) ➞ [1, 1, 2, 2, 3]
accumulating_list([]) ➞ []
An empty list input [] should return an empty list [].

CEVAP 1
yeni_liste = []
count = 0
liste = input("İstediğiniz kadar sayıyı aralarına boşluk bırakarak giriniz: ").split(" ")
for i in liste:
    sayi=int(i)
    yeni_liste.append(sayi+count)
    count += sayi
print(yeni_liste)

CEVAP 2

def toplamlar(liste):
    count = 0
    yeni_liste=[]
    for i in liste.split():
        sayi=int(i)
        yeni_liste.append(sayi+count)
        count += sayi
    return yeni_liste
print(toplamlar(input("give a number")))

CEVAP 3
def accumulating_list(lst):
    k=0
    t=[]
    for i in range(len(lst)):
        k=k+lst[i]
        t.append(k)
    return t
print(accumulating_list([1,2,3,4,]))


SORU 5

Write a Python code to sort the list at below without using .sort() method of list. elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11] 
Expected output: [2, 11, 12, 45, 77, 99, 333, 999, 8982]


CEVAP 1
def sıralama(number):
  
  for i in range(0,len(number)):
      for j in range(0,len(number)-1):
          if number[j] > number[j+1] :
              number[j],number[j+1]=number[j+1],number[j]
          else:
              continue
  print(number)
list=[999, 333, 2, 8982, 12, 45, 77, 99, 11]
sıralama(list)


CEVAP 2
list_=[999, 333, 2, 8982, 12, 45, 77, 99, 11]
new_list = []

while list_:
    min_element = list_[0]
    for i in list_:
        if i < min_element:
            min_element = 1
    new_list.append(min_element)
    list_.remove(min_element)
print(new_list)


SORU 6

https://edabit.com/challenge/6vSZmN66xhMRDX8YT

Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
Notes
The sublists should be returned in the order of each element's first appearance in the given list.


CEVAP 1
def advanced_sort(lst):
    lst_nw, set_nw = [] , set()
    for i in lst:
        if i not in set_nw:
            lst_nw.append([i for x in range(lst.count(i))])
            set_nw.add(i)
    return lst_nw


CEVAP 2
def advanced_sort(lst):
    	new_lst = []
	for i in lst:
		if [i]*lst.count(i) not in new_lst:
			 new_lst.append([i]*lst.count(i))
	return (new_lst)


SORU 7

https://edabit.com/challenge/YN33GEpLQqa5imcFx

The goal of this challenge is to return Pascal's triangle up to number 29. Pascal's triangle is the sum of the two upper corners.
    1
   1 1
  1 2 1
 1 3 3 1

# There will always be the 1 in the first
# place and the row in the second.
Create a function that returns a row from Pascal's triangle. To find the row and column you can use n!/(k!*(n-k)!) where n is the row down and k is the column.
pascals_triangle(1) ➞ "1 1"
pascals_triangle(4) ➞ "1 4 6 4 1"
pascals_triangle(6) ➞ "1 6 15 20 15 6 1"
pascals_triangle(8) ➞ "1 8 28 56 70 56 28 8 1"

CEVAP 

def pascals_triangle(n):
    lst = []
    for i in range(0, n+1):
        if i ==0 or i == 1:
            lst.append(1)
        else:
            n_lst = lst.copy()
            for j in range(len(n_lst)-1):
                lst[j+1] = n_lst[j] + n_lst[j+1]
            lst.append(1)
    return " ".join(str(item) for item in lst)

