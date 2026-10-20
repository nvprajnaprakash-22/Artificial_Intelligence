# Symbolic AI Engine (From Scratch)

Most modern AI relies on probabilistic neural networks. This project is an independent implementation of a **Symbolic AI Engine built from scratch in pure Python**, operating on **First-Order Logic (FOL)** and deterministic reasoning rather than statistical probability.

It parses natural language inputs, stores facts and rules in a Knowledge Base, matches patterns using First-Order Unification, and automatically derives new logical facts via Forward Chaining while flagging contradictions.

---

## 📁 Repository Structure

* **`primitives.py`** — AST data structures defining `Constant`, `Variable`, `Predicate`, and `Rule` (`premise => conclusion`).
* **`unify.py`** — First-Order Logic Unification algorithm that compares predicates and extracts variable bindings
  (e.g.,`?x`=>`Socrates`).
* **`kb.py`** — Knowledge Base state manager handling Forward Chaining inference and direct contradiction detection.
* **`parser.py`** — Hand-rolled regex tokenizer and parser converting plain English inputs into AST objects without third-party NLP libraries.
* **`main.py`** — Interactive Command-Line Interface (REPL) for submitting rules, facts, and queries.

---

## 🚀 Quickstart

Run the interactive engine directly with standard Python (no external dependencies required):

```bash
python main.py
