# primitives.py

class Constant:
    """Represents a concrete entity in the world (e.g., 'Socrates', 'Earth')."""
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Constant) and self.name == other.name

    def __hash__(self):
        return hash(("Constant", self.name))


class Variable:
    """Represents a logic variable placeholder (e.g., '?x', '?y')."""
    def __init__(self, name: str):
        self.name = name.lstrip("?")  # Strips '?' if present for uniform storage

    def __repr__(self):
        return f"?{self.name}"

    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name

    def __hash__(self):
        return hash(("Variable", self.name))


class Predicate:
    """Represents a relation or property (e.g., 'human(Socrates)' or '~mortal(?x)')."""
    def __init__(self, name: str, terms: list[Constant | Variable], negated: bool = False):
        self.name = name.lower()
        self.terms = terms
        self.negated = negated

    def __repr__(self):
        prefix = "~" if self.negated else ""
        args_str = ", ".join(str(t) for t in self.terms)
        return f"{prefix}{self.name}({args_str})"

    def __eq__(self, other):
        return (
            isinstance(other, Predicate)
            and self.name == other.name
            and self.terms == other.terms
            and self.negated == other.negated
        )


class Rule:
    """Represents logical implication: Premise => Conclusion."""
    def __init__(self, premise: Predicate, conclusion: Predicate):
        self.premise = premise
        self.conclusion = conclusion

    def __repr__(self):
        return f"{self.premise} => {self.conclusion}"


# --- TEST RUNNER ---
if __name__ == "__main__":
    # Create concrete terms
    socrates = Constant("Socrates")
    var_x = Variable("x")

    # Create predicates
    fact_human = Predicate("human", [socrates])
    rule_premise = Predicate("human", [var_x])
    rule_conclusion = Predicate("mortal", [var_x])

    # Create logical rule: human(?x) => mortal(?x)
    mortality_rule = Rule(premise=rule_premise, conclusion=rule_conclusion)

    # Print objects to verify string representations
    print("Constant:        ", socrates)
    print("Variable:        ", var_x)
    print("Fact Predicate:  ", fact_human)
    print("Logical Rule:    ", mortality_rule)
