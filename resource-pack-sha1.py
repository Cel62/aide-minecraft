import hashlib

filename = "D:\Dropbox\ResourcePack\GDLCA.zip"

with open(filename, "rb") as f:
    file_hash = hashlib.sha1()
    while chunk := f.read(8192):
        file_hash.update(chunk)

sha1_hash = file_hash.hexdigest()
print(sha1_hash)