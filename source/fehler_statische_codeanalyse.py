#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Elif Bedingung für a ist immer True -> Konnte keine Lösung anbieten.
Problem, dass man auch schreiben könnte return a and b and c, hat ergefunden.
"""
def test_foo(a: bool, b: bool, c: bool) -> bool:
    if (a is True) or (b is True and c is True):
        return True
    elif a is False and b is False and c is False:
        return False


def main() -> None:
    x = test_foo(True, True, True)
    print(x)


if __name__ == "__main__":
    main()