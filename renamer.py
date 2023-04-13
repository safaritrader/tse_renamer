import os

path = r"symbols"
files_location = os.listdir(path)

for entry in files_location:
    if "ك" in entry:
        name = entry.replace("ك" , "ک")
        print(name)
        print(entry)
        os.rename(os.path.join(path, entry), os.path.join(path, name))
    if "ي" in entry:
        name = entry.replace("ي", "ی")
        print(name)
        print(entry)
        os.rename(os.path.join(path, entry), os.path.join(path, name))