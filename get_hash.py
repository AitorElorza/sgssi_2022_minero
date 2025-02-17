import hashlib

"""
def get_hash(ifile):
    BLOCK_SIZE = 65536 # The size of each read from the file
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(ifile, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    hexdigest = str(file_hash.hexdigest())
    return hexdigest
    """

def get_hash(ifile):
    with open(ifile,'r') as bloc:
        content = bloc.read()
        hashed = hashlib.sha256(content.encode())
        hexdigest = str(hashed.hexdigest())
        return hexdigest
        