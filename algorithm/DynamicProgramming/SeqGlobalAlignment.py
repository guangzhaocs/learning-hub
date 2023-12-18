# -*- coding: UTF-8 -*-
"""
@File    : SeqGlobalAlignment.py
@Date    : 2023/2/15 16:25 
@Github  : https://github.com/guangzhaocs/algorithm/blob/main/DynamicProgramming/SeqGlobalAlignment.py
"""
import numpy as np


def score(a, b):
    """
    Define score function
       s(a, b) = +1 if a == b
       s(a, b) = −1 if a != b
       s(a, −) = s(−, b) = −1
    """
    if a == b and a != "-":
        return 1
    else:
        return -1


def flag(v1, v2, v3):
    """
    Define traceback matrix flag
       return 1 if case 1 (comes from DIAG)
       return 2 if case 2 (comes from LEFT)
       return 3 if case 3 (comes from UP)
       return 4 if case 1 == case 2 (comes from DIAG/LEFT)
       return 5 if case 1 == case 3 (comes from DIAG/UP)
       return 6 if case 2 == case 3 (comes from LEFT/UP)
       return 7 if case 1 == case 2 == case 3 (comes from DIAG/LEFT/UP)
    """
    max_v = max(v1, v2, v3)
    if v1 == max_v and v2 != max_v and v3 != max_v:
        return 1
    elif v1 != max_v and v2 == max_v and v3 != max_v:
        return 2
    elif v1 != max_v and v2 != max_v and v3 == max_v:
        return 3
    elif v1 == max_v and v2 == max_v and v3 != max_v:
        return 4
    elif v1 == max_v and v2 != max_v and v3 == max_v:
        return 5
    elif v1 != max_v and v2 == max_v and v3 == max_v:
        return 6
    else:
        return 7


def pad_seq(flag, seq1, seq2, i, j, arr):

    if flag == 1:
        for k in range(len(arr)):
            arr[k][0] = arr[k][0] + seq1[i]
            arr[k][1] = arr[k][1] + seq2[j]
    elif flag == 2:
        for k in range(len(arr)):
            arr[k][0] = arr[k][0] + "-"
            arr[k][1] = arr[k][1] + seq2[j]
    elif flag == 3:
        for k in range(len(arr)):
            arr[k][0] = arr[k][0] + seq1[i]
            arr[k][1] = arr[k][1] + "-"
    else:
        raise TypeError

    return arr


def trace_dp(seq1, seq2, trace_mat, i, j):
    """
    Recursion algorithm
    """

    if i == 0 and j == 0:
        return [["", ""]]
    elif i == 0 and j != 0:
        return [[j * '-', seq2[1:j+1]]]
    elif i != 0 and j == 0:
        return [[seq1[1:i+1], i * '-']]
    else:
        pass

    if trace_mat[i][j] == 1:
        _l = trace_dp(seq1, seq2, trace_mat, i - 1, j - 1)
        return pad_seq(1, seq1, seq2, i, j, _l)
    elif trace_mat[i][j] == 2:
        _l = trace_dp(seq1, seq2, trace_mat, i, j - 1)
        return pad_seq(2, seq1, seq2, i, j, _l)
    elif trace_mat[i][j] == 3:
        _l = trace_dp(seq1, seq2, trace_mat, i - 1, j)
        return pad_seq(3, seq1, seq2, i, j, _l)
    elif trace_mat[i][j] == 4:
        _l1 = trace_dp(seq1, seq2, trace_mat, i - 1, j - 1)
        _l1 = pad_seq(1, seq1, seq2, i, j, _l1)
        _l2 = trace_dp(seq1, seq2, trace_mat, i, j - 1)
        _l2 = pad_seq(2, seq1, seq2, i, j, _l2)
        _l = []
        _l.append(_item for _item in _l1)
        _l.append(_item for _item in _l2)
        return _l
    elif trace_mat[i][j] == 5:
        _l1 = trace_dp(seq1, seq2, trace_mat, i - 1, j - 1)
        _l1 = pad_seq(1, seq1, seq2, i, j, _l1)
        _l3 = trace_dp(seq1, seq2, trace_mat, i - 1, j)
        _l3 = pad_seq(3, seq1, seq2, i, j, _l3)
        _l = []
        _l.append(_item for _item in _l1)
        _l.append(_item for _item in _l3)
        return _l
    elif trace_mat[i][j] == 6:
        _l2 = trace_dp(seq1, seq2, trace_mat, i, j - 1)
        _l2 = pad_seq(2, seq1, seq2, i, j, _l2)
        _l3 = trace_dp(seq1, seq2, trace_mat, i - 1, j)
        _l3 = pad_seq(3, seq1, seq2, i, j, _l3)
        _l = []
        _l.append(_item for _item in _l2)
        _l.append(_item for _item in _l3)
    else:  # 7
        _l1 = trace_dp(seq1, seq2, trace_mat, i - 1, j - 1)
        _l1 = pad_seq(1, seq1, seq2, i, j, _l1)
        _l2 = trace_dp(seq1, seq2, trace_mat, i, j - 1)
        _l2 = pad_seq(2, seq1, seq2, i, j, _l2)
        _l3 = trace_dp(seq1, seq2, trace_mat, i - 1, j)
        _l3 = pad_seq(3, seq1, seq2, i, j, _l3)
        _l = []
        _l.append(_item for _item in _l1)
        _l.append(_item for _item in _l2)
        _l.append(_item for _item in _l3)
        return _l


def generate_final_path(seq1, seq2, trace_mat):
    return trace_dp(seq1, seq2, trace_mat, len(seq1) - 1, len(seq2) - 1)


def print_helper(seq1, seq2):

    align = ""
    for i, j in zip(seq1, seq2):
        if i == j:
            align += "|"
        else:
            align += " "

    print(seq1)
    print(align)
    print(seq2)
    print()


def global_alignment(seq1, seq2):

    seq1 = "-" + seq1
    seq2 = "-" + seq2

    l1 = len(seq1)
    l2 = len(seq2)

    dp_mat = np.zeros((l1, l2))
    trace_mat = np.zeros((l1, l2))

    # first row
    for i in range(1, l2):
        dp_mat[0][i] = dp_mat[0][i-1] + score("-", seq2[i])
        trace_mat[0][i] = 2

    # first column
    for i in range(1, l1):
        dp_mat[i][0] = dp_mat[i-1][0] + score("-", seq1[i])
        trace_mat[i][0] = 3

    # dp
    for i in range(1, l1):
        for j in range(1, l2):
            v1 = dp_mat[i - 1][j - 1] + score(seq1[i], seq2[j])
            v2 = dp_mat[i][j - 1] + score("-", seq2[j])
            v3 = dp_mat[i - 1][j] + score(seq1[i], "-")
            dp_mat[i][j] = max(v1, v2, v3)
            trace_mat[i][j] = flag(v1, v2, v3)

    # trace back all paths
    res = generate_final_path(seq1, seq2, trace_mat)

    # print final res
    print(" ----- Scoring matrix ----- ")
    print(dp_mat)
    print(" ----- Traceback matrix ----- ")
    print(trace_mat)
    print(" ----- All possible paths ----- ")
    for _align in res:
        print_helper(_align[0], _align[1])


if __name__ == '__main__':

    seq1 = "AGCCGTT"
    seq2 = "ATTAGTTA"
    global_alignment(seq1, seq2)