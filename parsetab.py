
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

<<<<<<< HEAD
_lr_signature = 'leftADDSUBTRACTleftASTERISKDIVIDEDIVIDE_INTINSERT INTO VALUES SET SELECT DELETE INT_LIT DOUBLE_LIT STRING_LIT ADD SUBTRACT DIVIDE DIVIDE_INT MODULO EQUAL EQUAL_NULL GT GE LT LE NE NOT COLUMN_NAME TABLE_NAME ASTERISK COMMA SEMICOLON OPENPAR CLOSEPAR FROM WHERE LIKE STRCMP IS NULL BETWEEN ANDstatement : insert_statement\n            | select_statement\n            | delete_statementinsert_statement : INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON\n            | INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON\n            | INSERT into_kw TABLE_NAME SET assignment_list SEMICOLONselect_statement : SELECT columns FROM TABLE_NAME SEMICOLON\n            | SELECT columns FROM TABLE_NAME WHERE condition SEMICOLONdelete_statement : DELETE FROM TABLE_NAME SEMICOLON\n            | DELETE FROM TABLE_NAME WHERE condition SEMICOLONinto_kw : INTO\n            | emptycolumns : ASTERISK\n            | column_namecolumn_name : COLUMN_NAME\n            | column_name COMMA COLUMN_NAMEassignment_list : COLUMN_NAME EQUAL literals\n            | assignment_list COMMA COLUMN_NAME EQUAL literalsvalue_list : literals\n            | value_list COMMA literalsliterals : STRING_LIT\n            | INT_LIT\n            | DOUBLE_LIT\n            | NULLcondition : string_cond\n            | num_cond\n            | NOT OPENPAR string_cond CLOSEPAR\n            | NOT OPENPAR num_cond CLOSEPARstring_cond : string_exp LIKE string_exp\n            | string_exp NOT LIKE string_exp\n            | string_exp EQUAL string_exp\n            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPARstring_exp : STRING_LITnum_cond : num_exp comparison_op num_exp\n            | num_exp BETWEEN num_exp AND num_exp\n            | num_exp NOT NULL\n            | num_exp IS NULLnum_exp : num_exp ADD num_factor\n            |  num_factor SUBTRACT num_exp\n            | num_factornum_factor : num_factor ASTERISK num_term\n            | num_factor DIVIDE num_term\n            | num_factor DIVIDE_INT num_term\n            | num_factor MODULO num_term\n            | num_termnum_term : OPENPAR num_exp CLOSEPAR\n            | num_valnum_val : INT_LIT\n            | DOUBLE_LIT\n            | COLUMN_NAMEcomparison_op : GE\n            | GT\n            | LE\n            | LT\n            | NE\n            | EQUAL\n            | EQUAL_NULLempty : '
    
_lr_action_items = {'ADD':([35,36,37,38,41,42,47,80,94,95,98,99,100,101,102,103,104,117,],[63,-49,-50,-45,-48,-40,-47,63,-38,63,63,-43,-42,-39,-44,-41,-46,63,]),'DIVIDE_INT':([36,37,38,41,42,47,94,99,100,102,103,104,],[-49,-50,-45,-48,75,-47,75,-43,-42,-44,-41,-46,]),'DIVIDE':([36,37,38,41,42,47,94,99,100,102,103,104,],[-49,-50,-45,-48,76,-47,76,-43,-42,-44,-41,-46,]),'EQUAL':([29,34,35,36,37,38,39,41,42,47,85,94,99,100,101,102,103,104,],[49,61,69,-49,-50,-45,-33,-48,-40,-47,106,-38,-43,-42,-39,-44,-41,-46,]),'WHERE':([19,20,],[25,27,]),'AND':([36,37,38,41,42,47,94,95,99,100,101,102,103,104,],[-49,-50,-45,-48,-40,-47,-38,113,-43,-42,-39,-44,-41,-46,]),'SET':([18,],[22,]),'SUBTRACT':([36,37,38,41,42,47,99,100,102,103,104,],[-49,-50,-45,-48,77,-47,-43,-42,-44,-41,-46,]),'GT':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[71,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'CLOSEPAR':([8,21,32,36,37,38,39,41,42,47,52,53,54,55,56,57,80,89,90,91,92,94,96,97,98,99,100,101,102,103,104,108,112,116,117,118,120,],[-15,-16,58,-49,-50,-45,-33,-48,-40,-47,-21,86,-24,-22,-23,-19,104,110,111,-29,-31,-38,-36,-37,-34,-43,-42,-39,-44,-41,-46,-20,-30,119,-35,120,-32,]),'SELECT':([0,],[4,]),'BETWEEN':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[64,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'COLUMN_NAME':([4,17,22,24,25,27,44,51,59,63,64,65,68,69,70,71,72,73,74,75,76,77,78,79,113,],[8,21,29,8,37,37,37,85,37,37,37,-54,-53,-56,-57,-52,37,-55,-51,37,37,37,37,37,37,]),'$end':([1,2,3,6,26,28,50,81,83,107,121,],[0,-1,-2,-3,-9,-7,-6,-10,-8,-4,-5,]),'SEMICOLON':([19,20,30,36,37,38,39,40,41,42,43,45,47,48,52,54,55,56,84,86,91,92,94,96,97,98,99,100,101,102,103,104,110,111,112,115,117,119,120,],[26,28,50,-49,-50,-45,-33,-26,-48,-40,-25,81,-47,83,-21,-24,-22,-23,-17,107,-29,-31,-38,-36,-37,-34,-43,-42,-39,-44,-41,-46,-28,-27,-30,-18,-35,121,-32,]),'NULL':([31,49,66,67,87,106,109,],[54,54,96,97,54,54,54,]),'MODULO':([36,37,38,41,42,47,94,99,100,102,103,104,],[-49,-50,-45,-48,78,-47,78,-43,-42,-44,-41,-46,]),'GE':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[74,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'STRING_LIT':([25,27,31,49,59,60,61,82,87,93,106,109,114,],[39,39,52,52,39,39,39,39,52,39,52,52,39,]),'LIKE':([34,39,62,],[60,-33,93,]),'LT':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[65,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'VALUES':([18,58,],[23,88,]),'IS':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[67,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'FROM':([7,8,9,10,11,21,],[15,-15,16,-14,-13,-16,]),'COMMA':([8,10,21,30,32,39,52,53,54,55,56,57,84,105,108,115,116,],[-15,17,-16,51,17,-33,-21,87,-24,-22,-23,-19,-17,114,-20,-18,87,]),'OPENPAR':([18,23,25,27,33,44,46,59,63,64,65,68,69,70,71,72,73,74,75,76,77,78,79,88,113,],[24,31,44,44,59,44,82,44,44,44,-54,-53,-56,-57,-52,44,-55,-51,44,44,44,44,44,109,44,]),'INT_LIT':([25,27,31,44,49,59,63,64,65,68,69,70,71,72,73,74,75,76,77,78,79,87,106,109,113,],[41,41,55,41,55,41,41,41,-54,-53,-56,-57,-52,41,-55,-51,41,41,41,41,41,55,55,55,41,]),'DELETE':([0,],[7,]),'EQUAL_NULL':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[70,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'TABLE_NAME':([5,12,13,14,15,16,],[-58,18,-11,-12,19,20,]),'LE':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[68,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'DOUBLE_LIT':([25,27,31,44,49,59,63,64,65,68,69,70,71,72,73,74,75,76,77,78,79,87,106,109,113,],[36,36,56,36,56,36,36,36,-54,-53,-56,-57,-52,36,-55,-51,36,36,36,36,36,56,56,56,36,]),'INTO':([5,],[13,]),'NOT':([25,27,34,35,36,37,38,39,41,42,47,94,99,100,101,102,103,104,],[33,33,62,66,-49,-50,-45,-33,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'STRCMP':([25,27,59,],[46,46,46,]),'NE':([35,36,37,38,41,42,47,94,99,100,101,102,103,104,],[73,-49,-50,-45,-48,-40,-47,-38,-43,-42,-39,-44,-41,-46,]),'INSERT':([0,],[5,]),'ASTERISK':([4,36,37,38,41,42,47,94,99,100,102,103,104,],[11,-49,-50,-45,-48,79,-47,79,-43,-42,-44,-41,-46,]),}
=======
_lr_signature = 'leftADDSUBTRACTleftASTERISKDIVIDEDIVIDE_INTINSERT INTO VALUES SET SELECT DELETE INT_LIT DOUBLE_LIT STRING_LIT ADD SUBTRACT DIVIDE DIVIDE_INT MODULO EQUAL EQUAL_NULL GT GE LT LE NE NOT COLUMN_NAME TABLE_NAME ASTERISK COMMA SEMICOLON OPENPAR CLOSEPAR FROM WHERE LIKE STRCMP IS NULL BETWEEN ANDstatement : insert_statement\n            | select_statement\n            | delete_statementinsert_statement : INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON\n            | INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON\n            | INSERT into_kw TABLE_NAME SET assignment_list SEMICOLONselect_statement : SELECT columns FROM TABLE_NAME SEMICOLON\n            | SELECT columns FROM TABLE_NAME WHERE condition SEMICOLONdelete_statement : DELETE FROM TABLE_NAME SEMICOLON\n            | DELETE FROM TABLE_NAME WHERE condition SEMICOLONinto_kw : INTO\n            | emptycolumns : ASTERISK\n            | column_namecolumn_name : COLUMN_NAME\n            | column_name COMMA COLUMN_NAMEassignment_list : COLUMN_NAME EQUAL literals\n            | assignment_list COMMA COLUMN_NAME EQUAL literalsvalue_list : literals\n            | value_list COMMA literalsliterals : STRING_LIT\n            | INT_LIT\n            | DOUBLE_LIT\n            | NULLcondition : col_cond\n            | string_cond\n            | num_cond\n            | NOT OPENPAR string_cond CLOSEPAR\n            | NOT OPENPAR num_cond CLOSEPARcol_cond : column_name comparison_op string_exp\n            | column_name comparison_op num_exp\n            | column_name LIKE string_exp\n            | column_name NOT LIKE string_expstring_cond : string_exp LIKE string_exp\n            | string_exp NOT LIKE string_exp\n            | string_exp comparison_op string_exp\n            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPARstring_exp : STRING_LITnum_cond : num_exp comparison_op num_exp\n            | num_exp BETWEEN num_exp AND num_exp\n            | num_exp NOT NULL\n            | num_exp IS NULLnum_exp : num_exp ADD num_factor\n            |  num_factor SUBTRACT num_exp\n            | num_factornum_factor : num_factor ASTERISK num_term\n            | num_factor DIVIDE num_term\n            | num_factor DIVIDE_INT num_term\n            | num_factor MODULO num_term\n            | num_termnum_term : OPENPAR num_exp CLOSEPAR\n            | num_valnum_val : INT_LIT\n            | DOUBLE_LIT\n            | COLUMN_NAMEcomparison_op : GE\n            | GT\n            | LE\n            | LT\n            | NE\n            | EQUAL\n            | EQUAL_NULLempty : '
    
_lr_action_items = {'BETWEEN':([29,32,33,35,40,43,45,76,94,95,96,97,98,102,109,],[-50,-45,70,-52,-53,-55,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'LE':([20,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,-50,57,-45,57,57,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'DIVIDE':([29,32,35,40,43,45,76,94,95,96,97,102,109,],[-50,63,-52,-53,-55,-54,-55,-46,-48,-47,-49,63,-51,]),'CLOSEPAR':([11,20,29,32,35,37,40,45,46,75,76,80,81,82,83,84,85,94,95,96,97,98,99,100,101,102,104,106,107,108,109,118,124,126,127,128,130,],[-15,-16,-50,-45,-52,-38,-53,-54,79,109,-55,-21,-24,-23,112,-19,-22,-46,-48,-47,-49,-44,-41,-42,-39,-43,-36,-34,119,120,-51,-35,-20,-40,130,131,-37,]),'INTO':([7,],[13,]),'LIKE':([20,31,34,37,43,52,72,],[-16,55,73,-38,-15,90,105,]),'STRING_LIT':([23,28,47,51,53,54,55,56,57,58,59,60,71,73,74,78,88,90,105,113,121,122,125,],[37,37,80,-56,37,-62,37,-57,-58,-60,-59,-61,37,37,37,37,80,37,37,80,37,80,80,]),'MODULO':([29,32,35,40,43,45,76,94,95,96,97,102,109,],[-50,64,-52,-53,-55,-54,-55,-46,-48,-47,-49,64,-51,]),'SUBTRACT':([29,32,35,40,43,45,76,94,95,96,97,109,],[-50,65,-52,-53,-55,-54,-55,-46,-48,-47,-49,-51,]),'NE':([20,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,-50,58,-45,58,58,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'DELETE':([0,],[6,]),'SEMICOLON':([18,21,29,30,32,35,37,39,40,41,44,45,48,50,76,80,81,82,85,91,92,93,94,95,96,97,98,99,100,101,102,104,106,109,112,115,116,118,119,120,126,129,130,131,],[22,27,-50,-25,-45,-52,-38,77,-53,-26,-27,-54,86,89,-55,-21,-24,-23,-22,-31,-30,-32,-46,-48,-47,-49,-44,-41,-42,-39,-43,-36,-34,-51,123,-17,-33,-35,-29,-28,-40,-18,-37,132,]),'TABLE_NAME':([7,12,13,14,15,17,],[-63,18,-11,-12,19,21,]),'LT':([20,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,-50,59,-45,59,59,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'ADD':([29,32,33,35,40,43,45,75,76,91,94,95,96,97,98,101,102,103,109,126,],[-50,-45,69,-52,-53,-55,-54,69,-55,69,-46,-48,-47,-49,-44,69,-43,69,-51,69,]),'DIVIDE_INT':([29,32,35,40,43,45,76,94,95,96,97,102,109,],[-50,62,-52,-53,-55,-54,-55,-46,-48,-47,-49,62,-51,]),'COMMA':([9,11,20,31,37,43,46,48,80,81,82,83,84,85,110,115,124,128,129,],[16,-15,-16,16,-38,-15,16,87,-21,-24,-23,113,-19,-22,121,-17,-20,113,-18,]),'OPENPAR':([19,23,25,28,36,38,42,51,53,54,56,57,58,59,60,61,62,63,64,65,68,69,70,74,111,117,],[24,38,47,38,74,38,78,-56,38,-62,-57,-58,-60,-59,-61,38,38,38,38,38,38,38,38,38,122,38,]),'NOT':([20,23,28,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,36,36,-50,52,-45,66,72,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'GE':([20,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,-50,51,-45,51,51,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'SELECT':([0,],[5,]),'INSERT':([0,],[7,]),'FROM':([6,8,9,10,11,20,],[12,-13,-14,17,-15,-16,]),'VALUES':([19,79,],[25,111,]),'INT_LIT':([23,28,38,47,51,53,54,56,57,58,59,60,61,62,63,64,65,68,69,70,74,88,113,117,122,125,],[40,40,40,85,-56,40,-62,-57,-58,-60,-59,-61,40,40,40,40,40,40,40,40,40,85,85,40,85,85,]),'$end':([1,2,3,4,22,27,77,86,89,123,132,],[0,-2,-1,-3,-9,-7,-10,-6,-8,-4,-5,]),'EQUAL_NULL':([20,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,-50,54,-45,54,54,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'STRCMP':([23,28,74,],[42,42,42,]),'COLUMN_NAME':([5,16,23,24,26,28,38,51,53,54,56,57,58,59,60,61,62,63,64,65,68,69,70,74,87,117,],[11,20,43,11,49,43,76,-56,76,-62,-57,-58,-60,-59,-61,76,76,76,76,76,76,76,76,76,114,76,]),'NULL':([47,66,67,88,113,122,125,],[81,99,100,81,81,81,81,]),'AND':([29,32,35,40,45,76,94,95,96,97,98,102,103,109,],[-50,-45,-52,-53,-54,-55,-46,-48,-47,-49,-44,-43,117,-51,]),'DOUBLE_LIT':([23,28,38,47,51,53,54,56,57,58,59,60,61,62,63,64,65,68,69,70,74,88,113,117,122,125,],[45,45,45,82,-56,45,-62,-57,-58,-60,-59,-61,45,45,45,45,45,45,45,45,45,82,82,45,82,82,]),'ASTERISK':([5,29,32,35,40,43,45,76,94,95,96,97,102,109,],[8,-50,61,-52,-53,-55,-54,-55,-46,-48,-47,-49,61,-51,]),'WHERE':([18,21,],[23,28,]),'SET':([19,],[26,]),'EQUAL':([20,29,31,32,33,34,35,37,40,43,45,49,76,94,95,96,97,98,102,109,114,],[-16,-50,60,-45,60,60,-52,-38,-53,-15,-54,88,-55,-46,-48,-47,-49,-44,-43,-51,125,]),'GT':([20,29,31,32,33,34,35,37,40,43,45,76,94,95,96,97,98,102,109,],[-16,-50,56,-45,56,56,-52,-38,-53,-15,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),'IS':([29,32,33,35,40,43,45,76,94,95,96,97,98,102,109,],[-50,-45,67,-52,-53,-55,-54,-55,-46,-48,-47,-49,-44,-43,-51,]),}
>>>>>>> 7a9ccd466dcbacb7a241277b9047f0ec23896544

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

<<<<<<< HEAD
_lr_goto_items = {'string_exp':([25,27,59,60,61,82,93,114,],[34,34,34,91,92,105,112,118,]),'value_list':([31,109,],[53,116,]),'statement':([0,],[1,]),'condition':([25,27,],[45,48,]),'num_exp':([25,27,44,59,64,72,77,113,],[35,35,80,35,95,98,101,117,]),'comparison_op':([35,],[72,]),'into_kw':([5,],[12,]),'assignment_list':([22,],[30,]),'insert_statement':([0,],[2,]),'select_statement':([0,],[3,]),'num_factor':([25,27,44,59,63,64,72,77,113,],[42,42,42,42,94,42,42,42,42,]),'num_cond':([25,27,59,],[40,40,89,]),'columns':([4,],[9,]),'string_cond':([25,27,59,],[43,43,90,]),'empty':([5,],[14,]),'num_term':([25,27,44,59,63,64,72,75,76,77,78,79,113,],[38,38,38,38,38,38,38,99,100,38,102,103,38,]),'column_name':([4,24,],[10,32,]),'literals':([31,49,87,106,109,],[57,84,108,115,57,]),'num_val':([25,27,44,59,63,64,72,75,76,77,78,79,113,],[47,47,47,47,47,47,47,47,47,47,47,47,47,]),'delete_statement':([0,],[6,]),}
=======
_lr_goto_items = {'statement':([0,],[1,]),'select_statement':([0,],[2,]),'num_exp':([23,28,38,53,65,68,70,74,117,],[33,33,75,91,98,101,103,33,126,]),'insert_statement':([0,],[3,]),'num_term':([23,28,38,53,61,62,63,64,65,68,69,70,74,117,],[29,29,29,29,94,95,96,97,29,29,29,29,29,29,]),'column_name':([5,23,24,28,],[9,31,46,31,]),'comparison_op':([31,33,34,],[53,68,71,]),'string_cond':([23,28,74,],[41,41,108,]),'columns':([5,],[10,]),'delete_statement':([0,],[4,]),'assignment_list':([26,],[48,]),'empty':([7,],[14,]),'num_cond':([23,28,74,],[44,44,107,]),'string_exp':([23,28,53,55,71,73,74,78,90,105,121,],[34,34,92,93,104,106,34,110,116,118,127,]),'num_factor':([23,28,38,53,65,68,69,70,74,117,],[32,32,32,32,32,32,102,32,32,32,]),'value_list':([47,122,],[83,128,]),'literals':([47,88,113,122,125,],[84,115,124,84,129,]),'into_kw':([7,],[15,]),'col_cond':([23,28,],[30,30,]),'condition':([23,28,],[39,50,]),'num_val':([23,28,38,53,61,62,63,64,65,68,69,70,74,117,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),}
>>>>>>> 7a9ccd466dcbacb7a241277b9047f0ec23896544

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> insert_statement','statement',1,'p_statement','mysqlparse.py',25),
  ('statement -> select_statement','statement',1,'p_statement','mysqlparse.py',26),
  ('statement -> delete_statement','statement',1,'p_statement','mysqlparse.py',27),
  ('insert_statement -> INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON','insert_statement',8,'p_insert_statement','mysqlparse.py',30),
  ('insert_statement -> INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON','insert_statement',11,'p_insert_statement','mysqlparse.py',31),
  ('insert_statement -> INSERT into_kw TABLE_NAME SET assignment_list SEMICOLON','insert_statement',6,'p_insert_statement','mysqlparse.py',32),
  ('select_statement -> SELECT columns FROM TABLE_NAME SEMICOLON','select_statement',5,'p_select_statement','mysqlparse.py',66),
  ('select_statement -> SELECT columns FROM TABLE_NAME WHERE condition SEMICOLON','select_statement',7,'p_select_statement','mysqlparse.py',67),
  ('delete_statement -> DELETE FROM TABLE_NAME SEMICOLON','delete_statement',4,'p_delete_statement','mysqlparse.py',109),
  ('delete_statement -> DELETE FROM TABLE_NAME WHERE condition SEMICOLON','delete_statement',6,'p_delete_statement','mysqlparse.py',110),
  ('into_kw -> INTO','into_kw',1,'p_into_kw','mysqlparse.py',141),
  ('into_kw -> empty','into_kw',1,'p_into_kw','mysqlparse.py',142),
  ('columns -> ASTERISK','columns',1,'p_columns','mysqlparse.py',157),
  ('columns -> column_name','columns',1,'p_columns','mysqlparse.py',158),
  ('column_name -> COLUMN_NAME','column_name',1,'p_column_name','mysqlparse.py',162),
  ('column_name -> column_name COMMA COLUMN_NAME','column_name',3,'p_column_name','mysqlparse.py',163),
  ('assignment_list -> COLUMN_NAME EQUAL literals','assignment_list',3,'p_assignment_list','mysqlparse.py',172),
  ('assignment_list -> assignment_list COMMA COLUMN_NAME EQUAL literals','assignment_list',5,'p_assignment_list','mysqlparse.py',173),
  ('value_list -> literals','value_list',1,'p_value_list','mysqlparse.py',183),
  ('value_list -> value_list COMMA literals','value_list',3,'p_value_list','mysqlparse.py',184),
  ('literals -> STRING_LIT','literals',1,'p_literals','mysqlparse.py',194),
  ('literals -> INT_LIT','literals',1,'p_literals','mysqlparse.py',195),
  ('literals -> DOUBLE_LIT','literals',1,'p_literals','mysqlparse.py',196),
  ('literals -> NULL','literals',1,'p_literals','mysqlparse.py',197),
<<<<<<< HEAD
  ('condition -> string_cond','condition',1,'p_condition','mysqlparse.py',201),
  ('condition -> num_cond','condition',1,'p_condition','mysqlparse.py',202),
  ('condition -> NOT OPENPAR string_cond CLOSEPAR','condition',4,'p_condition','mysqlparse.py',203),
  ('condition -> NOT OPENPAR num_cond CLOSEPAR','condition',4,'p_condition','mysqlparse.py',204),
  ('string_cond -> string_exp LIKE string_exp','string_cond',3,'p_string_cond','mysqlparse.py',212),
  ('string_cond -> string_exp NOT LIKE string_exp','string_cond',4,'p_string_cond','mysqlparse.py',213),
  ('string_cond -> string_exp EQUAL string_exp','string_cond',3,'p_string_cond','mysqlparse.py',214),
  ('string_cond -> STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR','string_cond',6,'p_string_cond','mysqlparse.py',215),
  ('string_exp -> STRING_LIT','string_exp',1,'p_string_exp','mysqlparse.py',224),
  ('num_cond -> num_exp comparison_op num_exp','num_cond',3,'p_num_cond','mysqlparse.py',230),
  ('num_cond -> num_exp BETWEEN num_exp AND num_exp','num_cond',5,'p_num_cond','mysqlparse.py',231),
  ('num_cond -> num_exp NOT NULL','num_cond',3,'p_num_cond','mysqlparse.py',232),
  ('num_cond -> num_exp IS NULL','num_cond',3,'p_num_cond','mysqlparse.py',233),
  ('num_exp -> num_exp ADD num_factor','num_exp',3,'p_num_exp','mysqlparse.py',288),
  ('num_exp -> num_factor SUBTRACT num_exp','num_exp',3,'p_num_exp','mysqlparse.py',289),
  ('num_exp -> num_factor','num_exp',1,'p_num_exp','mysqlparse.py',290),
  ('num_factor -> num_factor ASTERISK num_term','num_factor',3,'p_num_factor','mysqlparse.py',306),
  ('num_factor -> num_factor DIVIDE num_term','num_factor',3,'p_num_factor','mysqlparse.py',307),
  ('num_factor -> num_factor DIVIDE_INT num_term','num_factor',3,'p_num_factor','mysqlparse.py',308),
  ('num_factor -> num_factor MODULO num_term','num_factor',3,'p_num_factor','mysqlparse.py',309),
  ('num_factor -> num_term','num_factor',1,'p_num_factor','mysqlparse.py',310),
  ('num_term -> OPENPAR num_exp CLOSEPAR','num_term',3,'p_num_term','mysqlparse.py',327),
  ('num_term -> num_val','num_term',1,'p_num_term','mysqlparse.py',328),
  ('num_val -> INT_LIT','num_val',1,'p_num_val','mysqlparse.py',338),
  ('num_val -> DOUBLE_LIT','num_val',1,'p_num_val','mysqlparse.py',339),
  ('num_val -> COLUMN_NAME','num_val',1,'p_num_val','mysqlparse.py',340),
  ('comparison_op -> GE','comparison_op',1,'p_comparison_op','mysqlparse.py',349),
  ('comparison_op -> GT','comparison_op',1,'p_comparison_op','mysqlparse.py',350),
  ('comparison_op -> LE','comparison_op',1,'p_comparison_op','mysqlparse.py',351),
  ('comparison_op -> LT','comparison_op',1,'p_comparison_op','mysqlparse.py',352),
  ('comparison_op -> NE','comparison_op',1,'p_comparison_op','mysqlparse.py',353),
  ('comparison_op -> EQUAL','comparison_op',1,'p_comparison_op','mysqlparse.py',354),
  ('comparison_op -> EQUAL_NULL','comparison_op',1,'p_comparison_op','mysqlparse.py',355),
  ('empty -> <empty>','empty',0,'p_empty','mysqlparse.py',360),
=======
  ('condition -> col_cond','condition',1,'p_condition','mysqlparse.py',201),
  ('condition -> string_cond','condition',1,'p_condition','mysqlparse.py',202),
  ('condition -> num_cond','condition',1,'p_condition','mysqlparse.py',203),
  ('condition -> NOT OPENPAR string_cond CLOSEPAR','condition',4,'p_condition','mysqlparse.py',204),
  ('condition -> NOT OPENPAR num_cond CLOSEPAR','condition',4,'p_condition','mysqlparse.py',205),
  ('col_cond -> column_name comparison_op string_exp','col_cond',3,'p_col_cond','mysqlparse.py',213),
  ('col_cond -> column_name comparison_op num_exp','col_cond',3,'p_col_cond','mysqlparse.py',214),
  ('col_cond -> column_name LIKE string_exp','col_cond',3,'p_col_cond','mysqlparse.py',215),
  ('col_cond -> column_name NOT LIKE string_exp','col_cond',4,'p_col_cond','mysqlparse.py',216),
  ('string_cond -> string_exp LIKE string_exp','string_cond',3,'p_string_cond','mysqlparse.py',226),
  ('string_cond -> string_exp NOT LIKE string_exp','string_cond',4,'p_string_cond','mysqlparse.py',227),
  ('string_cond -> string_exp comparison_op string_exp','string_cond',3,'p_string_cond','mysqlparse.py',228),
  ('string_cond -> STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR','string_cond',6,'p_string_cond','mysqlparse.py',229),
  ('string_exp -> STRING_LIT','string_exp',1,'p_string_exp','mysqlparse.py',237),
  ('num_cond -> num_exp comparison_op num_exp','num_cond',3,'p_num_cond','mysqlparse.py',243),
  ('num_cond -> num_exp BETWEEN num_exp AND num_exp','num_cond',5,'p_num_cond','mysqlparse.py',244),
  ('num_cond -> num_exp NOT NULL','num_cond',3,'p_num_cond','mysqlparse.py',245),
  ('num_cond -> num_exp IS NULL','num_cond',3,'p_num_cond','mysqlparse.py',246),
  ('num_exp -> num_exp ADD num_factor','num_exp',3,'p_num_exp','mysqlparse.py',301),
  ('num_exp -> num_factor SUBTRACT num_exp','num_exp',3,'p_num_exp','mysqlparse.py',302),
  ('num_exp -> num_factor','num_exp',1,'p_num_exp','mysqlparse.py',303),
  ('num_factor -> num_factor ASTERISK num_term','num_factor',3,'p_num_factor','mysqlparse.py',317),
  ('num_factor -> num_factor DIVIDE num_term','num_factor',3,'p_num_factor','mysqlparse.py',318),
  ('num_factor -> num_factor DIVIDE_INT num_term','num_factor',3,'p_num_factor','mysqlparse.py',319),
  ('num_factor -> num_factor MODULO num_term','num_factor',3,'p_num_factor','mysqlparse.py',320),
  ('num_factor -> num_term','num_factor',1,'p_num_factor','mysqlparse.py',321),
  ('num_term -> OPENPAR num_exp CLOSEPAR','num_term',3,'p_num_term','mysqlparse.py',338),
  ('num_term -> num_val','num_term',1,'p_num_term','mysqlparse.py',339),
  ('num_val -> INT_LIT','num_val',1,'p_num_val','mysqlparse.py',349),
  ('num_val -> DOUBLE_LIT','num_val',1,'p_num_val','mysqlparse.py',350),
  ('num_val -> COLUMN_NAME','num_val',1,'p_num_val','mysqlparse.py',351),
  ('comparison_op -> GE','comparison_op',1,'p_comparison_op','mysqlparse.py',360),
  ('comparison_op -> GT','comparison_op',1,'p_comparison_op','mysqlparse.py',361),
  ('comparison_op -> LE','comparison_op',1,'p_comparison_op','mysqlparse.py',362),
  ('comparison_op -> LT','comparison_op',1,'p_comparison_op','mysqlparse.py',363),
  ('comparison_op -> NE','comparison_op',1,'p_comparison_op','mysqlparse.py',364),
  ('comparison_op -> EQUAL','comparison_op',1,'p_comparison_op','mysqlparse.py',365),
  ('comparison_op -> EQUAL_NULL','comparison_op',1,'p_comparison_op','mysqlparse.py',366),
  ('empty -> <empty>','empty',0,'p_empty','mysqlparse.py',371),
>>>>>>> 7a9ccd466dcbacb7a241277b9047f0ec23896544
]
