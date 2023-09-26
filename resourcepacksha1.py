import hashlib


def resourcePackSHA1(fileName):
    with open(fileName, "rb") as f:
        file_hash = hashlib.sha1()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()