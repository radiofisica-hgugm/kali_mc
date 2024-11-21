import hashlib
import os


def hash_file(filepath):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def hash_folder(folder_path):
    """Calculate the SHA-256 hash of a folder including all its contents."""
    sha256 = hashlib.sha256()

    for root, dirs, files in os.walk(folder_path):
        # Sort files and directories to ensure consistent ordering
        dirs.sort()
        files.sort()

        for name in files:
            filepath = os.path.join(root, name)
            # Update hash with the file path
            sha256.update(filepath.encode("utf-8"))
            # Update hash with the file's content
            sha256.update(hash_file(filepath).encode("utf-8"))

        # Update hash with directory names
        for name in dirs:
            dirpath = os.path.join(root, name)
            sha256.update(dirpath.encode("utf-8"))

    return sha256.hexdigest()
