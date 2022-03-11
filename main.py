import argparse

import pycosat


def get_var_from_cell(i, j, n):
    return i * n + j + 1


def get_cell_from_var(cell, n):
    return (cell - 1) // n, (cell - 1) % n


def get_cnf(n):
    result_cnf = []
    for i in range(n):
        at_least_one = []
        for j in range(n):
            at_least_one.append(get_var_from_cell(i, j, n))
        result_cnf.append(at_least_one)

    for i in range(n):
        for j in range(n):
            for k in range(j):
                result_cnf.append([-get_var_from_cell(i, k, n), -get_var_from_cell(i, j, n)])

    for j in range(n):
        for i in range(n):
            for k in range(i):
                result_cnf.append([-get_var_from_cell(i, j, n), -get_var_from_cell(k, j, n)])

    for s in range(2 * n - 1):
        for i in range(n):
            j = s - i
            if j < 0 or j >= n:
                continue
            for k in range(i):
                h = s - k
                if h < 0 or h >= n:
                    continue
                result_cnf.append([-get_var_from_cell(i, j, n), -get_var_from_cell(k, h, n)])

    for s in range(1 - n, n):
        for i in range(n):
            j = i - s
            if j < 0 or j >= n:
                continue
            for k in range(i):
                h = k - s
                if h < 0 or h >= n:
                    continue
                result_cnf.append([-get_var_from_cell(i, j, n), -get_var_from_cell(k, h, n)])

    return result_cnf


def print_answer_for(n):
    answer = pycosat.solve(get_cnf(n))
    if answer == "UNKNOWN":
        print("Solution could not be determined within the propagation limit!")
    elif answer == "UNSAT":
        print("CNF is not satisfiable!")
    else:
        for el in answer:
            if el < 0:
                continue
            print(get_cell_from_var(el, n))


parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input expression")
args = parser.parse_args()

print_answer_for(int(args.input))
