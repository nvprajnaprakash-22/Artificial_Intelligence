# kb.py
from primitives import Constant, Variable, Predicate, Rule
from unify import unify


def apply_substitution(pred: Predicate, bindings: dict) -> Predicate:
    """
    Replaces variables in a predicate with their bound values from unification.
    E.g., mortal(?x) + {'x': Socrates} -> mortal(Socrates)
    """
    new_terms = []
    for term in pred.terms:
        if isinstance(term, Variable) and term.name in bindings:
            new_terms.append(bindings[term.name])
        else:
            new_terms.append(term)
    return Predicate(pred.name, new_terms, negated=pred.negated)


class KnowledgeBase:
    def __init__(self):
        self.facts: list[Predicate] = []
        self.rules: list[Rule] = []

    def add_rule(self, rule: Rule):
        if rule not in self.rules:
            self.rules.append(rule)
            print(f"[KB] Added Rule: {rule}")

    def add_fact(self, fact: Predicate) -> bool:
      
        opposite_fact = Predicate(fact.name, fact.terms, negated=not fact.negated)
        if opposite_fact in self.facts:
            print(f"\n[CONTRADICTION DETECTED] Fact '{fact}' conflicts with existing '{opposite_fact}'!")
            return False

       
        if fact in self.facts:
            print(f"[KB] Fact '{fact}' is already known.")
            return True

       
        self.facts.append(fact)
        print(f"[KB] Added Fact: {fact}")
        self._forward_chain()
        return True

    def _forward_chain(self):
        """
        Scans all rules against current facts to derive new knowledge 
        until no further facts can be inferred (Fixpoint).
        """
        new_derived = True
        while new_derived:
            new_derived = False
           
            for fact in list(self.facts):
                for rule in self.rules:
                    bindings = unify(rule.premise, fact)
                    if bindings is not None:
                        derived_fact = apply_substitution(rule.conclusion, bindings)

                        if derived_fact not in self.facts:
                            print(f"  [Inference Engine] Derived new fact: {derived_fact}")
                            self.facts.append(derived_fact)
                            new_derived = True


# --- TEST RUNNER ---
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Define Terms
    var_x = Variable("x")
    socrates = Constant("Socrates")
    plato = Constant("Plato")

    # 1. Define Rule: human(?x) => mortal(?x)
    mortality_rule = Rule(
        premise=Predicate("human", [var_x]),
        conclusion=Predicate("mortal", [var_x])
    )
    kb.add_rule(mortality_rule)

    print("\n--- Testing Inference ---")
    # 2. Add Fact: human(Socrates)
    kb.add_fact(Predicate("human", [socrates]))

    # 3. Add Fact: human(Plato)
    kb.add_fact(Predicate("human", [plato]))

    print("\n--- Testing Contradiction Detection ---")
    # 4. Attempt to add contradicting fact: ~human(Socrates)
    kb.add_fact(Predicate("human", [socrates], negated=True))

    print("\n--- Final Knowledge Base Facts ---")
    for f in kb.facts:
        print(" •", f)
