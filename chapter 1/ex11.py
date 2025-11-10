year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

print(f"Original Tuple: {year}")
print("-" * 30)

print(f"Value at index -3: {year[-3]}")
print("-" * 30)

reversed_year_list = list(year)[::-1]
reversed_year_tuple = tuple(reversed_year_list)

print(f"Original tuple (after operations): {year}")
print(f"Reversed tuple: {reversed_year_tuple}")
print("-" * 30)

count_2009 = year.count(2009)
print(f"Number of times 2009 appears: {count_2009}")
print("-" * 30)

index_2018 = year.index(2018)
print(f"Index value of 2018: {index_2018}")
print("-" * 30)

length = len(year)
print(f"Length of the tuple: {length}")