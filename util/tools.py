import hashlib
import time

def get_hash_value(data:bytes) -> str:
    h = hashlib.sha1()
    h.update(data)
    return h.hexdigest()

def get_localtime() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())