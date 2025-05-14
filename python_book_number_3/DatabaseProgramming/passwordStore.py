def register(user, password):
  encrypted_password = encrypt(password)
  save_user(user, encrypted_password)

def login(user, password):
    store_password = get_password_from_db(user)
    encrypted_password = encrypted_password(password)
    if store_password != encrypted_password:
      return "Incorrect password"
    
import hashlib
def encrypted_password(password):
  m = hashlib.sha256()
  m.update(password.encode())
  return m.hexdigest()
if __name__ == "__main__":
  password = "secret"
  encrypted_password = encrypted_password(password)
  print(encrypted_password)  