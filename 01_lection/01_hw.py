code_exit = int(input())
interactor = int(input())
checker = int(input())

if interactor == 0:
    if code_exit == 0:
        print(checker)
    else:
        print(3)
elif interactor == 1:
    print(checker)
elif interactor == 4:
    if code_exit == 0:
        print(4)
    else:
        print(3)
elif interactor == 6:
    print(0)
elif interactor == 7:
    print(1)
else:
    print(interactor)
