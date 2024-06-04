import cppvariable as cvar
import cppfunction as cfunc
import re


def udfparse(line):
    """
    Parses a function signature from udf.h and returns the information as
    a Functionheader object.
    """
    line = line.strip().strip(";")
    r_space = line.split("(")[0].split()

    fname = r_space[-1]
    rtypename = " ".join(elem for elem in r_space[:-1])

    if "*" in rtypename or "*" in fname:
        # rettype is pointer
        rtypename = rtypename.replace("*", "")
        fname = fname.replace("*", "")
        ret_type = cvar.CPPVariableType(typestr=rtypename, ispointer=True)
    else:
        ret_type = cvar.CPPVariableType(typestr=rtypename, ispointer=False)

    params_list = (
        line.split("(")[1].replace(")", "").split(",")
    )  # ["int *x", "amf_t &y",...]
    clean_params_list = [param.strip() for param in params_list]

    params = []

    for param in clean_params_list:
        # param = param.strip()
        p_space = param.split()
        try:
            pname = p_space[-1]
        except:
            continue
        p_type = " ".join(elem for elem in p_space[:-1])

        if "*" in p_type or "*" in pname:
            p_type = p_type.replace("*", "")
            pname = pname.replace("*", "")
            isptr = True
        else:
            isptr = False

        p = cvar.CPPVariable(pname, typestr=p_type, ispointer=isptr)
        params.append(p)

    fun = cfunc.FunctionHeader(fname.strip(), ret_type, params)

    # plist = [(param.name, param.type.typestr, param.type.ispointer) for param in fun.parameters]
    # logger.debug(plist)

    return fun


"""
Used during codegen() on nodes.
"""


def parse_json_attr(attributestr):
    parts = attributestr.split(".")
    transformed_parts = [parts[0]]

    for part in parts[1:]:
        if "[" in part:
            prefix, suffix = part.split("[", 1)
            suffix = suffix.strip("]")
            transformed_parts.append(f'["{prefix}"][{suffix}]')
        else:
            transformed_parts.append(f'["{part}"]')

    transformed_str = "".join(transformed_parts)
    return transformed_str


def parse_http_attr(attributestr):
    parts = attributestr.split(".")
    transformed_parts = [parts[0], ".", parts[1]]

    for part in parts[2:]:
        if "[" in part:
            prefix, suffix = part.split("[", 1)
            suffix = suffix.strip("]")
            transformed_parts.append(f'["{prefix}"][{suffix}]')
        else:
            transformed_parts.append(f'["{part}"]')

    transformed_str = "".join(transformed_parts)
    return transformed_str


def make_clauses(paramstr):  # return list of clause strings
    rlogical = r"\s*(\|\||&&)\s*"

    # extractedNssais.Nssai[i].len_s_nssai && reqNssai.Nssai[slice].sST == extractedNssais.Nssai[i].sST && reqNssai.Nssai[slice].sD == extractedNssais.Nssai[i].sD
    cc = re.split(rlogical, paramstr)  # [a1 > b1', '&&', 'a2==b2']..etc.

    clist = []
    for clausename in cc:
        if clausename in ["&&", "||"]:
            clist.append([clausename])

        else:
            rop = r"(\>|\<|\>=|<=|==|!=)"
            parts = re.split(rop, clausename)

            cnames = [part.strip() for part in parts]
            clist.append(cnames)  # [[#a1#, #>#, #b1#], '&&', [a2==b2']]..etc.

    return clist
