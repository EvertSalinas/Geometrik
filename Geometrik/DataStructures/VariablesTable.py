class vars_Table:
    def __init__(self):
        self.variables = {}

    # Insert new variable to the table
    def insert(self, name, type, virtualAddress):
        self.variables[name] = [type, virtualAddress]

    # Check if variable exists
    def lookup(self, name):
        return self.variables.has_key(name)

    # Return variable's values
    def get(self, name):
        if self.variables.has_key(name):
            return (name, self.variables[name])
        else:
            return None

    # Search by virtual address and return id if exists
    def getIdByAddress(self, virtualAddress):
        for variable in self.variables:
            variableInfo = self.variables[variable]
            if virtualAddress in variableInfo:
                return variable