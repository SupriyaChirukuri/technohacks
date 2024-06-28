import re
import random
import string
import hashlib

class PasswordPolicy:
    def __init__(self):
        self.min_length = 12
        self.max_length = 24
        self.min_uppercase = 2
        self.min_lowercase = 2
        self.min_digits = 2
        self.min_special_chars = 2

    def check_password_strength(self, password):
        if len(password) < self.min_length:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"\W", password):
            return False
        return True

    def generate_password(self):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(self.min_length, self.max_length)))
        while not self.check_password_strength(password):
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(self.min_length, self.max_length)))
        return password

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password_uniqueness(self, password, existing_passwords):
        if password in existing_passwords:
            return False
        return True

    def create_password(self, existing_passwords):
        password = self.generate_password()
        while not self.check_password_uniqueness(password, existing_passwords):
            password = self.generate_password()
        return self.hash_password(password)

# Example usage:
policy = PasswordPolicy()
existing_passwords = ["password123", "mysecretpassword"]
new_password = policy.create_password(existing_passwords)
print("New password:", new_password)
