file = open("Lab1code.txt")  # Inserting Code Text file
keywords = ['auto', 'break', 'case', 'char',
            'const', 'continue', 'default', 'do',
            'double', 'else', 'enum', 'extern',
            'float', 'for', 'goto', 'if',
            'int', 'long', 'register', 'return',
            'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union',
            'unsigned', 'void', 'volatile', 'while']
operators = ['+', '-', '/', '*', '=']
logicalOperator = ['<', '>']

all = [] # All Lines will be stored here, by Spliting properly
for line in file:
    instruction = line
    instruction = instruction.rstrip()
    instruction = instruction.split(' ')
    for t in range(len(instruction)):
        if ',' in instruction[t] and len(instruction[t]) != 1:
            instruction[t] = instruction[t].split(',')
            instruction[t][-1] = ','
        if ';' in instruction[t] and len(instruction[t]) != 1:
            instruction[t] = instruction[t].split(';')
            instruction[t][-1] = ';'
        if '\t' in instruction[t] and len(instruction[t]) != 1:
            instruction[t] = instruction[t].split('\t')
        if '(' in instruction[t] and len(instruction[t]) != 1:
            instruction[t] = instruction[t].split('(')
            instruction[t][-1] = '('
        if ')' in instruction[t] and len(instruction[t]) != 1:
            instruction[t] = instruction[t].split(')')
            instruction[t][-1] = ')'
    while ("" in instruction):
        instruction.remove("")   # Space Removed
    for i in range(len(instruction)):
        if type(instruction[i]) == list:
            if "" in instruction[i]:
                instruction[i].remove('')  # Space Removed
    temp = []
    for v in instruction:
        if type(v) == str:
            temp.append(v)
        elif type(v) == list:
            for t in v:
                temp.append(t)
    instruction = temp
    all.append(instruction)

# Result Lists
key = []
identifiers = []
mathOpertor = []
logicop = []
numbers = []
others = []

# Checking if the token is a floating value
def checkFloat(element):
    try:
        float(element)
        return True
    except:
        return False

#Checking if Keyword
def isKeyword(element):
    if element.lower() in keywords:
        return True
    return False

#Checking if Math Operator
def isMathOperator(element):
    if element in operators:
        return True
    return False

#Checking if Logical Operator
def isLogicalOperator(element):
    if element in logicalOperator:
        return True
    return False

#Checking if Digit
def isDigit(element):
    if element.isnumeric() or checkFloat(element):
        return True
    return False

#Checking if Others
def isOthers(element):
    if element in [',', ';', '(', ')', '{', '}']:
        return True
    return False

#Checking if Identifier
def isIdentifier(element):
    if element not in (keywords and operators and logicalOperator):
        if element[0].isalpha():
            if element[-1].isnumeric() or element[-1].isalpha():
                return True
            return False
        return False
    return False

#Seperating the elements to the coresponding result list.
for line in all:
    for element in line:
        if isKeyword(element):
            key.append(element)
        elif isMathOperator(element):
            if element not in mathOpertor:
                mathOpertor.append(element)
        elif isLogicalOperator(element):
            if element not in logicop:
                logicop.append(element)
        elif isDigit(element):
            numbers.append(element)
        elif isOthers(element):
            if element not in others:
                others.append(element)
        elif isIdentifier(element):
            if element not in identifiers:
                identifiers.append(element)

# Prining all the results
print("Keywords: ",end="")
print(*key, sep=",")
print("Identifiers: ",end="")
print(*identifiers, sep=",")
print("Math Operators: ",end="")
print(*mathOpertor, sep=",")
print("Logical Operators: ",end="")
print(*logicop, sep=",")
print("Numerical Values: ",end="")
print(*numbers, sep=",")
print("Others: ",end="")
print(*others, sep="")