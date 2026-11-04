# --- 1. Tests for Equality and Inequality with Strings ---
print("--- String Equality and Inequality ---")
language = "Python"

# Test 1: Equality (True)
print("Is language == 'Python'? I predict True.")
print(language == 'Python')

# Test 2: Equality (False)
print("\nIs language == 'Java'? I predict False.")
print(language == 'Java')

# Test 3: Inequality (True)
print("\nIs language != 'Java'? I predict True.")
print(language != 'Java')

# Test 4: Inequality (False)
print("\nIs language != 'Python'? I predict False.")
print(language != 'Python')


# --- 2. Tests Using the lower() Method ---
print("\n--- Tests Using the lower() Method ---")
name = "Ada Lovelace"

# Test 5: lower() equality (True)
print("Is name.lower() == 'ada lovelace'? I predict True.")
print(name.lower() == 'ada lovelace')

# Test 6: lower() equality (False)
print("\nIs name.lower() == 'grace hopper'? I predict False.")
print(name.lower() == 'grace hopper')


# --- 3. Numerical Tests ---
print("\n--- Numerical Tests ---")
age = 22

# Test 7: Equality (True)
print("Is age == 22? I predict True.")
print(age == 22)

# Test 8: Equality (False)
print("\nIs age == 25? I predict False.")
print(age == 25)

# Test 9: Inequality (True)
print("\nIs age != 18? I predict True.")
print(age != 18)

# Test 10: Inequality (False)
print("\nIs age != 22? I predict False.")
print(age != 22)

# Test 11: Greater than (True)
print("\nIs age > 18? I predict True.")
print(age > 18)

# Test 12: Greater than (False)
print("\nIs age > 30? I predict False.")
print(age > 30)

# Test 13: Less than (True)
print("\nIs age < 25? I predict True.")
print(age < 25)

# Test 14: Less than (False)
print("\nIs age < 15? I predict False.")
print(age < 15)

# Test 15: Greater than or equal to (True)
print("\nIs age >= 22? I predict True.")
print(age >= 22)

# Test 16: Greater than or equal to (False)
print("\nIs age >= 25? I predict False.")
print(age >= 25)

# Test 17: Less than or equal to (True)
print("\nIs age <= 22? I predict True.")
print(age <= 22)

# Test 18: Less than or equal to (False)
print("\nIs age <= 18? I predict False.")
print(age <= 18)


# --- 4. Tests Using 'and' and 'or' Keywords ---
print("\n--- Tests Using 'and' and 'or' ---")
score = 85
is_active = True

# Test 19: Using 'and' (True - both conditions are True)
print("Is score > 80 and is_active == True? I predict True.")
print(score > 80 and is_active == True)

# Test 20: Using 'and' (False - one condition is False)
print("\nIs score > 90 and is_active == True? I predict False.")
print(score > 90 and is_active == True)

# Test 21: Using 'or' (True - at least one condition is True)
print("\nIs score > 90 or is_active == True? I predict True.")
print(score > 90 or is_active == True)

# Test 22: Using 'or' (False - both conditions are False)
print("\nIs score > 95 or is_active == False? I predict False.")
print(score > 95 or is_active == False)


# --- 5. Test Whether an Item Is in a List ---
print("\n--- Test Whether an Item Is in a List ---")
toppings = ['mushrooms', 'onions', 'pineapple']

# Test 23: Item is in the list (True)
print("Is 'onions' in toppings? I predict True.")
print('onions' in toppings)

# Test 24: Item is in the list (False)
print("\nIs 'pepperoni' in toppings? I predict False.")
print('pepperoni' in toppings)


# --- 6. Test Whether an Item Is Not in a List ---
print("\n--- Test Whether an Item Is Not in a List ---")

# Test 25: Item is not in the list (True)
print("Is 'extra cheese' not in toppings? I predict True.")
print('extra cheese' not in toppings)

# Test 26: Item is not in the list (False)
print("\nIs 'mushrooms' not in toppings? I predict False.")
print('mushrooms' not in toppings)