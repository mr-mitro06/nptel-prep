# Topic 1 to 5 Question Bank

DATA = [
    {
        "topicId": "isp-full-slides",
        "topicName": "Input Space Partitioning (ISP)",
        "sourcePdf": "ISP-full-slides.pdf",
        "questions": [
            {
                "id": "isp-001",
                "question": "In Input Space Partitioning (ISP), which two fundamental properties must every valid partition of an input domain satisfy?",
                "options": {
                    "A": "Minimality and Determinism",
                    "B": "Pairwise disjointness and Completeness",
                    "C": "Subsumption and Linear independence",
                    "D": "Commutativity and Associativity"
                },
                "correctAnswer": "B",
                "explanation": "A partition of set S is defined as a set of subsets {S1, S2, ..., Sn} such that the subsets are mutually pairwise disjoint (Si ∩ Sj = ∅ for i ≠ j) and together cover the entire domain completely (∪ Si = S).",
                "difficulty": "easy",
                "sourcePages": [2, 5]
            },
            {
                "id": "isp-002",
                "question": "What is the primary difference between the Interface-based approach and the Functionality-based approach to Input Domain Modeling (IDM)?",
                "options": {
                    "A": "Interface-based models semantic relationships, while Functionality-based models syntax only.",
                    "B": "Interface-based considers each parameter in isolation based on types, while Functionality-based considers behavioral requirements and interactions.",
                    "C": "Interface-based produces fewer test cases than Functionality-based under all criteria.",
                    "D": "Interface-based requires access to the source code, whereas Functionality-based is strictly black-box."
                },
                "correctAnswer": "B",
                "explanation": "The interface-based approach analyzes parameters in isolation directly from the interface syntax/types (simple and mechanical). The functionality-based approach incorporates domain knowledge, functional relationships between parameters, and requirements.",
                "difficulty": "medium",
                "sourcePages": [8, 9]
            },
            {
                "id": "isp-003",
                "question": "Given 3 input characteristics with 3, 4, and 2 partition blocks respectively, how many test requirements are generated under All Combinations Coverage (ACoC)?",
                "options": {
                    "A": "9",
                    "B": "24",
                    "C": "7",
                    "D": "12"
                },
                "correctAnswer": "B",
                "explanation": "All Combinations Coverage (ACoC) requires testing the Cartesian product of all partition blocks across all characteristics: 3 × 4 × 2 = 24 test combinations.",
                "difficulty": "easy",
                "sourcePages": [18]
            },
            {
                "id": "isp-004",
                "question": "For input characteristics with block sizes |B1| = 3, |B2| = 4, and |B3| = 2, what is the minimum number of tests needed to satisfy Each Choice Coverage (ECC)?",
                "options": {
                    "A": "4",
                    "B": "9",
                    "C": "24",
                    "D": "1"
                },
                "correctAnswer": "A",
                "explanation": "Each Choice Coverage (ECC) requires that every block from each characteristic is used at least once in some test case. The minimum number of tests required is max(|Bi|) = max(3, 4, 2) = 4.",
                "difficulty": "medium",
                "sourcePages": [19]
            },
            {
                "id": "isp-005",
                "question": "Under Base Choice Coverage (BCC), how many test cases are generated for characteristics with block sizes 4, 3, and 5?",
                "options": {
                    "A": "60",
                    "B": "10",
                    "C": "9",
                    "D": "12"
                },
                "correctAnswer": "B",
                "explanation": "The formula for Base Choice Coverage is: 1 + ∑ (|Bi| - 1). Here, 1 + (4 - 1) + (3 - 1) + (5 - 1) = 1 + 3 + 2 + 4 = 10 test cases.",
                "difficulty": "medium",
                "sourcePages": [24, 25]
            },
            {
                "id": "isp-006",
                "question": "Why is Base Choice Coverage (BCC) generally preferred over All Combinations Coverage (ACoC) in practical industrial testing?",
                "options": {
                    "A": "BCC subsumes All Combinations Coverage.",
                    "B": "BCC provides a linear growth in test cases while testing each non-base choice in isolation against nominal base values.",
                    "C": "BCC guarantees 100% path coverage of the source code.",
                    "D": "BCC eliminates the need to identify partition blocks."
                },
                "correctAnswer": "B",
                "explanation": "BCC scales linearly (1 + ∑(|Bi|-1)) instead of exponentially (∏|Bi|), and isolates the effect of each non-base (often exceptional or boundary) choice against a stable baseline of base choices.",
                "difficulty": "medium",
                "sourcePages": [23, 24]
            },
            {
                "id": "isp-007",
                "question": "What is the defining requirement of Pairwise Coverage (PWC)?",
                "options": {
                    "A": "A value from each block for each characteristic must be combined with a value from every other block for each other characteristic.",
                    "B": "Every input variable must be tested with exactly two values.",
                    "C": "Only pairs of variables that have direct data dependencies are tested.",
                    "D": "Every test case must execute at least two branches."
                },
                "correctAnswer": "A",
                "explanation": "Pairwise Coverage (also known as 2-wise coverage) mandates that for every pair of distinct characteristics, all possible combinations of blocks from those two characteristics must be covered by at least one test case.",
                "difficulty": "easy",
                "sourcePages": [20, 21]
            },
            {
                "id": "isp-008",
                "question": "What is the key difference between Base Choice Coverage (BCC) and Multiple Base Choice Coverage (MBCC)?",
                "options": {
                    "A": "MBCC chooses multiple base choices per characteristic, creating tests by varying each base choice individually.",
                    "B": "MBCC allows empty blocks in partitions.",
                    "C": "MBCC is identical to Pairwise Coverage.",
                    "D": "MBCC only applies to continuous floating-point variables."
                },
                "correctAnswer": "A",
                "explanation": "In MBCC, more than one base choice is designated for one or more characteristics. For each base choice, tests are constructed by varying non-base choices while holding remaining characteristics at their base values.",
                "difficulty": "medium",
                "sourcePages": [26, 27]
            },
            {
                "id": "isp-009",
                "question": "Which of the following is an example of an interface-based partition for an integer argument 'length' of an array?",
                "options": {
                    "A": "Array is sorted vs Array is unsorted",
                    "B": "length < 0, length = 0, length > 0",
                    "C": "Array contains duplicate elements vs Array contains unique elements",
                    "D": "Operation succeeds vs Operation throws TimeoutException"
                },
                "correctAnswer": "B",
                "explanation": "Checking 'length < 0', 'length = 0', 'length > 0' relies only on the type and value of the parameter 'length' in isolation (interface-based). The other options require knowing semantic relationships and functionality.",
                "difficulty": "easy",
                "sourcePages": [8, 12]
            },
            {
                "id": "isp-010",
                "question": "In Input Domain Modeling, what problem occurs if partition blocks are NOT disjoint?",
                "options": {
                    "A": "Some valid input values will have no test case assigned to them.",
                    "B": "An input value belongs to multiple blocks, leading to ambiguity and overlapping test goals.",
                    "C": "The input domain becomes infinite.",
                    "D": "All Combinations Coverage cannot be computed mathematically."
                },
                "correctAnswer": "B",
                "explanation": "If blocks overlap (not disjoint), a single test value belongs to multiple blocks, which causes ambiguity in test requirements and undermines systematic boundary analysis.",
                "difficulty": "medium",
                "sourcePages": [4, 5]
            },
            {
                "id": "isp-011",
                "question": "Which of the following represents the correct subsumption relationship between ISP criteria?",
                "options": {
                    "A": "Each Choice Coverage subsumes All Combinations Coverage.",
                    "B": "All Combinations Coverage subsumes Pairwise Coverage, and Pairwise Coverage subsumes Each Choice Coverage.",
                    "C": "Base Choice Coverage subsumes All Combinations Coverage.",
                    "D": "Each Choice Coverage subsumes Base Choice Coverage."
                },
                "correctAnswer": "B",
                "explanation": "ACoC covers all combinations of all characteristics; hence it subsumes TWC and PWC. PWC covers all pairs, which guarantees that every individual block is used, subsuming ECC.",
                "difficulty": "medium",
                "sourcePages": [28]
            },
            {
                "id": "isp-012",
                "question": "Suppose characteristic C1 has blocks {A, B}, C2 has {1, 2}, and C3 has {X, Y}. If Base Choice is selected as (A, 1, X), which of the following is NOT a valid BCC test case?",
                "options": {
                    "A": "(B, 1, X)",
                    "B": "(A, 2, X)",
                    "C": "(A, 1, Y)",
                    "D": "(B, 2, Y)"
                },
                "correctAnswer": "D",
                "explanation": "In BCC, tests are generated by varying one characteristic at a time from the base choice (A, 1, X). (B, 2, Y) varies all three characteristics simultaneously, which is not a single-variation BCC test.",
                "difficulty": "hard",
                "sourcePages": [24, 25]
            },
            {
                "id": "isp-013",
                "question": "What is the recommended approach in ISP when certain combinations of blocks are infeasible due to domain constraints?",
                "options": {
                    "A": "Redefine the entire software architecture.",
                    "B": "Drop the infeasible combinations from test requirements and document them.",
                    "C": "Force the program to crash using an illegal memory hook.",
                    "D": "Replace all characteristics with random noise."
                },
                "correctAnswer": "B",
                "explanation": "When domain semantics make certain block combinations impossible (e.g. Month = February and Day = 31), those combinations are marked as infeasible and excluded from test requirements.",
                "difficulty": "easy",
                "sourcePages": [29]
            },
            {
                "id": "isp-014",
                "question": "What are the four sequential steps in Input Domain Modeling (IDM)?",
                "options": {
                    "A": "Code compilation, Static analysis, Symbolic execution, Dynamic testing",
                    "B": "Identify testable functions, Find all parameters, Model the input domain, Apply a test criterion",
                    "C": "Write test cases, Run test cases, Measure coverage, Report bugs",
                    "D": "Build control flow graph, Identify def-use pairs, Compute prime paths, Select tests"
                },
                "correctAnswer": "B",
                "explanation": "The 4 steps in IDM defined by Ammann & Offutt are: (1) Identify testable functions, (2) Find all parameters, (3) Model the input domain (partitions/blocks), and (4) Apply a test criterion to choose combinations.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "isp-015",
                "question": "If a characteristic is partitioned into: b1: x < 0, b2: x = 0, b3: x > 0. This partition is:",
                "options": {
                    "A": "Disjoint but not complete over the integers.",
                    "B": "Complete but not disjoint over the integers.",
                    "C": "Both pairwise disjoint and complete over the integers.",
                    "D": "Neither disjoint nor complete over the integers."
                },
                "correctAnswer": "C",
                "explanation": "Every integer is either strictly negative, zero, or strictly positive (complete), and no integer can belong to more than one of these categories (pairwise disjoint).",
                "difficulty": "easy",
                "sourcePages": [4, 5]
            },
            {
                "id": "isp-016",
                "question": "In T-Wise Coverage (TWC), what does the parameter 't' represent?",
                "options": {
                    "A": "The number of test execution threads.",
                    "B": "The degree of interaction: all combinations of blocks from any t characteristics must be covered.",
                    "C": "The timeout limit in seconds.",
                    "D": "The number of base choice test cases."
                },
                "correctAnswer": "B",
                "explanation": "T-Wise Coverage generalizes pairwise coverage: for any subset of t characteristics, all combinations of blocks must be tested together.",
                "difficulty": "medium",
                "sourcePages": [21]
            },
            {
                "id": "isp-017",
                "question": "Why should special/boundary values (e.g., null, empty string, 0, max_int) be placed in separate partition blocks in ISP?",
                "options": {
                    "A": "To ensure they are explicitly tested rather than obscured by nominal values in the same block.",
                    "B": "Because compilers refuse to compile code without boundary partitions.",
                    "C": "To decrease the number of generated test cases.",
                    "D": "Because boundary values are always infeasible."
                },
                "correctAnswer": "A",
                "explanation": "If boundary or special values are lumped together with normal values in one large block, testing an arbitrary representative from that block might completely miss the edge-case behavior where faults frequently reside.",
                "difficulty": "medium",
                "sourcePages": [13, 14]
            },
            {
                "id": "isp-018",
                "question": "For 4 characteristics with 2 blocks each, what is the number of test cases required for All Combinations Coverage vs Each Choice Coverage?",
                "options": {
                    "A": "ACoC: 16, ECC: 2",
                    "B": "ACoC: 8, ECC: 4",
                    "C": "ACoC: 16, ECC: 8",
                    "D": "ACoC: 8, ECC: 2"
                },
                "correctAnswer": "A",
                "explanation": "ACoC = 2 × 2 × 2 × 2 = 16. ECC = max(|Bi|) = 2. With 2 tests, e.g., (b11, b21, b31, b41) and (b12, b22, b32, b42), all blocks are covered.",
                "difficulty": "medium",
                "sourcePages": [18, 19]
            },
            {
                "id": "isp-019",
                "question": "Which of the following is a disadvantage of the interface-based IDM approach compared to the functionality-based approach?",
                "options": {
                    "A": "It is difficult to automate.",
                    "B": "It may generate many redundant or infeasible tests because it ignores semantic inter-relationships between parameters.",
                    "C": "It cannot be applied when parameter types are known.",
                    "D": "It requires detailed knowledge of the implementation algorithms."
                },
                "correctAnswer": "B",
                "explanation": "Because interface-based IDM looks only at parameters individually, it often produces combinations that make no functional sense or miss critical multi-parameter constraints.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "isp-020",
                "question": "Suppose a function has 2 base choices identified for characteristic 1, and 1 base choice for characteristic 2. This strategy is an example of:",
                "options": {
                    "A": "Each Choice Coverage",
                    "B": "Multiple Base Choice Coverage (MBCC)",
                    "C": "Combinatorial Coverage",
                    "D": "Mutation Testing"
                },
                "correctAnswer": "B",
                "explanation": "When one or more characteristics have more than one base choice specified, the criterion applied is Multiple Base Choice Coverage (MBCC).",
                "difficulty": "easy",
                "sourcePages": [26]
            }
        ]
    },
    {
        "topicId": "graphs-structural-coverage",
        "topicName": "Graph Structural Coverage Criteria",
        "sourcePdf": "graphs-structural-coverage.pdf",
        "questions": [
            {
                "id": "gsc-001",
                "question": "In graph coverage testing, how is a 'test path' formally defined?",
                "options": {
                    "A": "Any arbitrary sequence of vertices in the graph.",
                    "B": "A path that starts at an initial node n0 ∈ N0 and ends at a final node nf ∈ Nf.",
                    "C": "A cycle that visits every node in the graph at least twice.",
                    "D": "A path containing only prime paths."
                },
                "correctAnswer": "B",
                "explanation": "A test path is a path that begins at an initial node (n0 ∈ N0) and terminates at a final/exit node (nf ∈ Nf). It corresponds to a complete execution trace of a test case.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gsc-002",
                "question": "What does Node Coverage (NC) require?",
                "options": {
                    "A": "Every reachable node in graph G must be visited by at least one test path.",
                    "B": "Every edge and node must be visited simultaneously.",
                    "C": "Every node must be visited in every test case.",
                    "D": "Every node must be visited an even number of times."
                },
                "correctAnswer": "A",
                "explanation": "Node Coverage requires the set of test requirements TR to contain every reachable node in the graph G. Test paths must visit each node at least once.",
                "difficulty": "easy",
                "sourcePages": [4]
            },
            {
                "id": "gsc-003",
                "question": "What is the formal definition of Edge Coverage (EC)?",
                "options": {
                    "A": "TR contains each reachable path of length up to 1, inclusive, in G.",
                    "B": "TR contains all cycles of length 2.",
                    "C": "TR contains all paths between initial nodes and final nodes.",
                    "D": "TR contains each node with in-degree greater than 1."
                },
                "correctAnswer": "A",
                "explanation": "Edge Coverage requires that TR contains each reachable path of length up to 1 inclusive in G, which corresponds to visiting every reachable edge (and isolated node).",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "gsc-004",
                "question": "Does Edge Coverage (EC) always subsume Node Coverage (NC)?",
                "options": {
                    "A": "No, Node Coverage subsumes Edge Coverage.",
                    "B": "Yes, visiting every edge (and reachable path of length up to 1) guarantees visiting every reachable node.",
                    "C": "Only in directed acyclic graphs.",
                    "D": "Only when the graph has no loops."
                },
                "correctAnswer": "B",
                "explanation": "Edge coverage subsumes node coverage because every reachable node (except isolated nodes, which have a path of length 0) is an endpoint of some reachable edge.",
                "difficulty": "easy",
                "sourcePages": [6, 17]
            },
            {
                "id": "gsc-005",
                "question": "What is a 'simple path' in a graph G?",
                "options": {
                    "A": "A path that contains no loops at all.",
                    "B": "A path from node ni to nj where no node appears more than once, except that the first and last nodes may be identical.",
                    "C": "A path containing at most two nodes.",
                    "D": "A path that executes in constant time O(1)."
                },
                "correctAnswer": "B",
                "explanation": "A path is simple if no node appears more than once, with the single exception that the first and last nodes may be the same (forming a simple cycle).",
                "difficulty": "medium",
                "sourcePages": [10, 11]
            },
            {
                "id": "gsc-006",
                "question": "What is a 'prime path'?",
                "options": {
                    "A": "A path whose length is a prime number.",
                    "B": "A simple path that does not appear as a proper subpath of any other simple path.",
                    "C": "A path containing only initial and final nodes.",
                    "D": "A path that visits every node in the graph."
                },
                "correctAnswer": "B",
                "explanation": "A prime path is a maximal simple path: a simple path that is not a proper subpath of any other simple path in the graph.",
                "difficulty": "medium",
                "sourcePages": [12]
            },
            {
                "id": "gsc-007",
                "question": "What is the key difference between touring with 'sidetrips' versus touring with 'detours'?",
                "options": {
                    "A": "A sidetrip leaves path p at node ni and returns to node ni; a detour leaves at ni and returns to a successor node ni+1.",
                    "B": "Sidetrips are allowed only in trees; detours are allowed only in DAGs.",
                    "C": "Detours return to the same node; sidetrips return to a predecessor node.",
                    "D": "There is no difference; both terms are strictly synonymous."
                },
                "correctAnswer": "A",
                "explanation": "Touring with sidetrips means departing from node ni to visit a cycle and returning to the exact same node ni. Touring with detours means departing at ni and returning to ni+1 (the next node in the subpath).",
                "difficulty": "hard",
                "sourcePages": [14, 15]
            },
            {
                "id": "gsc-008",
                "question": "Why is Complete Path Coverage (CPC) generally impossible or impractical for programs containing loops?",
                "options": {
                    "A": "Because loops can execute an unbounded number of iterations, making the number of paths infinite.",
                    "B": "Because loops cannot be represented in a Control Flow Graph.",
                    "C": "Because CPC only applies to specification graphs.",
                    "D": "Because CPC violates the definition of a test path."
                },
                "correctAnswer": "A",
                "explanation": "If a graph contains a cycle/loop, an infinite number of paths can be constructed by iterating the loop different numbers of times. Hence, CPC is impossible to satisfy with a finite test suite.",
                "difficulty": "easy",
                "sourcePages": [9]
            },
            {
                "id": "gsc-009",
                "question": "What is the requirement for Edge-Pair Coverage (EPC)?",
                "options": {
                    "A": "TR contains each reachable path of length up to 2, inclusive, in G.",
                    "B": "Every test case must execute exactly two edges.",
                    "C": "Every edge must be paired with every other edge in the graph.",
                    "D": "Edges must be visited in pairs of forwards and backwards traversals."
                },
                "correctAnswer": "A",
                "explanation": "Edge-Pair Coverage requires TR to contain every reachable path of length up to 2 (i.e. every pair of adjacent edges) in G.",
                "difficulty": "medium",
                "sourcePages": [8]
            },
            {
                "id": "gsc-010",
                "question": "Which of the following correctly displays the subsumption hierarchy among structural graph criteria?",
                "options": {
                    "A": "Node Coverage → Edge Coverage → Edge-Pair Coverage → Prime Path Coverage",
                    "B": "Complete Path Coverage → Prime Path Coverage → Edge-Pair Coverage → Edge Coverage → Node Coverage",
                    "C": "Prime Path Coverage → Complete Path Coverage → Edge Coverage",
                    "D": "Edge-Pair Coverage → Prime Path Coverage → Node Coverage"
                },
                "correctAnswer": "B",
                "explanation": "CPC subsumes PPC; PPC subsumes EPC; EPC subsumes EC; EC subsumes NC. (Where A → B denotes A subsumes B).",
                "difficulty": "medium",
                "sourcePages": [17]
            },
            {
                "id": "gsc-011",
                "question": "Consider a graph with nodes {1, 2, 3} and edges (1, 2), (2, 3), (3, 2). What is the path [2, 3, 2]?",
                "options": {
                    "A": "A prime path of length 2.",
                    "B": "A simple path that is not prime.",
                    "C": "Not a simple path because node 2 is repeated.",
                    "D": "An infeasible path in all graphs."
                },
                "correctAnswer": "A",
                "explanation": "[2, 3, 2] is a simple path because the only repeated node is the first and last (a simple cycle). It cannot be extended without repeating an internal node, so it is a prime path of length 2.",
                "difficulty": "hard",
                "sourcePages": [11, 12]
            },
            {
                "id": "gsc-012",
                "question": "Can a path of length 0 be a prime path?",
                "options": {
                    "A": "Yes, if a node has no incoming and no outgoing edges (an isolated node).",
                    "B": "No, prime paths must have length at least 1.",
                    "C": "No, length 0 paths are not paths.",
                    "D": "Yes, every single node in any graph is always a prime path."
                },
                "correctAnswer": "A",
                "explanation": "A path of length 0 is a single node [n]. If n has no edges connected to it, [n] cannot be extended to any longer simple path, making it a maximal simple path (prime path).",
                "difficulty": "hard",
                "sourcePages": [12]
            },
            {
                "id": "gsc-013",
                "question": "If test path p is [1, 2, 3, 4, 5], does p tour subpath [2, 3, 4] directly?",
                "options": {
                    "A": "Yes, [2, 3, 4] is a subpath of [1, 2, 3, 4, 5].",
                    "B": "No, because p starts at 1, not 2.",
                    "C": "No, it only tours [2, 3, 4] with sidetrips.",
                    "D": "Only if [2, 3, 4] is a prime path."
                },
                "correctAnswer": "A",
                "explanation": "A test path p tours a subpath q directly if q is a contiguous subpath of p. Here, [2, 3, 4] appears contiguously in [1, 2, 3, 4, 5].",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "gsc-014",
                "question": "Why does Prime Path Coverage (PPC) avoid the problem of infinite paths in graphs with loops?",
                "options": {
                    "A": "Because prime paths are simple paths, and by definition simple paths cannot loop indefinitely.",
                    "B": "Because PPC deletes all loops from the graph before testing.",
                    "C": "Because loops can only be traversed backwards under PPC.",
                    "D": "Because PPC limits test cases to at most 10 paths."
                },
                "correctAnswer": "A",
                "explanation": "Simple paths visit each node at most once (except possibly start and end nodes of a cycle). Therefore, on any finite graph, the length of simple paths is strictly bounded by |N| + 1, making the set of prime paths finite.",
                "difficulty": "medium",
                "sourcePages": [11, 12]
            },
            {
                "id": "gsc-015",
                "question": "What is Complete Round Trip Coverage (CRTC)?",
                "options": {
                    "A": "TR contains all round-trip paths (cycles of length >= 1) in G.",
                    "B": "TR requires touring each round-trip path of length 0.",
                    "C": "TR contains at least one round-trip path for each node.",
                    "D": "TR requires executing the program until it reboots."
                },
                "correctAnswer": "A",
                "explanation": "Complete Round Trip Coverage requires that TR contains all round-trip paths (paths of length 1 or more that start and end at the same node) in G.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "gsc-016",
                "question": "What is Simple Round Trip Coverage (SRTC)?",
                "options": {
                    "A": "TR contains at least one round-trip path for each reachable node that is the start of a round-trip path.",
                    "B": "TR contains all simple paths of length 1.",
                    "C": "TR requires round trips to be executed in zero time.",
                    "D": "TR contains all paths with no round trips."
                },
                "correctAnswer": "A",
                "explanation": "Simple Round Trip Coverage requires TR to contain at least one round-trip path for each reachable node that can begin a round-trip path.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "gsc-017",
                "question": "Does Prime Path Coverage subsume Complete Round Trip Coverage?",
                "options": {
                    "A": "Yes, prime paths include all simple cycles, but not non-simple round trips.",
                    "B": "No, because CRTC can include round trips that are not simple paths.",
                    "C": "Yes, PPC subsumes all path coverage criteria.",
                    "D": "Neither can be compared."
                },
                "correctAnswer": "B",
                "explanation": "CRTC requires all round trips, including those formed by composing multiple cycles. Prime paths only include simple cycles; thus PPC does not subsume CRTC.",
                "difficulty": "hard",
                "sourcePages": [17]
            },
            {
                "id": "gsc-018",
                "question": "If a graph has no cycles (is a Directed Acyclic Graph - DAG), what is the relationship between Prime Path Coverage and Complete Path Coverage?",
                "options": {
                    "A": "PPC is equivalent to CPC for all paths from initial to final nodes.",
                    "B": "CPC is still infinite.",
                    "C": "PPC generates fewer paths than Edge Coverage.",
                    "D": "PPC cannot be applied to DAGs."
                },
                "correctAnswer": "A",
                "explanation": "In an acyclic graph, every path is a simple path. Prime paths starting at initial nodes and ending at final nodes correspond precisely to all complete paths in the DAG.",
                "difficulty": "hard",
                "sourcePages": [12, 17]
            },
            {
                "id": "gsc-019",
                "question": "Which of the following test requirements can be infeasible?",
                "options": {
                    "A": "Only node coverage requirements.",
                    "B": "Test requirements in any criterion if the semantics of the code make that path or condition unreachable.",
                    "C": "Only edge-pair coverage requirements.",
                    "D": "Infeasible test requirements never occur in software testing."
                },
                "correctAnswer": "B",
                "explanation": "Infeasibility arises when control flow structures allow a theoretical path in the graph, but program semantics (contradictory branch conditions, impossible variable values) make executing that path impossible.",
                "difficulty": "easy",
                "sourcePages": [18]
            },
            {
                "id": "gsc-020",
                "question": "In best-effort touring, if a prime path cannot be toured directly due to infeasibility, what does the tester attempt?",
                "options": {
                    "A": "Tour the path with sidetrips or detours.",
                    "B": "Delete the node from the program.",
                    "C": "Declare 100% coverage immediately.",
                    "D": "Crash the compiler."
                },
                "correctAnswer": "A",
                "explanation": "When touring directly is infeasible, touring with sidetrips is permitted as a relaxed (best-effort) requirement to visit the critical segments of the subpath.",
                "difficulty": "medium",
                "sourcePages": [14, 15]
            }
        ]
    },
    {
        "topicId": "graphs-structural-coverage-algorithms",
        "topicName": "Graph Structural Coverage Algorithms",
        "sourcePdf": "graphs-structural-coverage-algorithms.pdf",
        "questions": [
            {
                "id": "gsa-001",
                "question": "In the standard algorithm to compute Prime Paths, what is the starting step?",
                "options": {
                    "A": "Identify all cycles of length 3.",
                    "B": "List all simple paths of length 0 (which are the individual nodes of the graph).",
                    "C": "Find all du-paths.",
                    "D": "Compute the cyclomatic complexity."
                },
                "correctAnswer": "B",
                "explanation": "The algorithm begins with candidate simple paths of length 0 (each node in the graph). At each subsequent step, paths of length k are extended by one edge to form paths of length k+1.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gsa-002",
                "question": "During prime path generation, when is a path of length k flagged with an exclamation mark (!) indicating it has terminated and cannot be extended?",
                "options": {
                    "A": "When the path forms a cycle (the next node is already in the path, matching the first node) or has no outgoing edges.",
                    "B": "When the path contains an odd number of edges.",
                    "C": "When the path visits an initial node.",
                    "D": "When the path length exceeds 10."
                },
                "correctAnswer": "A",
                "explanation": "A simple path cannot be extended if it forms a cycle (first node equals last node) or reaches a terminal node with no outgoing edges. Any further extension would violate the simple path definition.",
                "difficulty": "medium",
                "sourcePages": [4, 5]
            },
            {
                "id": "gsa-003",
                "question": "When does a path of length k get flagged with an asterisk (*) during prime path generation?",
                "options": {
                    "A": "When extending it would visit an internal node already present in the path (forming a non-simple path).",
                    "B": "When it is a test path from N0 to Nf.",
                    "C": "When it has the highest priority.",
                    "D": "When it contains an infeasible edge."
                },
                "correctAnswer": "A",
                "explanation": "A path is flagged with * when attempting to extend it reaches a node already in the path that is NOT the first node, meaning the extended path is not simple and must be pruned.",
                "difficulty": "hard",
                "sourcePages": [5, 6]
            },
            {
                "id": "gsa-004",
                "question": "After all candidate simple paths have been generated, what final filtering step is performed to identify the prime paths?",
                "options": {
                    "A": "Eliminate any simple path that is a proper subpath of another simple path in the candidate list.",
                    "B": "Sort the paths alphabetically.",
                    "C": "Remove all paths of length greater than 3.",
                    "D": "Keep only paths that start at node 1."
                },
                "correctAnswer": "A",
                "explanation": "A prime path is a maximal simple path. Any simple path that is completely contained as a proper subpath of another simple path is redundant and removed.",
                "difficulty": "medium",
                "sourcePages": [7, 8]
            },
            {
                "id": "gsa-005",
                "question": "Suppose we have a self-loop on node 2: edge (2, 2). Is [2, 2] a prime path?",
                "options": {
                    "A": "No, paths of length 1 cannot be prime.",
                    "B": "Yes, [2, 2] is a simple cycle of length 1 and cannot be extended to any longer simple cycle starting and ending at 2.",
                    "C": "Only if node 2 is an initial node.",
                    "D": "Only if node 2 has no other edges."
                },
                "correctAnswer": "B",
                "explanation": "[2, 2] is a simple cycle of length 1. It is simple because only the first and last nodes repeat. It cannot be extended without repeating node 2 internally, so it is a prime path.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "gsa-006",
                "question": "What is the maximum possible length of a prime path in a graph with N nodes?",
                "options": {
                    "A": "N - 1",
                    "B": "N",
                    "C": "N + 1",
                    "D": "2N"
                },
                "correctAnswer": "B",
                "explanation": "A simple path with no cycle has at most N nodes, giving length N - 1. A simple cycle can have N nodes in the cycle plus the repeated start node (N + 1 nodes), giving length N edges.",
                "difficulty": "hard",
                "sourcePages": [11]
            },
            {
                "id": "gsa-007",
                "question": "In a linear pipeline graph with 4 nodes: 1 → 2 → 3 → 4 and no other edges, how many prime paths exist?",
                "options": {
                    "A": "1 prime path: [1, 2, 3, 4]",
                    "B": "4 prime paths",
                    "C": "6 prime paths",
                    "D": "0 prime paths"
                },
                "correctAnswer": "A",
                "explanation": "All subpaths like [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4] are proper subpaths of [1, 2, 3, 4]. Since [1, 2, 3, 4] is maximal and simple, it is the sole prime path.",
                "difficulty": "medium",
                "sourcePages": [12]
            },
            {
                "id": "gsa-008",
                "question": "Why can touring with sidetrips satisfy a prime path requirement that cannot be toured directly?",
                "options": {
                    "A": "Because a sidetrip allows temporary diversion through a necessary loop or state update before returning to resume the required sequence.",
                    "B": "Because sidetrips remove nodes from the graph.",
                    "C": "Because sidetrips convert prime paths into node coverage.",
                    "D": "Because sidetrips bypass compiler optimization."
                },
                "correctAnswer": "A",
                "explanation": "Sometimes semantic constraints require loop execution (e.g. initializing an iterator or reading data) before proceeding. Sidetrips allow taking that loop at node ni and returning to ni to complete the path.",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "gsa-009",
                "question": "Consider graph with nodes {1, 2, 3, 4} and edges (1, 2), (1, 3), (2, 4), (3, 4). How many prime paths of length 2 exist?",
                "options": {
                    "A": "2: [1, 2, 4] and [1, 3, 4]",
                    "B": "4",
                    "C": "1",
                    "D": "0"
                },
                "correctAnswer": "A",
                "explanation": "The paths [1, 2, 4] and [1, 3, 4] are maximal simple paths because they start at 1 and terminate at 4. Neither is a subpath of any longer simple path. Hence there are 2 prime paths.",
                "difficulty": "easy",
                "sourcePages": [6, 7]
            },
            {
                "id": "gsa-010",
                "question": "What is the computational complexity of finding all prime paths in the worst case?",
                "options": {
                    "A": "O(1)",
                    "B": "O(|V| + |E|)",
                    "C": "Exponential in the number of vertices",
                    "D": "Logarithmic"
                },
                "correctAnswer": "C",
                "explanation": "In graphs with dense connectivity or multiple interleaved cycles, the number of simple paths can grow exponentially with the number of vertices.",
                "difficulty": "medium",
                "sourcePages": [15]
            },
            {
                "id": "gsa-011",
                "question": "If path [1, 2, 1] is a prime path, what kind of structural construct does it represent?",
                "options": {
                    "A": "A simple cycle of length 2 between nodes 1 and 2.",
                    "B": "An isolated vertex.",
                    "C": "A linear branch.",
                    "D": "An infeasible exception handler."
                },
                "correctAnswer": "A",
                "explanation": "[1, 2, 1] starts and ends at node 1, passing through node 2 without repeating internal nodes. This is a simple cycle of length 2.",
                "difficulty": "easy",
                "sourcePages": [8]
            },
            {
                "id": "gsa-012",
                "question": "When constructing test paths to cover prime paths, what is prefix and suffix path stitching?",
                "options": {
                    "A": "Appending a path from N0 to the start of the prime path, and from the end of the prime path to Nf, to create a valid test path.",
                    "B": "Editing the binary executable file directly.",
                    "C": "Removing unreached nodes from the source code.",
                    "D": "Reversing the graph edges."
                },
                "correctAnswer": "A",
                "explanation": "A prime path may not start at N0 or end at Nf. To execute it in a test case, it must be stitched: preceded by a path from an initial node and succeeded by a path to a final node.",
                "difficulty": "medium",
                "sourcePages": [16, 17]
            },
            {
                "id": "gsa-013",
                "question": "Can two different prime paths share common nodes and edges?",
                "options": {
                    "A": "No, prime paths must be completely node-disjoint.",
                    "B": "Yes, prime paths frequently overlap on shared subpaths as long as neither path is completely contained within the other.",
                    "C": "Only if the graph is bipartite.",
                    "D": "Only when edge coverage is 0%."
                },
                "correctAnswer": "B",
                "explanation": "Prime paths can overlap significantly. They are only required not to be proper subpaths of each other.",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "gsa-014",
                "question": "What is the length of the simple path [1, 2, 3]?",
                "options": {
                    "A": "3",
                    "B": "2",
                    "C": "1",
                    "D": "0"
                },
                "correctAnswer": "B",
                "explanation": "The length of a path in graph theory is the number of edges it contains. The path [1, 2, 3] has 2 edges: (1, 2) and (2, 3).",
                "difficulty": "easy",
                "sourcePages": [3]
            },
            {
                "id": "gsa-015",
                "question": "In prime path generation, if path [1, 2, 3, 2] is formed, is it a simple path?",
                "options": {
                    "A": "Yes, because node 2 repeats.",
                    "B": "No, because the repeated node (2) is not both the first and last node.",
                    "C": "Yes, any path of length 3 is simple.",
                    "D": "It depends on whether node 1 is an initial node."
                },
                "correctAnswer": "B",
                "explanation": "In a simple path, only the first and last nodes may be identical. In [1, 2, 3, 2], node 2 is repeated internally, violating simplicity.",
                "difficulty": "medium",
                "sourcePages": [4, 5]
            },
            {
                "id": "gsa-016",
                "question": "Which criterion guarantees that every loop in the graph is bypassed, executed once, and executed more than once (under typical loop topologies)?",
                "options": {
                    "A": "Node Coverage",
                    "B": "Edge Coverage",
                    "C": "Prime Path Coverage",
                    "D": "Each Choice Coverage"
                },
                "correctAnswer": "C",
                "explanation": "Prime Path Coverage naturally generates paths that bypass the loop (if possible), paths that enter and exit the loop once, and simple cycles that represent looping.",
                "difficulty": "medium",
                "sourcePages": [14, 18]
            },
            {
                "id": "gsa-017",
                "question": "Why is Edge-Pair Coverage (EPC) algorithmically simpler to compute than Prime Path Coverage?",
                "options": {
                    "A": "EPC only requires enumerating paths of fixed length 2, which requires checking pairs of adjacent edges without recursive expansion.",
                    "B": "EPC does not require graph analysis.",
                    "C": "EPC only applies to linear graphs.",
                    "D": "EPC has no test requirements."
                },
                "correctAnswer": "A",
                "explanation": "EPC only considers adjacent edge pairs (length 2), which is bounded by O(|E|^2) or out-degree products, whereas prime paths require finding maximal paths of variable lengths up to |V|.",
                "difficulty": "medium",
                "sourcePages": [2]
            },
            {
                "id": "gsa-018",
                "question": "If graph G has 3 nodes {1, 2, 3} arranged in a directed triangle: (1, 2), (2, 3), (3, 1). What are the prime paths?",
                "options": {
                    "A": "[1, 2, 3, 1], [2, 3, 1, 2], and [3, 1, 2, 3]",
                    "B": "Only [1, 2, 3]",
                    "C": "Only [1, 2]",
                    "D": "[1, 1], [2, 2], [3, 3]"
                },
                "correctAnswer": "A",
                "explanation": "The three maximal simple cycles are [1, 2, 3, 1], [2, 3, 1, 2], and [3, 1, 2, 3]. None is a subpath of another because they start at different nodes.",
                "difficulty": "hard",
                "sourcePages": [10, 11]
            },
            {
                "id": "gsa-019",
                "question": "What is the primary role of graph reduction or basic block aggregation before running prime path algorithms?",
                "options": {
                    "A": "To compress straight-line sequences of nodes into single nodes, drastically reducing graph size without altering branch topology.",
                    "B": "To convert the graph to an undirected graph.",
                    "C": "To eliminate all conditional statements.",
                    "D": "To force all paths to have length 1."
                },
                "correctAnswer": "A",
                "explanation": "Collapsing basic blocks (linear sequences of statements with single entry/exit) reduces graph node and edge counts, accelerating prime path computation without losing coverage precision.",
                "difficulty": "medium",
                "sourcePages": [19]
            },
            {
                "id": "gsa-020",
                "question": "What tool or technique can assist when prime paths cannot be statically verified as feasible?",
                "options": {
                    "A": "SMT / SAT solvers (symbolic execution) to solve path constraints.",
                    "B": "Ignoring all branch statements.",
                    "C": "Deleting test cases.",
                    "D": "Increasing hardware clock speed."
                },
                "correctAnswer": "A",
                "explanation": "Symbolic execution tools and constraint solvers (SMT solvers like Z3) determine whether the path predicate along a candidate prime path is satisfiable.",
                "difficulty": "easy",
                "sourcePages": [20]
            }
        ]
    },
    {
        "topicId": "graphs-data-flow",
        "topicName": "Graph Coverage - Data Flow",
        "sourcePdf": "graphs-data-flow.pdf",
        "questions": [
            {
                "id": "gdf-001",
                "question": "In data flow testing, what is a 'def' (definition) of a variable v?",
                "options": {
                    "A": "A location where variable v is read or printed.",
                    "B": "A location where a value is stored into memory or bound to variable v.",
                    "C": "A comment defining the variable purpose.",
                    "D": "The scope where variable v ceases to exist."
                },
                "correctAnswer": "B",
                "explanation": "A definition (def) is a statement or node where a value is stored in memory, assigned to a variable, or passed as an input/output parameter.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gdf-002",
                "question": "What is a 'use' of a variable v in data flow testing?",
                "options": {
                    "A": "A location where variable v is assigned a new value.",
                    "B": "A location where variable v's value is accessed, read, or referenced.",
                    "C": "The declaration line of variable v.",
                    "D": "The memory deallocation statement for v."
                },
                "correctAnswer": "B",
                "explanation": "A use is a location (node or edge) where the value of variable v is read, fetched, or used in a computation or conditional test.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gdf-003",
                "question": "What is a 'def-clear path' with respect to variable v?",
                "options": {
                    "A": "A path where variable v is cleared to null.",
                    "B": "A path from node ni to node nj where no node on the path (excluding ni and nj) defines variable v.",
                    "C": "A path containing no definitions of any variable.",
                    "D": "A path where variable v is defined at every node."
                },
                "correctAnswer": "B",
                "explanation": "A path is def-clear with respect to v if v is not assigned/re-defined at any intermediate node between the start node and the destination node.",
                "difficulty": "medium",
                "sourcePages": [4, 5]
            },
            {
                "id": "gdf-004",
                "question": "What is a 'du-path' (definition-use path)?",
                "options": {
                    "A": "A simple path from a definition of v to a use of v that is def-clear with respect to v.",
                    "B": "Any path that contains both a def and a use, regardless of cycles.",
                    "C": "A path that defines two variables simultaneously.",
                    "D": "A path where variable v is used before it is defined."
                },
                "correctAnswer": "A",
                "explanation": "A du-path with respect to variable v is a simple path from a node where v is defined to a node (or edge) where v is used, such that the path is def-clear for v.",
                "difficulty": "medium",
                "sourcePages": [6]
            },
            {
                "id": "gdf-005",
                "question": "What does a 'du-pair' represent?",
                "options": {
                    "A": "A pair of variables that always appear together.",
                    "B": "A pair (d, u) of a definition d of v and a use u of v such that there is at least one def-clear path from d to u.",
                    "C": "A pair of adjacent edges in the graph.",
                    "D": "A test case with two inputs."
                },
                "correctAnswer": "B",
                "explanation": "A du-pair (d, u) consists of a def d and use u of the same variable v where at least one def-clear path exists connecting d to u.",
                "difficulty": "medium",
                "sourcePages": [5]
            },
            {
                "id": "gdf-006",
                "question": "What is the requirement for All-Defs Coverage (ADC)?",
                "options": {
                    "A": "For each definition of each variable, at least one def-clear path to at least one reachable use must be toured.",
                    "B": "Every variable must be defined in every test case.",
                    "C": "All definitions must be reached and re-assigned.",
                    "D": "All definitions must be tested against all uses simultaneously."
                },
                "correctAnswer": "A",
                "explanation": "All-Defs Coverage requires that for every definition of every variable, at least one def-clear path from that definition to some reachable use is executed.",
                "difficulty": "medium",
                "sourcePages": [8]
            },
            {
                "id": "gdf-007",
                "question": "What is the requirement for All-Uses Coverage (AUC)?",
                "options": {
                    "A": "For each definition of each variable, at least one def-clear path to EACH reachable use of that definition must be toured.",
                    "B": "All variables must be used in a single expression.",
                    "C": "Every use must be tested with negative values.",
                    "D": "All uses must occur before any def."
                },
                "correctAnswer": "A",
                "explanation": "All-Uses Coverage requires that for every definition of a variable and every reachable use of that definition, at least one def-clear path connecting them is toured.",
                "difficulty": "medium",
                "sourcePages": [9]
            },
            {
                "id": "gdf-008",
                "question": "What does All-du-Paths Coverage (ADUPC) require?",
                "options": {
                    "A": "For every def-use pair, EVERY du-path between them must be toured.",
                    "B": "Only the shortest du-path must be toured.",
                    "C": "Only du-paths of length 1 must be toured.",
                    "D": "At least two du-paths per program."
                },
                "correctAnswer": "A",
                "explanation": "All-du-Paths Coverage requires that every du-path from each definition to each corresponding use must be covered by test paths.",
                "difficulty": "medium",
                "sourcePages": [10]
            },
            {
                "id": "gdf-009",
                "question": "Which of the following correctly describes the subsumption relationship among data flow criteria?",
                "options": {
                    "A": "All-Defs Coverage subsumes All-Uses Coverage.",
                    "B": "All-du-Paths Coverage subsumes All-Uses Coverage, and All-Uses Coverage subsumes All-Defs Coverage.",
                    "C": "All-Uses Coverage subsumes All-du-Paths Coverage.",
                    "D": "All-Defs Coverage subsumes Prime Path Coverage."
                },
                "correctAnswer": "B",
                "explanation": "Covering all du-paths (ADUPC) ensures every reachable def-use pair has at least one path covered (AUC), which ensures every def has at least one use covered (ADC).",
                "difficulty": "easy",
                "sourcePages": [12]
            },
            {
                "id": "gdf-010",
                "question": "Does Prime Path Coverage (PPC) subsume All-du-Paths Coverage (ADUPC)?",
                "options": {
                    "A": "Yes, always.",
                    "B": "No. Although du-paths are simple paths, touring prime paths with sidetrips does NOT guarantee def-clear touring.",
                    "C": "Yes, because PPC is the strongest possible coverage.",
                    "D": "Only when the graph has no loops."
                },
                "correctAnswer": "B",
                "explanation": "PPC does not subsume ADUPC (and ADUPC does not subsume PPC). If PPC tours a prime path with a sidetrip, that sidetrip might re-define the variable, violating the def-clear requirement of the du-path.",
                "difficulty": "hard",
                "sourcePages": [13, 14]
            },
            {
                "id": "gdf-011",
                "question": "What is the distinction between a Computation Use (c-use) and a Predicate Use (p-use)?",
                "options": {
                    "A": "c-use occurs in an assignment or output; p-use occurs in a conditional predicate deciding control flow.",
                    "B": "c-use is used in C programs; p-use is used in Python programs.",
                    "C": "p-use assigns a value; c-use frees memory.",
                    "D": "There is no difference in formal data flow theory."
                },
                "correctAnswer": "A",
                "explanation": "A computation use (c-use) directly affects a computation (e.g. RHS of assignment: y = x + 1), while a predicate use (p-use) governs control flow branching (e.g. if (x > 0)).",
                "difficulty": "medium",
                "sourcePages": [15]
            },
            {
                "id": "gdf-012",
                "question": "Suppose variable x is defined at node 1. Node 2 uses x. Node 3 re-defines x. Node 4 uses x. Is path [1, 2, 3, 4] a def-clear path with respect to the def of x at node 1?",
                "options": {
                    "A": "Yes, because x is used at node 4.",
                    "B": "No, because node 3 re-defines x, killing the definition from node 1.",
                    "C": "Yes, because node 2 is def-clear.",
                    "D": "Only if node 3 is a loop."
                },
                "correctAnswer": "B",
                "explanation": "At node 3, variable x is redefined. Therefore, the path [1, 2, 3, 4] is NOT def-clear with respect to the definition of x at node 1.",
                "difficulty": "easy",
                "sourcePages": [4, 5]
            },
            {
                "id": "gdf-013",
                "question": "What happens if a variable is used without a prior definition on some path?",
                "options": {
                    "A": "It indicates a potential data flow anomaly (uninitialized variable use / read before write).",
                    "B": "The compiler automatically fixes the logic.",
                    "C": "It is an example of All-Defs Coverage.",
                    "D": "It proves the program has no bugs."
                },
                "correctAnswer": "A",
                "explanation": "Referencing a variable without prior definition is a serious data flow anomaly (ur-anomaly: use before definition), usually resulting in undefined behavior or crashes.",
                "difficulty": "easy",
                "sourcePages": [16]
            },
            {
                "id": "gdf-014",
                "question": "What is a 'dd-anomaly' in data flow analysis?",
                "options": {
                    "A": "Double definition: a variable is defined twice without any intervening use.",
                    "B": "Data destruction error.",
                    "C": "Dynamic dispatch failure.",
                    "D": "Def-clear path violation."
                },
                "correctAnswer": "A",
                "explanation": "A dd-anomaly occurs when a variable is defined and then redefined without being read in between, indicating redundant computations or missing logic.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "gdf-015",
                "question": "Can a du-path contain a cycle?",
                "options": {
                    "A": "Yes, du-paths can contain any number of cycles.",
                    "B": "A du-path is a simple path; thus it can only contain a cycle if the first and last nodes are the same node (which must be def and use).",
                    "C": "No, du-paths cannot have any repeated nodes whatsoever.",
                    "D": "Only in recursive functions."
                },
                "correctAnswer": "B",
                "explanation": "By definition, a du-path is a simple path. Hence it cannot repeat any internal nodes. If the def and use are at the same node, it can be a simple cycle.",
                "difficulty": "hard",
                "sourcePages": [6]
            },
            {
                "id": "gdf-016",
                "question": "Why is data flow testing considered more effective at catching certain logic faults than pure control-flow testing (NC/EC)?",
                "options": {
                    "A": "Because it forces tests to verify the propagation and lifetime of data values between distant statements.",
                    "B": "Because it does not require running the code.",
                    "C": "Because it always requires fewer test cases.",
                    "D": "Because it replaces unit testing."
                },
                "correctAnswer": "A",
                "explanation": "Control flow testing merely touches edges, but data flow testing checks that values computed at one location are correctly received and used at other locations, detecting lifecycle and propagation bugs.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "gdf-017",
                "question": "If a method defines variable 'count' at node 1, and 'count' is used at node 3 and node 5, how many du-pairs exist for 'count' (assuming def-clear paths exist)?",
                "options": {
                    "A": "1",
                    "B": "2: (node 1, node 3) and (node 1, node 5)",
                    "C": "4",
                    "D": "0"
                },
                "correctAnswer": "B",
                "explanation": "There are 2 distinct use locations for the single def at node 1, yielding two du-pairs: (1, 3) and (1, 5).",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "gdf-018",
                "question": "In data flow testing, how are variables passed as reference parameters to a function treated?",
                "options": {
                    "A": "Only as uses.",
                    "B": "Potentially as both uses and defs, since the called function can read and modify their values.",
                    "C": "They are completely ignored.",
                    "D": "Only as defs."
                },
                "correctAnswer": "B",
                "explanation": "Reference parameters allow the callee to read the incoming value (use) and write a modified value back into caller's storage (def).",
                "difficulty": "medium",
                "sourcePages": [17]
            },
            {
                "id": "gdf-019",
                "question": "If a du-path is infeasible, what is the impact on test coverage measurement?",
                "options": {
                    "A": "100% coverage cannot be achieved unless infeasible du-paths are recognized and eliminated from TR.",
                    "B": "The program must be rewritten immediately.",
                    "C": "Coverage is automatically set to 0%.",
                    "D": "All other du-paths become infeasible."
                },
                "correctAnswer": "A",
                "explanation": "Just like structural coverage, infeasible du-paths cannot be executed by any input and must be recognized and excluded when calculating true coverage percentage.",
                "difficulty": "easy",
                "sourcePages": [18]
            },
            {
                "id": "gdf-020",
                "question": "Which data flow coverage criterion is the weakest among ADC, AUC, and ADUPC?",
                "options": {
                    "A": "All-du-Paths Coverage",
                    "B": "All-Uses Coverage",
                    "C": "All-Defs Coverage",
                    "D": "They are all of identical strength."
                },
                "correctAnswer": "C",
                "explanation": "All-Defs Coverage (ADC) is the weakest because it only requires covering one use for each def, whereas AUC requires covering all reachable uses, and ADUPC requires all paths to all uses.",
                "difficulty": "easy",
                "sourcePages": [12]
            }
        ]
    },
    {
        "topicId": "graphs-source-code",
        "topicName": "Graph Coverage from Source Code",
        "sourcePdf": "graphs-source-code.pdf",
        "questions": [
            {
                "id": "gsc-src-001",
                "question": "What is a 'basic block' in Control Flow Graph (CFG) construction from source code?",
                "options": {
                    "A": "A sequence of statements that can only be entered at the beginning and exited at the end without internal branches.",
                    "B": "A block of memory allocated by malloc.",
                    "C": "A method containing fewer than 5 lines of code.",
                    "D": "A try-catch block."
                },
                "correctAnswer": "A",
                "explanation": "A basic block is a maximal sequence of consecutive program statements in which flow of control enters at the first statement and leaves at the last statement without halt or possibility of branching in the middle.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "gsc-src-002",
                "question": "What is McCabe's Cyclomatic Complexity formula for a single connected component graph (P = 1)?",
                "options": {
                    "A": "V(G) = E - N + 2",
                    "B": "V(G) = N - E + 2",
                    "C": "V(G) = E + N - 2",
                    "D": "V(G) = E × N"
                },
                "correctAnswer": "A",
                "explanation": "For a single connected component (P = 1), Cyclomatic Complexity is given by V(G) = E - N + 2, where E is the number of edges and N is the number of nodes.",
                "difficulty": "easy",
                "sourcePages": [14, 15]
            },
            {
                "id": "gsc-src-003",
                "question": "How does an 'if-then-else' construct translate into nodes and edges in a standard CFG?",
                "options": {
                    "A": "A single predicate node with two outgoing edges (True and False branches) leading to respective then/else blocks, which join at a merge node.",
                    "B": "A single node with no edges.",
                    "C": "Three disconnected nodes.",
                    "D": "A cycle of length 3."
                },
                "correctAnswer": "A",
                "explanation": "The condition forms a decision node with two outgoing edges: one to the 'then' block and one to the 'else' block, both of which subsequently connect to the join node following the conditional.",
                "difficulty": "easy",
                "sourcePages": [4, 5]
            },
            {
                "id": "gsc-src-004",
                "question": "In languages like Java or C, how does short-circuit evaluation of 'if (A && B)' affect the CFG?",
                "options": {
                    "A": "It expands the condition into two decision nodes: evaluating A first; if A is false, B is skipped and control jumps directly to false branch.",
                    "B": "It turns the condition into a single node with no branches.",
                    "C": "It eliminates the if statement completely.",
                    "D": "It forces both A and B to always execute."
                },
                "correctAnswer": "A",
                "explanation": "Because && short-circuits, B is evaluated only when A is true. In a detailed CFG, this results in two sequential decision nodes rather than a single compound node.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "gsc-src-005",
                "question": "What graph feature distinguishes a 'while' loop from a 'do-while' loop in a CFG?",
                "options": {
                    "A": "In a 'while' loop the condition node is evaluated before the body; in 'do-while' the body is executed before the condition node.",
                    "B": "A 'while' loop has no edges.",
                    "C": "'do-while' loops have no condition node.",
                    "D": "'while' loops cannot have cycles."
                },
                "correctAnswer": "A",
                "explanation": "A while loop tests the loop condition at the entry (can execute 0 times), whereas a do-while loop executes the body first before branching on the condition at the bottom.",
                "difficulty": "easy",
                "sourcePages": [8, 9]
            },
            {
                "id": "gsc-src-006",
                "question": "If a method's CFG has 10 edges and 8 nodes (single component), what is its Cyclomatic Complexity?",
                "options": {
                    "A": "4",
                    "B": "2",
                    "C": "18",
                    "D": "10"
                },
                "correctAnswer": "A",
                "explanation": "V(G) = E - N + 2 = 10 - 8 + 2 = 4.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "gsc-src-007",
                "question": "What does Cyclomatic Complexity represent in terms of testing?",
                "options": {
                    "A": "The upper bound on the number of linearly independent paths needed to achieve branch/edge coverage.",
                    "B": "The total execution time of the method.",
                    "C": "The number of lines of assembly code.",
                    "D": "The number of variables in the class."
                },
                "correctAnswer": "A",
                "explanation": "V(G) defines the dimension of the cycle space and represents the maximum number of linearly independent basis paths through the program.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "gsc-src-008",
                "question": "How do 'switch' or 'case' statements with N branches affect a CFG?",
                "options": {
                    "A": "They create a single decision node with N outgoing edges to each case block (and default).",
                    "B": "They create N parallel independent graphs.",
                    "C": "They are modeled as infinite loops.",
                    "D": "They reduce complexity to 1."
                },
                "correctAnswer": "A",
                "explanation": "A switch construct evaluates the switch expression at a central node and branches out to the distinct case targets, joining after break statements.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "gsc-src-009",
                "question": "How are exceptions (e.g. throw / catch) represented in an inter-block CFG?",
                "options": {
                    "A": "As exceptional control flow edges departing from the throwing statement directly to the catch block or method exit.",
                    "B": "Exceptions cannot be represented in CFGs.",
                    "C": "They are represented as normal return statements.",
                    "D": "As isolated nodes with no incoming edges."
                },
                "correctAnswer": "A",
                "explanation": "Exceptional control flow introduces edges from potentially exception-throwing statements to corresponding catch handlers (or out of the method to callers).",
                "difficulty": "medium",
                "sourcePages": [11, 12]
            },
            {
                "id": "gsc-src-010",
                "question": "In basis path testing, what is a 'basis set' of paths?",
                "options": {
                    "A": "A set of linearly independent paths from which any path through the graph can be expressed as a linear combination.",
                    "B": "The set of all paths of length 1.",
                    "C": "All paths that contain return statements.",
                    "D": "Paths that only visit initial nodes."
                },
                "correctAnswer": "A",
                "explanation": "A basis set consists of linearly independent paths forming a basis for the graph's path space, guaranteeing that every edge is covered at least once.",
                "difficulty": "medium",
                "sourcePages": [16, 17]
            },
            {
                "id": "gsc-src-011",
                "question": "What is the relationship between Cyclomatic Complexity and the number of predicate (decision) nodes P in a binary decision graph?",
                "options": {
                    "A": "V(G) = P + 1",
                    "B": "V(G) = P - 1",
                    "C": "V(G) = 2P",
                    "D": "V(G) = P / 2"
                },
                "correctAnswer": "A",
                "explanation": "For a CFG where every decision node has out-degree 2 (binary decision nodes), McCabe proved that V(G) = P + 1.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "gsc-src-012",
                "question": "If a program has V(G) = 1, what does this indicate about the program's control flow?",
                "options": {
                    "A": "The program is a purely sequential straight-line program with no branches or loops.",
                    "B": "The program is an infinite loop.",
                    "C": "The program has 100 branches.",
                    "D": "The program cannot compile."
                },
                "correctAnswer": "A",
                "explanation": "V(G) = 1 implies 0 predicate nodes (P = 0): the code executes sequentially from start to finish without any conditional branching or loops.",
                "difficulty": "easy",
                "sourcePages": [14]
            },
            {
                "id": "gsc-src-013",
                "question": "Why is branch coverage on source code equivalent to Edge Coverage on its CFG?",
                "options": {
                    "A": "Because every conditional decision outcome (True/False branch) corresponds to an outgoing edge from the decision node in the CFG.",
                    "B": "Because both require testing loops 10 times.",
                    "C": "Because branches and edges are identical keywords in Java.",
                    "D": "They are not equivalent."
                },
                "correctAnswer": "A",
                "explanation": "Branch coverage requires executing both True and False outcomes of every branch. In the CFG, these outcomes correspond directly to the outgoing edges of decision nodes.",
                "difficulty": "easy",
                "sourcePages": [5, 6]
            },
            {
                "id": "gsc-src-014",
                "question": "What is statement coverage on source code equivalent to in the corresponding CFG?",
                "options": {
                    "A": "Node Coverage",
                    "B": "Prime Path Coverage",
                    "C": "Complete Path Coverage",
                    "D": "Data Flow Coverage"
                },
                "correctAnswer": "A",
                "explanation": "Each statement belongs to a basic block, which is represented by a node in the CFG. Executing every statement corresponds directly to visiting every node (Node Coverage).",
                "difficulty": "easy",
                "sourcePages": [3, 4]
            },
            {
                "id": "gsc-src-015",
                "question": "Consider code with a 'break' statement inside a loop. How does the 'break' appear in the CFG?",
                "options": {
                    "A": "An edge jumping directly from the break statement node to the loop exit node.",
                    "B": "A self-loop on the break statement.",
                    "C": "An edge back to the loop header.",
                    "D": "It deletes the loop from the graph."
                },
                "correctAnswer": "A",
                "explanation": "A 'break' statement terminates loop execution prematurely, creating an unconditional edge jumping out of the loop body to the statement immediately following the loop.",
                "difficulty": "easy",
                "sourcePages": [9]
            },
            {
                "id": "gsc-src-016",
                "question": "Consider code with a 'continue' statement inside a loop. How does the 'continue' appear in the CFG?",
                "options": {
                    "A": "An edge jumping from the continue statement to the loop update/condition node, skipping the rest of the loop body.",
                    "B": "An edge to the exit of the program.",
                    "C": "A cycle of length 0.",
                    "D": "An edge to the main() method."
                },
                "correctAnswer": "A",
                "explanation": "A 'continue' statement bypasses remaining statements in the current iteration and branches directly to the loop condition or iteration step.",
                "difficulty": "easy",
                "sourcePages": [9]
            },
            {
                "id": "gsc-src-017",
                "question": "Can high statement coverage (e.g., 100%) guarantee that all faults in conditional logic are detected?",
                "options": {
                    "A": "No, because statement coverage can be achieved without executing empty 'else' branches or testing false outcomes of single-branch 'if' statements.",
                    "B": "Yes, statement coverage is the strongest possible coverage.",
                    "C": "Yes, if the statements are written in C++.",
                    "D": "Only when all statements are print statements."
                },
                "correctAnswer": "A",
                "explanation": "For an 'if (cond) { doSomething(); }' without an 'else', a single test making 'cond' true achieves 100% statement coverage, but never tests the false outcome where bugs might occur.",
                "difficulty": "medium",
                "sourcePages": [5]
            },
            {
                "id": "gsc-src-018",
                "question": "What is the region-based formula for Cyclomatic Complexity on a planar graph?",
                "options": {
                    "A": "V(G) = Number of enclosed regions + 1",
                    "B": "V(G) = Number of regions - 1",
                    "C": "V(G) = Total nodes / Total edges",
                    "D": "V(G) = Number of external regions only"
                },
                "correctAnswer": "A",
                "explanation": "In a planar representation of a CFG, Cyclomatic Complexity equals the number of enclosed (bounded) regions plus 1 (the unbounded external region).",
                "difficulty": "medium",
                "sourcePages": [15]
            },
            {
                "id": "gsc-src-019",
                "question": "In source-code CFG analysis, what is an 'unreachable node' (dead code)?",
                "options": {
                    "A": "A node for which no path exists from the initial node N0.",
                    "B": "A node with no outgoing edges.",
                    "C": "A node that contains a return statement.",
                    "D": "A node with prime path length 0."
                },
                "correctAnswer": "A",
                "explanation": "An unreachable node has no valid path connecting it from the entry node N0. In code, this corresponds to unreachable or dead code (e.g. statements following an unconditional return).",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "gsc-src-020",
                "question": "Why is Cyclomatic Complexity widely used as a software quality and testing metric?",
                "options": {
                    "A": "High complexity correlates with higher defect rates and indicates how many test cases are minimally required to cover all decision outcomes.",
                    "B": "It measures CPU clock speed during test execution.",
                    "C": "It measures user interface responsiveness.",
                    "D": "It guarantees that the software will never crash."
                },
                "correctAnswer": "A",
                "explanation": "Cyclomatic complexity provides an objective measurement of structural branching, indicating cognitive difficulty, fault-proneness, and the minimum test effort needed for branch coverage.",
                "difficulty": "easy",
                "sourcePages": [16]
            }
        ]
    }
]
