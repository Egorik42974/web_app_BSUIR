import random


def generate_unique_id(cats):
    x = 0
    while x == 0 or check_id(cats, x):
        x = random.randint(1, 1000000000)
    return x


def check_id(cats, x):
    for i in cats:
        if i.cat_id == x:
            return True
    return False


def cat_delete(cats, cat_id):
    for i in cats:
        if i.cat_id == cat_id:
            cats.remove(i)


def get_cat(cats, cat_id):
    for i in cats:
        if i.cat_id == cat_id:
            return i
    return None


def add_pic(cats, cat_id, unique_fn):
    cat = get_cat(cats, cat_id)
    cat.img = unique_fn

