import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # Creating lists of all files with suffix and directories to walk through in order to find files that has suffix
    files_with_suffix = []
    dirs_to_walk = [path]

    # walking through directories
    while dirs_to_walk:
        folder = dirs_to_walk.pop(0) + "/"  # removing first element from walk list
        items = os.listdir(folder)  # getting all items from the folder

        # Going through all items and checking if item is directory or file. If it is a directory, adding it to walk
        # list else if it is file and ends with suffix, adding the item in files list
        for i in items:
            i = folder + i
            if os.path.isdir(i):
                dirs_to_walk.append(i)
            elif str(i).endswith(suffix):
                files_with_suffix.append(i)

    return files_with_suffix
