import numpy
edges11 = [[0,1], [1,2], [2,3], [3,4]]
edges12 = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8]]
edges2 = [[0,1], [1,2], [3,4], [4,5], [6,7], [7,8], [0,3], [1,4], [2,5], [3,6], [4,7], [5,8]]
edges3 = [[0,1], [1,2], [3,4], [4,5], [6,7], [7,8], [0,3], [1,4], [2,5], [3,6], [4,7], [5,8],
          [0,6], [1,7], [2,8], [0,2], [3,5], [6,8]]
edges_dir = [[-1,0], [0,1], [1,2], [2,3], [3,4], [4,-1]]


def build_m(edges):
    m = []
    graph_len = max(reduce(lambda x, y: x + y, edges, [])) + 1
    for e in edges:
        v = [0]*graph_len
        if e[0] != -1:
            v[e[0]] = 1
        if e[1] != -1:
            v[e[1]] = -1
        m.append(v)
    return numpy.matrix(m).transpose()

# S = build_m(edges3)
# print S
# print S * S.transpose()

S1 = build_m(edges11)
m1 = S1 * S1.transpose()

S2 = build_m(edges12)
m2 = S2 * S2.transpose()


S3 = build_m(edges2)
m3 = S3 * S3.transpose()

S_dir = build_m(edges_dir)
m_dir = S_dir * S_dir.transpose()


def calc_cut_inverse(m):
    cut_mat = numpy.ix_(xrange(1,len(m)), xrange(1,len(m)))
    return m[cut_mat].I


def bit(x,n):
    return (x>>n) & 1


def check_mat(m):
    cut_inv = calc_cut_inverse(m)
    assert len(cut_inv) < 15
    for i in xrange(2**len(cut_inv)):
        tmp_vec = numpy.matrix([bit(i, n) for n in xrange(len(cut_inv))]).I
        print tmp_vec.I
        v = cut_inv * tmp_vec
        v = [-int(sum(v))] + list(v.I.tolist()[0])
        new_v = m * numpy.matrix(v).I
        print new_v[0] - sum(new_v[1:])


def one_dim_dirichlet_lap(n = 5):
    A = []
    r = [0] * n
    r[0] = -2
    r[1] = 1
    A.append(r)
    for i in xrange(1,n-1):
        r = [0] * n
        r[i - 1] = 1
        r[i] = -2
        r[i + 1] = 1
        A.append(r)
    r = [0] * n
    r[-1] = -2
    r[-2] = 1
    A.append(r)
    return numpy.matrix(A)

