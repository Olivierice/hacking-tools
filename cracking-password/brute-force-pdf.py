import pikepdf
from tqdm import tqdm

# Load the wordlist to use
passwords = [ line.strip() for line in open("wordlist.txt") ]

for pwd in tqdm(passwords, "Decrypting PDF"):
	try:
		with pikepdf.open("my-pdf.pdf", password=pwd) as pdf:
			print("[+] Password found: ", pwd)
			break
	except pikepdf._qpdf.PasswordError as e:
		continue
