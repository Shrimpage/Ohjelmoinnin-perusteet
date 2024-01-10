
def funktio(luku):
    if (luku>100):
        return
    funktio(luku+1)
    print(luku)

funktio(1)