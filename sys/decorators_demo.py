def spamrun(fn):
    def sayspam(*args):
        print("spam,spam,spam")
        fn(*args)

    return sayspam


def spamrun1(fn):
    def sayspam1(*args):
        print("spam1,spam1,spam1")
        print(args)
        fn(*args)

    return sayspam1


@spamrun
@spamrun1
def useful(a, b):
    print(a * b)


def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate


@attrs(versionadded="2.2",
       author="Guido van Rossum")
def mymethod(f):
    print(getattr(mymethod, 'versionadded', 0))
    print(getattr(mymethod, 'author', 0))
    print(f)


if __name__ == "__main__":
    useful(2, 5)
    mymethod(2)