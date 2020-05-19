import pkgutil,requests

for filefiner, name, ispkg in pkgutil.iter_modules(requests.__path__, requests.__name__ + "."):
    print("{0} name: {1:12}, is_sub_package: {2}".format(filefiner, name, ispkg))
