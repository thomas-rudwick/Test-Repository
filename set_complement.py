#!/bin/usr/env python2

def main():
    x = list(map(int, raw_input('input numbers: ').split()))
    xnot = set(range(max(x))) - set(x)
    print ' '.join(map(str, sorted(list(xnot))))

if __name__ == '__main__':
    main()
