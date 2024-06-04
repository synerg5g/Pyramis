import re

R_STRUCT_COMPOUND_ATTRIBUTE = r'struct\s+\S+\s+\S+;' # struct str1 str2;
R_TYPEDEF = r'typedef\s+((\S+\s+)+)(\S+);'
line = "typedef struct a int;"
m = re.match(R_TYPEDEF, line)

if (m):
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
else:
    print("no match from start of string")