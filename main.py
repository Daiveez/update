from Lexer import Lexer
from Parser import Parser
from AST import Program
from Compiler import Compiler

import json

from llvmlite import ir
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float


LEXER_DEBUG: bool = False
PARSER_DEBUG: bool = True
COMPILER_DEBUG: bool = False

if __name__ == '__main__':
    with open("/Users/user/Downloads/python-compiler-1.3/src/tests/compiler_test", "r") as f:
        code: str = f.read()

    if LEXER_DEBUG:
        debug_lex: Lexer = Lexer(source=code)
        while debug_lex.current_char is not None:
            print(debug_lex.next_token())

    l: Lexer = Lexer(source=code)
    p: Parser = Parser(l)

    program: Program = p.parse_program()
    if len(p.errors) > 0:
        for err in p.errors:
            print(err)
        exit(1)

    if PARSER_DEBUG:
        with open("debug/ast.json", "w") as f:
            json.dump(program.json(), f, indent=4)

        print("Wrote AST to debug/ast.json successfully.")

    c: Compiler = Compiler()
    c.compile(program)

    module = ir.Module = c.module
    module.triple = llvm.get_default_triple()

    if COMPILER_DEBUG:
        print("===== COMPILER DEBUG =====")
        with open("debug/ir.ll", "w") as f:
            # Run llc -filetype=asm debug/ir.ll -o debug/assembly.s to generate assembly
            f.write(str(module))