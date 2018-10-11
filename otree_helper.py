from typing import List
from otree.api import BaseSubsession
"""
by Li Weicheng
"""


def get_all_treatments_from_config(subsession: BaseSubsession):
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
