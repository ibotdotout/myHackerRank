# https://www.hackerrank.com/challenges/hackerrank-language

import re


def solve(text):
    langs = "C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|" \
            "ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|" \
            "DART|GROOVY|OBJECTIVEC"
    return True if re.match("^([1-9]\d{4})\s("+langs+")$", text) else False


if __name__ == "__main__":
    n = input()
    for i in range(n):
        text = raw_input()
        print "VALID" if solve(text) else "INVALID"
