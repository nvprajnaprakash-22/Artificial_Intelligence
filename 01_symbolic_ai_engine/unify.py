# unify.py
from primitives import Constant, Variable, Predicate

def unify(p1: Predicate, p2: Predicate) -> dict | None:
    """
    Compares two predicates and returns a dictionary mapping variable names 
    to terms if they unify, or None if unification fails.
    """
    # 1. Check predicate structure
    if p1.name != p2.name or len(p1.terms) != len(p2.terms) or p1.negated != p2.negated:
        return None

    bindings = {}

    # 2. Compare terms pairwise
    for t1, t2 in zip(p1.terms, p2.terms):
        if t1 == t2:
            continue
        elif isinstance(t1, Variable):
            bindings[t1.name] = t2
        elif isinstance(t2, Variable):
            bindings[t2.name] = t1
        elif isinstance(t1, Constant) and isinstance(t2, Constant):
            if t1 != t2:
                return None  

    return bindings


# --- TEST RUNNER ---
if __name__ == "__main__":
    soc = Constant("Socrates")
    plato = Constant("Plato")
    var_x = Variable("x")
    var_y = Variable("y")

    # Test Case 1: Human(?x) vs Human(Socrates) -> Success
    p1 = Predicate("human", [var_x])
    p2 = Predicate("human", [soc])
    print("Test 1 Result:", unify(p1, p2))  # Expected: {'x': Socrates}

    # Test Case 2: Knows(Socrates, ?y) vs Knows(?x, Plato) -> Success
    p3 = Predicate("knows", [soc, var_y])
    p4 = Predicate("knows", [var_x, plato])
    print("Test 2 Result:", unify(p3, p4))  # Expected: {'x': Socrates, 'y': Plato}

    # Test Case 3: Human(Socrates) vs Human(Plato) -> Fail
    p5 = Predicate("human", [soc])
    p6 = Predicate("human", [plato])
    print("Test 3 Result:", unify(p5, p6))  # Expected: None
