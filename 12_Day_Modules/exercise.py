
import random 
import string

def random_user_id(length = 6):
    characters = string.ascii_letters+string.digits
    return "".join(random.choices(characters, k = length))

def user_id_gen_by_user():
    try:
        length, number = map(int, input("Insert the desired length and number of userID: ").split())
    except ValueError:
        print("Values not valid. Try again!")
    for i in range(number):
        print(random_user_id(length))

def rgb_color_gen():
    r, g, b = (random.randint(0,255) for i in range(3))
    return f"rgb({r}, {g}, {b})"

if __name__ == "__main__":
    print("🎲 Random RGB Color:", rgb_color_gen())

