from VariablesTable import VarsTable

class FunctionsDirectory:
    def __init__(self):
        self.functions = {}

    # Insert function to the directory
    def insert(self, functionName, type):
        self.functions[functionName] = {'type': type, 'parameters_types':[], 'parameter_addresses': [], 'variables': VarsTable()}

    # check if function exists
    def lookup(self, functionName):
        return self.functions.has_key(functionName)

    # Return the type of a function
    def getFunctionType(self, functionName):
        function = self.functions[functionName]
        return function['type']

    # Add list of parameter types to a function record
    def addParameterTypes(self, functionName, parameterTypeList):
        if self.functionExists(functionName):
            function = self.functions[functionName]
            function['parameters_types'] += parameterTypeList

    # Add list of parameter addresses to a function record
    def addParameterAddress(self, functionName, parameterAddressList):
        if self.functionExists(functionName):
            function = self.functions[functionName]
            function['parameter_addresses'] += parameterAddressList

    # Return list of parameter types
    def getParameterTypes(self, functionName):
        function = self.functions[functionName]
        return function['parameters_types']

    # Return list of parameter addresses
    def getParameterAddresses(self, functionName):
        function = self.functions[functionName]
        return function['parameter_addresses']

    # Validate parameters types match from functioncall
    def validateParameters(self, functionName, argumentTypeList):
        function = self.functions[functionName]

        if self.functionExists(functionName):
            return function['parameters_types'] == argumentTypeList

    # Add starting quadruple
    def addStartingQuad(self, functionName, quadruple):
        function = self.functions[functionName]
        function['starting_quadruple'] = quadruple

    # Return starting quadruple
    def getFunctionStartingQuad(self, functionName):
        function = self.functions[functionName]
        return function['starting_quadruple']

    # Insert variable to the VarsTable of a function
    def addFunctionVariable(self, functionName, variableName, variableType, address):
        function = self.functions[functionName]

        if function['variables'].lookup(variableName):
            return False
        else:
            function['variables'].insert(variableName, variableType, address)
            return True

    # Return variable from a VarsTable of a function
    def getVariable(self, functionName, variableName):
        function = self.functions[functionName]
        variables = function["variables"]

        variable = variables.get(variableName)

        return variable

    # Insert temporal variable to the VarsTable of a function
    def addTempVariable(self, functionName, variableType):
        function = self.functions[functionName]
        function['variables'].addTempToTotal(variableType)

    # Search by virtual address and return id if exists
    def getFunctionIdByAddress(self, globalScopeName, virtualAddress):
        function = self.functions[globalScopeName]
        return function['variables'].getIdByAddress(virtualAddress)

    # Add dimensions to a variable if it is an array
    def addDimensionToVariable(self, functionName, variableName, dimension):
        function = self.functions[functionName]
        function['variables'].addDimensionToVariable(variableName, dimension)

    # Return the dimensions from a variable
    def getDimensions(self, functionName, variableName):
        function = self.functions[functionName]
        return function['variables'].getDimensionsFromVariable(variableName)