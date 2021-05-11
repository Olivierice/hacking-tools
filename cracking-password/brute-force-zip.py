import zipfile
from tqdm import tqdm

wordlist = "wordlist.txt"

zip_file = "secret.zip"

zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(wordlist, "rb")))

print("Total passwords to test: ", n_words)

with open(wordlist, "rb") as wordlist:
	for word in tqdm(wordlist, total=n_words, unit="word"):
		try:
			zip_file.extractall(pwd=word.strip(),path="extracted_files")
		except:
			continue
		else:
			print("[+] Password found: ", word.decode().strip())
			exit(0)

print("[!] Password not found, try other wordlist [!]")
