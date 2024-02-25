fn = []
fv = []
dn = []

if __name__ == "__main__":
    print("WARNING! Any projects that use this module will need to be run from the project directory.")
afd = {}

def mkfile(filename, value, dir):
    fn.append(filename)
    fv.append(value)
    if not dir in dn:
        raise FileNotFoundError("No such directory")
    afd.update({filename: dir})
def mkdir(dirname):
    dn.append(dirname)