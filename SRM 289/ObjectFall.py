# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ObjectFall:
    def howLong(self, x, y, obstacles):
        o = {}
        time = 0
        f = y
        for i in obstacles:
            a = [int(p) for p in i.split(" ")]
            y = a[0]
            x1 = a[1]
            x2 = a[2]
            if y in o:
                o[y].append((x1, x2))
            else:
                o[y] = [(x1, x2)]

        for i in range(f, -1, -1):
            if i in o:
                for j in o[i]:
                    if j[0] <= x and x <= j[1]:
                        time += 5
                        x = j[1]
        return f+time
            

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(x, y, obstacles, __expected):
    startTime = time.time()
    instance = ObjectFall()
    exception = None
    try:
        __result = instance.howLong(x, y, obstacles);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("ObjectFall (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ObjectFall.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x = int(f.readline().rstrip())
            y = int(f.readline().rstrip())
            obstacles = []
            for i in range(0, int(f.readline())):
                obstacles.append(f.readline().rstrip())
            obstacles = tuple(obstacles)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x, y, obstacles, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1407715572
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
