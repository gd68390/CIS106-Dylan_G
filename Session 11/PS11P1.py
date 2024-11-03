def flist(name):

    print("Names printed in order: ")
    print(name)


def rlist(name):

    print()
    print("Names printed in reverse order: ")
    print(list(reversed(name)))
    

name = ["Holden", "Nelly", "Winslow", "Perez", "Juniper", "Tylers", "Valentino", "Rodriguez", "Gartland", "Einstein"];

flist(name)
rlist(name)