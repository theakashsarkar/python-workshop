import os

def get_files_and_dir(path):
  files = []
  dirs = []
  with os.scandir(path) as it:
    for entry in it:
      if entry.name.startswith('.'):
        continue
      if entry.is_dir():
        dirs.append(entry.name)
      elif entry.is_file(): 
        files.append(entry.name)
  return files, dirs
def traverse_dir(path):
  all_files = []
  all_dirs = [path]
  while len(all_dirs) > 0:
    d = all_dirs.pop()
    print("Traversing dir:", d)
    files, dirs = get_files_and_dir(d)
    all_files.extend(files)
    all_dirs.extend(dirs)
  print(all_files)
if __name__ == "__main__":
  files, dirs = get_files_and_dir("/Users/dev02/workspace/python")
  traverse_dir("/Users/dev02/workspace/python")
  # print(files)
  # print(dirs)