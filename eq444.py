from math import sqrt, log

def norm(v):
    return sqrt(v[0]**2 + v[1]**2)


def check_range(point, R, R1):
    tmp = norm(point)
    # print tmp, R1,  (tmp >= R1), (tmp <= (R * R1))
    return (tmp >= R1) and (tmp <= (R * R1))

def check_points(points, R, R1):
    flag = True
    for p in points:
        # print p
        tmp = check_range(p, R, R1)
        # print tmp
        flag = flag and tmp
        if not tmp:
            break
    return flag

def calc_diff_sum(R, R1):
    assert R1 > 2
    res = 0
    done_couples = set()
    # debug_points = set()
    for x in xrange(2, int(R*R1)):
        for y in xrange(2, int(R*R1)):
            points = [(x,y), (x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            if not check_points(points, R, R1):
                continue
            p0 = points[0]
            # debug_points.add(p0)
            for p in points[1:]:
                tmp_tuple = tuple(sorted([p0, p]))
                if (tmp_tuple not in done_couples):
                    done_couples.add(tmp_tuple)
                    res += (log(norm(p)) - log(norm(p0)))**2
    return res / log(R1)
    # print len(done_couples)
    # return debug_points, res / log(R1)

# calc_diff_sum(200, 2.1) # =9.310761106876132