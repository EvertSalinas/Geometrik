
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQUALNOTEQUALleftLESSERGREATERLESSEROREQUALGREATEROREQUALleftPLUSMINUSleftTIMESDEVIDEnonassocLPARENRPARENID PLUS MINUS TIMES DEVIDE ASSIGN EQUAL NOTEQUAL GREATER LESSER GREATEROREQUAL LESSEROREQUAL AND OR NOT LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE COMMA COLON SEMICOLON INT STRING FLOAT BLUE DRAWTRIANGLE FALSE INTTYPE FLOATTYPE DRAWCURVE BOOLEANTYPE BLACK RED IF BROWN DRAWLINE PROGRAM PRINT INPUT MAIN FUNCTION RETURN STRINGTYPE DRAWPOLYGON VOID ELSE BREAK VAR GREEN TRUE YELLOW DRAWSQUARE WHILE DRAWCIRCLE\n    program : PROGRAM MAIN SEMICOLON programvars programfunction block\n            | condition\n    \n    programvars : vars programvars\n                | empty\n    \n    programfunction : function programfunction\n                    | empty\n    \n    block : LBRACE blockprima RBRACE\n    \n    blockprima : statute blockprima\n               | empty\n    \n    statute : assignment\n            | condition\n            | write\n            | read\n            | cycle\n            | functioncall\n            | predefined\n            | return\n    \n    condition : IF LPAREN conditionprima RPAREN block\n    \n    conditionprima : condprimaaux\n                   | NOT condprimaaux\n    \n    condprimaaux : functioncall\n                 | singularexp2\n    \n    vars : VAR type varsprima SEMICOLON\n    \n    varsprima : ID\n              | ID COMMA varsprima\n              | empty\n    \n    type : INTTYPE\n         | FLOATTYPE\n         | STRINGTYPE\n         | BOOLEANTYPE\n         | array\n    \n    array : INTTYPE arrayprima\n          | FLOATTYPE arrayprima\n          | STRINGTYPE arrayprima\n    \n    arrayprima : LBRACKET INT RBRACKET\n    \n    assignment : ID assignmentarray ASSIGN assignmentprima SEMICOLON\n    \n    assignmentarray : empty\n                    | LBRACKET singularexp2 RBRACKET\n    \n    assignmentprima : functioncall\n                    | singularexp2\n    \n    singularexp2 : singularexp\n                 | NOT singularexp\n\n    \n    singularexp : singularexp AND expression\n                | singularexp OR expression\n                | expression\n    \n    expression : expression LESSER exp\n               | expression GREATER exp\n               | expression EQUAL exp\n               | expression NOTEQUAL exp\n               | expression LESSEROREQUAL exp\n               | expression GREATEROREQUAL exp\n               | exp\n    \n    exp : exp PLUS term\n        | exp MINUS term\n        | term\n    \n    term : term TIMES factor\n         | term DEVIDE factor\n         | factor\n    \n    factor : LPAREN singularexp2 RPAREN\n           | PLUS constant\n           | MINUS constant\n           | constant\n    \n    constant : ID constantprima\n             | FLOAT\n             | INT\n    \n    constantprima : empty\n                  | LBRACKET singularexp2 RBRACKET\n    \n    functioncall : ID LPAREN funcparam RPAREN SEMICOLON\n    \n    funcparam : empty\n              | singularexp2\n              | singularexp COMMA funcparam\n    \n    function : FUNCTION VOID ID LPAREN parameter RPAREN block\n             | FUNCTION type ID LPAREN parameter RPAREN block\n    \n    return : RETURN singularexp2 SEMICOLON\n    \n    parameter : empty\n              | parameterprima\n    \n    parameterprima : type ID\n                   | type ID COMMA parameterprima\n    \n    write : PRINT LPAREN singularexp2 RPAREN SEMICOLON\n    \n    read : ID ASSIGN INPUT SEMICOLON\n    \n    cycle : WHILE LPAREN singularexp2 RPAREN block\n    \n    color : BLUE\n          | GREEN\n          | RED\n          | YELLOW\n          | BROWN\n          | BLACK\n    \n    predefined : drawline\n               | drawsquare\n               | drawtriangle\n               | drawcircle\n               | drawcurve\n               | drawpolygon\n    \n    drawline : DRAWLINE LPAREN singularexp2  COMMA singularexp2  COMMA singularexp2  COMMA singularexp2  COMMA color RPAREN SEMICOLON\n    \n    drawsquare : DRAWSQUARE LPAREN singularexp2  COMMA singularexp2 COMMA color RPAREN SEMICOLON\n    \n    drawtriangle : DRAWTRIANGLE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON\n    \n    drawcircle : DRAWCIRCLE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON\n    \n    drawcurve : DRAWCURVE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON\n    \n    drawpolygon : DRAWPOLYGON LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON\n    \n    empty :\n    '
    
_lr_action_items = {'NOTEQUAL':([8,14,16,17,18,19,22,24,32,33,34,37,40,66,67,68,75,76,77,78,79,80,81,82,83,84,123,],[-62,-58,-100,-55,-65,-64,-52,47,-61,-100,-60,-63,-66,47,47,-59,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'DRAWTRIANGLE':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[98,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,98,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'RETURN':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[97,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,97,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'VOID':([61,],[94,]),'EQUAL':([8,14,16,17,18,19,22,24,32,33,34,37,40,66,67,68,75,76,77,78,79,80,81,82,83,84,123,],[-62,-58,-100,-55,-65,-64,-52,50,-61,-100,-60,-63,-66,50,50,-59,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'YELLOW':([197,198,199,201,202,228,],[207,207,207,207,207,207,]),'LBRACKET':([16,33,54,55,56,116,],[38,38,85,85,85,140,]),'WHILE':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[99,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,99,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'PROGRAM':([0,],[3,]),'BLACK':([197,198,199,201,202,228,],[209,209,209,209,209,209,]),'PRINT':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[100,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,100,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'MINUS':([6,8,14,15,16,17,18,19,22,23,30,31,32,33,34,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,68,75,76,77,78,79,80,81,82,83,84,97,123,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[12,-62,-58,12,-100,-55,-65,-64,44,12,12,12,-61,-100,-60,12,-63,12,12,-66,12,12,12,12,12,12,12,12,12,12,-59,-57,-56,-53,-54,44,44,44,44,44,44,12,-67,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'RED':([197,198,199,201,202,228,],[210,210,210,210,210,210,]),'STRINGTYPE':([27,61,150,151,194,],[54,54,54,54,54,]),'RPAREN':([8,9,10,11,14,16,17,18,19,20,21,22,24,32,33,34,35,37,39,40,45,46,66,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,123,124,146,147,150,151,154,155,165,166,167,168,182,203,204,205,206,207,208,209,210,211,212,214,215,229,],[-62,-22,29,-41,-58,-100,-55,-65,-64,-19,-21,-52,-45,-61,-100,-60,68,-63,-100,-66,-41,-20,-43,-44,-59,-42,-70,-41,-69,125,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,-100,-71,-68,-100,-100,170,171,-75,-76,183,184,-77,-78,-82,-86,216,-85,-83,-87,-84,217,218,220,221,230,]),'SEMICOLON':([5,8,11,14,16,17,18,19,22,24,32,33,34,37,40,54,55,56,57,58,59,66,67,68,69,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,123,125,128,131,147,148,149,159,171,177,178,179,216,217,218,220,221,230,],[7,-62,-41,-58,-100,-55,-65,-64,-52,-45,-61,-100,-60,-63,-66,-29,-27,-28,-30,-100,-31,-43,-44,-59,-42,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-34,-32,-33,127,-24,-26,-67,147,-100,152,-68,-35,-25,175,187,-40,191,-39,222,223,224,226,227,231,]),'DRAWLINE':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[115,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,115,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'DEVIDE':([8,14,16,17,18,19,32,33,34,37,40,68,75,76,77,78,123,],[-62,-58,-100,41,-65,-64,-61,-100,-60,-63,-66,-59,-57,-56,41,41,-67,]),'DRAWSQUARE':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[106,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,106,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'PLUS':([6,8,14,15,16,17,18,19,22,23,30,31,32,33,34,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,68,75,76,77,78,79,80,81,82,83,84,97,123,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[13,-62,-58,13,-100,-55,-65,-64,43,13,13,13,-61,-100,-60,13,-63,13,13,-66,13,13,13,13,13,13,13,13,13,13,-59,-57,-56,-53,-54,43,43,43,43,43,43,13,-67,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'COMMA':([8,11,14,17,18,19,22,24,32,33,34,37,40,66,67,68,69,72,75,76,77,78,79,80,81,82,83,84,90,123,153,156,157,158,162,163,182,185,188,189,190,192,193,213,225,],[-62,-41,-58,-55,-65,-64,-52,-45,-61,-100,-60,-63,-66,-43,-44,-59,-42,124,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,128,-67,169,172,173,174,180,181,194,197,198,199,200,201,202,219,228,]),'ASSIGN':([116,141,142,176,],[139,161,-37,-38,]),'$end':([1,2,65,95,135,],[0,-2,-18,-1,-7,]),'FUNCTION':([7,25,26,28,53,60,127,135,195,196,],[-100,-100,-4,61,-3,61,-23,-7,-73,-72,]),'BLUE':([197,198,199,201,202,228,],[204,204,204,204,204,204,]),'RBRACE':([64,65,96,101,102,104,105,107,108,109,110,111,112,113,114,117,118,121,122,135,143,147,152,175,186,187,191,222,223,224,226,227,231,],[-100,-18,-90,-16,135,-88,-12,-91,-14,-9,-17,-93,-13,-10,-92,-11,-100,-89,-15,-7,-8,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'FLOATTYPE':([27,61,150,151,194,],[56,56,56,56,56,]),'TIMES':([8,14,16,17,18,19,32,33,34,37,40,68,75,76,77,78,123,],[-62,-58,-100,42,-65,-64,-61,-100,-60,-63,-66,-59,-57,-56,42,42,-67,]),'LPAREN':([4,6,15,16,23,30,31,36,38,39,41,42,43,44,47,48,49,50,51,52,97,98,99,100,103,106,115,116,119,120,124,129,130,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[6,15,15,39,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,132,133,134,136,137,138,39,144,145,15,150,151,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'VAR':([7,25,127,],[27,27,-23,]),'INPUT':([139,],[159,]),'ID':([6,12,13,15,23,30,31,36,38,39,41,42,43,44,47,48,49,50,51,52,54,55,56,57,58,59,64,65,86,87,88,93,94,96,97,101,104,105,107,108,110,111,112,113,114,117,118,121,122,124,128,132,133,134,135,136,137,138,140,144,145,147,148,152,161,164,169,172,173,174,175,180,181,186,187,191,200,219,222,223,224,226,227,231,],[16,33,33,33,16,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-29,-27,-28,-30,90,-31,116,-18,-34,-32,-33,129,130,-90,33,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,116,-89,-15,33,90,33,33,33,-7,33,33,33,33,33,33,-68,-35,-74,16,182,33,33,33,33,-80,33,33,-81,-79,-36,33,33,-96,-97,-95,-99,-98,-94,]),'IF':([0,64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[4,4,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,4,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'AND':([8,11,14,16,17,18,19,22,24,32,33,34,37,40,45,66,67,68,69,72,75,76,77,78,79,80,81,82,83,84,123,],[-62,30,-58,-100,-55,-65,-64,-52,-45,-61,-100,-60,-63,-66,30,-43,-44,-59,30,30,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'LBRACE':([7,25,26,28,29,53,60,62,63,92,127,135,170,183,184,195,196,],[-100,-100,-4,-100,64,-3,-100,-6,64,-5,-23,-7,64,64,64,-73,-72,]),'INTTYPE':([27,61,150,151,194,],[55,55,55,55,55,]),'GREATER':([8,14,16,17,18,19,22,24,32,33,34,37,40,66,67,68,75,76,77,78,79,80,81,82,83,84,123,],[-62,-58,-100,-55,-65,-64,-52,48,-61,-100,-60,-63,-66,48,48,-59,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'DRAWPOLYGON':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[119,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,119,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'INT':([6,12,13,15,23,30,31,36,38,39,41,42,43,44,47,48,49,50,51,52,85,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,126,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'LESSEROREQUAL':([8,14,16,17,18,19,22,24,32,33,34,37,40,66,67,68,75,76,77,78,79,80,81,82,83,84,123,],[-62,-58,-100,-55,-65,-64,-52,49,-61,-100,-60,-63,-66,49,49,-59,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'FLOAT':([6,12,13,15,23,30,31,36,38,39,41,42,43,44,47,48,49,50,51,52,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'DRAWCURVE':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[120,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,120,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'LESSER':([8,14,16,17,18,19,22,24,32,33,34,37,40,66,67,68,75,76,77,78,79,80,81,82,83,84,123,],[-62,-58,-100,-55,-65,-64,-52,51,-61,-100,-60,-63,-66,51,51,-59,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'DRAWCIRCLE':([64,65,96,101,104,105,107,108,110,111,112,113,114,117,118,121,122,135,147,152,175,186,187,191,222,223,224,226,227,231,],[103,-18,-90,-16,-88,-12,-91,-14,-17,-93,-13,-10,-92,-11,103,-89,-15,-7,-68,-74,-80,-81,-79,-36,-96,-97,-95,-99,-98,-94,]),'GREATEROREQUAL':([8,14,16,17,18,19,22,24,32,33,34,37,40,66,67,68,75,76,77,78,79,80,81,82,83,84,123,],[-62,-58,-100,-55,-65,-64,-52,52,-61,-100,-60,-63,-66,52,52,-59,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'BOOLEANTYPE':([27,61,150,151,194,],[57,57,57,57,57,]),'NOT':([6,15,23,38,39,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[23,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'GREEN':([197,198,199,201,202,228,],[208,208,208,208,208,208,]),'RBRACKET':([8,11,14,17,18,19,22,24,32,33,34,37,40,66,67,68,69,70,75,76,77,78,79,80,81,82,83,84,123,126,160,],[-62,-41,-58,-55,-65,-64,-52,-45,-61,-100,-60,-63,-66,-43,-44,-59,-42,123,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,148,176,]),'MAIN':([3,],[5,]),'OR':([8,11,14,16,17,18,19,22,24,32,33,34,37,40,45,66,67,68,69,72,75,76,77,78,79,80,81,82,83,84,123,],[-62,31,-58,-100,-55,-65,-64,-52,-45,-61,-100,-60,-63,-66,31,-43,-44,-59,31,31,-57,-56,-53,-54,-49,-47,-50,-48,-46,-51,-67,]),'BROWN':([197,198,199,201,202,228,],[205,205,205,205,205,205,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([28,60,],[60,60,]),'drawtriangle':([64,118,],[96,96,]),'constant':([6,12,13,15,23,30,31,36,38,39,41,42,43,44,47,48,49,50,51,52,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[8,32,34,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'vars':([7,25,],[25,25,]),'color':([197,198,199,201,202,228,],[206,211,212,214,215,229,]),'singularexp2':([6,15,23,38,39,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[9,35,9,70,71,131,71,153,154,155,156,157,158,160,162,163,177,185,188,189,190,192,193,213,225,]),'assignmentprima':([161,],[178,]),'assignmentarray':([116,],[141,]),'return':([64,118,],[110,110,]),'array':([27,61,150,151,194,],[59,59,59,59,59,]),'singularexp':([6,15,23,36,38,39,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[11,11,45,69,11,72,11,72,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'conditionprima':([6,],[10,]),'predefined':([64,118,],[101,101,]),'blockprima':([64,118,],[102,143,]),'arrayprima':([54,55,56,],[86,87,88,]),'varsprima':([58,128,],[89,149,]),'drawline':([64,118,],[104,104,]),'write':([64,118,],[105,105,]),'program':([0,],[1,]),'programvars':([7,25,],[28,53,]),'factor':([6,15,23,30,31,36,38,39,41,42,43,44,47,48,49,50,51,52,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[14,14,14,14,14,14,14,14,75,76,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'drawcircle':([64,118,],[107,107,]),'type':([27,61,150,151,194,],[58,93,164,164,164,]),'empty':([7,16,25,28,33,39,58,60,64,116,118,124,128,150,151,],[26,40,26,62,40,73,91,62,109,142,109,73,91,165,165,]),'constantprima':([16,33,],[37,37,]),'funcparam':([39,124,],[74,146,]),'drawpolygon':([64,118,],[111,111,]),'read':([64,118,],[112,112,]),'assignment':([64,118,],[113,113,]),'drawcurve':([64,118,],[114,114,]),'programfunction':([28,60,],[63,92,]),'parameterprima':([150,151,194,],[166,166,203,]),'condition':([0,64,118,],[2,117,117,]),'cycle':([64,118,],[108,108,]),'statute':([64,118,],[118,118,]),'term':([6,15,23,30,31,36,38,39,43,44,47,48,49,50,51,52,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[17,17,17,17,17,17,17,17,77,78,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'parameter':([150,151,],[167,168,]),'drawsquare':([64,118,],[121,121,]),'functioncall':([6,23,64,118,161,],[21,21,122,122,179,]),'exp':([6,15,23,30,31,36,38,39,47,48,49,50,51,52,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[22,22,22,22,22,22,22,22,79,80,81,82,83,84,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'expression':([6,15,23,30,31,36,38,39,97,124,132,133,134,136,137,138,140,144,145,161,169,172,173,174,180,181,200,219,],[24,24,24,66,67,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'condprimaaux':([6,23,],[20,46,]),'block':([29,63,170,183,184,],[65,95,186,195,196,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM MAIN SEMICOLON programvars programfunction block','program',6,'p_PROGRAM','parserYacc.py',17),
  ('program -> condition','program',1,'p_PROGRAM','parserYacc.py',18),
  ('programvars -> vars programvars','programvars',2,'p_PROGRAMVARS','parserYacc.py',24),
  ('programvars -> empty','programvars',1,'p_PROGRAMVARS','parserYacc.py',25),
  ('programfunction -> function programfunction','programfunction',2,'p_PROGRAMFUNCTION','parserYacc.py',30),
  ('programfunction -> empty','programfunction',1,'p_PROGRAMFUNCTION','parserYacc.py',31),
  ('block -> LBRACE blockprima RBRACE','block',3,'p_BLOCK','parserYacc.py',36),
  ('blockprima -> statute blockprima','blockprima',2,'p_BLOCKPRIMA','parserYacc.py',41),
  ('blockprima -> empty','blockprima',1,'p_BLOCKPRIMA','parserYacc.py',42),
  ('statute -> assignment','statute',1,'p_STATUTE','parserYacc.py',47),
  ('statute -> condition','statute',1,'p_STATUTE','parserYacc.py',48),
  ('statute -> write','statute',1,'p_STATUTE','parserYacc.py',49),
  ('statute -> read','statute',1,'p_STATUTE','parserYacc.py',50),
  ('statute -> cycle','statute',1,'p_STATUTE','parserYacc.py',51),
  ('statute -> functioncall','statute',1,'p_STATUTE','parserYacc.py',52),
  ('statute -> predefined','statute',1,'p_STATUTE','parserYacc.py',53),
  ('statute -> return','statute',1,'p_STATUTE','parserYacc.py',54),
  ('condition -> IF LPAREN conditionprima RPAREN block','condition',5,'p_CONDITION','parserYacc.py',59),
  ('conditionprima -> condprimaaux','conditionprima',1,'p_CONDITIONPRIMA','parserYacc.py',64),
  ('conditionprima -> NOT condprimaaux','conditionprima',2,'p_CONDITIONPRIMA','parserYacc.py',65),
  ('condprimaaux -> functioncall','condprimaaux',1,'p_CONDPRIMAAUX','parserYacc.py',70),
  ('condprimaaux -> singularexp2','condprimaaux',1,'p_CONDPRIMAAUX','parserYacc.py',71),
  ('vars -> VAR type varsprima SEMICOLON','vars',4,'p_VARS','parserYacc.py',76),
  ('varsprima -> ID','varsprima',1,'p_VARSPRIMA','parserYacc.py',81),
  ('varsprima -> ID COMMA varsprima','varsprima',3,'p_VARSPRIMA','parserYacc.py',82),
  ('varsprima -> empty','varsprima',1,'p_VARSPRIMA','parserYacc.py',83),
  ('type -> INTTYPE','type',1,'p_TYPE','parserYacc.py',88),
  ('type -> FLOATTYPE','type',1,'p_TYPE','parserYacc.py',89),
  ('type -> STRINGTYPE','type',1,'p_TYPE','parserYacc.py',90),
  ('type -> BOOLEANTYPE','type',1,'p_TYPE','parserYacc.py',91),
  ('type -> array','type',1,'p_TYPE','parserYacc.py',92),
  ('array -> INTTYPE arrayprima','array',2,'p_ARRAY','parserYacc.py',97),
  ('array -> FLOATTYPE arrayprima','array',2,'p_ARRAY','parserYacc.py',98),
  ('array -> STRINGTYPE arrayprima','array',2,'p_ARRAY','parserYacc.py',99),
  ('arrayprima -> LBRACKET INT RBRACKET','arrayprima',3,'p_ARRAYPRIMA','parserYacc.py',104),
  ('assignment -> ID assignmentarray ASSIGN assignmentprima SEMICOLON','assignment',5,'p_ASSIGNMENT','parserYacc.py',110),
  ('assignmentarray -> empty','assignmentarray',1,'p_ASSIGNMENT_ARRAY','parserYacc.py',115),
  ('assignmentarray -> LBRACKET singularexp2 RBRACKET','assignmentarray',3,'p_ASSIGNMENT_ARRAY','parserYacc.py',116),
  ('assignmentprima -> functioncall','assignmentprima',1,'p_ASSIGNMENT_PRIMA','parserYacc.py',121),
  ('assignmentprima -> singularexp2','assignmentprima',1,'p_ASSIGNMENT_PRIMA','parserYacc.py',122),
  ('singularexp2 -> singularexp','singularexp2',1,'p_S_EXPRESSION2','parserYacc.py',127),
  ('singularexp2 -> NOT singularexp','singularexp2',2,'p_S_EXPRESSION2','parserYacc.py',128),
  ('singularexp -> singularexp AND expression','singularexp',3,'p_S_EXPRESSION','parserYacc.py',134),
  ('singularexp -> singularexp OR expression','singularexp',3,'p_S_EXPRESSION','parserYacc.py',135),
  ('singularexp -> expression','singularexp',1,'p_S_EXPRESSION','parserYacc.py',136),
  ('expression -> expression LESSER exp','expression',3,'p_EXPRESSION','parserYacc.py',141),
  ('expression -> expression GREATER exp','expression',3,'p_EXPRESSION','parserYacc.py',142),
  ('expression -> expression EQUAL exp','expression',3,'p_EXPRESSION','parserYacc.py',143),
  ('expression -> expression NOTEQUAL exp','expression',3,'p_EXPRESSION','parserYacc.py',144),
  ('expression -> expression LESSEROREQUAL exp','expression',3,'p_EXPRESSION','parserYacc.py',145),
  ('expression -> expression GREATEROREQUAL exp','expression',3,'p_EXPRESSION','parserYacc.py',146),
  ('expression -> exp','expression',1,'p_EXPRESSION','parserYacc.py',147),
  ('exp -> exp PLUS term','exp',3,'p_EXP','parserYacc.py',152),
  ('exp -> exp MINUS term','exp',3,'p_EXP','parserYacc.py',153),
  ('exp -> term','exp',1,'p_EXP','parserYacc.py',154),
  ('term -> term TIMES factor','term',3,'p_TERM','parserYacc.py',159),
  ('term -> term DEVIDE factor','term',3,'p_TERM','parserYacc.py',160),
  ('term -> factor','term',1,'p_TERM','parserYacc.py',161),
  ('factor -> LPAREN singularexp2 RPAREN','factor',3,'p_FACTOR','parserYacc.py',166),
  ('factor -> PLUS constant','factor',2,'p_FACTOR','parserYacc.py',167),
  ('factor -> MINUS constant','factor',2,'p_FACTOR','parserYacc.py',168),
  ('factor -> constant','factor',1,'p_FACTOR','parserYacc.py',169),
  ('constant -> ID constantprima','constant',2,'p_CONSTANT','parserYacc.py',174),
  ('constant -> FLOAT','constant',1,'p_CONSTANT','parserYacc.py',175),
  ('constant -> INT','constant',1,'p_CONSTANT','parserYacc.py',176),
  ('constantprima -> empty','constantprima',1,'p_CONSTANTPRIMA','parserYacc.py',181),
  ('constantprima -> LBRACKET singularexp2 RBRACKET','constantprima',3,'p_CONSTANTPRIMA','parserYacc.py',182),
  ('functioncall -> ID LPAREN funcparam RPAREN SEMICOLON','functioncall',5,'p_FUNCTIONCALL','parserYacc.py',188),
  ('funcparam -> empty','funcparam',1,'p_FUNCPARAM','parserYacc.py',194),
  ('funcparam -> singularexp2','funcparam',1,'p_FUNCPARAM','parserYacc.py',195),
  ('funcparam -> singularexp COMMA funcparam','funcparam',3,'p_FUNCPARAM','parserYacc.py',196),
  ('function -> FUNCTION VOID ID LPAREN parameter RPAREN block','function',7,'p_FUNCTION','parserYacc.py',201),
  ('function -> FUNCTION type ID LPAREN parameter RPAREN block','function',7,'p_FUNCTION','parserYacc.py',202),
  ('return -> RETURN singularexp2 SEMICOLON','return',3,'p_RETURN','parserYacc.py',207),
  ('parameter -> empty','parameter',1,'p_PARAMETER','parserYacc.py',212),
  ('parameter -> parameterprima','parameter',1,'p_PARAMETER','parserYacc.py',213),
  ('parameterprima -> type ID','parameterprima',2,'p_PARAMETERPRIMA','parserYacc.py',218),
  ('parameterprima -> type ID COMMA parameterprima','parameterprima',4,'p_PARAMETERPRIMA','parserYacc.py',219),
  ('write -> PRINT LPAREN singularexp2 RPAREN SEMICOLON','write',5,'p_WRITE','parserYacc.py',224),
  ('read -> ID ASSIGN INPUT SEMICOLON','read',4,'p_READ','parserYacc.py',229),
  ('cycle -> WHILE LPAREN singularexp2 RPAREN block','cycle',5,'p_CYCLE','parserYacc.py',234),
  ('color -> BLUE','color',1,'p_COLOR','parserYacc.py',239),
  ('color -> GREEN','color',1,'p_COLOR','parserYacc.py',240),
  ('color -> RED','color',1,'p_COLOR','parserYacc.py',241),
  ('color -> YELLOW','color',1,'p_COLOR','parserYacc.py',242),
  ('color -> BROWN','color',1,'p_COLOR','parserYacc.py',243),
  ('color -> BLACK','color',1,'p_COLOR','parserYacc.py',244),
  ('predefined -> drawline','predefined',1,'p_PREDEFINED','parserYacc.py',249),
  ('predefined -> drawsquare','predefined',1,'p_PREDEFINED','parserYacc.py',250),
  ('predefined -> drawtriangle','predefined',1,'p_PREDEFINED','parserYacc.py',251),
  ('predefined -> drawcircle','predefined',1,'p_PREDEFINED','parserYacc.py',252),
  ('predefined -> drawcurve','predefined',1,'p_PREDEFINED','parserYacc.py',253),
  ('predefined -> drawpolygon','predefined',1,'p_PREDEFINED','parserYacc.py',254),
  ('drawline -> DRAWLINE LPAREN singularexp2 COMMA singularexp2 COMMA singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON','drawline',13,'p_DRAWLINE','parserYacc.py',259),
  ('drawsquare -> DRAWSQUARE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON','drawsquare',9,'p_DRAWSQUARE','parserYacc.py',264),
  ('drawtriangle -> DRAWTRIANGLE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON','drawtriangle',9,'p_DRAWTRIANGLE','parserYacc.py',269),
  ('drawcircle -> DRAWCIRCLE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON','drawcircle',9,'p_DRAWCIRCLE','parserYacc.py',274),
  ('drawcurve -> DRAWCURVE LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON','drawcurve',9,'p_DRAWCURVE','parserYacc.py',279),
  ('drawpolygon -> DRAWPOLYGON LPAREN singularexp2 COMMA singularexp2 COMMA color RPAREN SEMICOLON','drawpolygon',9,'p_DRAWPOLYGON','parserYacc.py',284),
  ('empty -> <empty>','empty',0,'p_EMPTY','parserYacc.py',292),
]