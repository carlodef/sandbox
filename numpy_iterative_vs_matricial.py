import numpy as np

"""
Given a list of 3x3 matrices r1, r2, ..., rn, and a list of 3x1 vectors v1, v2,
... vn, what is the fastest way to compute the list of matrix products
np.dot(r1, v1), np.dot(r2, v2), ..., np.dot(rn, vn) ?
"""

N = 72
mat_list = []
vec_list = []
out_list = []

for i in range(N):
    vec_list.append(np.random.random((3, 1)))
    mat_list.append(np.random.random((3, 3)))

vectors = np.hstack(vec_list)
matrices = np.vstack(mat_list)

def iteratively():
    """
    """
    for i in range(N):
        out_list.append(np.dot(mat_list[i], vec_list[i]))


def matricially():
    """
    """
    vectors = np.hstack(vec_list)
    matrices = np.vstack(mat_list)
    tmp = np.dot(matrices, vectors)
    #for i in range(N):
    #    out_list.append(tmp[3*i:3*i+3, i])
