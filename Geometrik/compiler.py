from Geometrik.ScannerParser.parserYacc import parse
from Geometrik.ScannerParser.scannerLex import scanner

tokens = scanner("TestCode")
parse(tokens, "TestCode")
