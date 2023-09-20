#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def devided(dividend: int, divisor: int) -> int:
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    value = dividend/divisor
    return value

def main():
    x = devided(7, 0)
    print(x)

if __name__ == "__main__":
    main()