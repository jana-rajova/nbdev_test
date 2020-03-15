# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['Jana', 'hello', 'lang']

# Cell
class Jana:
    """
    Creade class Jana with the attribute person
    """
    attr1 = "person"
    count = 1

    def replicate(self, times=1):
        "This will cause Jana and all her replicates to divide and create new ones"
        Jana.count *= 2**times
        print("There are now ", Jana.count)
    def restart(self):
        Jana.count = 1
        print("We're back to", Jana.count, Jana.attr1)


# Cell
def hello(name):
    "Say hii"
    assert type(name) == str
    print("Hello", name)


# Cell
def lang(language):
    #language = input("Which language do you speak? ")
    print("Okay, I'll try to learn ", language, "!", sep="")