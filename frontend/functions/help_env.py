# Support functions for setup of the environment

# Import of dependencies
from pathlib import Path
from dotenv import load_dotenv


def find_env_file_old(directory=None):
    if directory is None:
        directory = Path.cwd()

    env_file = directory / '.env'
    if env_file.is_file():
        return env_file

    parent_directory = directory.parent
    if parent_directory == directory:
        # We have reached the root directory
        return None

    return find_env_file(parent_directory)


# Define Function to find the nearest .env file
def find_env_file(directory: Path = None) -> Path:
    """
    This function finds the nearest .env file in the directory tree.
    :param directory: Path to the current directory
    :return: Path to the nearest .env file
    """
    # Check if current directory is None
    if directory is None:
        # Set current directory to the working directory
        directory = Path.cwd()

    # Get all files in the current directory
    files = [file for file in directory.glob('*') if file.is_file() and file.name == '.env']

    # Check if there is a .env file in the current directory
    if len(files) > 1:
        raise ValueError("There are multiple .env files in the current directory.")
    elif len(files) == 1:
        return files[0]
    else:
        # Check if the current directory is the root directory
        if directory.parent == directory:
            # We have reached the root directory
            raise FileNotFoundError("There is no .env file in the current directory or any parent directory.")
        else:
            # Check the parent directory
            return find_env_file(directory.parent)


# Function to load the environment variables
def load_env_file(env_file: Path = None) -> bool:
    """
    This function loads the environment variables from the .env file.
    :param env_file: Path to the .env file
    :return: None
    """
    # Check if env_file is None
    if env_file is None:
        # Find the nearest .env file
        env_file = find_env_file()

    # Load the environment variables
    return load_dotenv(env_file)


# Check if run as script
if __name__ == '__main__':
    # Test the function
    print(load_env_file())
