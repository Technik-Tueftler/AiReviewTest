#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem gefunden mit dem teilen durch Null -> 
"""
def devided(dividend: int, divisor: int) -> int:
    value = dividend/divisor
    return value

def main():
    x = devided(7, 0)
    print(x)

if __name__ == "__main__":
    main()