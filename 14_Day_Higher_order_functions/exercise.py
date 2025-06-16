## 💻 Exercises: Day 14
"""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Exercises: Level 1

1. Explain the difference between map, filter, and reduce.
- These are built-in high-order functions, 
map(fn, iterable): applies fn individually to each item in iterable, returning a new iterable of the same length
filter(fn, iterable): applies fn individually to each item in iterable, returns a new iterable that is made of those items for which
fn(item) is True.
reduce(fn, iterable): aggregates the iterable into a single item, by applying fn cumulatively
2. Explain the difference between higher order function, closure and decorator
High order function: Function taking/returning other functions
Closure: The ability of the nested function the outer scope of the enclosing function
Decorator: Adding a new design pattern to a function without modifying its original structure
closure is the ability the access variables outside its scope. It happens in python when a nested function is encapsulated
3. Define a call function before map, filter or reduce, see examples.
4. Use for loop to print each country in the countries list.
5. Use for to print each name in the names list.
6. Use for to print each number in the numbers list.

### Exercises: Level 2

1. Use map to create a new list by changing each country to uppercase in the countries list
1. Use map to create a new list by changing each number to its square in the numbers list
1. Use map to change each name to uppercase in the names list
1. Use filter to filter out countries containing 'land'.
1. Use filter to filter out countries having exactly six characters.
1. Use filter to filter out countries containing six letters and more in the country list.
1. Use filter to filter out countries starting with an 'E'
1. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
1. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
1. Use reduce to sum all the numbers in the numbers list.
1. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
1. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
1. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
2. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
1. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

### Exercises: Level 3

1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
   - Sort countries by name, by capital, by population
   - Sort out the ten most spoken languages by location.
   - Sort out the ten most populated countries.
"""
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use map to create a new list by changing each country to uppercase in the countries list
def exercise_1():
    def upper_case(word):
        return word.upper()

    countries_uppercased = map(upper_case, countries)
    print(list(countries_uppercased))

#Use map to create a new list by changing each number to its square in the numbers list
def exercise_2():
    def square(number):
        return number * number    
    squared_numbers = map(square, numbers)
    print(list(squared_numbers))

#Use map to change each name to uppercase in the names list
def exercise_3():
    def upper_case(word):
        return word.upper()
    names_uppercased = map(upper_case, names)
    print(list(names_uppercased))

#Use filter to filter out countries containing 'land'.
def exercise_4():
    def noland(country):
        if "land" not in country:
            return True
        return False
    countries_without_land = filter(noland, countries)
    print(list(countries_without_land))

#Use filter to filter out countries having exactly six characters.
def exercise_5():
    def six_char(country):
        if len(country) != 6:
            return True
        return False
    countries_no_six_char = filter(six_char, countries)
    print(list(countries_no_six_char))

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def exercise_6():
    def is_string(item):
        if type(item) == type("string"):
            return True
        return False
    def get_string_lists(l):
        string_list = filter(is_string, l)
        print(list(string_list))

    test = ["sss", "aaa", 1.11, 2, 0b1000]
    get_string_lists(test)
    
#Use reduce to sum all the numbers in the numbers list.
def exercise_7():
    def add_numbers(num1, num2):
        return num1 + num2
    
    ans = reduce(add_numbers, numbers)
    return ans

# Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def exercise_8():
    def concatenate_string(s1, s2):
        return s1 + ', ' + s2
    
    concatenated_countries = reduce(concatenate_string, countries[1:], countries[0])
    before_last, last = concatenated_countries.rsplit(", ", 1)
    print(f"{before_last}, and {last} are north European countries")
    
# Declare a function called categorize_countries that returns a list of countries with some common pattern 
# (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) 
# in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries as all_countries
def exercise_9():
    def categorize_countries(pattern : str) -> list:
        return [
            country
            for country in all_countries
            if pattern.lower() in country.lower()
        ]
    patterns = ['land', 'island', 'stan']
    for pat in patterns:
        matching = categorize_countries(pat)
        print(f'Pattern {pat}: {matching}')

#Create a function returning a dictionary, 
#where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def exercise_10():
    def count_countries_by_initial() -> dict[str, int]:
        count = {}
        for c in all_countries:
            if c[0] not in count:
                count[c[0]] = 1
            else:
                count[c[0]] += 1
        return count
    count = count_countries_by_initial()
    for key, value in count.items():
        print(f'The number of countries starting with the letter {key} is {value}')

# Declare a get_first_ten_countries function 
# it returns a list of first ten countries from the countries.js list in the data folder.
def exercise_11():
    def get_first_ten_countries():
        return all_countries[:10]
    return get_first_ten_countries()

#1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#  - Sort countries by name, by capital, by population
#  - Sort out the ten most spoken languages by location.
#  - Sort out the ten most populated countries.
def exercise_12():
    print()
    
def main():
    print(exercise_11())

if __name__== "__main__":
    main()