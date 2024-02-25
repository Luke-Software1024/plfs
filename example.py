import plfs

plfs.mkdir("Test")
plfs.mkfile("FileInDir", "A fil in a dir", "Test")
print(f"{plfs.fn} contains {plfs.fv} and is in {plfs.afd}")
plfs.mkfile("FileInDir", "A fil in a dir", "NExistent")