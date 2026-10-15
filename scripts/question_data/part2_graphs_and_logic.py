# Topic 6 to 10 Question Bank

DATA = [
    {
        "topicId": "graphs-source-code-data-flow",
        "topicName": "Graph Coverage - Source Code Data Flow",
        "sourcePdf": "graphs-source-code-data-flow.pdf",
        "questions": [
            {
                "id": "gsc-df-001",
                "question": "How are variable declarations with initializers (e.g., 'int x = 10;') mapped in source code data flow?",
                "options": {
                    "A": "As a definition (def) of variable x at that node.",
                    "B": "Only as a use of variable x.",
                    "C": "Neither a def nor a use.",
                    "D": "As an infeasible path."
                },
                "correctAnswer": "A",
                "explanation": "Initializing a variable assigns a value to its allocated storage, creating a definition (def) of that variable at that node.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gsc-df-002",
                "question": "In the statement 'y = x + z;', what are the data flow definitions and uses?",
                "options": {
                    "A": "Def: {y}; Uses: {x, z}",
                    "B": "Defs: {x, z}; Use: {y}",
                    "C": "Defs: {x, y, z}; Uses: ∅",
                    "D": "Uses: {y}; Defs: ∅"
                },
                "correctAnswer": "A",
                "explanation": "Variable y is being assigned a new value (def), while variables x and z are read in the RHS expression to evaluate the sum (uses).",
                "difficulty": "easy",
                "sourcePages": [3, 4]
            },
            {
                "id": "gsc-df-003",
                "question": "In the statement 'x = x + 1;', which of the following is true?",
                "options": {
                    "A": "The statement contains both a use of x (RHS) and a definition of x (LHS).",
                    "B": "The statement is only a definition of x.",
                    "C": "The statement is only a use of x.",
                    "D": "The statement creates a dead definition anomaly."
                },
                "correctAnswer": "A",
                "explanation": "The current value of x is read on the RHS (use), and the incremented value is written back to x (def). The use occurs prior to the new def within the statement evaluation.",
                "difficulty": "medium",
                "sourcePages": [4]
            },
            {
                "id": "gsc-df-004",
                "question": "How does array indexing such as 'a[i] = 5;' complicate data flow analysis?",
                "options": {
                    "A": "Because the exact element defined depends on runtime value of index 'i', creating potential aliasing and ambiguity about whether subsequent reads of a[j] are def-clear.",
                    "B": "Arrays cannot be represented in CFGs.",
                    "C": "Arrays convert all definitions into uses.",
                    "D": "Array indices are always compile-time constants."
                },
                "correctAnswer": "A",
                "explanation": "If the index i is dynamic, static analysis cannot easily determine if a[i] and a[j] refer to the same memory location, complicating def-clear determination.",
                "difficulty": "hard",
                "sourcePages": [7, 8]
            },
            {
                "id": "gsc-df-005",
                "question": "In pointer-based languages (e.g. C/C++), what is the 'aliasing problem' in data flow testing?",
                "options": {
                    "A": "When two distinct pointer variables point to the same memory address, a write through one pointer defines the variable referenced by the other.",
                    "B": "When a function has two different names.",
                    "C": "When a file is given a symbolic link.",
                    "D": "When variables have the same identifier name in different scopes."
                },
                "correctAnswer": "A",
                "explanation": "Aliasing occurs when multiple references/pointers refer to the same object or memory cell. Modifying *p implicitly modifies *q if p == q, making def-clear detection challenging.",
                "difficulty": "hard",
                "sourcePages": [9, 10]
            },
            {
                "id": "gsc-df-006",
                "question": "What is the difference between intraprocedural data flow analysis and interprocedural data flow analysis?",
                "options": {
                    "A": "Intraprocedural analyzes flow within a single method; interprocedural tracks flow across method boundaries, callers, and callees.",
                    "B": "Intraprocedural is dynamic; interprocedural is static.",
                    "C": "Intraprocedural is for integers; interprocedural is for strings.",
                    "D": "There is no difference."
                },
                "correctAnswer": "A",
                "explanation": "Intraprocedural analysis operates strictly within the confines of an individual procedure. Interprocedural analysis traces definitions and uses through argument passing, returns, and global state across calls.",
                "difficulty": "medium",
                "sourcePages": [12, 13]
            },
            {
                "id": "gsc-df-007",
                "question": "In the loop 'for (int i = 0; i < N; i++) { ... }', where are the definitions and uses of loop variable 'i'?",
                "options": {
                    "A": "Initialization defines i; condition uses i; increment both uses and defines i.",
                    "B": "Initialization uses i; condition defines i.",
                    "C": "Variable i is only defined once and never used.",
                    "D": "i is neither defined nor used."
                },
                "correctAnswer": "A",
                "explanation": "'int i = 0' defines i initially. 'i < N' is a predicate use. 'i++' reads i (use) and updates i (def) at the end of each iteration.",
                "difficulty": "medium",
                "sourcePages": [5, 6]
            },
            {
                "id": "gsc-df-008",
                "question": "In the branch 'if (a > 0 && b < 10)', how are 'a' and 'b' classified?",
                "options": {
                    "A": "Predicate uses (p-uses)",
                    "B": "Computation uses (c-uses)",
                    "C": "Definitions (defs)",
                    "D": "Global constants"
                },
                "correctAnswer": "A",
                "explanation": "Variables evaluated inside conditional branch statements to determine execution paths are classified as predicate uses (p-uses).",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "gsc-df-009",
                "question": "What is a 'kill' of a definition d of variable v in data flow analysis?",
                "options": {
                    "A": "Any subsequent statement that assigns a new value to variable v, terminating the active lifetime of definition d.",
                    "B": "Terminating the process with SIGKILL.",
                    "C": "Catching an unhandled exception.",
                    "D": "Reading the variable value."
                },
                "correctAnswer": "A",
                "explanation": "A definition of variable v is 'killed' when another definition assigns a new value to v, meaning the earlier definition no longer reaches subsequent uses.",
                "difficulty": "medium",
                "sourcePages": [4]
            },
            {
                "id": "gsc-df-010",
                "question": "If method M modifies a class instance field 'this.balance', how should this field modification be tracked in data flow?",
                "options": {
                    "A": "As a definition of the instance field 'balance'.",
                    "B": "As an unused local variable.",
                    "C": "It cannot be tracked in object-oriented code.",
                    "D": "Only as a return expression."
                },
                "correctAnswer": "A",
                "explanation": "Instance variables persist across method invocations; writing to an object field is a state definition (def) that may reach uses in other methods of the object.",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "gsc-df-011",
                "question": "In data flow testing, what does a 'def-use pair with multiple def-clear paths' imply?",
                "options": {
                    "A": "Under All-Uses Coverage (AUC), executing any one def-clear path suffices; under All-du-Paths Coverage (ADUPC), ALL def-clear du-paths must be executed.",
                    "B": "The program is non-deterministic.",
                    "C": "The variable must be duplicated in source code.",
                    "D": "The compiler will reject the code."
                },
                "correctAnswer": "A",
                "explanation": "When multiple distinct paths connect a def to a use without redefining the variable, AUC is satisfied by testing any one path, whereas ADUPC mandates testing every single one.",
                "difficulty": "medium",
                "sourcePages": [11]
            },
            {
                "id": "gsc-df-012",
                "question": "What is static data flow analysis primarily used for in software engineering?",
                "options": {
                    "A": "Detecting anomalies such as uninitialized variable reads, dead stores, and null pointer dereferences without running the code.",
                    "B": "Generating CSS styling automatically.",
                    "C": "Measuring network bandwidth.",
                    "D": "Compressing executable files."
                },
                "correctAnswer": "A",
                "explanation": "Static data flow analysis scans the program structure to discover data lifecycle flaws like uninitialized reads (ur-anomaly) and redundant writes (dd-anomaly) at compile time.",
                "difficulty": "easy",
                "sourcePages": [15, 16]
            },
            {
                "id": "gsc-df-013",
                "question": "Consider a swap method: 'temp = a; a = b; b = temp;'. What is the du-pair for variable 'temp'?",
                "options": {
                    "A": "Def at statement 1 (temp = a), Use at statement 3 (b = temp)",
                    "B": "Def at statement 2, Use at statement 1",
                    "C": "Def at statement 3, Use at statement 2",
                    "D": "There is no du-pair for temp."
                },
                "correctAnswer": "A",
                "explanation": "Variable 'temp' is assigned the value of 'a' in the first statement (def) and read in the third statement (use), with statement 2 being def-clear with respect to temp.",
                "difficulty": "easy",
                "sourcePages": [3, 4]
            },
            {
                "id": "gsc-df-014",
                "question": "When is a du-path considered 'infeasible' in source code?",
                "options": {
                    "A": "When the branch conditions along the du-path are mutually contradictory, preventing any input from following it.",
                    "B": "When the variable has an integer type.",
                    "C": "When the path contains more than 3 statements.",
                    "D": "When the compiler optimizes the code."
                },
                "correctAnswer": "A",
                "explanation": "A path is semantically infeasible if its accumulated path condition (e.g. x > 5 AND x < 2) evaluates to false for all possible inputs.",
                "difficulty": "easy",
                "sourcePages": [17]
            },
            {
                "id": "gsc-df-015",
                "question": "How does variable scoping affect data flow analysis when an inner block shadows an outer variable with the same name?",
                "options": {
                    "A": "Definitions and uses in the inner scope refer to the shadowing variable and must be treated as a distinct variable from the outer one.",
                    "B": "The outer variable is permanently deleted from memory.",
                    "C": "The compiler combines both variables into a single du-pair.",
                    "D": "It causes an infinite loop in the CFG."
                },
                "correctAnswer": "A",
                "explanation": "Variable shadowing creates distinct storage locations with the same identifier; data flow tracking must respect lexical scoping to avoid false du-associations.",
                "difficulty": "medium",
                "sourcePages": [6]
            },
            {
                "id": "gsc-df-016",
                "question": "In a method with an early 'return' inside an if-statement, what happens to du-paths that pass through statements after the if-block?",
                "options": {
                    "A": "Executions that take the early return branch exit the method and will not reach uses located below the return statement.",
                    "B": "The return statement is ignored.",
                    "C": "The uses are executed after method termination.",
                    "D": "It creates a circular du-path."
                },
                "correctAnswer": "A",
                "explanation": "An early return diverts control flow directly to the method exit, precluding execution of subsequent code for that test input.",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "gsc-df-017",
                "question": "What is a 'du-path across loop iterations'?",
                "options": {
                    "A": "A du-path where variable v is defined inside the loop, and used during a subsequent iteration of the loop via the back-edge.",
                    "B": "A loop that executes zero times.",
                    "C": "A path that breaks out of the loop.",
                    "D": "A recursive call."
                },
                "correctAnswer": "A",
                "explanation": "Variables modified in one iteration and consumed in a later iteration create loop-carried data dependencies (loop du-paths).",
                "difficulty": "medium",
                "sourcePages": [10, 11]
            },
            {
                "id": "gsc-df-018",
                "question": "Why is dynamic data flow testing often more computationally expensive to monitor than branch coverage?",
                "options": {
                    "A": "Because runtime instrumentation must track memory read/write operations and verify def-clear paths for numerous variable pairs, not just branch outcomes.",
                    "B": "Because it requires running on supercomputers.",
                    "C": "Because data flow only works on assembly language.",
                    "D": "Because branch coverage requires no execution."
                },
                "correctAnswer": "A",
                "explanation": "Monitoring data flow requires recording variable definitions and tracking their propagation until use across complex execution histories, introducing significant instrumentation overhead.",
                "difficulty": "medium",
                "sourcePages": [18]
            },
            {
                "id": "gsc-df-019",
                "question": "In the statement 'printf(\"%d\", total);', how is 'total' classified?",
                "options": {
                    "A": "Computation use (c-use)",
                    "B": "Predicate use (p-use)",
                    "C": "Definition (def)",
                    "D": "Unreachable state"
                },
                "correctAnswer": "A",
                "explanation": "Passing a variable to an output function (like printf) consumes its value in an output computation, classifying it as a computation use (c-use).",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "gsc-df-020",
                "question": "If a variable is declared globally and modified by multiple concurrent threads, what hazard does data flow testing aim to detect?",
                "options": {
                    "A": "Data races and race conditions where unsynchronized concurrent defs and uses corrupt shared state.",
                    "B": "Syntax errors.",
                    "C": "Static typing failure.",
                    "D": "Prime path termination."
                },
                "correctAnswer": "A",
                "explanation": "Concurrent data flow analysis identifies unsynchronized interleaved writes and reads between threads, which manifest as dangerous race conditions.",
                "difficulty": "medium",
                "sourcePages": [19]
            }
        ]
    },
    {
        "topicId": "graphs-specification",
        "topicName": "Graph Coverage from Specifications",
        "sourcePdf": "graphs-specification.pdf",
        "questions": [
            {
                "id": "gsp-001",
                "question": "When deriving test graphs from software specifications, what formal model is most commonly used?",
                "options": {
                    "A": "Finite State Machines (FSM) or State Transition Diagrams",
                    "B": "Entity Relationship Diagrams",
                    "C": "Bar charts",
                    "D": "Truth tables only"
                },
                "correctAnswer": "A",
                "explanation": "Finite State Machines (FSM) and State Transition Diagrams provide a natural graph model where states are nodes and transitions are edges.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gsp-002",
                "question": "In a Finite State Machine specification, what do the nodes and directed edges correspond to?",
                "options": {
                    "A": "Nodes represent states of the system; edges represent transitions triggered by events or inputs.",
                    "B": "Nodes represent input variables; edges represent arithmetic operations.",
                    "C": "Nodes represent test cases; edges represent bugs.",
                    "D": "Nodes represent database tables; edges represent foreign keys."
                },
                "correctAnswer": "A",
                "explanation": "In an FSM graph representation, vertices/nodes represent recognizable software states (e.g., Idle, Connected, Authenticated), and edges represent valid transitions triggered by events.",
                "difficulty": "easy",
                "sourcePages": [3, 4]
            },
            {
                "id": "gsp-003",
                "question": "What is 'State Coverage' in specification-based testing?",
                "options": {
                    "A": "Visiting every defined state in the FSM at least once (equivalent to Node Coverage).",
                    "B": "Executing every transition in both directions.",
                    "C": "Testing only the initial and final states.",
                    "D": "Checking the CPU register states."
                },
                "correctAnswer": "A",
                "explanation": "State Coverage requires that every state in the specification model is visited by at least one test path, directly corresponding to Node Coverage on the FSM graph.",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "gsp-004",
                "question": "What is 'Transition Coverage' in specification-based testing?",
                "options": {
                    "A": "Executing every valid state transition in the FSM at least once (equivalent to Edge Coverage).",
                    "B": "Executing only transitions that lead to error states.",
                    "C": "Testing each transition 100 times.",
                    "D": "Testing transitions without sending inputs."
                },
                "correctAnswer": "A",
                "explanation": "Transition Coverage requires that each valid transition between states is traversed at least once, which is equivalent to Edge Coverage on the state graph.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "gsp-005",
                "question": "What is 'Transition-Pair Coverage'?",
                "options": {
                    "A": "Executing every pair of adjacent transitions in the FSM (equivalent to Edge-Pair Coverage).",
                    "B": "Executing two tests at the same time.",
                    "C": "Testing only transitions with two input parameters.",
                    "D": "Pairing state coverage with statement coverage."
                },
                "correctAnswer": "A",
                "explanation": "Transition-Pair Coverage requires testing every sequence of two consecutive transitions in the FSM, testing whether taking one transition leaves the system in a state capable of taking the next.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "gsp-006",
                "question": "What is a 'sneak path' in state-based testing?",
                "options": {
                    "A": "An illegal transition that occurs when an unexpected event is accepted by the implementation in a state where the specification does not allow it.",
                    "B": "A secret backdoor planted by malware.",
                    "C": "The fastest path through the graph.",
                    "D": "A test path with zero execution time."
                },
                "correctAnswer": "A",
                "explanation": "A sneak path is an erroneous or unspecified transition taken by the software when an input/event arrives that should have been ignored or rejected in that state.",
                "difficulty": "hard",
                "sourcePages": [8, 9]
            },
            {
                "id": "gsp-007",
                "question": "What does a 'guard condition' on a transition signify?",
                "options": {
                    "A": "A Boolean condition that must evaluate to true for the transition to fire upon receiving an event.",
                    "B": "A security antivirus scanner.",
                    "C": "A loop counter that limits transitions.",
                    "D": "The destination state."
                },
                "correctAnswer": "A",
                "explanation": "Transitions often have the syntax Event [Guard] / Action. The guard is a predicate that must hold true before the event can trigger the state transition.",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "gsp-008",
                "question": "Why is testing unspecified events (robustness/negative testing) critical in state-based specifications?",
                "options": {
                    "A": "To verify that the system gracefully handles unexpected user inputs or out-of-order events without crashing or corrupting state.",
                    "B": "To increase compile time.",
                    "C": "Because the specification guarantees no unexpected events will ever occur.",
                    "D": "To avoid achieving 100% state coverage."
                },
                "correctAnswer": "A",
                "explanation": "Systems must be robust against invalid sequences (e.g. clicking 'Checkout' before adding items to cart); testing unspecified events verifies error handling.",
                "difficulty": "medium",
                "sourcePages": [9]
            },
            {
                "id": "gsp-009",
                "question": "In UML Statecharts, what is a 'composite state' (or superstate)?",
                "options": {
                    "A": "A state that contains substates and internal transitions.",
                    "B": "A state with no incoming edges.",
                    "C": "A final state that halts the system.",
                    "D": "A state that has no name."
                },
                "correctAnswer": "A",
                "explanation": "Composite states encapsulate nested sub-states, enabling hierarchical organization and avoiding state space explosion in complex specifications.",
                "difficulty": "medium",
                "sourcePages": [10, 11]
            },
            {
                "id": "gsp-010",
                "question": "What are 'orthogonal regions' in UML Statecharts?",
                "options": {
                    "A": "Independent concurrent state machines running simultaneously within a composite state.",
                    "B": "States that can never be reached.",
                    "C": "Regions with 90-degree transition angles.",
                    "D": "Transitions that have no actions."
                },
                "correctAnswer": "A",
                "explanation": "Orthogonal regions model concurrent sub-behaviors where the system exists in multiple sub-states at the same time (e.g., UI state and Background Network Sync state).",
                "difficulty": "medium",
                "sourcePages": [11, 12]
            },
            {
                "id": "gsp-011",
                "question": "What is the 'state explosion problem' when testing FSMs with multiple concurrent components?",
                "options": {
                    "A": "The number of global states is the Cartesian product of individual component states, growing exponentially.",
                    "B": "The graph runs out of nodes.",
                    "C": "Memory on the server catches fire.",
                    "D": "The compiler refuses to draw more than 5 circles."
                },
                "correctAnswer": "A",
                "explanation": "Combining concurrent components results in a global state space whose size is the product of component state spaces (S1 × S2 × ... × Sn), leading to exponential growth.",
                "difficulty": "medium",
                "sourcePages": [12]
            },
            {
                "id": "gsp-012",
                "question": "How does Complete Path Coverage (CPC) apply to an FSM with cycles?",
                "options": {
                    "A": "Like CFGs, CPC is infinite if the FSM has cycles, making it impractical.",
                    "B": "CPC is always 1 test case on FSMs.",
                    "C": "Cycles are banned in FSMs.",
                    "D": "CPC only tests initial states."
                },
                "correctAnswer": "A",
                "explanation": "FSMs with feedback transitions or repetitive loops admit infinitely many transition sequences, rendering complete path coverage infeasible.",
                "difficulty": "easy",
                "sourcePages": [7]
            },
            {
                "id": "gsp-013",
                "question": "What is a 'history state' in a statechart?",
                "options": {
                    "A": "A pseudostate that restores the most recently active substate of a composite state when re-entered.",
                    "B": "A log of all previous test runs.",
                    "C": "The initial state of the program.",
                    "D": "A deleted state."
                },
                "correctAnswer": "A",
                "explanation": "The history state (H or H*) allows a composite state to resume execution at the specific nested substate it occupied immediately prior to being interrupted.",
                "difficulty": "hard",
                "sourcePages": [13]
            },
            {
                "id": "gsp-014",
                "question": "How are test cases constructed from a test path through an FSM?",
                "options": {
                    "A": "By applying the sequence of input events that trigger the transitions and verifying that the expected output actions and target states occur.",
                    "B": "By randomly generating bytes.",
                    "C": "By inspecting variable names in the debugger.",
                    "D": "By deleting all intermediate states."
                },
                "correctAnswer": "A",
                "explanation": "A test path through an FSM maps to an input sequence of events. The test oracle checks that each event produces expected actions and transitions to the correct state.",
                "difficulty": "easy",
                "sourcePages": [14]
            },
            {
                "id": "gsp-015",
                "question": "What is an 'or-state' versus an 'and-state' in hierarchical state machines?",
                "options": {
                    "A": "An or-state means the system is in exactly one substate; an and-state represents concurrent orthogonal regions where the system is in all substates simultaneously.",
                    "B": "Or-states are used only for error handling.",
                    "C": "And-states cannot have transitions.",
                    "D": "They are synonymous in statechart theory."
                },
                "correctAnswer": "A",
                "explanation": "An OR-state is mutually exclusive (active in one substate at a time). An AND-state decomposes into parallel orthogonal regions that are all active simultaneously.",
                "difficulty": "medium",
                "sourcePages": [11]
            },
            {
                "id": "gsp-016",
                "question": "What is a 'deadlock state' in an FSM model?",
                "options": {
                    "A": "A non-final state from which no outgoing transitions can ever be taken.",
                    "B": "A state that executes forever.",
                    "C": "The start state.",
                    "D": "A state with 10 outgoing edges."
                },
                "correctAnswer": "A",
                "explanation": "A deadlock state is an unintended sink node where the system becomes permanently stuck because no valid transition exists to exit the state.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "gsp-017",
                "question": "What is an 'unreachable state' in specification graphs?",
                "options": {
                    "A": "A state that cannot be reached by any sequence of transitions starting from the initial state.",
                    "B": "A state with no incoming edges.",
                    "C": "A state that is reachable from every node.",
                    "D": "A state representing power off."
                },
                "correctAnswer": "A",
                "explanation": "An unreachable state cannot be reached from the initial state under any valid sequence of transitions, indicating a specification error or orphaned design.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "gsp-018",
                "question": "Why is specification-based testing considered a black-box technique?",
                "options": {
                    "A": "Because test requirements are derived entirely from behavioral specifications and models, without relying on internal source code structure.",
                    "B": "Because it runs in the dark.",
                    "C": "Because the source code is encrypted.",
                    "D": "Because it only tests database tables."
                },
                "correctAnswer": "A",
                "explanation": "Black-box testing derives tests from external requirements, user stories, or behavioral models (like FSMs) without inspecting internal implementation source code.",
                "difficulty": "easy",
                "sourcePages": [2]
            },
            {
                "id": "gsp-019",
                "question": "In a state machine for an ATM, if the user enters 3 incorrect PINs, the system transitions from 'CardInserted' to 'CardConfiscated'. What is this transition testing?",
                "options": {
                    "A": "An exceptional/security error handling transition.",
                    "B": "A normal withdrawal path.",
                    "C": "An infeasible path.",
                    "D": "A sneak path."
                },
                "correctAnswer": "A",
                "explanation": "This transition explicitly tests the security countermeasure and error-recovery behavior specified for unauthorized access attempts.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "gsp-020",
                "question": "What is the primary advantage of generating tests from formal specifications before implementation begins?",
                "options": {
                    "A": "Tests can reveal specification ambiguities, omissions, and contradictions before code is even written, preventing costly defect propagation.",
                    "B": "It eliminates the need to compile the code.",
                    "C": "It guarantees 100% bug-free software.",
                    "D": "It replaces developers with compilers."
                },
                "correctAnswer": "A",
                "explanation": "Deriving tests from models early exposes gaps and inconsistencies in requirements, preventing defects from being baked into the implementation.",
                "difficulty": "medium",
                "sourcePages": [16]
            }
        ]
    },
    {
        "topicId": "logic-coverage-criteria",
        "topicName": "Logic Coverage Criteria (ACC, GACC, CACC, RACC)",
        "sourcePdf": "logic-coverage-criteria.pdf",
        "questions": [
            {
                "id": "lcc-001",
                "question": "In logic coverage criteria, what is the formal definition of a 'predicate'?",
                "options": {
                    "A": "An expression that evaluates to a Boolean value (true or false).",
                    "B": "A function that returns an integer.",
                    "C": "A loop counter variable.",
                    "D": "A string concatenation operator."
                },
                "correctAnswer": "A",
                "explanation": "A predicate is an expression that evaluates to a Boolean value. It may contain Boolean variables, relational operators (<, >, ==), and logical connectives (AND, OR, NOT).",
                "difficulty": "easy",
                "sourcePages": [2]
            },
            {
                "id": "lcc-002",
                "question": "What is a 'clause' in a Boolean predicate?",
                "options": {
                    "A": "A sub-expression that does not contain any logical operators (AND, OR, NOT).",
                    "B": "Any expression that contains an if-statement.",
                    "C": "A complete Java class.",
                    "D": "A loop condition."
                },
                "correctAnswer": "A",
                "explanation": "A clause is an atomic Boolean expression that contains no logical operators. E.g., in ((x > 0) || y), '(x > 0)' and 'y' are individual clauses.",
                "difficulty": "easy",
                "sourcePages": [2]
            },
            {
                "id": "lcc-003",
                "question": "What does Predicate Coverage (PC) require?",
                "options": {
                    "A": "For each predicate p, TR contains two requirements: p evaluates to true, and p evaluates to false.",
                    "B": "Every clause in the predicate must be true.",
                    "C": "Every clause must be evaluated 2^N times.",
                    "D": "Predicates must only contain AND operators."
                },
                "correctAnswer": "A",
                "explanation": "Predicate Coverage (PC) requires test cases that make the entire predicate evaluate to true at least once, and to false at least once.",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "lcc-004",
                "question": "What does Clause Coverage (CC) require?",
                "options": {
                    "A": "For each individual clause c in predicate p, TR contains two requirements: c evaluates to true, and c evaluates to false.",
                    "B": "The whole predicate must evaluate to true.",
                    "C": "Only the first clause in the predicate is tested.",
                    "D": "All clauses must be true at the same time."
                },
                "correctAnswer": "A",
                "explanation": "Clause Coverage (CC) requires that each individual clause in the predicate evaluates to true at least once and false at least once.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "lcc-005",
                "question": "Does Clause Coverage (CC) subsume Predicate Coverage (PC)?",
                "options": {
                    "A": "No! CC does not subsume PC, and PC does not subsume CC.",
                    "B": "Yes, CC always subsumes PC.",
                    "C": "Yes, PC always subsumes CC.",
                    "D": "Only when the predicate has 1 clause."
                },
                "correctAnswer": "A",
                "explanation": "Surprisingly, CC does not subsume PC! E.g. in p = a OR b, tests {(a=T, b=F), (a=F, b=T)} satisfy CC, but p evaluates to true in both tests! Thus PC is not satisfied.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "lcc-006",
                "question": "How many test cases are required to satisfy Combinatorial Coverage (CoC) for a predicate with N independent clauses?",
                "options": {
                    "A": "2^N",
                    "B": "2 × N",
                    "C": "N + 1",
                    "D": "N!"
                },
                "correctAnswer": "A",
                "explanation": "Combinatorial Coverage (CoC) requires testing every possible combination of truth assignments to the N clauses, which equals 2^N tests.",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "lcc-007",
                "question": "When is a clause c said to 'determine' predicate p?",
                "options": {
                    "A": "When toggling the truth value of c changes the truth value of p (with all minor clauses held fixed).",
                    "B": "When c is the longest clause.",
                    "C": "When c evaluates to true.",
                    "D": "When c is an arithmetic expression."
                },
                "correctAnswer": "A",
                "explanation": "Clause c determines p if and only if: changing the truth value of c while keeping the values of all other clauses fixed causes the evaluation of p to invert.",
                "difficulty": "medium",
                "sourcePages": [10, 11]
            },
            {
                "id": "lcc-008",
                "question": "In Active Clause Coverage (ACC), what are 'major clauses' and 'minor clauses'?",
                "options": {
                    "A": "For each requirement, one clause is chosen as the 'major clause' (the clause being tested for determination), while the remaining clauses are 'minor clauses'.",
                    "B": "Major clauses are in main(); minor clauses are in subroutines.",
                    "C": "Major clauses contain relational operators; minor clauses contain variables.",
                    "D": "Major clauses evaluate to true; minor clauses evaluate to false."
                },
                "correctAnswer": "A",
                "explanation": "When testing a specific clause c under ACC, c is designated as the major clause. All other clauses in that predicate are minor clauses.",
                "difficulty": "easy",
                "sourcePages": [12]
            },
            {
                "id": "lcc-009",
                "question": "What is General Active Clause Coverage (GACC)?",
                "options": {
                    "A": "For each major clause c, choose minor clauses such that c determines p. The minor clauses do NOT have to take the same truth values when c is true as when c is false.",
                    "B": "Minor clauses must be identical in both tests.",
                    "C": "All clauses must be active simultaneously.",
                    "D": "Predicate must evaluate to false in both tests."
                },
                "correctAnswer": "A",
                "explanation": "In GACC, clause c must determine p when c=T and when c=F, but the values assigned to minor clauses in the c=T test are allowed to differ from the c=F test.",
                "difficulty": "hard",
                "sourcePages": [14, 15]
            },
            {
                "id": "lcc-010",
                "question": "What is the defining condition of Restricted Active Clause Coverage (RACC)?",
                "options": {
                    "A": "The values assigned to the minor clauses MUST be strictly identical in the test where c is true and in the test where c is false.",
                    "B": "The predicate must contain at most 2 clauses.",
                    "C": "The predicate cannot contain the NOT operator.",
                    "D": "The test suite must be restricted to 1 test case."
                },
                "correctAnswer": "A",
                "explanation": "RACC restricts minor clauses to remain exactly identical in both the c=true and c=false tests for major clause c.",
                "difficulty": "medium",
                "sourcePages": [16, 17]
            },
            {
                "id": "lcc-011",
                "question": "What is Correlated Active Clause Coverage (CACC)?",
                "options": {
                    "A": "For each major clause c, minor clauses are chosen such that p evaluates to true when c is true (or false), and p evaluates to false when c is false (or true), but minor clauses may differ between the two tests.",
                    "B": "All clauses must be mathematically correlated.",
                    "C": "CACC is identical to Predicate Coverage.",
                    "D": "CACC requires 2^N tests."
                },
                "correctAnswer": "A",
                "explanation": "CACC requires that toggling major clause c in the test pair causes predicate p to toggle as well, while allowing minor clauses to differ between the two tests.",
                "difficulty": "hard",
                "sourcePages": [18, 19]
            },
            {
                "id": "lcc-012",
                "question": "Which of the following correctly orders the Active Clause Coverage criteria by strength?",
                "options": {
                    "A": "RACC subsumes CACC, CACC subsumes GACC.",
                    "B": "GACC subsumes CACC, CACC subsumes RACC.",
                    "C": "CACC subsumes RACC, RACC subsumes GACC.",
                    "D": "GACC subsumes PC, but RACC does not."
                },
                "correctAnswer": "A",
                "explanation": "RACC imposes the strictest requirement (identical minor clauses). Any test pair satisfying RACC satisfies CACC. CACC guarantees the predicate toggles, satisfying GACC.",
                "difficulty": "medium",
                "sourcePages": [20, 21]
            },
            {
                "id": "lcc-013",
                "question": "Does GACC guarantee Predicate Coverage (PC)?",
                "options": {
                    "A": "No! In GACC, it is possible for p to evaluate to true (or false) in both the c=T and c=F tests if minor clauses change between tests.",
                    "B": "Yes, GACC always guarantees PC.",
                    "C": "Only if N = 2.",
                    "D": "Only when the predicate has no AND operators."
                },
                "correctAnswer": "A",
                "explanation": "Under GACC, minor clauses may differ between the two tests, which can result in the predicate evaluating to True in both tests. Thus GACC does NOT subsume PC!",
                "difficulty": "hard",
                "sourcePages": [21, 22]
            },
            {
                "id": "lcc-014",
                "question": "Do CACC and RACC guarantee Predicate Coverage (PC)?",
                "options": {
                    "A": "Yes, both CACC and RACC guarantee that p evaluates to True in one test and False in the other.",
                    "B": "No, neither does.",
                    "C": "Only RACC does.",
                    "D": "Only CACC does."
                },
                "correctAnswer": "A",
                "explanation": "Both CACC and RACC explicitly require that the predicate evaluates to opposite truth values in the test pair, directly satisfying Predicate Coverage.",
                "difficulty": "medium",
                "sourcePages": [20]
            },
            {
                "id": "lcc-015",
                "question": "For predicate p = A ∧ B, what truth assignment to minor clause B makes major clause A determine p?",
                "options": {
                    "A": "B must be TRUE.",
                    "B": "B must be FALSE.",
                    "C": "B can be either TRUE or FALSE.",
                    "D": "B must be null."
                },
                "correctAnswer": "A",
                "explanation": "If B is FALSE, p = A ∧ F = F regardless of A (A has no effect). If B is TRUE, p = A ∧ T = A. Thus, A determines p if and only if B is TRUE.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "lcc-016",
                "question": "For predicate p = A ∨ B, what truth assignment to minor clause B makes major clause A determine p?",
                "options": {
                    "A": "B must be FALSE.",
                    "B": "B must be TRUE.",
                    "C": "B can be either TRUE or FALSE.",
                    "D": "B must be undefined."
                },
                "correctAnswer": "A",
                "explanation": "If B is TRUE, p = A ∨ T = T regardless of A. If B is FALSE, p = A ∨ F = A. Thus, A determines p if and only if B is FALSE.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "lcc-017",
                "question": "What is Inactive Clause Coverage (ICC)?",
                "options": {
                    "A": "Tests where minor clauses are chosen such that major clause c does NOT determine the predicate p.",
                    "B": "Tests where no code is executed.",
                    "C": "Testing dead code.",
                    "D": "Testing inactive user sessions."
                },
                "correctAnswer": "A",
                "explanation": "Inactive Clause Coverage tests situations where the major clause is prevented from determining the predicate by the configuration of minor clauses.",
                "difficulty": "medium",
                "sourcePages": [24, 25]
            },
            {
                "id": "lcc-018",
                "question": "Why is Combinatorial Coverage (CoC) impractical for predicates with many clauses (e.g. N = 10)?",
                "options": {
                    "A": "Because 2^10 = 1024 tests are required for a single decision predicate, leading to combinatorial explosion.",
                    "B": "Because compilers limit predicates to 5 clauses.",
                    "C": "Because CoC does not test all clauses.",
                    "D": "Because CoC cannot be used with boolean variables."
                },
                "correctAnswer": "A",
                "explanation": "2^N grows exponentially. For N=10, 1024 test cases are needed for just one condition. Active Clause Coverage criteria provide rigorous testing with approximately 2N tests.",
                "difficulty": "easy",
                "sourcePages": [8, 9]
            },
            {
                "id": "lcc-019",
                "question": "What is the Minimum Number of tests required for RACC on a predicate with N independent clauses?",
                "options": {
                    "A": "N + 1 tests (by sharing tests among different major clauses).",
                    "B": "2^N tests.",
                    "C": "1 test.",
                    "D": "N! tests."
                },
                "correctAnswer": "A",
                "explanation": "Each major clause requires 2 tests (one T, one F). By carefully sharing test cases between different major clauses, RACC can often be satisfied with as few as N + 1 tests.",
                "difficulty": "hard",
                "sourcePages": [26]
            },
            {
                "id": "lcc-020",
                "question": "Which of the following Federal Aviation Administration (FAA) software safety standards requires Modified Condition/Decision Coverage (MC/DC), which is closely related to RACC/CACC?",
                "options": {
                    "A": "DO-178B / DO-178C (Level A avionics software)",
                    "B": "ISO 9001",
                    "C": "IEEE 802.11",
                    "D": "PCI-DSS"
                },
                "correctAnswer": "A",
                "explanation": "DO-178B/C Level A avionics safety mandates MC/DC (which corresponds directly to Correlated / Restricted Active Clause Coverage) for flight-critical code.",
                "difficulty": "medium",
                "sourcePages": [27]
            }
        ]
    },
    {
        "topicId": "logic-coverage-algorithms",
        "topicName": "Logic Coverage Algorithms",
        "sourcePdf": "logic-coverage-algorithms.pdf",
        "questions": [
            {
                "id": "lca-001",
                "question": "What is the Boolean derivative (Boolean difference) of predicate p with respect to clause c, denoted pc?",
                "options": {
                    "A": "pc = p(c=true) ⊕ p(c=false)",
                    "B": "pc = p(c=true) ∧ p(c=false)",
                    "C": "pc = p(c=true) ∨ p(c=false)",
                    "D": "pc = ¬p(c=true)"
                },
                "correctAnswer": "A",
                "explanation": "The Boolean difference pc is formally defined as p(c=true) XOR p(c=false). It evaluates to true if and only if changing c changes the value of p.",
                "difficulty": "medium",
                "sourcePages": [2, 3]
            },
            {
                "id": "lca-002",
                "question": "What does pc = true indicate regarding clause c and predicate p?",
                "options": {
                    "A": "Clause c determines predicate p under those minor clause truth assignments.",
                    "B": "Clause c has no effect on predicate p.",
                    "C": "Predicate p is a contradiction.",
                    "D": "Clause c is false."
                },
                "correctAnswer": "A",
                "explanation": "When pc evaluates to true, the truth value of p depends directly on c; toggling c will toggle p. Hence c determines p.",
                "difficulty": "easy",
                "sourcePages": [3, 4]
            },
            {
                "id": "lca-003",
                "question": "For predicate p = a ∧ (b ∨ c), what is the condition for clause 'a' to determine p, computed via pa?",
                "options": {
                    "A": "b ∨ c must be TRUE.",
                    "B": "b ∧ c must be TRUE.",
                    "C": "b must be FALSE.",
                    "D": "c must be FALSE."
                },
                "correctAnswer": "A",
                "explanation": "pa = p(a=T) ⊕ p(a=F) = (T ∧ (b ∨ c)) ⊕ (F ∧ (b ∨ c)) = (b ∨ c) ⊕ F = b ∨ c. Thus, 'a' determines p whenever (b ∨ c) is TRUE.",
                "difficulty": "medium",
                "sourcePages": [5, 6]
            },
            {
                "id": "lca-004",
                "question": "For predicate p = a ∨ (b ∧ c), what is the condition for clause 'a' to determine p?",
                "options": {
                    "A": "¬(b ∧ c) must be TRUE (i.e. at least one of b or c is FALSE).",
                    "B": "b ∧ c must be TRUE.",
                    "C": "b must be TRUE and c must be TRUE.",
                    "D": "b and c must both be TRUE."
                },
                "correctAnswer": "A",
                "explanation": "pa = p(a=T) ⊕ p(a=F) = (T ∨ (b ∧ c)) ⊕ (F ∨ (b ∧ c)) = T ⊕ (b ∧ c) = ¬(b ∧ c). Thus 'a' determines p when b ∧ c is FALSE.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "lca-005",
                "question": "What algebraic identity applies when simplifying XOR expressions with FALSE: X ⊕ FALSE?",
                "options": {
                    "A": "X",
                    "B": "FALSE",
                    "C": "TRUE",
                    "D": "¬X"
                },
                "correctAnswer": "A",
                "explanation": "In Boolean algebra, XOR with false is the identity operation: X ⊕ 0 = X.",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "lca-006",
                "question": "What algebraic identity applies when simplifying XOR expressions with TRUE: X ⊕ TRUE?",
                "options": {
                    "A": "¬X",
                    "B": "X",
                    "C": "TRUE",
                    "D": "FALSE"
                },
                "correctAnswer": "A",
                "explanation": "XOR with true inverts the value: X ⊕ 1 = ¬X (NOT X).",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "lca-007",
                "question": "For predicate p = a ⊕ b, what is pa (the condition under which clause 'a' determines p)?",
                "options": {
                    "A": "TRUE (clause 'a' ALWAYS determines p, regardless of b!)",
                    "B": "b must be TRUE.",
                    "C": "b must be FALSE.",
                    "D": "FALSE"
                },
                "correctAnswer": "A",
                "explanation": "pa = (T ⊕ b) ⊕ (F ⊕ b) = ¬b ⊕ b = TRUE. In an XOR predicate, any clause always determines the predicate regardless of the other clause's value!",
                "difficulty": "hard",
                "sourcePages": [8]
            },
            {
                "id": "lca-008",
                "question": "If pc simplifies to FALSE for some clause c, what does this imply about clause c in predicate p?",
                "options": {
                    "A": "Clause c is redundant (irrelevant) and can never determine predicate p under any condition.",
                    "B": "Clause c is the most important clause.",
                    "C": "Predicate p is always true.",
                    "D": "Clause c must be tested 100 times."
                },
                "correctAnswer": "A",
                "explanation": "If pc = FALSE, no truth assignment to minor clauses can ever allow c to toggle p. Clause c is logically dead/redundant in that predicate.",
                "difficulty": "medium",
                "sourcePages": [9]
            },
            {
                "id": "lca-009",
                "question": "How can Karnaugh maps (K-maps) or truth tables assist in finding ACC test cases?",
                "options": {
                    "A": "By finding adjacent cells in the map differing in only clause c where the output cell values differ (one 1, one 0).",
                    "B": "By eliminating all prime implicants.",
                    "C": "By converting Boolean logic into assembly code.",
                    "D": "By proving the code has no memory leaks."
                },
                "correctAnswer": "A",
                "explanation": "In a K-map, adjacent cells differ by exactly one variable (clause). If two adjacent cells along variable c have opposite outputs (one 1, one 0), they form an exact RACC test pair for c.",
                "difficulty": "medium",
                "sourcePages": [10, 11]
            },
            {
                "id": "lca-010",
                "question": "What is an 'infeasible test requirement' in logic coverage?",
                "options": {
                    "A": "A clause assignment that violates semantic constraints (e.g. requiring x > 5 to be true AND x < 2 to be true simultaneously).",
                    "B": "A test that takes more than 1 millisecond.",
                    "C": "A test written in Python.",
                    "D": "A test requirement with no ID."
                },
                "correctAnswer": "A",
                "explanation": "Clauses are not always independent; relational expressions sharing variables may be contradictory (e.g., x < 0 and x > 10 cannot both be true), making certain rows of the truth table infeasible.",
                "difficulty": "easy",
                "sourcePages": [12, 13]
            },
            {
                "id": "lca-011",
                "question": "If a clause assignment is infeasible, what is the proper action in RACC/CACC testing?",
                "options": {
                    "A": "Recognize the constraint, declare the requirement infeasible, and select an alternate feasible test pair (or document the infeasibility).",
                    "B": "Force memory to corrupt.",
                    "C": "Delete the entire method.",
                    "D": "Ignore all testing criteria."
                },
                "correctAnswer": "A",
                "explanation": "Infeasible test requirements cannot be satisfied by any real execution input; they must be identified, documented, and excluded from achievable coverage goals.",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "lca-012",
                "question": "For predicate p = (a ∧ b) ∨ (a ∧ c), what is pa?",
                "options": {
                    "A": "b ∨ c",
                    "B": "b ∧ c",
                    "C": "¬b ∧ ¬c",
                    "D": "TRUE"
                },
                "correctAnswer": "A",
                "explanation": "Factoring gives p = a ∧ (b ∨ c). When a=T, p = b ∨ c. When a=F, p = F. pa = (b ∨ c) ⊕ F = b ∨ c.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "lca-013",
                "question": "When can RACC be impossible to satisfy while CACC is satisfiable?",
                "options": {
                    "A": "When clause dependencies or multiple occurrences of a clause prevent minor clauses from remaining identical while toggling p.",
                    "B": "Never; RACC and CACC are identical.",
                    "C": "Only when N = 1.",
                    "D": "Only when predicates contain no variables."
                },
                "correctAnswer": "A",
                "explanation": "If a clause appears multiple times in different parts of an expression or has relational dependencies, fixing minor clauses identically might be impossible, while allowing correlated variations (CACC) succeeds.",
                "difficulty": "hard",
                "sourcePages": [14, 15]
            },
            {
                "id": "lca-014",
                "question": "In the predicate p = a ∧ b, which pair of (a, b) inputs satisfies RACC for major clause a?",
                "options": {
                    "A": "(T, T) and (F, T)",
                    "B": "(T, F) and (F, F)",
                    "C": "(T, T) and (T, F)",
                    "D": "(F, T) and (F, F)"
                },
                "correctAnswer": "A",
                "explanation": "For major clause a, minor clause b must be fixed to T. The test pair is (a=T, b=T) [p=T] and (a=F, b=T) [p=F].",
                "difficulty": "easy",
                "sourcePages": [11]
            },
            {
                "id": "lca-015",
                "question": "In the predicate p = a ∨ b, which pair of (a, b) inputs satisfies RACC for major clause a?",
                "options": {
                    "A": "(T, F) and (F, F)",
                    "B": "(T, T) and (F, T)",
                    "C": "(T, T) and (T, F)",
                    "D": "(F, T) and (F, F)"
                },
                "correctAnswer": "A",
                "explanation": "For major clause a, minor clause b must be fixed to F. The test pair is (a=T, b=F) [p=T] and (a=F, b=F) [p=F].",
                "difficulty": "easy",
                "sourcePages": [11]
            },
            {
                "id": "lca-016",
                "question": "Can the test (T, T) for p = a ∧ b be reused as the 'c is true' test when testing major clause b under RACC?",
                "options": {
                    "A": "Yes! For b=T with a=T, the test is (T, T). This enables sharing test cases across clauses to minimize test suite size.",
                    "B": "No, tests cannot be shared.",
                    "C": "Only if b is defined as a global variable.",
                    "D": "Only if a == b."
                },
                "correctAnswer": "A",
                "explanation": "For clause a, tests are (T, T) and (F, T). For clause b, tests are (T, T) and (T, F). The test (T, T) is shared, giving a total of only 3 tests: {(T, T), (F, T), (T, F)} for N+1 = 3 tests.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "lca-017",
                "question": "What is the boolean difference for p = ¬a with respect to clause a?",
                "options": {
                    "A": "pa = ¬T ⊕ ¬F = F ⊕ T = TRUE",
                    "B": "pa = FALSE",
                    "C": "pa = a",
                    "D": "pa = ¬a"
                },
                "correctAnswer": "A",
                "explanation": "Inverting a single clause always determines its negation: changing a from T to F changes ¬a from F to T. The derivative is identically TRUE.",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "lca-018",
                "question": "What algorithmic representation allows efficient computation of boolean derivatives for large predicates?",
                "options": {
                    "A": "Binary Decision Diagrams (BDDs)",
                    "B": "Linked lists of strings",
                    "C": "Floating-point arrays",
                    "D": "Stack traces"
                },
                "correctAnswer": "A",
                "explanation": "Reduced Ordered Binary Decision Diagrams (ROBDDs) provide canonical representations of Boolean functions, enabling fast Boolean difference and satisfiability checks.",
                "difficulty": "hard",
                "sourcePages": [17]
            },
            {
                "id": "lca-019",
                "question": "Suppose p = a ↔ b (equivalence / XNOR). What is pa?",
                "options": {
                    "A": "TRUE (toggling a always changes whether a equals b)",
                    "B": "FALSE",
                    "C": "b",
                    "D": "¬b"
                },
                "correctAnswer": "A",
                "explanation": "a ↔ b is the negation of XOR (a XNOR b). Like XOR, toggling either operand unconditionally flips the equivalence, so pa = TRUE.",
                "difficulty": "hard",
                "sourcePages": [8]
            },
            {
                "id": "lca-020",
                "question": "What is the primary practical goal of logic coverage algorithms in safety-critical software engineering?",
                "options": {
                    "A": "To systematically prove that each decision condition independently controls program branching without requiring exhaustive 2^N testing.",
                    "B": "To eliminate the need for functional specifications.",
                    "C": "To automatically translate code into assembly.",
                    "D": "To verify processor clock frequency."
                },
                "correctAnswer": "A",
                "explanation": "Logic coverage algorithms (like RACC/MC-DC) mathematically ensure that every single decision clause is tested to show it can independently affect execution, achieving near-exhaustive confidence with linear test effort.",
                "difficulty": "medium",
                "sourcePages": [18]
            }
        ]
    }
]
