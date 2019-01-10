import os

# %% adf
a = 'apple是苹果'
print(a)
print(type(a))
print(len(a))

# %%
a_gbk = bytes(a, encoding="gbk")
print(a_gbk)
print(len(a_gbk))
print(type(a_gbk))

# %%
a_utf8 = bytes(a, encoding="utf8")
print(a_utf8)
print(len(a_utf8))
print(type(a_utf8))

# %% adsf
file = open("test.txt", mode="w", encoding="utf8")
file.write(a)
file.close()

# %%  adsf
file2 = open("test.txt", mode="r", encoding="utf8")
print(file2.read())
file2.close()

os.remove("test.txt")


# %%
def add2(a: int, b: int) -> int:
    """
    add函数

    :param a: asdf
    :param b: adsf
    :return: adsf
    """
    return a + b


add2(1.2, 2)

print("""
adsf
adsf
asdf
""")

import os

cwd = os.getcwd()
print(cwd)

path = cwd + "/words_game_normal/dicts/3500常用字.txt"




