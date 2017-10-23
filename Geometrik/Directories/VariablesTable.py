class VarsTable:
    def __init__(self):
        self.variables = {
            'total':
                {
                    'int': 0,
                    'float': 0,
                    'boolean': 0,
                    'string': 0
                },
            'temp_total':
                {
                    'int': 0,
                    'float': 0,
                    'boolean': 0,
                    'string': 0
                }
        }

    def insert(self, name, Type, virtualAddress):
        self.variables[name] = [Type, virtualAddress]
        self.addVarsTotals(Type)

    def lookup(self, name):
        return self.variables.has_key(name)

    def get(self, name):
        if self.variables.has_key(name):
            return (name, self.variables[name])
        else:
            return None

    def getVarsTotals(self):
        return self.variables['total']

    def getTempTotals(self):
        return self.variables['temp_total']

    def addVarsTotals(self, Type):
        totals = self.variables['total']
        totals[Type] += 1

    def addTempType(self, Type):
        temp_totals = self.variables['temp_total']
        temp_totals[Type] += 1

    def getIdByAddress(self, virtualAddress):
        for variable in self.variables:
            if variable != 'total' and variable != 'temp_total':
                variableInfo = self.variables[variable]

                if virtualAddress in variableInfo:
                    return variable

    def addDimensionToVariable(self, name, dimension):

        # if len(self.variables[variableName]) > 2:
        #     variableProperties = self.variables[variableName]
        #
        #     dimensions = variableProperties[2]
        #
        #     dimensions[2] =

        self.variables[name].append({
            'dimensions': {
                1
                : dimension
            }
        })

    def getDimensionsFromVariable(self, name):
        try:
            variable = self.variables[name]
        except (KeyError):
            return None

        if len(self.variables[name]) > 2:
            variableProperties = self.variables[name]

            return variableProperties[2]
        else:
            return None