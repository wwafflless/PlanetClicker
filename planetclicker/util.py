def singleton(class_):
    """
    Decorator that makes a class a singleton.
    """

    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
