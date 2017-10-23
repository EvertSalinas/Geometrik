from Geometrik.LexerParser.parserYacc import parse
from Geometrik.LexerParser.scannerLex import scanner

tokens = scanner("TestCode")
parse(tokens, "TestCode")
