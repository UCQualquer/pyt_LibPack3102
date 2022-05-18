import hashlib as hs
import base64 as b64
from Crypto.Cipher import AES
from My_Pack.Crypt import generateRandomByteToken as grbt
from My_Pack.Essentials import ensureType, Tuple


""" Decription:
    Uses AES to encrypt data, while doing a message integrity check when decrypting.

    Use 16 bytes long key to AES 128, 24 to AES 192, or 32 to AES 256
"""



def encrypt(data: bytes, key: bytes) -> Tuple[bytes, str]:
    """ Encrypts [data] using [key].
    The encryption method depends on [key] lenght: 16, 24 or 32 for AES 128, 192 or 256, respectively.

    Args:
        data (bytes): Byte data to be encrypted.
        key (bytes): 16, 24 or 32 bytes long encryption key.

    Raises:
        ValueError: Raises if [key]'s len is unsupported.

    Returns:
        Tuple[bytes, str]: Tuple containing the encrypted [data] and a hash for message integrity check.
    """

    # Ensure that the inputs are of valid type.
    ensureType(data, bytes, 'data')
    ensureType(key, bytes, 'key')
    
    # Ensure that [key] has a valid lenght.
    if not (len(key) in (16, 24, 32)): raise ValueError(f'[key] must be 16, 24 or 32 bytes long')

    # Creates the derivative key for posterior use in the integrity check.
    deriv = hs.sha256(key).digest()

    # Creates [data] hash for integrity check and encrypts [data] using [key].
    hash_integrity = hs.md5(data + deriv).hexdigest()
    encrypted_data = __aesEncrypt(data, key)

    return encrypted_data, hash_integrity

def decrypt(data: bytes, key: bytes, hash_integrity: str) -> bytes:
    """ Decrypts [data] using [key] and perform a integrity check using [hash_integrity]

    Args:
        data (bytes): Byte data to be decrypted.
        key (bytes): 16, 24 or 32 bytes long encryption key.
        hash_integrity (str): A hash of the [data] for integrity check. It's given by the [encrypt] method.

    Raises:
        ValueError: Raises if [key]'s len is unsupported.
        ValueError: Raises if the data fails in the integrity check.

    Returns:
        bytes: Decrypted [data]
    """

    # Ensure that the inputs are of valid type.
    ensureType(data, bytes, 'data')
    ensureType(key, bytes, 'key')
    ensureType(hash_integrity, str, 'hash_integrity')

    # Ensure that [key] has a valid lenght.
    if not (len(key) in (16, 24, 32)): raise ValueError(f'[key] must be 16, 24 or 32 bytes long')

    # Creates the derivative key for posterior use in the integrity check.
    deriv = hs.sha256(key).digest()

    # Decrypts [data] using [key] and create its hash to compare in the integrity check.
    decrypted_data = __aesDecrypt(data, key)
    hash_int = hs.md5(decrypted_data + deriv).hexdigest()

    # Integrity check.
    if not (hash_int == hash_integrity):
        raise ValueError('Invalid data. It has been corrupted or modified')

    return decrypted_data


def __aesEncrypt(data: bytes, key: bytes) -> bytes:
    # Set block_size. AES only supports multiples of 16
    BS = 16

    # [pad] function, that fills the remaining spaces to make the data multiple of 16.
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode('utf-8')
    data = pad(data)

    # Creates an initialization vector. Its use remains blurry in my head.
    iv = grbt(16)

    # Creates AES object with [key], mode and [iv]. After, encrypts [data].
    aes = AES.new(key, AES.MODE_CBC, iv)
    encrypted = aes.encrypt(data)

    # Return an urlsafe sum of [iv] and [encrypted]
    return b64.urlsafe_b64encode(iv + encrypted) 

def __aesDecrypt(data: bytes, key: bytes) -> bytes:
    # Set block_size. AES only supports multiples of 16
    BS = 16

    # [unpad] function, that remove the padding used to make the data multiple of 16
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    # Unurlsafes [data] and gets the initialization vector
    enc = b64.urlsafe_b64decode(data)
    iv = enc[:BS]

    # Creates AES object with [key], mode and [iv]. After, decrypts [data].
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted = aes.decrypt(enc[BS:])

    # Returns unpaded [decrypted]
    return unpad(decrypted)