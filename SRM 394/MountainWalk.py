# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class MountainWalk:
    def possible(self, a, b):
        if (a, b) in self.visited:
            return False
            
        if a < 0 or a > self.max_x-1:
            return False
        if b < 0 or b > self.max_y-1:
            return False

        val = int(self.areaMap[self.x][self.y])
        if abs(int(self.areaMap[a][b]) - val) <= self.heightDifference:
            self.x = a
            self.y = b
            return True
            
    def cellsVisited(self, areaMap, heightDifference):
        self.visited = {}
        self.areaMap = areaMap
        self.heightDifference = heightDifference
        self.max_x = len(areaMap)
        self.max_y = len(areaMap[0])
        self.x =0
        self.y = 0
        a = 1
        while True:
            self.visited[(self.x, self.y)] =True            
            if self.possible(self.x+1, self.y):
                a += 1
            elif self.possible(self.x,self.y-1):
                a += 1
            elif self.possible(self.x-1,self.y):
                a += 1
            elif self.possible(self.x,self.y+1):
                a+=1
            else:
                break
        return a

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

def do_test(areaMap, heightDifference, __expected):
    startTime = time.time()
    instance = MountainWalk()
    exception = None
    try:
        __result = instance.cellsVisited(areaMap, heightDifference);
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
    sys.stdout.write("MountainWalk (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MountainWalk.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            areaMap = []
            for i in range(0, int(f.readline())):
                areaMap.append(f.readline().rstrip())
            areaMap = tuple(areaMap)
            heightDifference = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(areaMap, heightDifference, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1407626612
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
