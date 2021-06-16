# 3.1. Create a list called years_list, starting with the year of your birth, and each year
# thereafter until the year of your fifth birthday.
years_list = [1997, 1998, 1999, 2000, 2001, 2002]
print(f"3.1. List of the first 6 years of my life: {years_list}\n")

# 3.2. In which year in years_list was your third birthday? Remember, you were 0
# years of age for your first year.
year_third_birthday = years_list[3]
print(f"3.2. Year of my third birthday: {year_third_birthday}\n")

# 3.3. In which year in years_list were you the oldest?
year_oldest = years_list[-1]
print(f"3.3. Year whe I was oldest: {year_oldest}\n")

# 3.4. Make a list called things with these three strings as elements: "mozzarella",
# "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]
print(f"3.4. List 'Things': {things}\n")

# 3.5. Capitalize the element in things that refers to a person and then print the list.
# Did it change the element in the list?
things[1] = things[1].capitalize()
print(f"3.5. List 'things' after cinderella was capitalized: {things}\n")

# 3.6. Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(f"3.6. List 'things after mozzarella was uppercased: {things}\n")

# 3.7. Delete the disease element from things, collect your Nobel Prize, and print the
# list.
things.remove(things[2])
print(f"3.7. List 'things' after salmonella was removed: {things}\n")

# 3.8. Create a list called surprise with the elements "Groucho", "Chico", and "Harpo".
suprise = ["Groucho", "Chico", "Harpo"]
print(f"3.8. New 'surprise' list: {suprise}\n")

# 3.9. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

suprise[-1] = suprise[-1][::-1].lower().capitalize()
print(f"3.9. Last element after being lowered, reversed and capitalized: {suprise[-1]}\n")

# 3.10. Make an English-to-French dictionary called e2f and print it. Here are your
# starter words: dog is chien, cat is chat, and walrus is morse.

e2f = {'dog': 'chien',
       'cat': 'chat',
       'walrus': 'morse'}
print(f"3.10. New dictionary 'e2f': {e2f}\n")

# 3.11. Using your three-word dictionary e2f, print the French word for walrus
print(f"3.11. French word for walrus: {e2f['walrus']}\n")

# 3.12. Make a French-to-English dictionary called f2e from e2f. Use the items
# method.
# initializez f2e ca si dictionary
f2e = {}
# numele key-ului din f2e va fi valoarea din e2f si valoarea lui va fi numele key-ului din e2f
for english, french in e2f.items():
    f2e[french] = english

print(f"3.12. French-to-English dictionary called f2e from e2f: {f2e}\n")

# 3.13. Using f2e, print the English equivalent of the French word chien.
print(f"3.13. The english equivalent of the french word chien: {f2e['chien']}\n")

# 3.14. Make and print a set of English words from the keys in e2f.
set_e2f = set(e2f)
print(f"3.14. Set 'set_e2f' from 'e2f' dictionary: {set_e2f}\n")

# 3.15. Make a multilevel dictionary called life. Use these strings for the topmost keys:
# 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictio‐
# nary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list
# of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys
# refer to empty dictionaries.
life={'animals': {'cats': ['Henry', 'Grumpy', 'Lucy'],
                  'octopi': {},
                  'emus': {}
                  },
      'plants': {},
      'other': {}
      }

# 3.16. Print the top-level keys of life.
# Could've used print( list( life.keys() ) )
print("3.16. Top-level keys in 'life' dictionary:")
for key, _ in life.items():
    print(key)
print()

# 3.17. Print the keys for life['animals'].
print("3.17. Keys for life[animals]: ")
for key, _ in life['animals'].items():
    print(key)
print()

# 3.18. Print the values for life['animals']['cats'].
print(f"3.18. Values for life['animals']['cats']: {life['animals']['cats']}")


