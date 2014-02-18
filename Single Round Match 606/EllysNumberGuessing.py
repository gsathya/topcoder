# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class EllysNumberGuessing:
    def getNumber(self, guesses, answers):
        ans = {}

        for i in range(len(guesses)):
            a = answers[i]+guesses[i]
            b = guesses[i]-answers[i]
            if a > 1 and a < 1000000000:
                ans[a] = ans.get(a, 0) +1
            if b > 1 and b < 1000000000:
                ans[b] = ans.get(b, 0) +1

        ans = sorted(ans.items(), key=lambda (x,y): y, reverse=True)

        print ans

        if ans[0][1] != len(guesses):
            return -2
        if len(ans) > 1 and ans[0][1] == ans[1][1]:
            return -1
        else:
            return ans[0][0]

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

def do_test(guesses, answers, __expected):
    startTime = time.time()
    instance = EllysNumberGuessing()
    exception = None
    try:
        __result = instance.getNumber(guesses, answers);
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
    sys.stdout.write("EllysNumberGuessing (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("EllysNumberGuessing.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            guesses = []
            for i in range(0, int(f.readline())):
                guesses.append(int(f.readline().rstrip()))
            guesses = tuple(guesses)
            answers = []
            for i in range(0, int(f.readline())):
                answers.append(int(f.readline().rstrip()))
            answers = tuple(answers)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(guesses, answers, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1391047914
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
