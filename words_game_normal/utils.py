def read_char_list(path: str, encoding="utf-8"):
    """
    读入汉字，成为List
    :param path:
    :param encoding:
    :return:
    """
    return [char for char in open(path, encoding=encoding).read()]

