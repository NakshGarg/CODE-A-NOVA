import random
import string
print("🔐 Password Generator")
length = int(input("Enter password length: "))
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation
all_chars = lowercase + uppercase + digits + special_chars
for _ in range(length):
    password += random.choice(all_chars)
print("\n✅ Generated Password:")
print(password)
