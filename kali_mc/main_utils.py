import hashlib
import os


def hash_selected_files(folder_path, file_names):
    """
    Compute a hash for a specific list of files, ensuring consistent ordering.

    Args:
        folder_path (str): Path to the folder containing the files.
        file_names (list): List of file names to hash, sorted in the desired order.

    Returns:
        str: The computed hash.
    """
    hasher = hashlib.sha256()

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                while chunk := f.read(65536):  # Read file in chunks for efficiency
                    hasher.update(chunk)
        else:
            raise FileNotFoundError(f"File {file_name} does not exist in {folder_path}")

    return hasher.hexdigest()
