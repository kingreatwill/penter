# 访问编译器的符号表
import symtable

table = symtable.symtable("def some_func(): pass", "string", "exec")
print("--------------symtable.SymbolTable")
print(table.lookup("some_func").is_namespace())

print(table.get_type())
print(table.get_id())
print(table.get_name())
print(table.get_lineno())
print(table.get_symbols())
print(table.get_children())
print("--------------symtable.Function")
func1 = table.get_children()[0]
print(func1.get_name())
print("--------------symtable.Symbol")
symbol1 = table.get_symbols()[0]
print(symbol1.get_name())

print("---------symbol.sym_name")
import symbol
print(symbol.sym_name)