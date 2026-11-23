from functools import reduce


def a(x):
    return f"a({x})"

def b(x):
    return f"b({x})"

def c():
    return "c()"

functions = {
    "a": a,
    "b": b,
    "c": c
}

s = "abc"

result = reduce(lambda acc, char: functions[char](acc), reversed(s[:-1]), functions[s[-1]]())

print(result)
