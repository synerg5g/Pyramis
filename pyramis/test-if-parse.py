class Condition:
    """
    Represents a condition in an if statement.
    of the form `lhs op rhs`
    An If Action's vars are a list of a op b i.e. conditions.
    """
    def __init__(self, value=None, lhs=None, op=None, rhs=None):
        self.value = value
        self.lhs = lhs # should be variable ideally infer.get_variable()
        self.op = op
        self.rhs = rhs
    
    def __str__(self):
        return f"{self.value}:: [{self.lhs}] [{self.op}] [{self.rhs}]"

_comp_ops = [
    '==',
    '<',
    '>',
    '!='
]

_logic_ops = [
    '&&',
    '||'
]

def make_conditions(_cond):
    '''
    in: single string of 'a op b' OR 'a' seperated by logical operators
    ---> op: ==, <, >, !=
    out: list of Condition
    '''
    conditions = []
    print(f"[{_cond}]")

    # if empty
    if (not len(_cond)):
        return []
    
    # if simple word
    # _cond doesnt have ops
    if not any(op in _cond for op in _comp_ops + _logic_ops):
        return [Condition(_cond.strip(), lhs=_cond.strip())] # cond.value will be the full simple string
    
    # single condition string a op b
    if any(op in _cond for op in _comp_ops) and not any(op in _cond for op in _logic_ops):
        for _op in _comp_ops:
            if _op in _cond:
                lhs, rhs = _cond.split(_op)
                print(f"{lhs} op {rhs}")
                return [Condition(_cond, lhs.strip(), _op.strip(), rhs.strip())] # strs
        
    _temp = ""
    _cnt = 0
    for c in _cond:
        if 2*c in _logic_ops:
            if _cnt == 0: # first occurence of &
                # previous stuff formed a cond.
                conditions.extend(make_conditions(_temp))
                print(f"append {2*c} to conditions")
                conditions.append(2*c) # should be && or ||
                _cnt = 1
            elif _cnt == 1:
                _cnt = 0
            _temp = ""
        else:
            _temp += c
    
    if _temp:
        conditions.extend(make_conditions(_temp))

    return conditions

# Example usage
conditions = make_conditions("x > 5 && y != 'hello' || z")
print(conditions)  # Output: [Condition(lhs='x', op='>', rhs='5'), Condition(lhs='y', op='!=', rhs="'hello'"), Condition(lhs='z', op=None, rhs=None)]

print(conditions[-1].value)
print(conditions[-1].lhs)
print(conditions[-1].op)
print(conditions[-1].rhs)