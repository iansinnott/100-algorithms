from sys import argv

# Would be great to understand this one a bit better. I've done it before but
# the logic never really seems to stick. I ended up using this session as an
# opportunity to write more python and get familiar with it :p
def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        hanoi(height - 1, left, middle, right)
        print(left, '=>', right)
        hanoi(height - 1, middle, right, left)

def main(height):
    if height < 1:
        raise RuntimeError("First argument must be greater than zero")
    hanoi(height)

main(int(argv[1]))
