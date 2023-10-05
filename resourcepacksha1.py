from hashlib import sha1


def resourcePackSHA1(fileName):
    with open(fileName, "rb") as f:
        file_hash = sha1()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()
