
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'progAND BOOLDCL BOOLVAL DIVIDE ELIF ELSE EQ FLOATDCL FNUMBER FOR GE GT IF INTDCL INUMBER LE LPAREN LT MINUS NAME NE OR PLUS POW PRINT RPAREN TIMES WHILEprog : stmtsstmts : statement stmts\n            | statement statement : INTDCL NAME ";"\n                | INTDCL NAME "=" expression ";" statement : FLOATDCL NAME ";"\n                | FLOATDCL NAME "=" expression ";" statement : BOOLDCL NAME ";"\n                | BOOLDCL NAME "=" boolean_expression ";" statement : PRINT expression ";"statement : IF LPAREN boolean_expression RPAREN "{" stmts "}" elifs else elifs : elif elifs\n            | elif elif : ELIF LPAREN boolean_expression RPAREN "{" stmts "}"\n            | empty else : ELSE "{" stmts "}"\n            | empty statement : WHILE LPAREN boolean_expression RPAREN "{" stmts "}" statement : FOR LPAREN statement boolean_expression ";" step RPAREN "{" stmts "}"step : NAME PLUS "=" expression\n            | NAME MINUS "=" expression\n            | NAME TIMES "=" expression\n            | NAME DIVIDE "=" expression\n            | NAME PLUS PLUS\n            | NAME MINUS MINUS\n            | PLUS PLUS NAME\n            | MINUS MINUS NAMEstatement : NAME "=" expression ";"expression : LPAREN expression RPARENexpression : expression PLUS expression\n                | expression MINUS expression\n                | expression TIMES expression\n                | expression DIVIDE expression\n                | expression POW expression expression : INUMBERexpression : FNUMBERexpression : boolean_expressionboolean_expression : LPAREN boolean_expression RPARENboolean_expression : boolean_expression AND boolean_expression\n                        | boolean_expression OR boolean_expression\n                        | comparison\n                        | boolean_val comparison : expression EQ expression\n                | expression NE expression\n                | expression LT expression\n                | expression LE expression\n                | expression GT expression\n                | expression GE expression boolean_val : boolexp\n                    | NAME boolexp : BOOLVALexpression : NAMEempty :'
    
_lr_action_items = {'INTDCL':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[4,4,4,-4,-6,-8,-10,-28,-5,-7,-9,4,4,-53,-18,-53,-13,-15,4,-11,-17,-12,4,-19,-16,4,-14,]),'FLOATDCL':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[6,6,6,-4,-6,-8,-10,-28,-5,-7,-9,6,6,-53,-18,-53,-13,-15,6,-11,-17,-12,6,-19,-16,6,-14,]),'BOOLDCL':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[7,7,7,-4,-6,-8,-10,-28,-5,-7,-9,7,7,-53,-18,-53,-13,-15,7,-11,-17,-12,7,-19,-16,7,-14,]),'PRINT':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[8,8,8,-4,-6,-8,-10,-28,-5,-7,-9,8,8,-53,-18,-53,-13,-15,8,-11,-17,-12,8,-19,-16,8,-14,]),'IF':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[9,9,9,-4,-6,-8,-10,-28,-5,-7,-9,9,9,-53,-18,-53,-13,-15,9,-11,-17,-12,9,-19,-16,9,-14,]),'WHILE':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[10,10,10,-4,-6,-8,-10,-28,-5,-7,-9,10,10,-53,-18,-53,-13,-15,10,-11,-17,-12,10,-19,-16,10,-14,]),'FOR':([0,3,29,30,33,35,37,60,82,83,84,85,86,94,95,103,104,106,107,116,118,119,126,128,131,132,134,],[11,11,11,-4,-6,-8,-10,-28,-5,-7,-9,11,11,-53,-18,-53,-13,-15,11,-11,-17,-12,11,-19,-16,11,-14,]),'NAME':([0,3,4,6,7,8,14,18,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,60,82,83,84,85,86,87,94,95,101,102,103,104,106,107,109,111,112,113,116,118,119,120,126,128,131,132,134,],[5,5,13,15,16,22,22,22,56,56,5,-4,22,-6,22,-8,56,-10,22,22,22,22,22,22,22,22,22,22,22,56,56,22,56,-28,-5,-7,-9,5,5,91,-53,-18,114,115,-53,-13,-15,5,22,22,22,22,-11,-17,-12,56,5,-19,-16,5,-14,]),'$end':([1,2,3,12,30,33,35,37,60,82,83,84,94,95,103,104,106,116,118,119,128,131,134,],[0,-1,-3,-2,-4,-6,-8,-10,-28,-5,-7,-9,-53,-18,-53,-13,-15,-11,-17,-12,-19,-16,-14,]),'}':([3,12,30,33,35,37,60,82,83,84,88,89,94,95,103,104,106,116,118,119,121,128,129,131,133,134,],[-3,-2,-4,-6,-8,-10,-28,-5,-7,-9,94,95,-53,-18,-53,-13,-15,-11,-17,-12,128,-19,131,-16,134,-14,]),'=':([5,13,15,16,97,98,99,100,],[14,31,34,36,109,111,112,113,]),'LPAREN':([8,9,10,11,14,18,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,60,82,83,84,94,95,103,104,105,106,109,111,112,113,116,118,119,120,128,131,134,],[18,27,28,29,18,18,53,53,-4,18,-6,18,-8,53,-10,18,18,18,18,18,18,18,18,18,18,18,53,53,53,53,-28,-5,-7,-9,-53,-18,-53,-13,120,-15,18,18,18,18,-11,-17,-12,53,-19,-16,-14,]),'INUMBER':([8,14,18,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,60,82,83,84,94,95,103,104,106,109,111,112,113,116,118,119,120,128,131,134,],[19,19,19,19,19,-4,19,-6,19,-8,19,-10,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-28,-5,-7,-9,-53,-18,-53,-13,-15,19,19,19,19,-11,-17,-12,19,-19,-16,-14,]),'FNUMBER':([8,14,18,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,60,82,83,84,94,95,103,104,106,109,111,112,113,116,118,119,120,128,131,134,],[20,20,20,20,20,-4,20,-6,20,-8,20,-10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-28,-5,-7,-9,-53,-18,-53,-13,-15,20,20,20,20,-11,-17,-12,20,-19,-16,-14,]),'BOOLVAL':([8,14,18,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,60,82,83,84,94,95,103,104,106,109,111,112,113,116,118,119,120,128,131,134,],[26,26,26,26,26,-4,26,-6,26,-8,26,-10,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-28,-5,-7,-9,-53,-18,-53,-13,-15,26,26,26,26,-11,-17,-12,26,-19,-16,-14,]),';':([13,15,16,17,19,20,21,22,23,24,25,26,32,56,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,81,],[30,33,35,37,-35,-36,-37,-50,-41,-42,-49,-51,60,-50,82,83,84,-30,-31,-32,-33,-34,-43,-44,-45,-46,-47,-48,-29,-38,-39,-40,87,]),'PLUS':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,87,91,92,97,122,123,124,125,127,],[38,-35,-36,-37,-50,-41,-42,-49,-51,38,38,-37,-37,38,-50,-37,38,38,-37,38,38,38,38,38,38,38,38,38,38,38,-29,-38,-37,-37,-37,-37,92,97,101,108,38,38,38,38,-37,]),'MINUS':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,87,91,93,98,122,123,124,125,127,],[39,-35,-36,-37,-50,-41,-42,-49,-51,39,39,-37,-37,39,-50,-37,39,39,-37,39,39,39,39,39,39,39,39,39,39,39,-29,-38,-37,-37,-37,-37,93,98,102,110,39,39,39,39,-37,]),'TIMES':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,91,122,123,124,125,127,],[40,-35,-36,-37,-50,-41,-42,-49,-51,40,40,-37,-37,40,-50,-37,40,40,-37,40,40,40,40,40,40,40,40,40,40,40,-29,-38,-37,-37,-37,-37,99,40,40,40,40,-37,]),'DIVIDE':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,91,122,123,124,125,127,],[41,-35,-36,-37,-50,-41,-42,-49,-51,41,41,-37,-37,41,-50,-37,41,41,-37,41,41,41,41,41,41,41,41,41,41,41,-29,-38,-37,-37,-37,-37,100,41,41,41,41,-37,]),'POW':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[42,-35,-36,-37,-50,-41,-42,-49,-51,42,42,-37,-37,42,-50,-37,42,42,-37,42,42,42,42,42,42,42,42,42,42,42,-29,-38,-37,-37,-37,-37,42,42,42,42,-37,]),'EQ':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[43,-35,-36,-37,-50,-41,-42,-49,-51,43,43,-37,-37,43,-50,-37,43,43,-37,43,43,43,43,43,43,43,43,43,43,43,-29,-38,-37,-37,-37,-37,43,43,43,43,-37,]),'NE':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[44,-35,-36,-37,-50,-41,-42,-49,-51,44,44,-37,-37,44,-50,-37,44,44,-37,44,44,44,44,44,44,44,44,44,44,44,-29,-38,-37,-37,-37,-37,44,44,44,44,-37,]),'LT':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[45,-35,-36,-37,-50,-41,-42,-49,-51,45,45,-37,-37,45,-50,-37,45,45,-37,45,45,45,45,45,45,45,45,45,45,45,-29,-38,-37,-37,-37,-37,45,45,45,45,-37,]),'LE':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[46,-35,-36,-37,-50,-41,-42,-49,-51,46,46,-37,-37,46,-50,-37,46,46,-37,46,46,46,46,46,46,46,46,46,46,46,-29,-38,-37,-37,-37,-37,46,46,46,46,-37,]),'GT':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[47,-35,-36,-37,-50,-41,-42,-49,-51,47,47,-37,-37,47,-50,-37,47,47,-37,47,47,47,47,47,47,47,47,47,47,47,-29,-38,-37,-37,-37,-37,47,47,47,47,-37,]),'GE':([17,19,20,21,22,23,24,25,26,32,49,50,54,55,56,57,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,122,123,124,125,127,],[48,-35,-36,-37,-50,-41,-42,-49,-51,48,48,-37,-37,48,-50,-37,48,48,-37,48,48,48,48,48,48,48,48,48,48,48,-29,-38,-37,-37,-37,-37,48,48,48,48,-37,]),'RPAREN':([19,20,21,22,23,24,25,26,49,50,54,56,57,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,90,108,110,114,115,122,123,124,125,127,],[-35,-36,-37,-50,-41,-42,-49,-51,74,75,79,-50,80,-30,-31,-32,-33,-34,-43,-44,-45,-46,-47,-48,-29,-38,-39,-40,75,96,-24,-25,-26,-27,-20,-21,-22,-23,130,]),'AND':([19,20,21,22,23,24,25,26,50,54,56,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,127,],[-35,-36,51,-50,-41,-42,-49,-51,51,51,-50,51,51,-30,-31,-32,-33,-34,-43,-44,-45,-46,-47,-48,-29,-38,51,51,51,51,51,]),'OR':([19,20,21,22,23,24,25,26,50,54,56,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,127,],[-35,-36,52,-50,-41,-42,-49,-51,52,52,-50,52,52,-30,-31,-32,-33,-34,-43,-44,-45,-46,-47,-48,-29,-38,52,52,52,52,52,]),'{':([79,80,96,117,130,],[85,86,107,126,132,]),'ELIF':([94,104,106,134,],[105,105,-15,-14,]),'ELSE':([94,103,104,106,119,134,],[-53,117,-13,-15,-12,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'stmts':([0,3,85,86,107,126,132,],[2,12,88,89,121,129,133,]),'statement':([0,3,29,85,86,107,126,132,],[3,3,58,3,3,3,3,3,]),'expression':([8,14,18,27,28,31,34,36,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,109,111,112,113,120,],[17,32,49,55,55,59,61,55,63,64,65,66,67,68,69,70,71,72,73,55,55,49,55,122,123,124,125,55,]),'boolean_expression':([8,14,18,27,28,31,34,36,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,109,111,112,113,120,],[21,21,50,54,57,21,21,62,21,21,21,21,21,21,21,21,21,21,21,76,77,78,81,21,21,21,21,127,]),'comparison':([8,14,18,27,28,31,34,36,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,109,111,112,113,120,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'boolean_val':([8,14,18,27,28,31,34,36,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,109,111,112,113,120,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'boolexp':([8,14,18,27,28,31,34,36,38,39,40,41,42,43,44,45,46,47,48,51,52,53,58,109,111,112,113,120,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'step':([87,],[90,]),'elifs':([94,104,],[103,119,]),'elif':([94,104,],[104,104,]),'empty':([94,103,104,],[106,118,106,]),'else':([103,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> stmts','prog',1,'p_prog','compiler2.py',108),
  ('stmts -> statement stmts','stmts',2,'p_statements_recursion','compiler2.py',117),
  ('stmts -> statement','stmts',1,'p_statements_recursion','compiler2.py',118),
  ('statement -> INTDCL NAME ;','statement',3,'p_statement_declare_int','compiler2.py',127),
  ('statement -> INTDCL NAME = expression ;','statement',5,'p_statement_declare_int','compiler2.py',128),
  ('statement -> FLOATDCL NAME ;','statement',3,'p_statement_declare_float','compiler2.py',140),
  ('statement -> FLOATDCL NAME = expression ;','statement',5,'p_statement_declare_float','compiler2.py',141),
  ('statement -> BOOLDCL NAME ;','statement',3,'p_statement_declare_bool','compiler2.py',153),
  ('statement -> BOOLDCL NAME = boolean_expression ;','statement',5,'p_statement_declare_bool','compiler2.py',154),
  ('statement -> PRINT expression ;','statement',3,'p_statement_print','compiler2.py',167),
  ('statement -> IF LPAREN boolean_expression RPAREN { stmts } elifs else','statement',9,'p_statement_if','compiler2.py',176),
  ('elifs -> elif elifs','elifs',2,'p_elif_recursion','compiler2.py',196),
  ('elifs -> elif','elifs',1,'p_elif_recursion','compiler2.py',197),
  ('elif -> ELIF LPAREN boolean_expression RPAREN { stmts }','elif',7,'p_elif','compiler2.py',206),
  ('elif -> empty','elif',1,'p_elif','compiler2.py',207),
  ('else -> ELSE { stmts }','else',4,'p_else','compiler2.py',223),
  ('else -> empty','else',1,'p_else','compiler2.py',224),
  ('statement -> WHILE LPAREN boolean_expression RPAREN { stmts }','statement',7,'p_statement_while','compiler2.py',237),
  ('statement -> FOR LPAREN statement boolean_expression ; step RPAREN { stmts }','statement',10,'p_statement_for','compiler2.py',252),
  ('step -> NAME PLUS = expression','step',4,'p_expression_step','compiler2.py',276),
  ('step -> NAME MINUS = expression','step',4,'p_expression_step','compiler2.py',277),
  ('step -> NAME TIMES = expression','step',4,'p_expression_step','compiler2.py',278),
  ('step -> NAME DIVIDE = expression','step',4,'p_expression_step','compiler2.py',279),
  ('step -> NAME PLUS PLUS','step',3,'p_expression_step','compiler2.py',280),
  ('step -> NAME MINUS MINUS','step',3,'p_expression_step','compiler2.py',281),
  ('step -> PLUS PLUS NAME','step',3,'p_expression_step','compiler2.py',282),
  ('step -> MINUS MINUS NAME','step',3,'p_expression_step','compiler2.py',283),
  ('statement -> NAME = expression ;','statement',4,'p_statement_assign','compiler2.py',304),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','compiler2.py',323),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','compiler2.py',329),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','compiler2.py',330),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','compiler2.py',331),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','compiler2.py',332),
  ('expression -> expression POW expression','expression',3,'p_expression_binop','compiler2.py',333),
  ('expression -> INUMBER','expression',1,'p_expression_inumber','compiler2.py',344),
  ('expression -> FNUMBER','expression',1,'p_expression_fnumber','compiler2.py',353),
  ('expression -> boolean_expression','expression',1,'p_expression_boolean','compiler2.py',362),
  ('boolean_expression -> LPAREN boolean_expression RPAREN','boolean_expression',3,'p_boolean_expression_group','compiler2.py',368),
  ('boolean_expression -> boolean_expression AND boolean_expression','boolean_expression',3,'p_boolean_expression','compiler2.py',374),
  ('boolean_expression -> boolean_expression OR boolean_expression','boolean_expression',3,'p_boolean_expression','compiler2.py',375),
  ('boolean_expression -> comparison','boolean_expression',1,'p_boolean_expression','compiler2.py',376),
  ('boolean_expression -> boolean_val','boolean_expression',1,'p_boolean_expression','compiler2.py',377),
  ('comparison -> expression EQ expression','comparison',3,'p_comparison','compiler2.py',394),
  ('comparison -> expression NE expression','comparison',3,'p_comparison','compiler2.py',395),
  ('comparison -> expression LT expression','comparison',3,'p_comparison','compiler2.py',396),
  ('comparison -> expression LE expression','comparison',3,'p_comparison','compiler2.py',397),
  ('comparison -> expression GT expression','comparison',3,'p_comparison','compiler2.py',398),
  ('comparison -> expression GE expression','comparison',3,'p_comparison','compiler2.py',399),
  ('boolean_val -> boolexp','boolean_val',1,'p_boolean_val','compiler2.py',410),
  ('boolean_val -> NAME','boolean_val',1,'p_boolean_val','compiler2.py',411),
  ('boolexp -> BOOLVAL','boolexp',1,'p_bool_expression','compiler2.py',423),
  ('expression -> NAME','expression',1,'p_expression_name','compiler2.py',432),
  ('empty -> <empty>','empty',0,'p_empty','compiler2.py',442),
]
