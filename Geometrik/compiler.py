from scannerLex import scanner
from parserYacc import parse

tokens = scanner("TestCode")
parse(tokens, "TestCode")
