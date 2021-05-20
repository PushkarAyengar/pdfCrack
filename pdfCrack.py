import pikepdf
from tqdm import tqdm

# load the password list

passwords = [ line.strip() for line in open("pass.txt")]

# iterate over the passwords

for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("sample.pdf", password = password) as pdf:
        # Passwords has been decrypted, break out of the loop
            print("[+] Password Found: ", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, continue

        continue
