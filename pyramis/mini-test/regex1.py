import re
R_STRUCT_OR_TYPEDEF_STRUCT = r'(?:typedef\s+)?struct\s+(\w*)\s*\{?'

tds = "typedef struct structname {"
s = "struct {"

match1 = re.match(R_STRUCT_OR_TYPEDEF_STRUCT, tds)
match2 = re.match(R_STRUCT_OR_TYPEDEF_STRUCT, s)

g1 = match1.group(1)
g2 = match2.group(1)
print(g1)
print(g2)