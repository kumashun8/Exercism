def two_fer(name=None):
    if name == None:
        name = "you"
    return "One for {}, one for me.".format(name)