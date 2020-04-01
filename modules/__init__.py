from . import test

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
items = [
    test
]


def register():
    for c in items:
        c.register()


def unregister():
    for c in items:
        c.unregister()
