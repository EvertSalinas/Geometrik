from Memory.Memory import MemoryBlock

memoria = MemoryBlock()

a1 = memoria.storeVariableToMemory(1, 'int') # 0

a2 = memoria.storeConstantToMemory('false', 'bool') # 3000

a3 = memoria.storeTempToMemory('ajai', 'string') # 5500

a4 = memoria.storeVariableToMemory(2, 'int') # 1

a5 = memoria.storeConstantToMemory(1.0, 'float') # 2500

a6 = memoria.storeVariableToMemory(3, 'int') # 2

a7 = memoria.storeTempToMemory('nop', 'string') # 5501

a8 = memoria.storeConstantToMemory('sip', 'string') # 3500

a9 = memoria.storeVariableToMemory(4, 'int') # 3

a10 = memoria.storeVariableToMemory('true', 'bool') # 1000

a11 = memoria.storeTempToMemory(2.0, 'float') # 4500

a12 = memoria.storeConstantToMemory(5, 'int') # 2000

a13 = memoria.storeVariableToMemory(6, 'int') # 4


# print memoria.memoryBlock
'''
print (a1, 'int')
print (a2, 'bool')
print (a3, 'string')
print (a4, 'int')
print (a5, 'float')
print (a6, 'int')
print (a7, 'string')
print (a8, 'string')
print (a9, 'int')
print (a10, 'bool')
print (a11, 'float')
print (a12, 'int')
print (a13, 'int')
'''
print (memoria.getValueByAddress(1))
memoria.deleteValueByAddress(2)
print (memoria.getValueByAddress(2))