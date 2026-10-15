# Topic 10 to 15 Question Bank

DATA = [
    {
        "topicId": "logic-source-code1",
        "topicName": "Logic Coverage from Source Code (Part 1)",
        "sourcePdf": "logic-source-code1.pdf",
        "questions": [
            {
                "id": "lsc1-001",
                "question": "What four conditions constitute the RIPR model for a software failure to be observed?",
                "options": {
                    "A": "Reachability, Infection, Propagation, Revealability",
                    "B": "Regression, Integration, Performance, Recovery",
                    "C": "Read, Inspect, Process, Return",
                    "D": "Refactor, Instrument, Profile, Release"
                },
                "correctAnswer": "A",
                "explanation": "The RIPR model establishes that for a fault to result in an observed failure: (1) execution must Reach the fault, (2) the fault must Infect internal state, (3) the infected state must Propagate to output, and (4) the incorrect output must be Revealed to the oracle.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "lsc1-002",
                "question": "In the RIPR model, what is 'Infection'?",
                "options": {
                    "A": "The program state becomes incorrect immediately after executing the faulted statement.",
                    "B": "A computer virus enters the machine.",
                    "C": "The test runner crashes.",
                    "D": "The compiler issues a warning."
                },
                "correctAnswer": "A",
                "explanation": "Infection occurs when executing the faulty statement causes the internal state (variable values, memory, program counter) to differ from what the correct version would hold.",
                "difficulty": "medium",
                "sourcePages": [3]
            },
            {
                "id": "lsc1-003",
                "question": "In the RIPR model, what is 'Propagation'?",
                "options": {
                    "A": "The infected internal state persists through subsequent computations until it affects the program's observable output.",
                    "B": "Sharing the code on GitHub.",
                    "C": "Running tests across multiple threads.",
                    "D": "Executing a loop 10 times."
                },
                "correctAnswer": "A",
                "explanation": "Propagation means the corrupted internal state is not masked or overwritten by subsequent computations, but instead flows forward to taint observable variables or output.",
                "difficulty": "medium",
                "sourcePages": [3]
            },
            {
                "id": "lsc1-004",
                "question": "In the Thermostat program example, what does the clause 'override' typically represent in the heating decision predicate?",
                "options": {
                    "A": "A manual override setting that can force heating ON regardless of the scheduled time program.",
                    "B": "An error code indicating sensor failure.",
                    "C": "A method to delete user preferences.",
                    "D": "The cooling fan speed."
                },
                "correctAnswer": "A",
                "explanation": "In the thermostat control predicate, the 'override' boolean clause models manual user intervention that takes precedence over the automated schedule.",
                "difficulty": "easy",
                "sourcePages": [5, 6]
            },
            {
                "id": "lsc1-005",
                "question": "How does short-circuit evaluation of logical operators (&&, ||) in source code affect logic coverage testing?",
                "options": {
                    "A": "If earlier clauses evaluate such that the predicate outcome is fixed, later clauses are not evaluated by the runtime, which can mask potential runtime faults in those skipped expressions.",
                    "B": "It doubles execution speed with no testing impact.",
                    "C": "It converts all booleans to integers.",
                    "D": "It forces every clause to be evaluated in all tests."
                },
                "correctAnswer": "A",
                "explanation": "In languages with short-circuiting, if clause A is false in 'A && B', clause B is never executed. Testing must explicitly choose inputs where A is true to execute and verify clause B.",
                "difficulty": "medium",
                "sourcePages": [4, 7]
            },
            {
                "id": "lsc1-006",
                "question": "Consider 'if (p != null && p.isActive())'. What happens if short-circuit evaluation is NOT used?",
                "options": {
                    "A": "A NullPointerException would occur when p is null, because p.isActive() would still be evaluated.",
                    "B": "The program executes faster.",
                    "C": "isActive() returns false.",
                    "D": "The compiler optimizes out the check."
                },
                "correctAnswer": "A",
                "explanation": "Short-circuit evaluation is essential here to protect against dereferencing null pointers. Without short-circuiting, p.isActive() would execute when p is null, crashing the system.",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "lsc1-007",
                "question": "In source code logic testing, why is Predicate Coverage (Branch Coverage) considered insufficient to uncover faults in complex conditions like 'if (a || b)'?",
                "options": {
                    "A": "Because tests {(a=T, b=F) [true], (a=F, b=F) [false]} achieve 100% Branch Coverage without ever testing clause 'b' evaluating to true.",
                    "B": "Because branch coverage is black-box.",
                    "C": "Because branch coverage cannot test while loops.",
                    "D": "Because branch coverage requires writing new compilers."
                },
                "correctAnswer": "A",
                "explanation": "100% Branch Coverage can be achieved without ever exercising individual clauses (like 'b') under both truth values, leaving sub-condition bugs undetected.",
                "difficulty": "medium",
                "sourcePages": [8]
            },
            {
                "id": "lsc1-008",
                "question": "In the Thermostat logic, if predicate is 'p = (temp < target - threshold) || override', what makes 'override' determine p?",
                "options": {
                    "A": "(temp < target - threshold) must be FALSE.",
                    "B": "(temp < target - threshold) must be TRUE.",
                    "C": "target must be 0.",
                    "D": "temp must equal target."
                },
                "correctAnswer": "A",
                "explanation": "In an OR expression (A || B), clause B determines the outcome only when clause A is FALSE. If A were TRUE, the predicate would evaluate to TRUE regardless of B.",
                "difficulty": "medium",
                "sourcePages": [6]
            },
            {
                "id": "lsc1-009",
                "question": "What is 'state masking' in the context of the RIPR propagation step?",
                "options": {
                    "A": "When an infected variable value is overwritten or neutralized before it can alter the program output.",
                    "B": "Setting a variable to 0.",
                    "C": "Using private variables in a class.",
                    "D": "Hiding GUI windows."
                },
                "correctAnswer": "A",
                "explanation": "State masking occurs when a corrupted state is wiped out (e.g., multiplied by 0, overwritten by a subsequent assignment, or filtered by a min/max clamp) so the output appears normal despite the internal fault.",
                "difficulty": "medium",
                "sourcePages": [3, 9]
            },
            {
                "id": "lsc1-010",
                "question": "When generating tests for source code logic, what is a 'reachability condition'?",
                "options": {
                    "A": "The path condition that must be satisfied by input variables to execute control flow up to the decision statement containing the predicate.",
                    "B": "Connecting to the internet.",
                    "C": "Checking if a variable is in scope.",
                    "D": "Checking if the server is running."
                },
                "correctAnswer": "A",
                "explanation": "Before a predicate's clauses can be tested, the test inputs must satisfy all prior branching conditions required to reach that decision point in the program.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "lsc1-011",
                "question": "Suppose predicate p in source code has 3 clauses: a, b, c. If short-circuiting is active, how does the order of clauses matter?",
                "options": {
                    "A": "Clauses placed first are always evaluated, while clauses placed later may be skipped depending on the outcome of earlier clauses.",
                    "B": "The order has no operational effect whatsoever.",
                    "C": "Short-circuiting reverses the order of execution.",
                    "D": "Only the middle clause is evaluated."
                },
                "correctAnswer": "A",
                "explanation": "Left-to-right evaluation with short-circuiting means that whether clause b and c are reached depends entirely on the truth value returned by preceding clauses.",
                "difficulty": "easy",
                "sourcePages": [7]
            },
            {
                "id": "lsc1-012",
                "question": "Why might a clause in a source code predicate be syntactically present but semantically dead?",
                "options": {
                    "A": "Because prior enclosing if-conditions or mathematical identities prevent the conditions required for that clause to determine the predicate.",
                    "B": "Because it has no semicolon.",
                    "C": "Because the programmer forgot to capitalize it.",
                    "D": "Because it is inside a comment."
                },
                "correctAnswer": "A",
                "explanation": "Contextual constraints (such as an outer guard 'if (x > 0)') can make a sub-clause in an inner predicate unreachable or unable to toggle the predicate, rendering it semantically dead.",
                "difficulty": "hard",
                "sourcePages": [11, 12]
            },
            {
                "id": "lsc1-013",
                "question": "In the Thermostat program, what test inputs are needed to satisfy Clause Coverage for 'temp < target - threshold'?",
                "options": {
                    "A": "One test where temp < target - threshold evaluates to true, and one test where it evaluates to false.",
                    "B": "Testing with temp = -100 only.",
                    "C": "Testing only when target = 0.",
                    "D": "Four tests covering all combinations of day and night."
                },
                "correctAnswer": "A",
                "explanation": "Clause Coverage requires each clause to evaluate to both True and False at least once during test execution.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "lsc1-014",
                "question": "If an infected state does NOT propagate to the output during testing, what is the consequence?",
                "options": {
                    "A": "The test will pass (false negative), leaving the latent bug undetected.",
                    "B": "The test will automatically fail.",
                    "C": "The compiler will halt.",
                    "D": "The source code will be corrupted."
                },
                "correctAnswer": "A",
                "explanation": "If propagation fails, the external oracle observes the expected output and marks the test as passed, despite the fact that a faulty statement was executed.",
                "difficulty": "medium",
                "sourcePages": [3]
            },
            {
                "id": "lsc1-015",
                "question": "What is the role of test oracles in the 'Revealability' step of the RIPR model?",
                "options": {
                    "A": "The test oracle must actively inspect the relevant output or state to detect and report the discrepancy.",
                    "B": "The test oracle predicts future weather.",
                    "C": "The test oracle only measures execution time.",
                    "D": "The test oracle compiles source code."
                },
                "correctAnswer": "A",
                "explanation": "Even if the output is corrupted, if the test oracle fails to assert or check that specific output value, the failure will not be revealed to the tester.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "lsc1-016",
                "question": "How can multiple occurrences of the same variable in a predicate (e.g. 'x > 0 && x < 10') be handled in logic coverage?",
                "options": {
                    "A": "As two correlated clauses that share a domain constraint, where certain combinations like (F, F) are infeasible.",
                    "B": "By renaming one of the variables in the code.",
                    "C": "By deleting the second condition.",
                    "D": "By treating them as completely independent variables."
                },
                "correctAnswer": "A",
                "explanation": "When the same variable occurs in multiple clauses, relational constraints tie their truth values together. Tests must be chosen respecting their mutual feasibility.",
                "difficulty": "medium",
                "sourcePages": [13]
            },
            {
                "id": "lsc1-017",
                "question": "What is a 'side-effect' in a predicate clause (e.g. 'if (a && b++ > 0)')?",
                "options": {
                    "A": "Evaluating the clause alters program state (variable values), which can lead to unpredictable behavior if short-circuiting skips the clause.",
                    "B": "A compiler error.",
                    "C": "A database rollback.",
                    "D": "A hardware interruption."
                },
                "correctAnswer": "A",
                "explanation": "Side-effects in boolean expressions (like modifying b with ++) mean that whether state changes occur depends on whether preceding clauses short-circuit, a notorious source of bugs.",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "lsc1-018",
                "question": "Why is testing boolean methods used as clauses (e.g. 'if (isValid(x) && isReady(y))') particularly important?",
                "options": {
                    "A": "Because the internal implementation of the called method could fail or alter state, and its return value directly dictates high-level branch decisions.",
                    "B": "Because boolean methods cannot be compiled.",
                    "C": "Because methods cannot be called in if statements.",
                    "D": "Because boolean methods always return true."
                },
                "correctAnswer": "A",
                "explanation": "Method calls in predicates hide procedural complexity inside a single clause. Testing both true and false outcomes validates both return pathways and their effects on callers.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "lsc1-019",
                "question": "In the Thermostat program, what test pair demonstrates that 'override' actively determines the heating decision?",
                "options": {
                    "A": "Hold normal conditions such that heating is OFF (temp > target); then toggling override from FALSE to TRUE turns heating from OFF to ON.",
                    "B": "Set override to FALSE in both tests.",
                    "C": "Disconnect the temperature sensor.",
                    "D": "Set temperature to absolute zero."
                },
                "correctAnswer": "A",
                "explanation": "Holding minor clauses in the state where heating is normally off isolates 'override' as the sole deciding factor, proving it actively determines the heating command.",
                "difficulty": "medium",
                "sourcePages": [6]
            },
            {
                "id": "lsc1-020",
                "question": "What is the primary takeaway of applying the RIPR model to source code testing?",
                "options": {
                    "A": "Executing a line of code containing a fault does not guarantee finding a bug; the test must also infect state, propagate to output, and be verified by an oracle.",
                    "B": "Writing tests is unnecessary if code compiles.",
                    "C": "Coverage metrics alone guarantee software reliability.",
                    "D": "All faults automatically propagate to stdout."
                },
                "correctAnswer": "A",
                "explanation": "The RIPR model proves that coverage (reachability) is merely a prerequisite. High-quality tests must also trigger state infection, ensure propagation, and verify outputs.",
                "difficulty": "medium",
                "sourcePages": [3, 16]
            }
        ]
    },
    {
        "topicId": "logic-source-code2",
        "topicName": "Logic Coverage from Source Code (Part 2)",
        "sourcePdf": "logic-source-code2.pdf",
        "questions": [
            {
                "id": "lsc2-001",
                "question": "In the classic TriTyp program, what is the primary purpose of the method?",
                "options": {
                    "A": "To classify a triangle given the lengths of its three sides into Equilateral, Isosceles, Scalene, or Invalid.",
                    "B": "To calculate the area of a circle.",
                    "C": "To sort three floating-point numbers.",
                    "D": "To render 3D graphics on GPU."
                },
                "correctAnswer": "A",
                "explanation": "TriTyp is a standard benchmark program in software testing literature that takes three side lengths (s1, s2, s3) and determines if they form a valid triangle and what type it is.",
                "difficulty": "easy",
                "sourcePages": [2]
            },
            {
                "id": "lsc2-002",
                "question": "In TriTyp, what is the Triangle Inequality theorem condition for three sides a, b, and c to form a valid triangle?",
                "options": {
                    "A": "(a + b > c) ∧ (a + c > b) ∧ (b + c > a)",
                    "B": "a + b + c = 180",
                    "C": "a^2 + b^2 = c^2",
                    "D": "a = b = c"
                },
                "correctAnswer": "A",
                "explanation": "For any non-degenerate triangle, the sum of the lengths of any two sides must be strictly greater than the length of the remaining side.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "lsc2-003",
                "question": "What triangle classification should TriTyp return for side inputs (3, 3, 3)?",
                "options": {
                    "A": "Equilateral",
                    "B": "Isosceles",
                    "C": "Scalene",
                    "D": "Not a Triangle"
                },
                "correctAnswer": "A",
                "explanation": "All three sides are equal (3 = 3 = 3), satisfying the definition of an equilateral triangle.",
                "difficulty": "easy",
                "sourcePages": [2, 4]
            },
            {
                "id": "lsc2-004",
                "question": "What triangle classification should TriTyp return for side inputs (3, 3, 5)?",
                "options": {
                    "A": "Isosceles",
                    "B": "Equilateral",
                    "C": "Scalene",
                    "D": "Not a Triangle"
                },
                "correctAnswer": "A",
                "explanation": "Two sides are equal (3 = 3) and they satisfy the triangle inequality (3 + 3 = 6 > 5), making it an isosceles triangle.",
                "difficulty": "easy",
                "sourcePages": [2, 4]
            },
            {
                "id": "lsc2-005",
                "question": "What classification should TriTyp return for side inputs (1, 2, 5)?",
                "options": {
                    "A": "Not a Triangle (Invalid)",
                    "B": "Scalene",
                    "C": "Isosceles",
                    "D": "Equilateral"
                },
                "correctAnswer": "A",
                "explanation": "1 + 2 = 3, which is NOT greater than 5 (violates triangle inequality 1 + 2 > 5). Thus, no triangle can be formed.",
                "difficulty": "easy",
                "sourcePages": [3, 4]
            },
            {
                "id": "lsc2-006",
                "question": "What classification should TriTyp return for side inputs (3, 4, 5)?",
                "options": {
                    "A": "Scalene",
                    "B": "Equilateral",
                    "C": "Isosceles",
                    "D": "Not a Triangle"
                },
                "correctAnswer": "A",
                "explanation": "All three sides are of distinct lengths and satisfy the triangle inequality (3+4>5, 3+5>4, 4+5>3), making it a scalene triangle.",
                "difficulty": "easy",
                "sourcePages": [2]
            },
            {
                "id": "lsc2-007",
                "question": "In TriTyp, what boundary condition occurs when inputs are (2, 2, 4)?",
                "options": {
                    "A": "Degenerate line segment (2 + 2 = 4, not strictly greater), which must be classified as Not a Triangle.",
                    "B": "Isosceles triangle.",
                    "C": "Equilateral triangle.",
                    "D": "Right-angled triangle."
                },
                "correctAnswer": "A",
                "explanation": "A common boundary error in TriTyp implementations is using >= instead of >. When 2 + 2 = 4, the sides collapse into a flat straight line segment, not a valid triangle.",
                "difficulty": "medium",
                "sourcePages": [3, 5]
            },
            {
                "id": "lsc2-008",
                "question": "What happens in TriTyp if one of the side lengths is negative or zero, such as (-1, 4, 4)?",
                "options": {
                    "A": "It must be rejected as Not a Triangle (or invalid input).",
                    "B": "It is classified as an isosceles triangle.",
                    "C": "The program enters an infinite loop.",
                    "D": "It is converted to positive absolute values."
                },
                "correctAnswer": "A",
                "explanation": "Physical side lengths must be strictly positive (> 0). Negative or zero lengths must be caught and rejected by input validation predicates.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "lsc2-009",
                "question": "In the predicate 'if (s1 <= 0 || s2 <= 0 || s3 <= 0)', what does clause 's1 <= 0' determine under RACC?",
                "options": {
                    "A": "It determines the predicate when minor clauses 's2 <= 0' and 's3 <= 0' are both FALSE.",
                    "B": "It determines the predicate when s2 and s3 are both negative.",
                    "C": "It never determines the predicate.",
                    "D": "Only when s1 == s2."
                },
                "correctAnswer": "A",
                "explanation": "In an OR predicate (A || B || C), clause A determines the outcome if and only if all other clauses (B and C) are FALSE.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "lsc2-010",
                "question": "Consider the compound equilateral test: 'if (s1 == s2 && s2 == s3)'. How many clauses are in this predicate?",
                "options": {
                    "A": "2 clauses: (s1 == s2) and (s2 == s3)",
                    "B": "3 clauses",
                    "C": "1 clause",
                    "D": "4 clauses"
                },
                "correctAnswer": "A",
                "explanation": "The predicate contains two relational sub-expressions joined by &&: clause 1 is (s1 == s2) and clause 2 is (s2 == s3). By transitivity, if both are true, s1 == s3.",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "lsc2-011",
                "question": "For the predicate 'if (s1 == s2 && s2 == s3)', what test inputs satisfy RACC for the major clause (s1 == s2)?",
                "options": {
                    "A": "(3, 3, 3) [True, True -> True] and (4, 3, 3) [False, True -> False]",
                    "B": "(3, 3, 3) and (2, 2, 2)",
                    "C": "(3, 4, 5) and (1, 2, 3)",
                    "D": "(0, 0, 0) and (1, 1, 1)"
                },
                "correctAnswer": "A",
                "explanation": "For major clause (s1 == s2), minor clause (s2 == s3) must be fixed to TRUE (e.g. s2=3, s3=3). Then test 1 uses s1=3 (clause is True), and test 2 uses s1=4 (clause is False).",
                "difficulty": "hard",
                "sourcePages": [8, 9]
            },
            {
                "id": "lsc2-012",
                "question": "Why is TriTyp frequently used as an illustrative benchmark in software testing education?",
                "options": {
                    "A": "Despite having few lines of code, it features rich decision logic, subtle boundary conditions, and non-trivial relational clause dependencies.",
                    "B": "Because it was the first program ever written.",
                    "C": "Because it has no branch statements.",
                    "D": "Because it runs only on quantum computers."
                },
                "correctAnswer": "A",
                "explanation": "TriTyp is compact yet contains rich boundary logic (triangle inequality, invalid inputs, edge cases), making it an ideal case study for logic criteria and testing techniques.",
                "difficulty": "easy",
                "sourcePages": [2]
            },
            {
                "id": "lsc2-013",
                "question": "In TriTyp, if integer overflow occurs during side addition (e.g., s1 + s2 wraps around to negative), what defect arises?",
                "options": {
                    "A": "A valid large triangle could be incorrectly flagged as invalid because (s1 + s2 > s3) evaluates to false due to arithmetic overflow.",
                    "B": "The program automatically converts to floating point.",
                    "C": "The sides become imaginary numbers.",
                    "D": "The compiler catches it at runtime."
                },
                "correctAnswer": "A",
                "explanation": "In 32-bit signed integer arithmetic, if s1 and s2 are very large positive numbers (e.g. Integer.MAX_VALUE - 1), s1 + s2 overflows to negative, corrupting the inequality check.",
                "difficulty": "hard",
                "sourcePages": [10]
            },
            {
                "id": "lsc2-014",
                "question": "How many permutation tests are necessary to thoroughly test isosceles triangles in TriTyp?",
                "options": {
                    "A": "3 permutations: (s1 == s2), (s1 == s3), and (s2 == s3).",
                    "B": "1 test is sufficient.",
                    "C": "9 tests.",
                    "D": "0 tests."
                },
                "correctAnswer": "A",
                "explanation": "An isosceles triangle can have any pair of its three sides equal: (a, a, b), (a, b, a), or (b, a, a). All three permutations must be tested to ensure code doesn't favor one pairing.",
                "difficulty": "medium",
                "sourcePages": [11]
            },
            {
                "id": "lsc2-015",
                "question": "If TriTyp is implemented using nested if-statements rather than compound boolean expressions, how does this affect testing?",
                "options": {
                    "A": "The predicates become simpler (single clauses), shifting the testing focus from logic coverage criteria to structural branch and path coverage on the CFG.",
                    "B": "It eliminates all bugs automatically.",
                    "C": "It makes the code impossible to test.",
                    "D": "It doubles the number of input parameters."
                },
                "correctAnswer": "A",
                "explanation": "Refactoring compound predicates into nested single-clause conditionals translates logic coverage directly into branch/edge coverage in the resulting CFG.",
                "difficulty": "medium",
                "sourcePages": [12]
            },
            {
                "id": "lsc2-016",
                "question": "What is an 'off-by-one' boundary value test for the triangle inequality check 'a + b > c' with a = 5 and b = 5?",
                "options": {
                    "A": "c = 9 (valid, 10 > 9), c = 10 (boundary equality, invalid), c = 11 (invalid, 10 < 11)",
                    "B": "c = 0",
                    "C": "c = 100",
                    "D": "c = -5"
                },
                "correctAnswer": "A",
                "explanation": "Boundary value testing probes values immediately on, below, and above the boundary: c=9 (just inside valid region), c=10 (on boundary threshold), c=11 (just outside).",
                "difficulty": "medium",
                "sourcePages": [5]
            },
            {
                "id": "lsc2-017",
                "question": "Suppose TriTyp has an optimization that sorts the side lengths such that s1 <= s2 <= s3 first. How does this simplify the validity check?",
                "options": {
                    "A": "Only the single inequality (s1 + s2 > s3) needs to be tested, because the other two inequalities (s1 + s3 > s2 and s2 + s3 > s1) are mathematically guaranteed.",
                    "B": "All checks are eliminated.",
                    "C": "It converts all triangles to equilateral.",
                    "D": "It requires testing all 6 permutations."
                },
                "correctAnswer": "A",
                "explanation": "If s3 is the longest side (s1 <= s2 <= s3), adding s3 to any positive side will trivially exceed the remaining side. Thus, only s1 + s2 > s3 needs verification.",
                "difficulty": "medium",
                "sourcePages": [13]
            },
            {
                "id": "lsc2-018",
                "question": "In TriTyp testing, what would a test oracle checking the return code 0 (Invalid), 1 (Scalene), 2 (Isosceles), 3 (Equilateral) verify?",
                "options": {
                    "A": "Revealability: confirming that the observable output matches the mathematically expected classification for the input sides.",
                    "B": "The CPU temperature.",
                    "C": "The disk space remaining.",
                    "D": "The compiler version."
                },
                "correctAnswer": "A",
                "explanation": "Comparing the returned type against ground truth for that side combination constitutes the test oracle step (Revealability).",
                "difficulty": "easy",
                "sourcePages": [14]
            },
            {
                "id": "lsc2-019",
                "question": "What happens if a test suite for TriTyp only includes valid triangles (e.g. Equilateral, Isosceles, Scalene) but NO invalid inputs?",
                "options": {
                    "A": "It fails to achieve complete branch coverage, missing the entire error-handling logic for non-triangles.",
                    "B": "It achieves 100% path coverage.",
                    "C": "It is sufficient for production deployment.",
                    "D": "The compiler throws an error."
                },
                "correctAnswer": "A",
                "explanation": "Omitting invalid inputs leaves the entire 'Not a Triangle' branch untested, failing branch coverage and leaving invalid-input bugs completely exposed.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "lsc2-020",
                "question": "Which of the following side sets represents an Isosceles Right Triangle?",
                "options": {
                    "A": "(1, 1, √2) or approximately (1, 1, 1.414)",
                    "B": "(3, 4, 5)",
                    "C": "(2, 2, 2)",
                    "D": "(5, 12, 13)"
                },
                "correctAnswer": "A",
                "explanation": "Two sides are equal (1, 1) and their squares satisfy the Pythagorean theorem: 1^2 + 1^2 = 2 = (√2)^2. This is an isosceles right triangle.",
                "difficulty": "medium",
                "sourcePages": [4]
            }
        ]
    },
    {
        "topicId": "mutation-testing-source-code",
        "topicName": "Mutation Testing Principles & Practice",
        "sourcePdf": "mutation-testing-source-code.pdf",
        "questions": [
            {
                "id": "mut-src-001",
                "question": "In mutation testing, what is the 'ground string'?",
                "options": {
                    "A": "The original, unmodified program or software artifact under test.",
                    "B": "A string of zeros in memory.",
                    "C": "The text of the mutation operator.",
                    "D": "The console error log."
                },
                "correctAnswer": "A",
                "explanation": "The ground string P is the original program (or grammar/specification) before any mutation operators are applied.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "mut-src-002",
                "question": "What is a 'mutant' in mutation testing?",
                "options": {
                    "A": "A modified version of the ground string program created by applying a single syntactic change (mutation operator).",
                    "B": "A test case that fails.",
                    "C": "A compiler error message.",
                    "D": "An infected operating system process."
                },
                "correctAnswer": "A",
                "explanation": "A mutant P' is a syntactically valid program that differs from the original program P by a small syntactic modification introduced by a mutation operator.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "mut-src-003",
                "question": "When is a mutant said to be 'strongly killed' by a test case t?",
                "options": {
                    "A": "When the observable output of the mutant differs from the observable output of the original program: P'(t) ≠ P(t).",
                    "B": "When the mutant crashes the computer.",
                    "C": "When the compiler rejects the mutant.",
                    "D": "When the test case is executed twice."
                },
                "correctAnswer": "A",
                "explanation": "Strongly killing a mutant requires that the test case produces a different final output on the mutant compared to the original program (Reachability + Infection + Propagation).",
                "difficulty": "medium",
                "sourcePages": [8, 9]
            },
            {
                "id": "mut-src-004",
                "question": "When is a mutant said to be 'weakly killed' by a test case t?",
                "options": {
                    "A": "When execution reaches the mutated statement and immediately causes an infected (differing) internal program state, regardless of whether it propagates to the final output.",
                    "B": "When the test runs with low CPU priority.",
                    "C": "When the mutant produces the same output as the original program.",
                    "D": "When the mutant is killed on only 1 operating system."
                },
                "correctAnswer": "A",
                "explanation": "Weak mutation requires only Reachability and Infection: the internal execution state immediately following the mutated statement must differ between P and P'.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "mut-src-005",
                "question": "What is an 'equivalent mutant'?",
                "options": {
                    "A": "A mutant that has different syntax but always produces the exact same output behavior as the original program for all possible inputs.",
                    "B": "A mutant that has the same file size.",
                    "C": "A mutant created by two different programmers.",
                    "D": "A mutant with identical line numbers."
                },
                "correctAnswer": "A",
                "explanation": "An equivalent mutant is semantically identical to the original program. No test case can ever kill an equivalent mutant because its output never differs from the original.",
                "difficulty": "medium",
                "sourcePages": [11]
            },
            {
                "id": "mut-src-006",
                "question": "What is the formula for Mutation Score (MS) in mutation testing?",
                "options": {
                    "A": "MS = K / (M - E), where K = killed mutants, M = total mutants, and E = equivalent mutants.",
                    "B": "MS = K / M",
                    "C": "MS = (M - K) / E",
                    "D": "MS = K × M"
                },
                "correctAnswer": "A",
                "explanation": "Mutation Score represents the percentage of non-equivalent mutants killed by the test suite: K / (M - E). If MS = 1.0 (100%), the test suite is mutation-adequate.",
                "difficulty": "medium",
                "sourcePages": [12]
            },
            {
                "id": "mut-src-007",
                "question": "Why is the Equivalent Mutant Problem known to be fundamentally undecidable in general software engineering?",
                "options": {
                    "A": "Because deciding whether two arbitrary programs compute identical functions is equivalent to the Halting Problem (Rice's Theorem).",
                    "B": "Because mutants are deleted after compilation.",
                    "C": "Because compilers do not support math.",
                    "D": "Because test suites are always finite."
                },
                "correctAnswer": "A",
                "explanation": "Determining semantic equivalence between two arbitrary programs is undecidable in general computability theory (Rice's theorem / Halting problem).",
                "difficulty": "hard",
                "sourcePages": [11]
            },
            {
                "id": "mut-src-008",
                "question": "What are the two core fundamental hypotheses underlying mutation testing?",
                "options": {
                    "A": "The Competent Programmer Hypothesis and the Coupling Effect Hypothesis",
                    "B": "The Halting Hypothesis and Church-Turing Thesis",
                    "C": "Moore's Law and Amdahl's Law",
                    "D": "Agile Manifesto and Waterfall Model"
                },
                "correctAnswer": "A",
                "explanation": "Mutation testing rests on: (1) Competent Programmer Hypothesis (programmers write code close to correct, so faults are small syntactic slips) and (2) Coupling Effect (tests that kill simple faults also detect complex faults).",
                "difficulty": "medium",
                "sourcePages": [13]
            },
            {
                "id": "mut-src-009",
                "question": "What does the 'Coupling Effect' hypothesis state?",
                "options": {
                    "A": "Complex faults are coupled to simple faults in such a way that a test suite capable of detecting all simple first-order mutants will detect the vast majority of complex faults.",
                    "B": "Hardware and software must be tightly coupled.",
                    "C": "Two classes that call each other cannot be tested.",
                    "D": "Mutants must be tested in pairs."
                },
                "correctAnswer": "A",
                "explanation": "The Coupling Effect asserts that simple single-token mutations simulate fundamental flaws so well that test suites killing them are sufficiently thorough to catch complex, multi-point bugs.",
                "difficulty": "medium",
                "sourcePages": [13]
            },
            {
                "id": "mut-src-010",
                "question": "Consider the method 'int Min(int A, int B) { if (A < B) return A; else return B; }'. If mutant 1 changes 'A < B' to 'A <= B', is this an equivalent mutant?",
                "options": {
                    "A": "Yes! When A < B, both return A. When A > B, both return B. When A == B, original returns B (=A) and mutant returns A (=B). Their output is identical for all inputs!",
                    "B": "No, it is killed by input (3, 3).",
                    "C": "No, it is killed by input (2, 5).",
                    "D": "It causes a compile error."
                },
                "correctAnswer": "A",
                "explanation": "When A == B, returning A vs returning B produces the exact same numerical result. For all other inputs, the branch outcome is identical. Thus the mutant is semantically equivalent!",
                "difficulty": "hard",
                "sourcePages": [4, 5, 11]
            },
            {
                "id": "mut-src-011",
                "question": "For the same Min method 'if (A < B) return A; else return B;', suppose mutant 2 changes 'A < B' to 'A > B'. Which test input kills this mutant strongly?",
                "options": {
                    "A": "A = 2, B = 5",
                    "B": "A = 3, B = 3",
                    "C": "A = 0, B = 0",
                    "D": "No test case can kill it."
                },
                "correctAnswer": "A",
                "explanation": "With (2, 5): Original checks 2 < 5 (True) and returns 2. Mutant checks 2 > 5 (False) and returns 5. Since 2 ≠ 5, the mutant is strongly killed!",
                "difficulty": "easy",
                "sourcePages": [5, 6]
            },
            {
                "id": "mut-src-012",
                "question": "What is a 'First-Order Mutant' versus a 'Higher-Order Mutant'?",
                "options": {
                    "A": "A First-Order mutant has exactly one mutation applied; a Higher-Order mutant has two or more mutations applied simultaneously.",
                    "B": "First-Order mutants are for Java; Higher-Order are for Python.",
                    "C": "First-Order mutants run first.",
                    "D": "Higher-Order mutants are equivalent mutants."
                },
                "correctAnswer": "A",
                "explanation": "First-Order Mutants (FOM) introduce exactly one mutation per program instance. Higher-Order Mutants (HOM) combine two or more mutations in a single program copy.",
                "difficulty": "easy",
                "sourcePages": [7]
            },
            {
                "id": "mut-src-013",
                "question": "What is the primary computational bottleneck of mutation testing in continuous integration pipelines?",
                "options": {
                    "A": "The large number of mutants generated, requiring running the test suite hundreds or thousands of times (one per mutant).",
                    "B": "It requires special quantum hardware.",
                    "C": "It cannot run on Windows.",
                    "D": "It consumes all hard drive storage permanently."
                },
                "correctAnswer": "A",
                "explanation": "Mutation generates O(Lines × Operators) mutants. Running the test suite against every single mutant is computationally expensive ('do-fewer, do-faster, do-smarter' optimizations are used).",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "mut-src-014",
                "question": "How does 'weak mutation' achieve significant performance speedups over 'strong mutation'?",
                "options": {
                    "A": "It checks state infection immediately after the mutated statement inside the same execution run without executing the rest of the program.",
                    "B": "It deletes all assertions from tests.",
                    "C": "It skips running the original program.",
                    "D": "It only tests 1 mutant per repository."
                },
                "correctAnswer": "A",
                "explanation": "Weak mutation monitors whether the state is infected right after the mutated statement executes. This avoids running the rest of the program or propagating to the end, enabling fast in-process checks.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "mut-src-015",
                "question": "If a test suite executes 100 mutants, kills 80, and 10 are proven to be equivalent mutants, what is the Mutation Score?",
                "options": {
                    "A": "80 / (100 - 10) = 80 / 90 ≈ 88.89%",
                    "B": "80 / 100 = 80%",
                    "C": "70 / 90 ≈ 77.78%",
                    "D": "100%"
                },
                "correctAnswer": "A",
                "explanation": "Mutation Score = K / (M - E) = 80 / (100 - 10) = 80 / 90 = 88.89%.",
                "difficulty": "medium",
                "sourcePages": [12]
            },
            {
                "id": "mut-src-016",
                "question": "What is a 'stillborn mutant' in mutation testing?",
                "options": {
                    "A": "A mutant that cannot even be compiled or syntactically parsed.",
                    "B": "A mutant that kills the operating system.",
                    "C": "An equivalent mutant.",
                    "D": "A mutant that passes all tests."
                },
                "correctAnswer": "A",
                "explanation": "A stillborn mutant is syntactically invalid or fails compilation; modern mutation tools only generate valid mutants that successfully compile.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "mut-src-017",
                "question": "What is a 'trivial mutant'?",
                "options": {
                    "A": "A mutant that is killed by almost any test case that reaches it.",
                    "B": "A mutant that cannot be killed.",
                    "C": "An equivalent mutant.",
                    "D": "A mutant with no operators."
                },
                "correctAnswer": "A",
                "explanation": "Trivial mutants are very easy to kill (e.g. replacing a return value with null or crashing on entry), providing little discriminative value for test quality.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "mut-src-018",
                "question": "Why is mutation testing considered the 'gold standard' for evaluating test suite quality?",
                "options": {
                    "A": "Because it directly measures the test suite's ability to detect synthetic faults, exposing deficiencies that code coverage metrics miss.",
                    "B": "Because it requires no programming skills.",
                    "C": "Because it is required by HTML5.",
                    "D": "Because it guarantees zero lines of code."
                },
                "correctAnswer": "A",
                "explanation": "High line/branch coverage does not guarantee assertions are thorough. Mutation testing measures whether test assertions actually catch deliberate bugs, revealing gaps in test oracles.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "mut-src-019",
                "question": "What is 'mutant subsumption'?",
                "options": {
                    "A": "Mutant m1 subsumes mutant m2 if any test case that kills m1 is guaranteed to also kill m2.",
                    "B": "When a mutant deletes another mutant.",
                    "C": "When all mutants are equivalent.",
                    "D": "When tests run in parallel."
                },
                "correctAnswer": "A",
                "explanation": "If killing m1 always implies killing m2, m1 is strictly harder to kill and subsumes m2. Subsumption helps identify minimal sets of non-redundant mutants.",
                "difficulty": "hard",
                "sourcePages": [15]
            },
            {
                "id": "mut-src-020",
                "question": "In mutation testing, what is 'test suite minimization' based on mutant kills?",
                "options": {
                    "A": "Finding a minimal subset of test cases that kills all killable mutants.",
                    "B": "Deleting all tests that fail.",
                    "C": "Running only 1 test.",
                    "D": "Minimizing compiler warnings."
                },
                "correctAnswer": "A",
                "explanation": "By framing test selection as a set-cover problem over killed mutants, one can identify the smallest subset of tests that maintains 100% mutation score.",
                "difficulty": "medium",
                "sourcePages": [17]
            }
        ]
    },
    {
        "topicId": "mutation-operators-source-code",
        "topicName": "Mutation Operators for Source Code",
        "sourcePdf": "mutation-operators-source-code.pdf",
        "questions": [
            {
                "id": "mop-001",
                "question": "What does the Arithmetic Operator Replacement (AOR) mutation operator do?",
                "options": {
                    "A": "Replaces each occurrence of an arithmetic operator (+, -, *, /, %) with each of the other arithmetic operators.",
                    "B": "Replaces integers with floating-point numbers.",
                    "C": "Deletes all mathematical equations.",
                    "D": "Replaces if statements with while loops."
                },
                "correctAnswer": "A",
                "explanation": "AOR systematically substitutes basic arithmetic operators (e.g. replacing 'a + b' with 'a - b', 'a * b', 'a / b', 'a % b').",
                "difficulty": "easy",
                "sourcePages": [5, 6]
            },
            {
                "id": "mop-002",
                "question": "What does the Relational Operator Replacement (ROR) mutation operator do?",
                "options": {
                    "A": "Replaces relational operators (<, <=, >, >=, ==, !=) with each of the other relational operators and boolean constants (True, False).",
                    "B": "Replaces database foreign keys.",
                    "C": "Converts variables into relational tables.",
                    "D": "Replaces strings with integers."
                },
                "correctAnswer": "A",
                "explanation": "ROR targets comparison predicates by replacing each relational operator with other comparison operators (e.g., swapping '<' for '<=', '==', '!=', etc.).",
                "difficulty": "easy",
                "sourcePages": [6, 7]
            },
            {
                "id": "mop-003",
                "question": "What does the Conditional Operator Replacement (COR) operator do?",
                "options": {
                    "A": "Replaces logical connectives (&&, ||) with each other, or with left/right operand projections.",
                    "B": "Replaces conditional branches with print statements.",
                    "C": "Replaces class constructors.",
                    "D": "Converts while loops into for loops."
                },
                "correctAnswer": "A",
                "explanation": "COR mutates logical expressions by swapping '&&' with '||' (or vice versa) and testing boolean connective logic.",
                "difficulty": "easy",
                "sourcePages": [7]
            },
            {
                "id": "mop-004",
                "question": "What does the Unary Operator Insertion (UOI) mutation operator do?",
                "options": {
                    "A": "Inserts unary operators (e.g. -, ++, --, !) before or after variables and expressions.",
                    "B": "Deletes the main method.",
                    "C": "Replaces two variables with one.",
                    "D": "Inserts comments into source code."
                },
                "correctAnswer": "A",
                "explanation": "UOI inserts unary negation, increment, decrement, or logical NOT (e.g., changing 'x' to '-x', '++x', or '!x').",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "mop-005",
                "question": "What does the Scalar Variable Replacement (SVR) operator do?",
                "options": {
                    "A": "Replaces each occurrence of a scalar variable with other scalar variables of compatible type in the same scope.",
                    "B": "Converts scalar variables into arrays.",
                    "C": "Deletes all scalar variables.",
                    "D": "Renames variables in the debugger."
                },
                "correctAnswer": "A",
                "explanation": "SVR replaces variable references with other in-scope variables of the same type (e.g. replacing 'width' with 'height'), mimicking common typographical errors.",
                "difficulty": "medium",
                "sourcePages": [9]
            },
            {
                "id": "mop-006",
                "question": "What is 'Selective Mutation'?",
                "options": {
                    "A": "Selecting a small, carefully chosen subset of mutation operators that drastically reduces the total number of mutants while maintaining almost 100% test effectiveness.",
                    "B": "Mutating only test files rather than source code.",
                    "C": "Selecting mutants at random without criteria.",
                    "D": "Mutating code only on weekends."
                },
                "correctAnswer": "A",
                "explanation": "Exhaustive mutation generates excessive mutants. Selective mutation identifies a core set of 5 key operators (e.g., AOR, ROR, COR, UOI, SVR) that retains ~99% fault detection efficacy with a fraction of mutants.",
                "difficulty": "medium",
                "sourcePages": [4, 10]
            },
            {
                "id": "mop-007",
                "question": "What does the Assignment Operator Replacement (ASR) operator do?",
                "options": {
                    "A": "Replaces assignment operators (e.g. '=', '+=', '-=', '*=', '/=') with each other.",
                    "B": "Deletes assignment statements.",
                    "C": "Swaps LHS and RHS.",
                    "D": "Replaces variables with null."
                },
                "correctAnswer": "A",
                "explanation": "ASR targets assignment shorthand operators (e.g. replacing 'x += y' with 'x -= y' or 'x = y').",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "mop-008",
                "question": "In the statement 'int z = x + y;', how many AOR mutants are generated by replacing '+' with the remaining 4 standard arithmetic operators (-, *, /, %)?",
                "options": {
                    "A": "4 mutants",
                    "B": "1 mutant",
                    "C": "10 mutants",
                    "D": "0 mutants"
                },
                "correctAnswer": "A",
                "explanation": "Replacing '+' with '-', '*', '/', and '%' produces exactly 4 first-order AOR mutants.",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "mop-009",
                "question": "What does the Statement Deletion (SDL) mutation operator do?",
                "options": {
                    "A": "Deletes a statement or replaces it with a no-op.",
                    "B": "Deletes the entire file.",
                    "C": "Deletes the git commit history.",
                    "D": "Deletes test assertions."
                },
                "correctAnswer": "A",
                "explanation": "SDL tests whether each statement is truly necessary for correctness by removing it completely and checking if the test suite fails.",
                "difficulty": "easy",
                "sourcePages": [11]
            },
            {
                "id": "mop-010",
                "question": "If original code is 'if (x > 0)' and ROR mutates it to 'if (true)', what does killing this mutant require?",
                "options": {
                    "A": "A test case where x <= 0 that triggers an observable failure because the mutant incorrectly enters the true branch.",
                    "B": "A test where x = 100.",
                    "C": "A test that runs with x as null.",
                    "D": "No test can kill it."
                },
                "correctAnswer": "A",
                "explanation": "When x > 0, original and mutant both take the true branch. To kill it, a test must supply x <= 0 (where original takes false branch but mutant takes true branch) and verify output difference.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "mop-011",
                "question": "What is the primary rationale for designing mutation operators that mimic 'typical programmer mistakes'?",
                "options": {
                    "A": "To ensure tests are targeted at realistic faults likely to be introduced during human development, adhering to the Competent Programmer Hypothesis.",
                    "B": "To make testing as easy as possible.",
                    "C": "Because computers do not make mistakes.",
                    "D": "To avoid writing test assertions."
                },
                "correctAnswer": "A",
                "explanation": "Operators are designed based on empirical studies of common coding slips (e.g., using < instead of <=, off-by-one errors, wrong arithmetic operators, inverted logic).",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "mop-012",
                "question": "What does Logical Operator Replacement (LOR) mutate?",
                "options": {
                    "A": "Bitwise and logical operators (such as &, |, ^) by substituting them with alternative bitwise operators.",
                    "B": "Only boolean literals.",
                    "C": "Variable names.",
                    "D": "Class declarations."
                },
                "correctAnswer": "A",
                "explanation": "LOR mutates bitwise and logical connective operators (&, |, ^, ~).",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "mop-013",
                "question": "In the statement 'y = x * 2;', if an AOR operator changes '*' to '/', what input for x will FAIL to kill the mutant if output is integer-truncated?",
                "options": {
                    "A": "x = 0 (because 0 * 2 = 0 and 0 / 2 = 0, both producing identical output!)",
                    "B": "x = 10",
                    "C": "x = -5",
                    "D": "x = 3"
                },
                "correctAnswer": "A",
                "explanation": "For x = 0: original computes 0 * 2 = 0; mutant computes 0 / 2 = 0. The output is identical, so x = 0 fails to kill the mutant. A test like x = 4 (8 vs 2) is needed.",
                "difficulty": "medium",
                "sourcePages": [5]
            },
            {
                "id": "mop-014",
                "question": "What is 'Constant Replacement' (CR) operator?",
                "options": {
                    "A": "Replaces literal constants with boundary values (e.g. replacing constant C with C+1, C-1, 0, or -C).",
                    "B": "Replaces variable names with numbers.",
                    "C": "Deletes all constants.",
                    "D": "Declares all variables as static final."
                },
                "correctAnswer": "A",
                "explanation": "Constant Replacement mutates hardcoded literals (e.g. changing 10 to 9, 11, 0, or -10) to probe boundary tolerances.",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "mop-015",
                "question": "Why is mutant reduction (e.g. selective mutation or random sampling) essential in large software codebases?",
                "options": {
                    "A": "A large codebase can easily yield 500,000+ mutants; running the entire test suite on each would take days without reduction.",
                    "B": "Compilers cannot compile more than 100 files.",
                    "C": "Git repositories have a 10 mutant limit.",
                    "D": "Mutants expire after 1 hour."
                },
                "correctAnswer": "A",
                "explanation": "Exhaustive mutation on millions of lines of code produces millions of mutants. Reducing mutant count via selective operators makes mutation testing practical in CI/CD pipelines.",
                "difficulty": "easy",
                "sourcePages": [4, 12]
            },
            {
                "id": "mop-016",
                "question": "What does the Absolute Value Insertion (ABS) operator do?",
                "options": {
                    "A": "Replaces an expression 'e' with 'abs(e)' or '-abs(e)'.",
                    "B": "Deletes the variable.",
                    "C": "Converts integers to strings.",
                    "D": "Rounds numbers to nearest integer."
                },
                "correctAnswer": "A",
                "explanation": "ABS mutates arithmetic expressions by forcing them to their absolute value or negative absolute value, testing sign-dependence.",
                "difficulty": "easy",
                "sourcePages": [9]
            },
            {
                "id": "mop-017",
                "question": "What is an 'operator-based mutant generator'?",
                "options": {
                    "A": "A static tool that parses the Abstract Syntax Tree (AST) of the program and applies transformation rules corresponding to defined mutation operators.",
                    "B": "A human software tester.",
                    "C": "A network router.",
                    "D": "A database indexer."
                },
                "correctAnswer": "A",
                "explanation": "Modern mutation testing frameworks (like Pitest for Java or MutPy for Python) parse code into ASTs and rewrite nodes matching mutation operator patterns.",
                "difficulty": "medium",
                "sourcePages": [13]
            },
            {
                "id": "mop-018",
                "question": "In Java bytecode mutation testing, why do modern tools mutate bytecode directly rather than source code?",
                "options": {
                    "A": "Mutating bytecode in-memory is much faster because it avoids recompiling the Java source code from scratch for every mutant.",
                    "B": "Bytecode has no bugs.",
                    "C": "Java source code is read-only.",
                    "D": "Bytecode mutation cannot generate equivalent mutants."
                },
                "correctAnswer": "A",
                "explanation": "Direct bytecode manipulation (using frameworks like ASM) mutates compiled class files in memory and loads them via custom ClassLoaders in milliseconds, bypassing javac overhead.",
                "difficulty": "hard",
                "sourcePages": [14]
            },
            {
                "id": "mop-019",
                "question": "Which of the following mutation operators belongs to the classic '5 Selective Mutation Operators' identified by Offutt et al.?",
                "options": {
                    "A": "AOR, ROR, COR, UOI, SVR",
                    "B": "SQL, HTML, CSS, XML, JSON",
                    "C": "ADD, SUB, MUL, DIV, MOD",
                    "D": "TRY, CATCH, FINALLY, THROW, THROWS"
                },
                "correctAnswer": "A",
                "explanation": "Offutt's empirical research showed that the 5 selective operators (AOR, ROR, COR, UOI, SVR) achieve over 99% coverage effectiveness compared to applying all 22+ operators.",
                "difficulty": "medium",
                "sourcePages": [10]
            },
            {
                "id": "mop-020",
                "question": "How does killing a mutant that was created by replacing 'a < b' with 'a <= b' validate the test suite?",
                "options": {
                    "A": "It proves the test suite includes a precise boundary test case where a == b.",
                    "B": "It proves the test suite has 10,000 tests.",
                    "C": "It proves the code is written in C++.",
                    "D": "It proves the code runs in O(1) time."
                },
                "correctAnswer": "A",
                "explanation": "The only input where 'a < b' evaluates differently from 'a <= b' is the exact boundary condition a == b. Killing this mutant confirms that boundary value testing was performed.",
                "difficulty": "medium",
                "sourcePages": [6, 15]
            }
        ]
    },
    {
        "topicId": "mutation-for-integration",
        "topicName": "Mutation Testing for Integration",
        "sourcePdf": "mutation-for-integration.pdf",
        "questions": [
            {
                "id": "mfi-001",
                "question": "What is the primary target of Integration Mutation (Interface Mutation)?",
                "options": {
                    "A": "Interactions, method invocations, parameter exchanges, and shared state at the boundaries between communicating modules or classes.",
                    "B": "Single arithmetic statements inside private helper methods.",
                    "C": "HTML styling.",
                    "D": "Operating system device drivers."
                },
                "correctAnswer": "A",
                "explanation": "Integration mutation tests whether the connections and data exchanges between software units (caller and callee methods, parameters, return values) are verified thoroughly.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "mfi-002",
                "question": "What does the Integration Parameter Variable Replacement (IPVR) operator do?",
                "options": {
                    "A": "Replaces each parameter in a method call with each other variable of compatible type that is in scope at the call site.",
                    "B": "Deletes the method definition.",
                    "C": "Converts parameters into global variables.",
                    "D": "Renames the method."
                },
                "correctAnswer": "A",
                "explanation": "IPVR substitutes an argument in a method call with another compatible variable in scope (e.g. calling f(y, y) instead of f(x, y)), testing if the wrong variable was passed.",
                "difficulty": "medium",
                "sourcePages": [5, 6]
            },
            {
                "id": "mfi-003",
                "question": "What does the Integration Parameter Exchange (IPEX) operator do?",
                "options": {
                    "A": "Exchanges the order of two parameters of the same type in a method call: e.g. f(a, b) mutated to f(b, a).",
                    "B": "Deletes both parameters.",
                    "C": "Exchanges parameters between two different methods.",
                    "D": "Replaces parameters with null."
                },
                "correctAnswer": "A",
                "explanation": "IPEX swaps arguments of matching types in a call list (e.g. copying f(source, dest) to f(dest, source)), testing order-reversal mistakes.",
                "difficulty": "easy",
                "sourcePages": [7, 8]
            },
            {
                "id": "mfi-004",
                "question": "What does the Integration Method Call Deletion (IMCD) operator do?",
                "options": {
                    "A": "Deletes a method call statement from the caller, or replaces a call returning a value with a default value.",
                    "B": "Deletes the called class from the disk.",
                    "C": "Calls the method twice.",
                    "D": "Inline expands the method."
                },
                "correctAnswer": "A",
                "explanation": "IMCD eliminates a method call (e.g. deleting 'logger.log()' or 'notifyObservers()') to verify whether the method call's side-effect is actually necessary and checked by tests.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "mfi-005",
                "question": "What does the Integration Return Expression Modification (IRET) operator do?",
                "options": {
                    "A": "Modifies the expression in a return statement of a called method, or replaces it with another compatible expression or default value.",
                    "B": "Prevents the method from ever returning.",
                    "C": "Returns multiple values simultaneously.",
                    "D": "Changes the return type in the bytecode."
                },
                "correctAnswer": "A",
                "explanation": "IRET mutates the return value computed by a callee (e.g. changing 'return result;' to 'return result + 1;' or 'return null;'), checking if the caller properly validates the return value.",
                "difficulty": "medium",
                "sourcePages": [11, 12]
            },
            {
                "id": "mfi-006",
                "question": "What does the Integration Variable Lifetime / Scope Modification (IVLF) operator test?",
                "options": {
                    "A": "Alters the initialization, persistence, or lifetime of shared or static state across multiple method calls.",
                    "B": "Sets a timer to terminate the process.",
                    "C": "Deletes local variables on the stack.",
                    "D": "Measures garbage collection cycles."
                },
                "correctAnswer": "A",
                "explanation": "IVLF mutates state persistence across calls, checking whether modules properly handle persistent vs re-initialized shared variables.",
                "difficulty": "hard",
                "sourcePages": [13, 14]
            },
            {
                "id": "mfi-007",
                "question": "Why does integration mutation typically generate far fewer mutants than unit-level source code mutation?",
                "options": {
                    "A": "Because it only mutates interface call boundaries and inter-method parameter exchanges, rather than every statement and operator in the entire method body.",
                    "B": "Because integration tests are shorter.",
                    "C": "Because integration testing is only done on small scripts.",
                    "D": "Because compilers forbid integration mutation."
                },
                "correctAnswer": "A",
                "explanation": "Interface mutation focuses strictly on inter-unit call sites and parameter lists, producing significantly fewer mutants than mutating every arithmetic and relational operator inside all bodies.",
                "difficulty": "medium",
                "sourcePages": [4, 15]
            },
            {
                "id": "mfi-008",
                "question": "Suppose method transfer(fromAccount, toAccount, amount) is called. What mutant does IPEX produce?",
                "options": {
                    "A": "transfer(toAccount, fromAccount, amount)",
                    "B": "transfer(fromAccount, fromAccount, amount)",
                    "C": "transfer(null, null, 0)",
                    "D": "transfer(amount, toAccount, fromAccount)"
                },
                "correctAnswer": "A",
                "explanation": "IPEX exchanges two arguments of the same type (Account), swapping fromAccount and toAccount. A valid test must ensure funds are withdrawn from the correct account.",
                "difficulty": "easy",
                "sourcePages": [7]
            },
            {
                "id": "mfi-009",
                "question": "How is an IMCD mutant killed when a void method call like 'cache.clear()' is deleted?",
                "options": {
                    "A": "By a test that performs an operation where stale cache data leads to an observable incorrect result.",
                    "B": "By checking the compilation log.",
                    "C": "By running the test in debug mode.",
                    "D": "It can never be killed."
                },
                "correctAnswer": "A",
                "explanation": "To kill the deletion of 'cache.clear()', the test must verify that stale data does not persist and corrupt subsequent computations.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "mfi-010",
                "question": "What is the difference between Unit Mutation and Integration Mutation regarding fault localization?",
                "options": {
                    "A": "Unit mutation detects internal logic mistakes inside a function; integration mutation detects interaction, communication, and interface mismatches between units.",
                    "B": "Unit mutation tests hardware; integration mutation tests software.",
                    "C": "Integration mutation only works on databases.",
                    "D": "There is no difference."
                },
                "correctAnswer": "A",
                "explanation": "Unit mutation isolates algorithms within single methods, while integration mutation targets defects that emerge when multiple units interact across interfaces.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "mfi-011",
                "question": "If caller invokes 'printer.print(doc, copies)' where 'copies' is an integer, what mutant does IPVR produce if another integer 'priority' is in scope?",
                "options": {
                    "A": "printer.print(doc, priority)",
                    "B": "printer.print(copies, doc)",
                    "C": "printer.print(null, copies)",
                    "D": "printer.print(doc, copies + 1)"
                },
                "correctAnswer": "A",
                "explanation": "IPVR replaces the argument 'copies' with another compatible in-scope variable 'priority', creating printer.print(doc, priority).",
                "difficulty": "medium",
                "sourcePages": [5]
            },
            {
                "id": "mfi-012",
                "question": "What is an 'over-loaded method call mutation' in object-oriented integration testing?",
                "options": {
                    "A": "Mutating an invocation to bind to a different overloaded variant of the method with different parameter types.",
                    "B": "Calling a method 10,000 times in a tight loop.",
                    "C": "Overloading the CPU.",
                    "D": "Deleting the method signature."
                },
                "correctAnswer": "A",
                "explanation": "Object-oriented languages allow method overloading. A call mutation can switch an invocation between overloaded versions (e.g. process(Object) vs process(String)).",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "mfi-013",
                "question": "What is a 'polymorphic call mutation'?",
                "options": {
                    "A": "Mutating the runtime receiver object or type binding to invoke an overriding method from a different subclass in the inheritance hierarchy.",
                    "B": "Calling two methods at once.",
                    "C": "Converting a method to static.",
                    "D": "Deleting the base class."
                },
                "correctAnswer": "A",
                "explanation": "Polymorphic call mutation alters dynamic dispatch by substituting alternative subclass instances, verifying that the caller correctly interacts with polymorphic implementations.",
                "difficulty": "hard",
                "sourcePages": [17, 18]
            },
            {
                "id": "mfi-014",
                "question": "In integration testing, what is the 'Contract' between caller and callee?",
                "options": {
                    "A": "Preconditions, Postconditions, and Class Invariants (Design by Contract).",
                    "B": "A legal NDA signed by developers.",
                    "C": "A license agreement displayed to users.",
                    "D": "A database schema."
                },
                "correctAnswer": "A",
                "explanation": "Design by Contract establishes preconditions (what the caller must satisfy), postconditions (what the callee guarantees on return), and invariants that must hold across interactions.",
                "difficulty": "easy",
                "sourcePages": [19]
            },
            {
                "id": "mfi-015",
                "question": "If a callee returns null instead of an empty list, and the caller crashes with NullPointerException, what integration issue is exposed?",
                "options": {
                    "A": "An interface contract violation and missing defensive null handling in the caller.",
                    "B": "A compiler defect.",
                    "C": "Hardware memory corruption.",
                    "D": "An infinite recursion."
                },
                "correctAnswer": "A",
                "explanation": "This exposes an interface mismatch where the caller assumes a non-null collection, demonstrating why mutating return expressions (IRET) is critical in integration testing.",
                "difficulty": "easy",
                "sourcePages": [11, 20]
            },
            {
                "id": "mfi-016",
                "question": "Why is mock/stub testing relevant to integration mutation?",
                "options": {
                    "A": "Mutating mocks or mutating the interactions with mocks verifies whether the caller properly verifies and reacts to mock responses.",
                    "B": "Mocks eliminate the need for testing.",
                    "C": "Mocks can only be used in unit testing.",
                    "D": "Mocks cannot return values."
                },
                "correctAnswer": "A",
                "explanation": "When testing integrated components with test doubles, mutating mock configurations verifies that callers properly handle variations, exceptions, and data returns from collaborators.",
                "difficulty": "medium",
                "sourcePages": [21]
            },
            {
                "id": "mfi-017",
                "question": "What is 'coupling mutation score' in integration testing?",
                "options": {
                    "A": "The percentage of integration/interface mutants killed by the integration test suite.",
                    "B": "The degree of coupling between two Git branches.",
                    "C": "The number of lines of glue code.",
                    "D": "The number of database connections."
                },
                "correctAnswer": "A",
                "explanation": "Coupling mutation score assesses how effectively integration tests exercise and validate the connections between integrated subsystems.",
                "difficulty": "medium",
                "sourcePages": [22]
            },
            {
                "id": "mfi-018",
                "question": "In message-passing architectures (e.g. microservices or actor models), how does integration mutation apply?",
                "options": {
                    "A": "By mutating message payloads, headers, routing keys, and drop/delay behaviors between communicating services.",
                    "B": "By deleting the database.",
                    "C": "By turning off the network router.",
                    "D": "By rewriting microservices in assembly."
                },
                "correctAnswer": "A",
                "explanation": "In distributed systems, integration mutation alters message structure, payload fields, and delivery semantics (chaos engineering / fault injection) across service boundaries.",
                "difficulty": "medium",
                "sourcePages": [23]
            },
            {
                "id": "mfi-019",
                "question": "Suppose method calculateTotal(cart, discount) is called. If IPVR replaces 'discount' with 'taxRate' (both floats), what integration defect is simulated?",
                "options": {
                    "A": "Passing the wrong numeric coefficient to the billing subsystem.",
                    "B": "Syntax error.",
                    "C": "Null pointer dereference.",
                    "D": "Heap overflow."
                },
                "correctAnswer": "A",
                "explanation": "Passing the wrong argument of identical type is one of the most common human integration mistakes. IPVR tests whether tests detect this swap.",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "mfi-020",
                "question": "What is the primary benefit of achieving a high integration mutation score before deploying software?",
                "options": {
                    "A": "Confidence that individual units not only function in isolation, but communicate, pass parameters, and handle responses correctly when integrated.",
                    "B": "Guaranteed zero memory usage.",
                    "C": "Immediate release without code review.",
                    "D": "Faster compiler speed."
                },
                "correctAnswer": "A",
                "explanation": "A high integration mutation score confirms that component interactions, edge-case responses, and parameter hand-offs have been robustly tested end-to-end.",
                "difficulty": "medium",
                "sourcePages": [24]
            }
        ]
    },
    {
        "topicId": "regression-testing",
        "topicName": "Regression Testing (Selection & Prioritization)",
        "sourcePdf": "regression-testing.pdf",
        "questions": [
            {
                "id": "reg-001",
                "question": "What is the fundamental objective of Regression Testing?",
                "options": {
                    "A": "To retest software after modifications to confirm that new bugs or regressions have not been introduced into existing, previously working features.",
                    "B": "To write code backwards.",
                    "C": "To test the software only once before deletion.",
                    "D": "To revert the software to version 1.0."
                },
                "correctAnswer": "A",
                "explanation": "Regression testing ensures that code modifications (bug fixes, enhancements, refactoring) do not unintentionally break existing functionality.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "reg-002",
                "question": "What is the 'Retest-All' regression testing strategy?",
                "options": {
                    "A": "Re-running every single test case in the entire test suite on every modified build.",
                    "B": "Writing all tests again from scratch.",
                    "C": "Retesting only failed tests.",
                    "D": "Retesting only once per year."
                },
                "correctAnswer": "A",
                "explanation": "The Retest-All strategy re-executes the entire existing test suite indiscriminately. While safe, it becomes prohibitively slow and expensive as suites grow.",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "reg-003",
                "question": "What is Regression Test Selection (RTS)?",
                "options": {
                    "A": "Selecting a relevant subset of existing test cases that execute the modified parts of the software or components affected by the changes.",
                    "B": "Selecting tests at random.",
                    "C": "Selecting tests based on author names.",
                    "D": "Deleting test cases that take more than 1 second."
                },
                "correctAnswer": "A",
                "explanation": "RTS algorithms analyze source code diffs or impact graphs to identify and execute only those test cases whose execution traces traverse modified code.",
                "difficulty": "easy",
                "sourcePages": [5, 6]
            },
            {
                "id": "reg-004",
                "question": "What is a 'Safe' Regression Test Selection technique?",
                "options": {
                    "A": "An RTS technique that guarantees selecting every test case in the suite that could possibly reveal a fault in the modified program (under certain standard assumptions).",
                    "B": "A technique that never runs tests.",
                    "C": "A technique that encrypts test scripts.",
                    "D": "A technique that runs in an isolated sandbox."
                },
                "correctAnswer": "A",
                "explanation": "A safe RTS algorithm guarantees that any test case capable of producing a different output between the original and modified version will be included in the selected test subset.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "reg-005",
                "question": "What is Test Suite Minimization (TSM) / Test Suite Reduction?",
                "options": {
                    "A": "Permanently identifying and removing redundant test cases from the test suite while preserving coverage of all test requirements.",
                    "B": "Compressing test files with ZIP.",
                    "C": "Shortening test method names.",
                    "D": "Running tests in low-power mode."
                },
                "correctAnswer": "A",
                "explanation": "Test Suite Minimization removes redundant tests that cover requirements already satisfied by other tests, permanently reducing maintenance overhead.",
                "difficulty": "medium",
                "sourcePages": [8]
            },
            {
                "id": "reg-006",
                "question": "What is Test Case Prioritization (TCP)?",
                "options": {
                    "A": "Re-ordering test cases so that those with higher likelihood of revealing faults or higher code coverage are executed earlier in the test run.",
                    "B": "Deleting low priority tests.",
                    "C": "Running only high-priority user stories.",
                    "D": "Assigning tests to senior developers."
                },
                "correctAnswer": "A",
                "explanation": "Test Case Prioritization schedules tests in an optimal execution order to maximize the rate of fault detection, giving developers rapid feedback on breakages.",
                "difficulty": "easy",
                "sourcePages": [9, 10]
            },
            {
                "id": "reg-007",
                "question": "What metric is standardly used to evaluate the effectiveness of Test Case Prioritization schedules?",
                "options": {
                    "A": "APFD (Average Percentage of Faults Detected)",
                    "B": "LOC (Lines of Code)",
                    "C": "CPU utilization percentage",
                    "D": "Cyclomatic complexity"
                },
                "correctAnswer": "A",
                "explanation": "APFD measures how quickly a prioritized test suite reveals faults: higher APFD values indicate that faults are detected earlier in the test execution cycle.",
                "difficulty": "medium",
                "sourcePages": [11]
            },
            {
                "id": "reg-008",
                "question": "What is the formula for APFD (Average Percentage of Faults Detected) for n tests and m faults, where TFi is the index of the first test that detects fault i?",
                "options": {
                    "A": "APFD = 1 - (∑ TFi) / (n × m) + 1 / (2n)",
                    "B": "APFD = (n × m) / ∑ TFi",
                    "C": "APFD = ∑ TFi / (n + m)",
                    "D": "APFD = 1 - (n / m)"
                },
                "correctAnswer": "A",
                "explanation": "The standard APFD formula is: APFD = 1 - (TF1 + TF2 + ... + TFm) / (n × m) + 1 / (2n). It ranges from 0 to 1 (or 0% to 100%).",
                "difficulty": "hard",
                "sourcePages": [11, 12]
            },
            {
                "id": "reg-009",
                "question": "Suppose a test suite of 5 tests {T1, T2, T3, T4, T5} detects 2 faults. If the faults are detected by T1 (position 1) and T2 (position 2), what is the APFD?",
                "options": {
                    "A": "APFD = 1 - (1 + 2) / (5 × 2) + 1 / (2 × 5) = 1 - 3/10 + 1/10 = 0.80 (80%)",
                    "B": "0.50 (50%)",
                    "C": "0.20 (20%)",
                    "D": "1.00 (100%)"
                },
                "correctAnswer": "A",
                "explanation": "APFD = 1 - (1 + 2) / 10 + 1 / 10 = 1 - 0.3 + 0.1 = 0.80 (80%).",
                "difficulty": "hard",
                "sourcePages": [12]
            },
            {
                "id": "reg-010",
                "question": "What is a 'flaky test' in regression testing?",
                "options": {
                    "A": "A test that exhibits both passing and failing outcomes across different runs on the exact same version of code without any source changes.",
                    "B": "A test that takes less than 1 ms.",
                    "C": "A test written in JavaScript.",
                    "D": "A test that tests floating-point numbers."
                },
                "correctAnswer": "A",
                "explanation": "Flaky tests exhibit non-deterministic results due to race conditions, timing issues, network latencies, or order dependencies, undermining developer trust in CI.",
                "difficulty": "easy",
                "sourcePages": [14]
            },
            {
                "id": "reg-011",
                "question": "In Regression Test Selection, what is the 'analysis cost vs execution cost' tradeoff?",
                "options": {
                    "A": "If the time required to perform dependency/impact analysis to select tests exceeds the execution time saved by skipping tests, RTS provides no net benefit.",
                    "B": "RTS always costs zero time.",
                    "C": "Analysis cost only applies to cloud testing.",
                    "D": "Execution cost is always higher than analysis cost."
                },
                "correctAnswer": "A",
                "explanation": "For RTS to be economically viable: Cost(Analysis) + Cost(Selected Tests) must be strictly less than Cost(Retest-All). For very small suites, Retest-All is faster.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "reg-012",
                "question": "What is 'Code Churn' in regression testing analysis?",
                "options": {
                    "A": "The volume of lines of code added, modified, or deleted between two software versions.",
                    "B": "The rotation speed of a hard disk.",
                    "C": "The frequency of developer coffee breaks.",
                    "D": "The number of comments in a file."
                },
                "correctAnswer": "A",
                "explanation": "High code churn (frequent edits across many files) indicates high change instability and correlates strongly with regression defect density.",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "reg-013",
                "question": "What is 'Change Impact Analysis'?",
                "options": {
                    "A": "Techniques that determine the potential ripple effects and affected dependencies resulting from a proposed modification to software.",
                    "B": "A financial audit.",
                    "C": "Measuring the download speed of git clone.",
                    "D": "Checking disk space before writing code."
                },
                "correctAnswer": "A",
                "explanation": "Impact analysis traces data and call dependencies from changed code to identify all callers, data structures, and downstream features that could be influenced.",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "reg-014",
                "question": "How does Test Case Prioritization based on 'Total Statement Coverage' differ from 'Additional Statement Coverage'?",
                "options": {
                    "A": "Total coverage orders tests by overall statements covered; Additional coverage iteratively picks the test that covers the maximum number of statements NOT YET covered by previously chosen tests.",
                    "B": "Total coverage deletes tests; Additional coverage adds new tests.",
                    "C": "They produce the identical ordering in all cases.",
                    "D": "Additional coverage requires running tests in reverse."
                },
                "correctAnswer": "A",
                "explanation": "Total prioritization picks tests greedily by total coverage. Additional prioritization dynamically recalculates coverage, selecting tests that maximize marginal coverage gain.",
                "difficulty": "hard",
                "sourcePages": [10]
            },
            {
                "id": "reg-015",
                "question": "What is the primary risk of aggressive Test Suite Minimization (TSM)?",
                "options": {
                    "A": "Minimization permanently removes tests that are redundant for a specific coverage metric (e.g. branch coverage), but those removed tests might have detected future regression faults.",
                    "B": "Minimization makes the test suite run too fast.",
                    "C": "Minimization corrupts git commits.",
                    "D": "Minimization increases file size."
                },
                "correctAnswer": "A",
                "explanation": "Two tests might cover the same branch with different inputs. Minimizing one test preserves branch coverage, but sacrifices fault-detection capability for other subtle bugs.",
                "difficulty": "medium",
                "sourcePages": [8]
            },
            {
                "id": "reg-016",
                "question": "What role does Continuous Integration (CI) play in modern regression testing?",
                "options": {
                    "A": "It automatically builds and runs regression tests upon every code commit or pull request, giving immediate regression feedback to developers.",
                    "B": "It replaces manual code reviews with automated deployment.",
                    "C": "It eliminates the need for unit testing.",
                    "D": "It prevents developers from committing code."
                },
                "correctAnswer": "A",
                "explanation": "CI platforms (e.g. GitHub Actions, Jenkins) automate test execution on every change, detecting regression bugs within minutes of commit.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "reg-017",
                "question": "What is 'test order dependency' in regression test execution?",
                "options": {
                    "A": "When test B only passes if test A runs before it (due to shared mutable state or database side-effects).",
                    "B": "Sorting test files alphabetically.",
                    "C": "Running unit tests before integration tests.",
                    "D": "Executing tests on a single CPU core."
                },
                "correctAnswer": "A",
                "explanation": "Order dependency occurs when tests are not cleanly isolated and leak state, causing tests to pass or fail depending on the sequence in which they execute.",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "reg-018",
                "question": "What is a 'regression test oracle'?",
                "options": {
                    "A": "A mechanism (such as golden master outputs, assertions, or diff comparisons) that verifies current execution results against expected correct behavior.",
                    "B": "A database server.",
                    "C": "A machine learning model predicting stock prices.",
                    "D": "A developer who writes requirements."
                },
                "correctAnswer": "A",
                "explanation": "An oracle determines whether test execution produced the expected behavior, flagging regressions when discrepancies emerge.",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "reg-019",
                "question": "Why is history-based test prioritization (prioritizing tests that failed recently or test frequently modified files) effective?",
                "options": {
                    "A": "Empirical evidence shows that faults cluster in recently modified code and in components that have historically failed.",
                    "B": "Because older tests expire.",
                    "C": "Because recent files have smaller sizes.",
                    "D": "Because historical tests take less time to execute."
                },
                "correctAnswer": "A",
                "explanation": "Defect clustering and churn correlation mean tests touching recently modified or historically buggy components have a significantly higher likelihood of finding new regressions.",
                "difficulty": "medium",
                "sourcePages": [10, 13]
            },
            {
                "id": "reg-020",
                "question": "What is 'smoke testing' in the context of regression test suites?",
                "options": {
                    "A": "A quick preliminary subset of critical tests executed first to verify that core builds and basic functionalities work before running exhaustive regression suites.",
                    "B": "Testing hardware cooling fans.",
                    "C": "Stress testing until the server overheats.",
                    "D": "Testing only network firewalls."
                },
                "correctAnswer": "A",
                "explanation": "Smoke tests (or build verification tests) verify fundamental sanity. If basic smoke tests fail, the build is rejected immediately without wasting time on full regression runs.",
                "difficulty": "easy",
                "sourcePages": [15]
            }
        ]
    }
]
