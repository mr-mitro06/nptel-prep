import os
import json

REVISION_DATA = [
    {
        "topicId": "isp-full-slides",
        "topicName": "Input Space Partitioning (ISP)",
        "sourcePdf": "ISP-full-slides.pdf",
        "keyDefinitions": [
            {"term": "Partition", "definition": "A decomposition of a domain S into non-overlapping subsets (blocks) B1, B2, ..., Bn that are pairwise disjoint (Bi ∩ Bj = ∅) and complete (∪ Bi = S)."},
            {"term": "Input Domain Model (IDM)", "definition": "The formal model specifying input characteristics and their partition blocks before choosing combinations."},
            {"term": "Interface-based IDM", "definition": "Derives characteristics mechanically from parameter types and syntax in isolation."},
            {"term": "Functionality-based IDM", "definition": "Derives characteristics from functional requirements, domain rules, and semantic relationships."}
        ],
        "formulas": [
            {"name": "All Combinations Coverage (ACoC)", "formula": "Total Tests = ∏ |Bi|", "note": "Cartesian product of all characteristic blocks (exponential growth)."},
            {"name": "Each Choice Coverage (ECC)", "formula": "Min Tests = max(|Bi|)", "note": "Every block from every characteristic is exercised at least once."},
            {"name": "Base Choice Coverage (BCC)", "formula": "Total Tests = 1 + ∑ (|Bi| - 1)", "note": "Varies one non-base choice at a time while holding others at base values."},
            {"name": "Multiple Base Choice Coverage (MBCC)", "formula": "Total Tests = M + ∑ (M × (|Bi| - 1))", "note": "Applies BCC across M specified base choice combinations."}
        ],
        "comparisons": [
            {"conceptA": "Interface-based IDM", "conceptB": "Functionality-based IDM", "distinction": "Interface-based is fast and simple but ignores parameter interactions; Functionality-based captures domain semantics and invalid combinations."},
            {"conceptA": "ACoC", "conceptB": "BCC", "distinction": "ACoC tests all combinations (∏ |Bi|) but explodes exponentially; BCC scales linearly (1 + ∑(|Bi|-1)) while providing strong isolation of edge cases."}
        ],
        "commonMisconceptions": [
            "Overlapping blocks are acceptable in ISP: False! Overlapping blocks violate pairwise disjointness and create ambiguity.",
            "Each Choice Coverage guarantees branch coverage: False! ECC only exercises input blocks once, ignoring combinations."
        ],
        "highYieldFacts": [
            "Always isolate special/boundary values (null, 0, empty string, max_int) in their own blocks.",
            "Subsumption hierarchy: ACoC subsumes PWC (Pairwise); PWC subsumes ECC.",
            "BCC subsumes ECC because every non-base block and base block is tested."
        ]
    },
    {
        "topicId": "graphs-structural-coverage",
        "topicName": "Graph Structural Coverage Criteria",
        "sourcePdf": "graphs-structural-coverage.pdf",
        "keyDefinitions": [
            {"term": "Test Path", "definition": "A path in graph G that starts at an initial node n0 ∈ N0 and ends at a final node nf ∈ Nf."},
            {"term": "Simple Path", "definition": "A path where no node is repeated, except possibly that the first and last nodes may be identical (forming a cycle)."},
            {"term": "Prime Path", "definition": "A maximal simple path that does not appear as a proper subpath of any other simple path in the graph."},
            {"term": "Sidetrip vs Detour", "definition": "A sidetrip leaves path at node ni and returns to node ni; a detour leaves at ni and returns to successor node ni+1."}
        ],
        "formulas": [
            {"name": "Node Coverage (NC)", "formula": "TR = N (Reachable Nodes)", "note": "Visit every reachable node at least once."},
            {"name": "Edge Coverage (EC)", "formula": "TR = Paths of length up to 1", "note": "Visit every reachable edge in G."},
            {"name": "Edge-Pair Coverage (EPC)", "formula": "TR = Paths of length up to 2", "note": "Visit every reachable adjacent pair of edges."}
        ],
        "comparisons": [
            {"conceptA": "Node Coverage (NC)", "conceptB": "Edge Coverage (EC)", "distinction": "Edge Coverage strictly subsumes Node Coverage. EC traverses both branches of if-statements; NC may skip empty else branches."},
            {"conceptA": "Complete Path Coverage (CPC)", "conceptB": "Prime Path Coverage (PPC)", "distinction": "CPC requires traversing all paths (infinite with loops); PPC limits paths to maximal simple paths, making test requirements finite."}
        ],
        "commonMisconceptions": [
            "100% statement coverage implies 100% branch coverage: False! Statement coverage (NC) can be satisfied while skipping empty else-branches.",
            "Prime Path Coverage subsumes Complete Round Trip Coverage: False! CRTC covers composite round-trips that are not simple paths."
        ],
        "highYieldFacts": [
            "Subsumption: CPC → PPC → EPC → EC → NC.",
            "Max length of a prime path in an N-node graph is N (simple cycle of N edges).",
            "A self-loop [n, n] is always a prime path of length 1."
        ]
    },
    {
        "topicId": "graphs-structural-coverage-algorithms",
        "topicName": "Graph Structural Coverage Algorithms",
        "sourcePdf": "graphs-structural-coverage-algorithms.pdf",
        "keyDefinitions": [
            {"term": "Prime Path Generation Algorithm", "definition": "Iterative breadth-first expansion: begins with simple paths of length 0 (nodes), extends by one edge to length 1, 2, ..., pruning cycles and dead ends."},
            {"term": "Termination Marker (!)", "definition": "Marks a candidate simple path that forms a cycle (first node = last node) or reaches a sink with no outgoing edges."},
            {"term": "Pruning Marker (*)", "definition": "Marks a candidate path where extending would repeat an internal node (non-simple path)."},
            {"term": "Proper Subpath Pruning", "definition": "Final filter eliminating any simple path that is completely contained within a longer candidate path."}
        ],
        "formulas": [
            {"name": "Path Length", "formula": "Length = Number of edges", "note": "A path of k nodes has length k - 1 edges."},
            {"name": "Basic Block Reduction", "formula": "Collapses linear chains (in-degree=1, out-degree=1) into single nodes", "note": "Drastically reduces graph size without altering branch structure."}
        ],
        "comparisons": [
            {"conceptA": "Touring Directly", "conceptB": "Touring with Sidetrips", "distinction": "Direct touring requires subpath to be contiguous; touring with sidetrips permits diversions via cycles from node ni back to ni."}
        ],
        "commonMisconceptions": [
            "All prime paths start at N0 and end at Nf: False! Prime paths can begin and end at internal nodes; test paths must stitch prefixes/suffixes.",
            "Prime path computation is always polynomial time: False! Dense graphs can exhibit exponential numbers of simple paths."
        ],
        "highYieldFacts": [
            "If a graph is a DAG (acyclic), PPC is equivalent to testing all complete paths from N0 to Nf.",
            "Best-effort touring allows sidetrips when direct touring is infeasible."
        ]
    },
    {
        "topicId": "graphs-data-flow",
        "topicName": "Graph Coverage - Data Flow",
        "sourcePdf": "graphs-data-flow.pdf",
        "keyDefinitions": [
            {"term": "Definition (def)", "definition": "A node or statement where a variable's value is stored, assigned, or read into memory."},
            {"term": "Use", "definition": "A node or edge where a variable's value is referenced or read."},
            {"term": "Def-Clear Path", "definition": "A path from node ni to nj where no intermediate node redefines variable v."},
            {"term": "du-path", "definition": "A simple path from a def of v to a use of v that is def-clear with respect to v."},
            {"term": "du-pair", "definition": "A pair (d, u) of a def and a use where at least one def-clear path connects d to u."}
        ],
        "formulas": [
            {"name": "All-Defs Coverage (ADC)", "formula": "TR = at least one def-clear path from each def to some use", "note": "Weakest data flow criterion."},
            {"name": "All-Uses Coverage (AUC)", "formula": "TR = at least one def-clear path from each def to EACH reachable use", "note": "Standard industrial data flow target."},
            {"name": "All-du-Paths Coverage (ADUPC)", "formula": "TR = EVERY du-path between every def and use", "note": "Strongest data flow criterion."}
        ],
        "comparisons": [
            {"conceptA": "Computation Use (c-use)", "conceptB": "Predicate Use (p-use)", "distinction": "c-use occurs in computations/assignments; p-use occurs inside conditional predicates governing branching."},
            {"conceptA": "PPC", "conceptB": "ADUPC", "distinction": "Neither subsumes the other! PPC sidetrips can violate def-clear conditions, while ADUPC does not require all structural prime paths."}
        ],
        "commonMisconceptions": [
            "Prime Path Coverage subsumes All-du-Paths Coverage: False! Touring a prime path with a sidetrip that redefines the variable violates the def-clear property.",
            "A du-path can loop infinitely: False! By definition, du-paths are simple paths."
        ],
        "highYieldFacts": [
            "Subsumption among data flow criteria: ADUPC → AUC → ADC.",
            "Data flow anomalies: ur-anomaly (use before def), dd-anomaly (double definition without use), du-anomaly (def without use)."
        ]
    },
    {
        "topicId": "graphs-source-code",
        "topicName": "Graph Coverage from Source Code",
        "sourcePdf": "graphs-source-code.pdf",
        "keyDefinitions": [
            {"term": "Basic Block", "definition": "A maximal straight-line sequence of instructions with single entry and single exit."},
            {"term": "Control Flow Graph (CFG)", "definition": "A directed graph representing all paths that might be traversed through a program during execution."},
            {"term": "Cyclomatic Complexity V(G)", "definition": "A software metric measuring the number of linearly independent paths in the graph."}
        ],
        "formulas": [
            {"name": "Cyclomatic Complexity (Standard)", "formula": "V(G) = E - N + 2P", "note": "For single procedure (P=1): V(G) = E - N + 2."},
            {"name": "Cyclomatic Complexity (Predicates)", "formula": "V(G) = P + 1", "note": "Where P is the number of binary decision/predicate nodes."},
            {"name": "Cyclomatic Complexity (Planar)", "formula": "V(G) = Enclosed Regions + 1", "note": "For planar CFG representations."}
        ],
        "comparisons": [
            {"conceptA": "Statement Coverage", "conceptB": "Branch Coverage", "distinction": "Statement coverage = Node Coverage on CFG; Branch coverage = Edge Coverage on CFG."},
            {"conceptA": "While Loop", "conceptB": "Do-While Loop", "distinction": "While loop tests condition at entry (can execute 0 times); Do-while executes body first before condition."}
        ],
        "commonMisconceptions": [
            "Short-circuit expressions (A && B) form a single node: False! In detailed CFGs, short-circuiting splits into two sequential decision nodes.",
            "Cyclomatic complexity counts total lines of code: False! It measures decision topology (edges - nodes + 2)."
        ],
        "highYieldFacts": [
            "V(G) = 1 implies pure sequential code with no branches or loops.",
            "Basis path testing generates V(G) linearly independent test paths.",
            "Break jumps directly to loop exit; Continue jumps to loop condition/increment."
        ]
    },
    {
        "topicId": "graphs-source-code-data-flow",
        "topicName": "Graph Coverage - Source Code Data Flow",
        "sourcePdf": "graphs-source-code-data-flow.pdf",
        "keyDefinitions": [
            {"term": "Source Code Defs", "definition": "Variable initialization, assignments (x = ...), inputs (scanf, cin), and pass-by-reference returns."},
            {"term": "Source Code Uses", "definition": "Expressions in RHS, conditional guards (if, while), method arguments, and output statements."},
            {"term": "Aliasing", "definition": "When multiple pointers or reference variables refer to the exact same memory location."}
        ],
        "formulas": [
            {"name": "Intraprocedural Data Flow", "formula": "Analysis scoped within a single function", "note": "Tracks local variable defs and uses."},
            {"name": "Interprocedural Data Flow", "formula": "Analysis tracing across callers and callees", "note": "Tracks parameters, return values, and global/heap state."}
        ],
        "comparisons": [
            {"conceptA": "Static Data Flow Analysis", "conceptB": "Dynamic Data Flow Testing", "distinction": "Static analysis checks code without execution (catches uninitialized reads); Dynamic testing executes inputs to verify def-clear paths."}
        ],
        "commonMisconceptions": [
            "Array writes 'a[i] = 5' are easy to track statically: False! If i is dynamic, static analysis cannot easily resolve aliasing with a[j].",
            "Shadowed variables share du-pairs: False! Lexical scoping separates shadowed variables into distinct memory identities."
        ],
        "highYieldFacts": [
            "Statements like 'x = x + 1' contain a use of x followed by a new definition of x.",
            "Loop increments 'i++' contain both a use and a def in each iteration."
        ]
    },
    {
        "topicId": "graphs-specification",
        "topicName": "Graph Coverage from Specifications",
        "sourcePdf": "graphs-specification.pdf",
        "keyDefinitions": [
            {"term": "Finite State Machine (FSM)", "definition": "A behavioral model composed of states (nodes), transitions (edges), events, guard conditions, and actions."},
            {"term": "State Coverage", "definition": "TR requires visiting every defined state in the FSM (equivalent to Node Coverage)."},
            {"term": "Transition Coverage", "definition": "TR requires traversing every valid transition in the FSM (equivalent to Edge Coverage)."},
            {"term": "Sneak Path", "definition": "An illegal transition taken when an unexpected event is erroneously accepted in a state where it is unspecified."}
        ],
        "formulas": [
            {"name": "Transition Syntax", "formula": "Event [Guard] / Action", "note": "Transition fires when Event arrives and Guard condition is True."},
            {"name": "State Explosion", "formula": "|Global States| = ∏ |Component States|", "note": "Cartesian explosion in concurrent FSM systems."}
        ],
        "comparisons": [
            {"conceptA": "State Coverage", "conceptB": "Transition Coverage", "distinction": "State coverage tests each state once; Transition coverage tests all paths connecting states (Edge coverage)."},
            {"conceptA": "Composite State (OR)", "conceptB": "Orthogonal Region (AND)", "distinction": "OR-states are mutually exclusive (in one substate at a time); AND-states execute concurrently (in all subregions)."}
        ],
        "commonMisconceptions": [
            "Negative testing is unnecessary on FSMs: False! Testing unspecified inputs/events is critical to prevent sneak paths.",
            "Specification testing requires reading source code: False! It is strictly black-box derived from behavioral requirements."
        ],
        "highYieldFacts": [
            "History state (H) restores the last active substate upon re-entry.",
            "FSM cycles make Complete Path Coverage infinite and infeasible."
        ]
    },
    {
        "topicId": "logic-coverage-criteria",
        "topicName": "Logic Coverage Criteria (ACC, GACC, CACC, RACC)",
        "sourcePdf": "logic-coverage-criteria.pdf",
        "keyDefinitions": [
            {"term": "Predicate", "definition": "An expression that evaluates to a Boolean value."},
            {"term": "Clause", "definition": "An atomic Boolean expression that contains no logical connectives (AND, OR, NOT)."},
            {"term": "Major vs Minor Clause", "definition": "The clause c being tested for determination is the major clause; all other clauses in the predicate are minor clauses."},
            {"term": "Determination", "definition": "Clause c determines predicate p if toggling c inverts the truth value of p (with minor clauses held fixed)."}
        ],
        "formulas": [
            {"name": "Combinatorial Coverage (CoC)", "formula": "Total Tests = 2^N", "note": "Tests all 2^N truth assignments for N clauses."},
            {"name": "Predicate Coverage (PC)", "formula": "TR = {p = True, p = False}", "note": "Tests predicate evaluating to both outcomes."},
            {"name": "Clause Coverage (CC)", "formula": "For each c: TR = {c = True, c = False}", "note": "Tests each clause evaluating to both outcomes."}
        ],
        "comparisons": [
            {"conceptA": "CC", "conceptB": "PC", "distinction": "CC does NOT subsume PC, and PC does NOT subsume CC! (In p = a || b, tests (T, F) and (F, T) satisfy CC but p is always True)."},
            {"conceptA": "RACC", "conceptB": "CACC", "distinction": "RACC mandates identical minor clause values between test pairs; CACC allows minor clauses to vary as long as predicate toggles with major clause."},
            {"conceptA": "GACC", "conceptB": "PC", "distinction": "GACC does NOT subsume PC because differing minor clauses can leave p=True in both tests!"}
        ],
        "commonMisconceptions": [
            "Clause coverage always ensures branch coverage: False! CC does not subsume PC.",
            "GACC guarantees both predicate outcomes: False! Only CACC and RACC guarantee PC."
        ],
        "highYieldFacts": [
            "Subsumption: CoC → RACC → GACC; CoC → CACC → GACC; RACC/CACC → PC.",
            "DO-178B/C avionics Level A standard mandates MC/DC (equivalent to CACC/RACC).",
            "Minimum test count for RACC with N clauses is N + 1 tests (via shared test cases)."
        ]
    },
    {
        "topicId": "logic-coverage-algorithms",
        "topicName": "Logic Coverage Algorithms",
        "sourcePdf": "logic-coverage-algorithms.pdf",
        "keyDefinitions": [
            {"term": "Boolean Derivative (Boolean Difference)", "definition": "pc = p(c=true) ⊕ p(c=false). Condition under which clause c determines predicate p."},
            {"term": "Determination Condition", "definition": "Clause c determines p if and only if pc evaluates to TRUE."},
            {"term": "Infeasible Logic Combination", "definition": "A truth table combination that cannot occur due to algebraic dependencies (e.g. x < 0 AND x > 10)."}
        ],
        "formulas": [
            {"name": "Boolean Derivative", "formula": "pc = p(c=T) ⊕ p(c=F)", "note": "pc = TRUE implies c independently controls p."},
            {"name": "AND Predicate (p = a ∧ b)", "formula": "pa = b", "note": "Clause 'a' determines p iff 'b' is TRUE."},
            {"name": "OR Predicate (p = a ∨ b)", "formula": "pa = ¬b", "note": "Clause 'a' determines p iff 'b' is FALSE."},
            {"name": "XOR Predicate (p = a ⊕ b)", "formula": "pa = TRUE", "note": "In an XOR gate, any clause always determines the predicate!"}
        ],
        "comparisons": [
            {"conceptA": "X ⊕ FALSE", "conceptB": "X ⊕ TRUE", "distinction": "X ⊕ 0 = X (identity); X ⊕ 1 = ¬X (inversion)."}
        ],
        "commonMisconceptions": [
            "If pc = FALSE, clause c is the most important clause: False! pc = FALSE means clause c is completely dead/redundant and can never affect p."
        ],
        "highYieldFacts": [
            "K-map adjacent cells differing only in clause c with opposite outputs form an exact RACC test pair.",
            "ROBDDs (Reduced Ordered Binary Decision Diagrams) enable fast automated Boolean derivatives."
        ]
    },
    {
        "topicId": "logic-source-code1",
        "topicName": "Logic Coverage from Source Code (Part 1)",
        "sourcePdf": "logic-source-code1.pdf",
        "keyDefinitions": [
            {"term": "RIPR Model", "definition": "Reachability, Infection, Propagation, Revealability. The 4 sequential conditions required to observe a software failure."},
            {"term": "Reachability", "definition": "Test inputs must cause execution to reach the location containing the fault."},
            {"term": "Infection", "definition": "Executing the faulty statement must cause the internal program state to become incorrect."},
            {"term": "Propagation", "definition": "The infected state must propagate through variables and execution to observable output."},
            {"term": "Revealability", "definition": "The test oracle must inspect the faulty output and report the failure."}
        ],
        "formulas": [
            {"name": "Short-Circuit Evaluation", "formula": "A && B: if A is false, B is skipped; A || B: if A is true, B is skipped", "note": "Controls which clauses are reached dynamically."}
        ],
        "comparisons": [
            {"conceptA": "Reachability", "conceptB": "Infection", "distinction": "Executing a line (reachability) does not mean a bug was triggered; inputs must trigger an incorrect state (infection)."}
        ],
        "commonMisconceptions": [
            "100% line coverage means all bugs are caught: False! If state is masked or does not propagate, the test passes with a false negative."
        ],
        "highYieldFacts": [
            "State masking (e.g. multiplying corrupted variable by 0) prevents propagation.",
            "Side-effects in clauses (e.g. if (a && b++ > 0)) lead to bugs when short-circuiting skips the clause."
        ]
    },
    {
        "topicId": "logic-source-code2",
        "topicName": "Logic Coverage from Source Code (Part 2)",
        "sourcePdf": "logic-source-code2.pdf",
        "keyDefinitions": [
            {"term": "TriTyp Case Study", "definition": "A standard testing benchmark that classifies triangles from three side lengths (s1, s2, s3) into Equilateral, Isosceles, Scalene, or Invalid."},
            {"term": "Triangle Inequality", "definition": "Three sides form a valid triangle iff (s1 + s2 > s3) ∧ (s1 + s3 > s2) ∧ (s2 + s3 > s1)."},
            {"term": "Degenerate Triangle", "definition": "When the sum of two sides equals the third (e.g. 2, 2, 4), forming a flat line segment (Invalid)."}
        ],
        "formulas": [
            {"name": "Valid Triangle Condition", "formula": "s1 > 0 ∧ s2 > 0 ∧ s3 > 0 ∧ (s1+s2 > s3) ∧ (s1+s3 > s2) ∧ (s2+s3 > s1)", "note": "All conditions must be satisfied."},
            {"name": "Equilateral Condition", "formula": "s1 == s2 ∧ s2 == s3", "note": "All 3 sides equal."},
            {"name": "Isosceles Condition", "formula": "(s1 == s2 ∨ s1 == s3 ∨ s2 == s3) ∧ ValidTriangle", "note": "At least 2 sides equal."}
        ],
        "comparisons": [
            {"conceptA": "Scalene Triangle", "conceptB": "Invalid Triangle", "distinction": "Scalene satisfies triangle inequality with all sides distinct; Invalid violates the inequality (e.g. 1, 2, 5)."}
        ],
        "commonMisconceptions": [
            "Sides (2, 2, 4) form an isosceles triangle: False! 2 + 2 = 4 (not > 4); it is a degenerate line segment, classified as Invalid.",
            "Testing only valid triangles is sufficient: False! Missing non-triangle tests leaves error handling completely unexercised."
        ],
        "highYieldFacts": [
            "If side lengths are sorted (s1 <= s2 <= s3), only one check is needed: s1 + s2 > s3.",
            "Integer overflow during side addition (s1 + s2) can wrap to negative, causing valid large triangles to fail."
        ]
    },
    {
        "topicId": "mutation-testing-source-code",
        "topicName": "Mutation Testing Principles & Practice",
        "sourcePdf": "mutation-testing-source-code.pdf",
        "keyDefinitions": [
            {"term": "Ground String", "definition": "The original, unmodified program under test."},
            {"term": "Mutant", "definition": "A syntactically valid program variant created by introducing a small syntactic change via a mutation operator."},
            {"term": "Strongly Killed Mutant", "definition": "A test case causes the observable output of the mutant to differ from the original: P'(t) ≠ P(t)."},
            {"term": "Weakly Killed Mutant", "definition": "A test case causes the internal state immediately after the mutated statement to differ between P and P'."},
            {"term": "Equivalent Mutant", "definition": "A mutant that is semantically identical to the original program and can never be killed by any test case."}
        ],
        "formulas": [
            {"name": "Mutation Score (MS)", "formula": "MS = K / (M - E)", "note": "K = killed mutants, M = total mutants, E = equivalent mutants. (MS = 1.0 is mutation adequate)."},
            {"name": "Weak Mutation Requirements", "formula": "Reachability + Infection", "note": "Does not require propagation to program exit."}
        ],
        "comparisons": [
            {"conceptA": "Strong Mutation", "conceptB": "Weak Mutation", "distinction": "Strong mutation requires reachability, infection, and propagation to output; Weak mutation checks state infection immediately after the statement."},
            {"conceptA": "Competent Programmer Hypothesis", "conceptB": "Coupling Effect", "distinction": "Competent programmer assumes faults are small syntactic slips; Coupling effect states tests killing simple mutants also detect complex bugs."}
        ],
        "commonMisconceptions": [
            "Equivalent mutants can be detected automatically by compilers: False! The Equivalent Mutant Problem is undecidable (Rice's Theorem).",
            "100% code coverage guarantees 100% mutation score: False! Tests without strong assertions achieve high coverage but kill few mutants."
        ],
        "highYieldFacts": [
            "Mutation testing evaluates test suite quality (oracle strength), not the program directly.",
            "First-Order Mutants (FOM) have 1 change; Higher-Order Mutants (HOM) combine multiple changes."
        ]
    },
    {
        "topicId": "mutation-operators-source-code",
        "topicName": "Mutation Operators for Source Code",
        "sourcePdf": "mutation-operators-source-code.pdf",
        "keyDefinitions": [
            {"term": "Mutation Operator", "definition": "A syntactic transformation rule that generates a mutant by modifying an AST node or token."},
            {"term": "AOR", "definition": "Arithmetic Operator Replacement: replaces +, -, *, /, % with each other."},
            {"term": "ROR", "definition": "Relational Operator Replacement: replaces <, <=, >, >=, ==, != with each other and True/False."},
            {"term": "COR", "definition": "Conditional Operator Replacement: replaces && and || with each other."},
            {"term": "UOI", "definition": "Unary Operator Insertion: inserts -, ++, --, ! before/after variables."},
            {"term": "SVR", "definition": "Scalar Variable Replacement: substitutes variables with other compatible in-scope variables."}
        ],
        "formulas": [
            {"name": "Selective Mutation (5 Operators)", "formula": "AOR + ROR + COR + UOI + SVR", "note": "Reduces mutant volume drastically while retaining ~99% test effectiveness."}
        ],
        "comparisons": [
            {"conceptA": "Source Code Mutation", "conceptB": "Bytecode Mutation", "distinction": "Source code mutation requires expensive recompilation; Bytecode mutation modifies class files in-memory in milliseconds."}
        ],
        "commonMisconceptions": [
            "All possible mutation operators should always be applied: False! Selective mutation is preferred to avoid computational bottlenecks."
        ],
        "highYieldFacts": [
            "Killing an 'a < b' to 'a <= b' mutant explicitly validates boundary value testing (a == b).",
            "Statement Deletion (SDL) tests whether a statement is truly necessary for program correctness."
        ]
    },
    {
        "topicId": "mutation-for-integration",
        "topicName": "Mutation Testing for Integration",
        "sourcePdf": "mutation-for-integration.pdf",
        "keyDefinitions": [
            {"term": "Integration Mutation", "definition": "Tests interactions, method call boundaries, and parameter exchanges between communicating modules."},
            {"term": "IPVR", "definition": "Integration Parameter Variable Replacement: substitutes an argument in a call with another in-scope variable."},
            {"term": "IPEX", "definition": "Integration Parameter Exchange: swaps the order of two arguments of the same type in a call: f(a, b) -> f(b, a)."},
            {"term": "IMCD", "definition": "Integration Method Call Deletion: removes a method invocation to test if its side-effect is validated."},
            {"term": "IRET", "definition": "Integration Return Expression Modification: alters return values computed by callee."}
        ],
        "formulas": [
            {"name": "Integration Fault Model", "formula": "Call Site Mismatches + Parameter Swaps + Contract Breaches", "note": "Focuses on interfaces rather than internal statement logic."}
        ],
        "comparisons": [
            {"conceptA": "Unit Mutation", "conceptB": "Integration Mutation", "distinction": "Unit mutation mutates internal arithmetic/relational logic inside methods; Integration mutation mutates method call boundaries and interfaces."}
        ],
        "commonMisconceptions": [
            "Passing arguments in reverse order (IPEX) is caught by the compiler: False! If parameters share the same type (e.g. fromAcc, toAcc), the compiler cannot detect the swap."
        ],
        "highYieldFacts": [
            "Integration mutation produces far fewer mutants than unit mutation, making it very cost-effective.",
            "Validating return expressions (IRET) prevents callers from crashing when callees return null or empty lists."
        ]
    },
    {
        "topicId": "regression-testing",
        "topicName": "Regression Testing (Selection & Prioritization)",
        "sourcePdf": "regression-testing.pdf",
        "keyDefinitions": [
            {"term": "Regression Testing", "definition": "Re-testing software after changes to ensure previously working functionality has not broken."},
            {"term": "Retest-All", "definition": "Re-running the entire test suite on every modified build (safe but expensive)."},
            {"term": "Regression Test Selection (RTS)", "definition": "Selecting a subset of existing tests that exercise changed or impacted code."},
            {"term": "Safe RTS", "definition": "Guarantees selecting all tests that could possibly reveal a fault in the modified code."},
            {"term": "Test Suite Minimization (TSM)", "definition": "Permanently removing redundant test cases while preserving requirement coverage."},
            {"term": "Test Case Prioritization (TCP)", "definition": "Ordering test execution to maximize the rate of fault detection as early as possible."}
        ],
        "formulas": [
            {"name": "APFD (Average Percentage of Faults Detected)", "formula": "APFD = 1 - (∑ TFi) / (n × m) + 1 / (2n)", "note": "n = total tests, m = total faults, TFi = test position detecting fault i."},
            {"name": "RTS Economic Feasibility", "formula": "Cost(Analysis) + Cost(Selected Tests) < Cost(Retest-All)", "note": "Condition required for RTS to be beneficial."}
        ],
        "comparisons": [
            {"conceptA": "Total Coverage Prioritization", "conceptB": "Additional Coverage Prioritization", "distinction": "Total sorts tests by absolute coverage; Additional iteratively selects the test maximizing marginal uncovered statements."}
        ],
        "commonMisconceptions": [
            "Test suite minimization has no drawbacks: False! Removing redundant tests for one metric (e.g. branch coverage) reduces future defect detection capability.",
            "Flaky tests are caused by code logic errors: False! Flakiness typically stems from non-determinism, race conditions, and network timing."
        ],
        "highYieldFacts": [
            "High APFD values (approaching 100%) indicate fast fault detection and rapid developer feedback.",
            "Smoke testing runs a small subset of critical tests first before full regression runs."
        ]
    },
    {
        "topicId": "oo-testing",
        "topicName": "Object-Oriented Testing",
        "sourcePdf": "OO-testing.pdf",
        "keyDefinitions": [
            {"term": "Encapsulation Challenge", "definition": "Private fields reduce observability, requiring accessor methods or state inspection to verify postconditions."},
            {"term": "Inheritance Challenge", "definition": "Inherited methods operate in a new subclass context and must be retested in the derived environment."},
            {"term": "Polymorphism Challenge", "definition": "Dynamic binding allows a call site to bind to multiple subclass methods at runtime, requiring testing all feasible receiver types."},
            {"term": "Class Invariant", "definition": "A condition that must remain true for every valid instance across all stable points."}
        ],
        "formulas": [
            {"name": "Flattened Class Testing", "formula": "Subclass Test Scope = Inherited Methods + Overridden Methods + New Methods", "note": "Tests the complete unified method interface."}
        ],
        "comparisons": [
            {"conceptA": "Stub", "conceptB": "Mock", "distinction": "Stubs supply canned state (state verification); Mocks verify behavioral interactions and method invocation protocols (behavior verification)."},
            {"conceptA": "LSP Conformance", "conceptB": "Subclassing", "distinction": "Liskov Substitution requires subclass to pass all superclass test suites without breaking invariants."}
        ],
        "commonMisconceptions": [
            "If a superclass passes all tests, inherited methods need no retesting: False! Context dependency and method overriding can break superclass assumptions."
        ],
        "highYieldFacts": [
            "State-based testing treats public methods as transitions on the Class State Machine.",
            "Dependency Injection decouples classes, allowing effortless injection of mocks and stubs."
        ]
    },
    {
        "topicId": "web-apps-testing",
        "topicName": "Web Applications Testing",
        "sourcePdf": "web-apps-testing.pdf",
        "keyDefinitions": [
            {"term": "Three-Tier Architecture", "definition": "Client Tier (Browser/DOM), Application Tier (Server APIs/Business Logic), Data Persistence Tier (Database)."},
            {"term": "Cross-Site Scripting (XSS)", "definition": "Injecting malicious client-side JavaScript executed by victims' browsers (Reflected, Stored, DOM XSS)."},
            {"term": "SQL Injection (SQLi)", "definition": "Manipulating backend database queries by injecting unsanitized SQL payload fragments."},
            {"term": "Cross-Site Request Forgery (CSRF)", "definition": "Tricking an authenticated user's browser into submitting unauthorized HTTP requests."},
            {"term": "Page Object Model (POM)", "definition": "A design pattern encapsulating web page elements and interactions into reusable test classes."}
        ],
        "formulas": [
            {"name": "HTTP Status Codes", "formula": "2xx = Success, 3xx = Redirection, 4xx = Client Error (404 Not Found), 5xx = Server Error", "note": "Standard response classification."}
        ],
        "comparisons": [
            {"conceptA": "Client-side Validation", "conceptB": "Server-side Validation", "distinction": "Client validation improves UX but is trivially bypassed; Server-side validation is strictly mandatory for security and data integrity."}
        ],
        "commonMisconceptions": [
            "HTTPS encrypts data to protect against SQL injection: False! HTTPS only encrypts the transport channel; backend SQL queries can still be exploited.",
            "Client-side cookies cannot be stolen if sent over HTTPS: False! XSS scripts can read document.cookie unless the HttpOnly flag is set."
        ],
        "highYieldFacts": [
            "SameSite cookie attributes and anti-CSRF tokens defend against CSRF attacks.",
            "Headless browsers execute full browser engines in memory without GUI overhead for rapid CI pipelines."
        ]
    },
    {
        "topicId": "mobile-apps-testing",
        "topicName": "Mobile Applications Testing",
        "sourcePdf": "mobile-apps-testing.pdf",
        "keyDefinitions": [
            {"term": "Device Fragmentation", "definition": "The multitude of diverse hardware models, OS versions, screen sizes, and chipsets."},
            {"term": "Interrupt Testing", "definition": "Verifying that the app handles calls, SMS notifications, alarms, and low battery alerts gracefully without state loss."},
            {"term": "Emulator vs Simulator vs Real Device", "definition": "Emulator mimics hardware+OS; Simulator mimics software APIs; Real device provides actual touch, thermal, and sensor behavior."},
            {"term": "App Lifecycle", "definition": "States (Created, Resumed, Paused, Stopped, Destroyed) governed by the mobile OS."}
        ],
        "formulas": [
            {"name": "Touch Target Minimum Size", "formula": "48 × 48 dp (Android) / 44 × 44 pt (iOS)", "note": "Standard mobile accessibility guideline."}
        ],
        "comparisons": [
            {"conceptA": "Cold Start", "conceptB": "Warm Start", "distinction": "Cold start launches app from scratch (slowest); Warm start resumes an existing background process from memory."}
        ],
        "commonMisconceptions": [
            "Testing on simulators alone is sufficient: False! Physical sensors, touch latency, hardware acceleration, and thermal throttling require real device testing.",
            "Screen rotation never causes data loss: False! In Android, rotation destroys and recreates the Activity by default."
        ],
        "highYieldFacts": [
            "Appium is the standard open-source cross-platform mobile automation framework.",
            "Monkey testing injects pseudo-random streams of user touches to test crash resilience."
        ]
    },
    {
        "topicId": "non-functional-testing",
        "topicName": "Non-Functional Testing (Performance & Security)",
        "sourcePdf": "non-functional-testing.pdf",
        "keyDefinitions": [
            {"term": "Load Testing", "definition": "Evaluating response times and throughput under expected normal and peak user traffic."},
            {"term": "Stress Testing", "definition": "Testing beyond maximum design capacity to discover the breaking point and observe recovery."},
            {"term": "Spike Testing", "definition": "Testing rapid, sudden surges in user traffic followed by immediate drops."},
            {"term": "Soak / Endurance Testing", "definition": "Testing sustained realistic load over extended hours to uncover slow memory and resource leaks."},
            {"term": "CIA Triad", "definition": "Confidentiality (secrecy), Integrity (data accuracy/tamper-resistance), Availability (accessibility)."}
        ],
        "formulas": [
            {"name": "Response Time Formula", "formula": "Response Time = Network Latency + Server Processing Time + Transfer Time", "note": "Total round-trip elapsed time."},
            {"name": "Throughput Formula", "formula": "Throughput = Total Transactions / Elapsed Seconds (TPS)", "note": "System processing velocity."}
        ],
        "comparisons": [
            {"conceptA": "Authentication", "conceptB": "Authorization", "distinction": "Authentication verifies identity (WHO you are); Authorization verifies permissions (WHAT you are allowed to access)."}
        ],
        "commonMisconceptions": [
            "Performance testing can be accurately done on developer laptops: False! Production parity in network latency, database volume, and hardware topology is essential."
        ],
        "highYieldFacts": [
            "JMeter, k6, and Locust are standard open-source load generation tools.",
            "Penetration testing simulates cyberattacks to uncover exploit pathways before attackers do."
        ]
    },
    {
        "topicId": "exer-student",
        "topicName": "Comprehensive Testing Exercises & Case Studies",
        "sourcePdf": "exer-student.pdf",
        "keyDefinitions": [
            {"term": "Integrated Case Studies", "definition": "End-to-end problems combining ISP, CFGs, Prime Paths, Logic Coverage (ACC), and Mutation analysis on realistic code."},
            {"term": "Bounded Stack Case Study", "definition": "A classic test object with state transitions (Empty, Normal, Full) and boundary exceptions (underflow/overflow)."},
            {"term": "TriTyp Decision Synthesis", "definition": "Evaluating compound logic predicates and RACC test pairs on triangle classification."}
        ],
        "formulas": [
            {"name": "Cyclomatic Complexity Synthesis", "formula": "V(G) = E - N + 2 = P + 1", "note": "Checked against control flow regions."},
            {"name": "APFD Comprehensive Formula", "formula": "APFD = 1 - (∑ TFi) / (n × m) + 1 / (2n)", "note": "Calculates prioritization quality."}
        ],
        "comparisons": [
            {"conceptA": "Theory", "conceptB": "Practical Tradeoffs", "distinction": "Theory provides formal coverage criteria; Engineering practice balances coverage targets against time, tool capabilities, and budget."}
        ],
        "commonMisconceptions": [
            "Ad-hoc testing is cheaper than systematic coverage: False! Ad-hoc testing leaves high-risk edge cases undiscovered, multiplying production fixing costs."
        ],
        "highYieldFacts": [
            "Systematic testing provides objective stopping criteria and quantifiable quality metrics.",
            "All-Combinations explodes exponentially; Base Choice and Selective Mutation scale linearly."
        ]
    }
]

out_dir = os.path.join(os.getcwd(), "data")
os.makedirs(out_dir, exist_ok=True)
rev_file = os.path.join(out_dir, "revision.json")
with open(rev_file, "w", encoding="utf-8") as fp:
    json.dump(REVISION_DATA, fp, indent=2, ensure_ascii=False)

print(f"Revision data saved for {len(REVISION_DATA)} topics to {rev_file}")
