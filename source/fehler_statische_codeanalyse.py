#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def test_foo(a: bool, b: bool, c: bool) -> bool:
    return a or (b and c)


def main() -> None:
    x = test_foo(True, True, True)
    print(x)


if __name__ == "__main__":
    main()