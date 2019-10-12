import hashlib


def generateHashCode(string):
    return int(hashlib.sha256(
        string.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
