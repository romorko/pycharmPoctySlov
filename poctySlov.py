import _collections
pocty = _collections.defaultdict(int)
###toto je komentar
try:
    with open("text.txt") as file:
        for line in file:
            for slovo in line.split():
                print(slovo)
                pocty[slovo]+=1
    for kluc,hodnota in pocty.items():
        print(kluc,hodnota)

except IOError as ex:
    print("Subor sa nepodarilo otvorit")


