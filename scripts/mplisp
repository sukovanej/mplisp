#!/usr/bin/env python3
import sys
from mplisp import evaluator


def main():
    for filename in sys.argv[1:]:
        with open(filename) as file_object:
            result = evaluator.evaluate(file_object.read())

            for line in result:
                if line is not None:
                    print(line)


if __name__ == "__main__":
    main()
