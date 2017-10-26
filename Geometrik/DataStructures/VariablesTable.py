class vars_Table:
    def __init__(self):
        self.variables = {
            'total':
                {
                    'int': 0,
                    'float': 0,
                    'boolean': 0,
                    'string': 0
                },
            'temporal_total':
                {
                    'int': 0,
                    'float': 0,
                    'boolean': 0,
                    'string': 0
                }
        }

    # Insert new variable to the table
    def insert(self, name, type, virtualAddress):
        self.variables[name] = [type, virtualAddress]
        self.addVariableToTotal(type)

    # Check if variable exists
    def lookup(self, name):
        return self.variables.has_key(name)

    # Return variable's values
    def get(self, name):
        if self.variables.has_key(name):
            return (name, self.variables[name])
        else:
            return None

    # Return the total of variables
    def getTotalVariables(self):
        return self.variables['total']

    # Return the total of temporals
    def getTotalTemporals(self):
        return self.variables['temporal_total']

    # Increment the amount of variables of a given type
    def addVariableToTotal(self, type):
        totals = self.variables['total']
        totals[type] += 1

    # Increment the amount of temporals of a given type
    def addTempToTotal(self, type):
        temp_totals = self.variables['temporal_total']
        temp_totals[type] += 1

    # Search by virtual address and return id if exists
    def getIdByAddress(self, virtualAddress):
        for variable in self.variables:
            if variable != 'total' and variable != 'temporal_total':
                variableInfo = self.variables[variable]

                if virtualAddress in variableInfo:
                    return variable