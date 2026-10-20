# main.py
from kb import KnowledgeBase
from parser import parse_input


def run_repl():
    kb = KnowledgeBase()
    
    print("Supported syntax examples:")
    print("  • Rule:  If ?x is human then ?x is mortal")
    print("  • Fact:  Socrates is human")
    print("  • Query: Is Socrates mortal?")
    print("Commands: 'facts' (view all), 'rules' (view rules), 'exit'")
    
    while True:
        try:
            user_input = input("AI-Engine > ").strip()
            if not user_input:
                continue

            cmd = user_input.lower()
            if cmd in ["exit", "quit"]:
                print("Exiting engine. Goodbye!")
                break
            elif cmd == "facts":
                print("\n[Current Facts in Knowledge Base]")
                for f in kb.facts:
                    print("  •", f)
                print()
                continue
            elif cmd == "rules":
                print("\n[Current Rules in Knowledge Base]")
                for r in kb.rules:
                    print("  •", r)
                print()
                continue

            # Parse and execute input
            kind, obj = parse_input(user_input)

            if kind == "RULE":
                kb.add_rule(obj)

            elif kind == "FACT":
                kb.add_fact(obj)

            elif kind == "QUERY":
                if obj in kb.facts:
                    print(f"  Answer: YES, '{obj}' is verified in the Knowledge Base.\n")
                else:
                    print(f"  Answer: UNKNOWN or UNVERIFIED ('{obj}' is not in memory).\n")

            else:
                print("  [Syntax Error] Format not recognized. Try 'X is Y' or 'If ?x is A then ?x is B'\n")

        except KeyboardInterrupt:
            print("\nExiting engine.")
            break


if __name__ == "__main__":
    run_repl()
