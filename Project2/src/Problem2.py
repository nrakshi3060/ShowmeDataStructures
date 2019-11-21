import os


def is_directory(path):
    return not os.path.isfile(path)


def find_files(suffix, path):
    try:
        list_dir = os.listdir(path)
        return find_files_func(suffix, path, list_dir, 0)
    except Exception:
        print(" No such file or directory: '{}' exists".format(path))


def is_cfile(suffix, path):
    return path.endswith(suffix)


def find_files_func(suffix, path, list_dir, index):
    if index == len(list_dir):
        return []
    output = find_files_func(suffix, path, list_dir, index + 1)
    new_path = path + "/" + list_dir[index]
    to_append = []
    if is_directory(new_path):
        to_append.extend(find_files(suffix, new_path))
    else:
        if is_cfile(suffix, list_dir[index]):
            to_append.append(new_path)
    output.extend(to_append)
    return output


print("------------------TestCase 1------------------------")
path = "testdir"
l1 = find_files(".c", path)

for item in l1:
    print(item)

print("------------------TestCase 2------------------------")
path = "testdir1"
l2 = find_files(".c", path)
print(l2)

print("------------------TestCase 3------------------------")
path2 = "testdir2"
l3 = find_files(".h", path2)

print("------------------TestCase 4------------------------")
path2 = None
l4 = find_files(".h", path2)
