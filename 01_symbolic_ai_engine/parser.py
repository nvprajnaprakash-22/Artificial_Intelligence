# parser.py
import re
from primitives import Constant, Variable, Predicate, Rule


def parse_term(token: str) -> Constant | Variable:
    """Converts a token string into a Variable if it starts with '?', else Constant."""
    token = token.strip()
    if token.startswith("?"):
        return Variable(token)
    return Constant(token)


def parse_input(text: str) -> tuple[str, Predicate | Rule | None]:
    """
    Parses natural language strings into symbolic primitives.
    Returns a tuple: (INPUT_TYPE, OBJECT)
    Types: 'RULE', 'FACT', 'QUERY', 'UNKNOWN'
    """
    text = text.strip().rstrip(".?")

    # 1. Rule Pattern: "If ?x is human then ?x is mortal"
    rule_match = re.match(r"^If (\?\w+|\w+) is (\w+) then \1 is (\w+)$", text, re.IGNORECASE)
    if rule_match:
        var_token, premise_name, conclusion_name = rule_match.groups()
        term = parse_term(var_token)
        premise = Predicate(premise_name, [term])
        conclusion = Predicate(conclusion_name, [term])
        return "RULE", Rule(premise, conclusion)

    # 2. Query Pattern: "Is Socrates mortal"
    query_match = re.match(r"^Is (\?\w+|\w+) (not )?(\w+)$", text, re.IGNORECASE)
    if query_match:
        entity, negation, prop = query_match.groups()
        term = parse_term(entity)
        is_negated = bool(negation)
        return "QUERY", Predicate(prop, [term], negated=is_negated)

    # 3. Fact Pattern: "Socrates is human" or "Socrates is not human"
    fact_match = re.match(r"^(\?\w+|\w+) is (not )?(\w+)$", text, re.IGNORECASE)
    if fact_match:
        entity, negation, prop = fact_match.groups()
        term = parse_term(entity)
        is_negated = bool(negation)
        return "FACT", Predicate(prop, [term], negated=is_negated)

    return "UNKNOWN", None


# --- TEST RUNNER ---
if __name__ == "__main__":
    test_strings = [
        "If ?x is human then ?x is mortal",
        "Socrates is human",
        "Socrates is not human",
        "Is Socrates mortal?"
    ]

    for s in test_strings:
        kind, obj = parse_input(s)
        print(f"Input: '{s}'")
        print(f"   Parsed ({kind}): {obj}\n")
