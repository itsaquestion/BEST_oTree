import random
from typing import List
# from otree.api import BaseSubsession
from collections import deque

"""
by Li Weicheng
"""


def get_all_treatments_from_config(subsession):
    """
    从config读取所有treatment
    :return:
    """
    treatments_keys = {k: v for k, v in subsession.session.config.items() if k.startswith('Treatment_') and v}.keys()
    # treatments_keys
    all_treatments = [s.replace("Treatment_", "") for s in treatments_keys]
    return all_treatments


def head_tail_pairing(matrix: List[List]):
    """
    首尾配对，直到中间；参与人必须是偶数
    :param matrix: matrix = group.get_group_matrix()
    :return: new matrix
    """
    n = len(matrix) * len(matrix[0])

    new_structure = [None] * int(n / 2)
    for i in range(1, int(n / 2) + 1):
        # print(i)
        new_structure[i - 1] = [i, n - i + 1]

    return new_structure


def shift(a_list: list, n: int = 1) -> list:
    """
    rotate一个list，是deque.rotate的一个包装，用法相同。
    主要用于对指定的group或者player进行treatment的轮替。

    :param a_list:
    :param n:
    :return: 平移后的list
    """
    a_dq = deque(a_list)
    a_dq.rotate(n)
    return list(a_dq)


def swap_str(str_list: List[str], str_1: str, str_2: str) -> List[str]:
    """
    只要出现str_1，就替换成str_2；只要出现str_2，就替换成str_1

    :param str_list:
    :param str_1:
    :param str_2:
    :return:
    """
    str_list_cpy = str_list.copy()
    has_str_1 = [i for i, val in enumerate(str_list_cpy) if str_1 in val]
    has_str_2 = [i for i, val in enumerate(str_list_cpy) if str_2 in val]

    for idx, val in enumerate(str_list_cpy):
        if idx in has_str_1:
            str_list_cpy[idx] = str_list_cpy[idx].replace(str_1, str_2)
        elif idx in has_str_2:
            str_list_cpy[idx] = str_list_cpy[idx].replace(str_2, str_1)

    return str_list_cpy


def shuffle_in_groups(gm: List[List]) -> list:
    """
    组内洗牌。
    :param gm: List<Group>
    :return: 组内洗牌后的List<Group>
    """
    return [random.sample(g, len(g)) for g in gm]


def shuffle_in_groups_by_role(gm: List[List], role: str) -> list:
    """
    针对特定role的组内洗牌。同组、同角色随机分配。这表示分组前后role不变，但是role内部的相对位置随机化。
    :param gm: List<Group>
    :param role: 要洗牌的role
    :return: 组内洗牌后的List<Group>
    """
    # return list(map(lambda x: random.sample(x, len(x)), gs))
    return [shuffle_by_role(g, role) for g in gm]


def shuffle_by_role(g: List, role: str) -> list:
    """
    对于某个组，同一个role内部乱序。
    :param g: 某个Group
    :param role: 指定需要乱序的role
    :return: 乱序完成的Group。
    """

    the_player = [p for _, p in enumerate(g) if p.role() == role]
    the_pos = [idx for idx, p in enumerate(g) if p.role() == role]

    random.shuffle(the_player)

    new_g = assign_by_pos(g, the_pos, the_player)

    return new_g


def assign_by_pos(old_list: list, pos: List[int], new_value: list) -> list:
    """
    等同于R中的：old_list[pos] <- new_value，但是是一个纯函数。
    返回修改后的新List，原List不变。（是个纯函数）
    :param old_list: 要修改的list
    :param pos: 要修改的位置
    :param new_value: 新的值
    :return: 新的List
    """

    new_list = old_list.copy()
    for i, _ in enumerate(pos):
        new_list[pos[i]] = new_value[i]

    return new_list
