################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")
print(sum(dct.values()))

pass

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")
min = min(dct.values())
for element in dct.items():
    if element[1]==min :
      print(element[0]) 
pass

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")
dct_square={}
for element in dct.items() :
   dct_square[element[0]]=element[1]**2 
print(dct_square)
pass

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")
for i in dct.keys():
   if (dct[i]%2==0):
      print(i)
pass

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")
dct_inverse={}
for element in dct.items() :
   dct_inverse[element[1]]=element[0] 
print(dct_inverse)
pass
pass

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

dct_count={}
for char in s : 
  if char in dct_count:
    dct_count[char]+=1
  else : 
     dct_count[char]=1   
print(dct_count)
pass

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")
lst_word=[]
for char in responses:
   lst_word.append(responses_mapping.get(char, '?'))
print(lst_word)
pass

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")
dct_1={'a':1, 'b':2}
dct_2={'c':2, 'd':4}
dct_3=dct_1|dct_2
print(dct_3)
pass

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""
dct_animals={'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_dct={key:dct_animals[key] for key in sorted(dct_animals)}
print(sorted_dct)
print("Exercise 4.9")

pass

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")
sorted_dct2=dict(sorted(dct_animals.items(), key=lambda item:item[1]))
print(sorted_dct2)
pass

print("---")