# Topic 16 to 20 Question Bank

DATA = [
    {
        "topicId": "oo-testing",
        "topicName": "Object-Oriented Testing",
        "sourcePdf": "OO-testing.pdf",
        "questions": [
            {
                "id": "oo-001",
                "question": "How does Encapsulation (information hiding) impact software testing in Object-Oriented systems?",
                "options": {
                    "A": "Internal state is hidden within private fields, making it harder to inspect state after test execution and verify postconditions without dedicated accessor methods or state observers.",
                    "B": "Encapsulation prevents classes from being compiled.",
                    "C": "Encapsulation makes all methods static.",
                    "D": "Encapsulation eliminates all software bugs automatically."
                },
                "correctAnswer": "A",
                "explanation": "Because private instance variables cannot be accessed directly by external test cases, observing whether state was correctly mutated (observability) requires getters, inspecting return values, or state instrumentation.",
                "difficulty": "medium",
                "sourcePages": [4, 5]
            },
            {
                "id": "oo-002",
                "question": "What testing challenge is introduced by Inheritance in Object-Oriented programming?",
                "options": {
                    "A": "Inherited methods operate in a new subclass context with potentially overridden state or collaborator methods, meaning inherited methods cannot simply be assumed correct without re-testing.",
                    "B": "Inherited methods cannot be executed.",
                    "C": "Subclasses cannot have constructors.",
                    "D": "Base classes must be deleted after inheritance."
                },
                "correctAnswer": "A",
                "explanation": "Even if method m() passed all tests in superclass Base, when inherited by SubClass, it may interact with overridden methods or new subclass invariants, necessitating context-sensitive retesting.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "oo-003",
                "question": "What testing challenge arises from Polymorphism and Dynamic Binding?",
                "options": {
                    "A": "A single method call site (e.g. obj.draw()) can bind dynamically to many different subclass implementations at runtime, requiring tests to cover all feasible concrete receiver types.",
                    "B": "Polymorphism causes memory leaks in all compilers.",
                    "C": "Polymorphism requires writing code in C.",
                    "D": "Polymorphism eliminates the need for test oracles."
                },
                "correctAnswer": "A",
                "explanation": "Dynamic dispatch means the actual code executed is decided at runtime based on the object's dynamic type, creating a combinatorial explosion of polymorphic call targets that must be tested.",
                "difficulty": "medium",
                "sourcePages": [8, 9]
            },
            {
                "id": "oo-004",
                "question": "Why can Abstract Classes and Interfaces NOT be tested directly as units?",
                "options": {
                    "A": "Because they cannot be directly instantiated without providing concrete implementations for their abstract method declarations.",
                    "B": "Because they have no names.",
                    "C": "Because Java bans testing abstract classes.",
                    "D": "Because they only contain integer constants."
                },
                "correctAnswer": "A",
                "explanation": "Abstract classes and interfaces contain unimplemented method signatures and cannot be instantiated with 'new'. Testing their contracts requires concrete subclasses, test doubles, or mock objects.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "oo-005",
                "question": "What is 'State-based Testing' of an Object-Oriented class?",
                "options": {
                    "A": "Testing that sequences of method invocations correctly transition an object between valid internal states according to its Class State Machine.",
                    "B": "Testing software across different US states.",
                    "C": "Testing only the main method.",
                    "D": "Testing while the computer is turned off."
                },
                "correctAnswer": "A",
                "explanation": "An object encapsulates mutable state. State-based testing treats methods as state transitions, executing sequences of calls to verify that transitions, guards, and invariants are preserved.",
                "difficulty": "easy",
                "sourcePages": [12, 13]
            },
            {
                "id": "oo-006",
                "question": "What is a 'State Definition Anomaly' in class testing?",
                "options": {
                    "A": "When an instance variable is left uninitialized or corrupted by a method call sequence, placing the object into an inconsistent internal state.",
                    "B": "When a class has too many comments.",
                    "C": "When a method has more than 3 parameters.",
                    "D": "When an interface is implemented twice."
                },
                "correctAnswer": "A",
                "explanation": "A state definition anomaly occurs when method operations violate class invariants or fail to properly initialize/update interrelated instance variables.",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "oo-007",
                "question": "In class testing, what is a 'Class Invariant'?",
                "options": {
                    "A": "A condition that must hold true for every valid instance of the class at all stable points (after constructor execution and after every public method call).",
                    "B": "A constant that cannot be printed.",
                    "C": "A method that takes no arguments.",
                    "D": "The class filename on disk."
                },
                "correctAnswer": "A",
                "explanation": "A class invariant (e.g. balance >= 0, or size <= capacity) expresses fundamental structural truth about the object's valid state that must be maintained across all public operations.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "oo-008",
                "question": "What is the 'flattened class' testing approach for inheritance?",
                "options": {
                    "A": "Treating a subclass as if all inherited methods were copied directly into it, and testing the entire flattened set of methods in the subclass context.",
                    "B": "Deleting all subclasses.",
                    "C": "Compressing the class bytecode.",
                    "D": "Converting object-oriented code into procedural C."
                },
                "correctAnswer": "A",
                "explanation": "Class flattening conceptually expands the subclass to include all inherited methods as if locally defined, ensuring thorough test coverage of inherited operations in the subclass environment.",
                "difficulty": "medium",
                "sourcePages": [16, 17]
            },
            {
                "id": "oo-009",
                "question": "What is 'Method Interleaving' testing in class state testing?",
                "options": {
                    "A": "Executing arbitrary permutations and sequences of different public methods (e.g. push, pop, top, push, clear) to discover sequence-dependent defects.",
                    "B": "Writing methods in two languages simultaneously.",
                    "C": "Running two compilers at once.",
                    "D": "Deleting private methods."
                },
                "correctAnswer": "A",
                "explanation": "Method interleaving tests whether methods behave correctly when executed in diverse sequences, catching bugs caused by unexpected state remnants from prior calls.",
                "difficulty": "medium",
                "sourcePages": [18]
            },
            {
                "id": "oo-010",
                "question": "How does the 'Liskov Substitution Principle (LSP)' relate to testing derived classes?",
                "options": {
                    "A": "If SubClass is an LSP-compliant subtype of BaseClass, any test case written for BaseClass should pass when executed with a SubClass instance without altering correctness.",
                    "B": "Subclasses must have fewer methods than base classes.",
                    "C": "Subclasses cannot throw exceptions.",
                    "D": "Subclasses must be static."
                },
                "correctAnswer": "A",
                "explanation": "LSP states that objects of a superclass should be replaceable with objects of a subclass without affecting program correctness. Re-executing base class tests on subclasses validates LSP conformance.",
                "difficulty": "hard",
                "sourcePages": [19]
            },
            {
                "id": "oo-011",
                "question": "What is an 'equivalent state' in class state-machine testing?",
                "options": {
                    "A": "Two distinct internal state representations that produce identical observable behavior for all subsequent method call sequences.",
                    "B": "Two states with the same integer ID.",
                    "C": "States in two different programs.",
                    "D": "States with the same number of variables."
                },
                "correctAnswer": "A",
                "explanation": "In behavioral testing, two states are equivalent if no sequence of operations can distinguish between them based on observable outputs and return values.",
                "difficulty": "hard",
                "sourcePages": [20]
            },
            {
                "id": "oo-012",
                "question": "What is a 'Sneaking Method' anomaly in OO testing?",
                "options": {
                    "A": "A method that inadvertently modifies instance state that it should have treated as read-only, violating encapsulation or contracts.",
                    "B": "A method that runs in background threads.",
                    "C": "A method with no name.",
                    "D": "A method that is never called."
                },
                "correctAnswer": "A",
                "explanation": "A sneaking method introduces unintended state changes (unwanted side-effects) on variables that are outside its defined functional responsibility.",
                "difficulty": "hard",
                "sourcePages": [21]
            },
            {
                "id": "oo-013",
                "question": "In OO unit testing (such as with JUnit or NUnit), what is the role of the '@BeforeEach' / 'setUp()' fixture method?",
                "options": {
                    "A": "To create a fresh, clean instance of the object under test before each individual test case, ensuring test isolation.",
                    "B": "To compile the test code.",
                    "C": "To print debugging logs to console.",
                    "D": "To delete old test files."
                },
                "correctAnswer": "A",
                "explanation": "Test isolation is critical in OO testing: setUp() reconstructs a pristine object state before every test method executes, preventing test order leakage and shared state contamination.",
                "difficulty": "easy",
                "sourcePages": [22]
            },
            {
                "id": "oo-014",
                "question": "What is a 'Mock Object' in OO testing?",
                "options": {
                    "A": "A simulated collaborator object that verifies expected method invocations, parameter values, and return interactions with the class under test.",
                    "B": "A cartoon drawn by developers.",
                    "C": "An object that throws an error on every line.",
                    "D": "A database backup file."
                },
                "correctAnswer": "A",
                "explanation": "Mocks are test doubles programmed with expectations (which methods should be called, with what arguments) that verify behavioral interactions between components in isolation.",
                "difficulty": "easy",
                "sourcePages": [23]
            },
            {
                "id": "oo-015",
                "question": "What is the difference between a Stub and a Mock in object testing?",
                "options": {
                    "A": "A stub provides pre-canned answers to calls made during the test; a mock verifies that specific method calls and interaction protocols actually occurred.",
                    "B": "Stubs are written in Java; mocks are written in C++.",
                    "C": "Stubs test databases; mocks test web pages.",
                    "D": "There is no difference."
                },
                "correctAnswer": "A",
                "explanation": "Stubs provide canned state/data to the system under test (state verification), while Mocks verify behavioral interactions and call protocols (behavior verification).",
                "difficulty": "medium",
                "sourcePages": [24]
            },
            {
                "id": "oo-016",
                "question": "What problem does Dependency Injection (DI) solve from a testing perspective?",
                "options": {
                    "A": "It decouples classes from hardcoded dependencies, allowing testers to easily inject mock or stub objects for unit testing.",
                    "B": "It accelerates CPU clock rates.",
                    "C": "It eliminates the need for constructors.",
                    "D": "It replaces relational databases."
                },
                "correctAnswer": "A",
                "explanation": "When classes instantiate concrete dependencies directly with 'new', swapping them with test doubles is difficult. Dependency injection allows test frameworks to supply test doubles seamlessly.",
                "difficulty": "medium",
                "sourcePages": [25]
            },
            {
                "id": "oo-017",
                "question": "Why is testing generic / parameterized classes (e.g. 'Stack<T>') challenging?",
                "options": {
                    "A": "Because the class must behave correctly for diverse type parameters (primitive wrappers, custom objects, comparable types, nullable types).",
                    "B": "Because generic classes cannot be compiled.",
                    "C": "Because generics are deleted at compile time in all languages.",
                    "D": "Because generic types cannot be instantiated."
                },
                "correctAnswer": "A",
                "explanation": "Generic components must be verified against heterogeneous type arguments, including types with custom equals/hashCode, edge-case comparison behaviors, and null semantics.",
                "difficulty": "medium",
                "sourcePages": [26]
            },
            {
                "id": "oo-018",
                "question": "What is 'Object Mutation Testing'?",
                "options": {
                    "A": "Applying mutation operators specifically tailored to OO language features, such as changing access modifiers, swapping super/this calls, and modifying overriding relationships.",
                    "B": "Mutating DNA in biology.",
                    "C": "Deleting object constructors.",
                    "D": "Running code on different operating systems."
                },
                "correctAnswer": "A",
                "explanation": "Class-level mutation operators mutate OO constructs: access modifiers (public -> private), super calls, method overrides, and polymorphic references.",
                "difficulty": "medium",
                "sourcePages": [27]
            },
            {
                "id": "oo-019",
                "question": "What is an 'illegal state transition' in class testing?",
                "options": {
                    "A": "Calling a method when the object is in a state that does not permit it (e.g. calling pop() on an EmptyStack), which should trigger a defined exception.",
                    "B": "Moving a computer across state lines.",
                    "C": "Calling a private method.",
                    "D": "Running a test twice."
                },
                "correctAnswer": "A",
                "explanation": "State machines define valid transitions. Invocations in invalid states (like pop() on empty stack) must be verified to fail gracefully with expected exceptions (e.g. UnderflowException).",
                "difficulty": "easy",
                "sourcePages": [13, 14]
            },
            {
                "id": "oo-020",
                "question": "What is 'Round-Trip Path Testing' on an object's state transition diagram?",
                "options": {
                    "A": "Testing sequences of method calls that transition an object out of a state and eventually bring it back to that exact same state.",
                    "B": "Testing tests in reverse order.",
                    "C": "Testing round-off errors in floating-point math.",
                    "D": "Testing network pings."
                },
                "correctAnswer": "A",
                "explanation": "Round-trip testing verifies reversible operations (e.g. insert followed by delete, open followed by close), checking that returning to the original state leaves no residual corruptions.",
                "difficulty": "medium",
                "sourcePages": [28]
            }
        ]
    },
    {
        "topicId": "web-apps-testing",
        "topicName": "Web Applications Testing",
        "sourcePdf": "web-apps-testing.pdf",
        "questions": [
            {
                "id": "wat-001",
                "question": "What are the three primary architectural tiers in modern web applications?",
                "options": {
                    "A": "Client tier (Browser), Business Logic / Application tier (Server), Data tier (Database)",
                    "B": "HTML tier, CSS tier, Font tier",
                    "C": "Input tier, Processing tier, Output tier",
                    "D": "Git tier, Docker tier, Cloud tier"
                },
                "correctAnswer": "A",
                "explanation": "Web applications are organized as multi-tier architectures: Presentation/Client tier (browser/DOM), Business Logic tier (application server/APIs), and Data persistence tier (database).",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "wat-002",
                "question": "Why is client-side form validation alone (using JavaScript or HTML attributes) INSUFFICIENT for web application security and reliability?",
                "options": {
                    "A": "Because client-side validation can be easily bypassed by attackers using tools like curl, Postman, or disabling JavaScript in the browser.",
                    "B": "Because browsers do not support validation.",
                    "C": "Because client-side validation slows down internet connections.",
                    "D": "Because client-side validation only works on Windows."
                },
                "correctAnswer": "A",
                "explanation": "Never trust the client. Any malicious user can bypass browser validation by crafting raw HTTP requests directly to backend endpoints. Server-side validation is strictly mandatory.",
                "difficulty": "easy",
                "sourcePages": [7, 8]
            },
            {
                "id": "wat-003",
                "question": "Because HTTP is fundamentally a stateless protocol, how do web applications maintain user session state across multiple requests?",
                "options": {
                    "A": "Using Session Cookies, Server-side Sessions, URL rewriting, or LocalStorage / Token headers (e.g. JWT).",
                    "B": "By keeping the TCP connection open forever.",
                    "C": "By forcing users to re-login on every click.",
                    "D": "Through DNS server records."
                },
                "correctAnswer": "A",
                "explanation": "HTTP is stateless: each request is independent. Session tracking mechanisms (cookies containing session tokens, authorization headers, URL rewriting) tie requests to a persistent session.",
                "difficulty": "medium",
                "sourcePages": [9, 10]
            },
            {
                "id": "wat-004",
                "question": "What is a Cross-Site Scripting (XSS) vulnerability in web testing?",
                "options": {
                    "A": "An injection attack where malicious client-side JavaScript scripts are injected into web pages viewed by other unsuspecting users.",
                    "B": "When CSS stylesheets do not load.",
                    "C": "When a link points to the wrong URL.",
                    "D": "A database connection timeout."
                },
                "correctAnswer": "A",
                "explanation": "XSS occurs when an application includes untrusted user input without proper HTML sanitization/escaping, allowing attacker scripts to run in victims' browsers and steal session cookies.",
                "difficulty": "medium",
                "sourcePages": [18, 19]
            },
            {
                "id": "wat-005",
                "question": "What is SQL Injection (SQLi) and how is it tested?",
                "options": {
                    "A": "Inserting malicious SQL query fragments into input fields to manipulate backend database queries; tested using payload strings like '' OR '1'='1'.",
                    "B": "Injecting CSS into a web page.",
                    "C": "Testing if SQL server runs on Linux.",
                    "D": "Measuring query response times."
                },
                "correctAnswer": "A",
                "explanation": "SQLi occurs when user input is concatenated directly into SQL statements without parameterized queries or ORM sanitization, allowing attackers to access or destroy data.",
                "difficulty": "easy",
                "sourcePages": [20, 21]
            },
            {
                "id": "wat-006",
                "question": "What is Cross-Site Request Forgery (CSRF)?",
                "options": {
                    "A": "An attack that tricks an authenticated user's browser into transmitting unauthorized commands to a web application where the user is currently authenticated.",
                    "B": "A broken hyperlink.",
                    "C": "A fake CSS stylesheet.",
                    "D": "A server restart."
                },
                "correctAnswer": "A",
                "explanation": "CSRF exploits the browser's automatic inclusion of credentials (cookies) to execute unwanted actions on behalf of the victim; tested by checking for anti-CSRF tokens and SameSite cookies.",
                "difficulty": "medium",
                "sourcePages": [22, 23]
            },
            {
                "id": "wat-007",
                "question": "What is 'Cross-Browser Compatibility Testing'?",
                "options": {
                    "A": "Verifying that a web application renders correctly and functions identically across diverse web browsers (Chrome, Firefox, Safari, Edge) and rendering engines.",
                    "B": "Testing if two browsers can run at the same time.",
                    "C": "Measuring internet download speeds.",
                    "D": "Testing with all browser extensions enabled."
                },
                "correctAnswer": "A",
                "explanation": "Different browsers and layout engines (Blink, Gecko, WebKit) may interpret CSS rules, JavaScript features, and HTML elements differently, requiring compatibility verification.",
                "difficulty": "easy",
                "sourcePages": [12, 13]
            },
            {
                "id": "wat-008",
                "question": "What is the Document Object Model (DOM) in web testing?",
                "options": {
                    "A": "The in-memory hierarchical tree representation of the HTML document structure manipulated by client-side JavaScript.",
                    "B": "A database format.",
                    "C": "A network protocol.",
                    "D": "A software development methodology."
                },
                "correctAnswer": "A",
                "explanation": "The DOM represents the page structure as a tree of objects. Functional testing frameworks (e.g. Selenium, Playwright, Cypress) interact directly with DOM nodes.",
                "difficulty": "easy",
                "sourcePages": [4, 5]
            },
            {
                "id": "wat-009",
                "question": "Why is testing Asynchronous JavaScript and XML (AJAX) / Fetch requests more complex than traditional static page testing?",
                "options": {
                    "A": "Because updates occur dynamically and asynchronously in the background without a full page reload, introducing timing dependencies and race conditions for test assertions.",
                    "B": "Because AJAX requests do not use HTTP.",
                    "C": "Because AJAX only works in Chrome.",
                    "D": "Because XML is deprecated."
                },
                "correctAnswer": "A",
                "explanation": "Asynchronous calls mean elements appear or change state dynamically over time; test scripts must use explicit waits rather than hardcoded sleeps to avoid synchronization flakiness.",
                "difficulty": "medium",
                "sourcePages": [14, 15]
            },
            {
                "id": "wat-010",
                "question": "What is 'Broken Link Testing' on static web sites?",
                "options": {
                    "A": "Crawling all hyperlinks (anchor tags) to verify that none return HTTP 404 (Not Found) or 500 (Server Error) status codes.",
                    "B": "Checking if the keyboard works.",
                    "C": "Testing Wi-Fi connection.",
                    "D": "Testing Bluetooth devices."
                },
                "correctAnswer": "A",
                "explanation": "Hyperlink verification spiders through site URLs to ensure that internal navigation anchors, assets (images, stylesheets), and external links resolve successfully.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "wat-011",
                "question": "In web testing, what does an HTTP 500 status code indicate?",
                "options": {
                    "A": "Internal Server Error: an unhandled exception occurred on the backend server.",
                    "B": "The page was found successfully.",
                    "C": "The user is not authorized.",
                    "D": "The request was cached."
                },
                "correctAnswer": "A",
                "explanation": "HTTP 500 indicates an unexpected condition on the server that prevented it from fulfilling the request, signaling a server-side bug or crash.",
                "difficulty": "easy",
                "sourcePages": [6]
            },
            {
                "id": "wat-012",
                "question": "What is 'Responsive Web Design (RWD) Testing'?",
                "options": {
                    "A": "Testing that the layout, fonts, and controls dynamically adapt gracefully across different viewport widths and screen resolutions (mobile, tablet, desktop).",
                    "B": "Testing how fast the server responds.",
                    "C": "Testing user typing speed.",
                    "D": "Testing email responsiveness."
                },
                "correctAnswer": "A",
                "explanation": "RWD testing checks CSS media queries and fluid grids to ensure visual elements remain legible, interactive, and free from horizontal scrolling across various device widths.",
                "difficulty": "easy",
                "sourcePages": [11]
            },
            {
                "id": "wat-013",
                "question": "What is the 'Page Object Model' (POM) design pattern in automated web testing?",
                "options": {
                    "A": "A pattern that encapsulates web page elements and interactions into dedicated class objects, separating test logic from DOM selector details.",
                    "B": "A pattern that converts web pages into PDF documents.",
                    "C": "A database schema for web pages.",
                    "D": "A tool that writes HTML code."
                },
                "correctAnswer": "A",
                "explanation": "POM enhances test maintenance by modeling pages as classes with methods representing services offered by the page, insulating test cases from changes in HTML markup and selectors.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "wat-014",
                "question": "What is the purpose of testing browser LocalStorage and SessionStorage?",
                "options": {
                    "A": "To verify that client-persisted state, preferences, and offline tokens are accurately saved, retrieved, and cleared upon logout.",
                    "B": "To measure hard drive spin rates.",
                    "C": "To test server disk space.",
                    "D": "To delete browser bookmarks."
                },
                "correctAnswer": "A",
                "explanation": "Web Storage APIs store key-value data on the client. Testing ensures data integrity, quota handling, and that sensitive authentication artifacts are invalidated on logout.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "wat-015",
                "question": "What is 'Session Hijacking' and how is it mitigated and tested?",
                "options": {
                    "A": "An attacker steals a valid session ID to impersonate the user; tested by verifying the use of HttpOnly and Secure cookie flags and HTTPS encryption.",
                    "B": "When a user logs out.",
                    "C": "When a browser tab crashes.",
                    "D": "When the server reboots."
                },
                "correctAnswer": "A",
                "explanation": "HttpOnly cookies prevent JavaScript from accessing session tokens (mitigating XSS theft), and Secure flags ensure cookies are only transmitted over TLS/HTTPS.",
                "difficulty": "medium",
                "sourcePages": [10, 24]
            },
            {
                "id": "wat-016",
                "question": "What is Web Accessibility Testing (WCAG compliance)?",
                "options": {
                    "A": "Evaluating whether a web application is usable by individuals with disabilities, including screen reader support, keyboard navigation, and color contrast.",
                    "B": "Testing if the website is available 24/7.",
                    "C": "Testing internet connection speed.",
                    "D": "Testing website translation to Spanish."
                },
                "correctAnswer": "A",
                "explanation": "WCAG (Web Content Accessibility Guidelines) outlines standards for perceivable, operable, understandable, and robust content, verified via accessibility audits and screen readers.",
                "difficulty": "easy",
                "sourcePages": [17]
            },
            {
                "id": "wat-017",
                "question": "In REST API testing for web backends, what are the standard expectations for idempotency of HTTP methods?",
                "options": {
                    "A": "GET, PUT, and DELETE should be idempotent (multiple identical requests have the same side-effect as one); POST is typically non-idempotent.",
                    "B": "All HTTP methods must be non-idempotent.",
                    "C": "Only POST is idempotent.",
                    "D": "Idempotency only applies to email servers."
                },
                "correctAnswer": "A",
                "explanation": "Idempotent HTTP methods (GET, PUT, DELETE) guarantee that repeating the request multiple times produces the exact same server state as a single invocation.",
                "difficulty": "medium",
                "sourcePages": [25]
            },
            {
                "id": "wat-018",
                "question": "What is 'DOM XSS' (Document Object Model-based Cross-Site Scripting)?",
                "options": {
                    "A": "An XSS vulnerability that executes entirely on the client side when unsafe JavaScript sinks (like innerHTML or eval) consume data from untrusted sources (like location.search).",
                    "B": "An error in the database server.",
                    "C": "A network cable failure.",
                    "D": "An uncompressed image file."
                },
                "correctAnswer": "A",
                "explanation": "In DOM XSS, the malicious payload never touches the backend server; client-side JavaScript reads from an untrusted source (document.location) and writes directly to an unsafe sink (element.innerHTML).",
                "difficulty": "hard",
                "sourcePages": [19]
            },
            {
                "id": "wat-019",
                "question": "What is a 'Content Security Policy' (CSP) header in web security?",
                "options": {
                    "A": "An HTTP header that restricts the domains and resource types (scripts, images, styles) that the browser is permitted to load and execute.",
                    "B": "A copyright statement on the homepage.",
                    "C": "A database access token.",
                    "D": "A CSS stylesheet."
                },
                "correctAnswer": "A",
                "explanation": "CSP is a powerful defense-in-depth header that mitigates XSS and data injection by whitelisting trusted script origins and disabling unauthorized inline scripts.",
                "difficulty": "medium",
                "sourcePages": [24]
            },
            {
                "id": "wat-020",
                "question": "What is headless browser testing?",
                "options": {
                    "A": "Running automated browser tests without rendering a graphical user interface (GUI) on screen, enabling fast execution in CI/CD environments.",
                    "B": "Testing without a keyboard.",
                    "C": "Testing without an internet connection.",
                    "D": "Testing code that has no main method."
                },
                "correctAnswer": "A",
                "explanation": "Headless browsers (e.g. headless Chrome, Puppeteer, Playwright) execute the real browser engine in memory without UI rendering overhead, ideal for automated pipelines.",
                "difficulty": "easy",
                "sourcePages": [16]
            }
        ]
    },
    {
        "topicId": "mobile-apps-testing",
        "topicName": "Mobile Applications Testing",
        "sourcePdf": "mobile-apps-testing.pdf",
        "questions": [
            {
                "id": "mat-001",
                "question": "What is the primary factor driving 'Device Fragmentation' in mobile applications testing?",
                "options": {
                    "A": "The vast multitude of different device hardware configurations, screen sizes, processor architectures, and operating system versions (especially in Android).",
                    "B": "Broken glass screens.",
                    "C": "Different charging cables.",
                    "D": "Too many mobile games."
                },
                "correctAnswer": "A",
                "explanation": "Device fragmentation arises from thousands of distinct hardware models, diverse display resolutions/aspect ratios, hardware sensors, and fragmented OS distributions.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "mat-002",
                "question": "What is 'Interrupt Testing' in mobile application quality assurance?",
                "options": {
                    "A": "Verifying that the application gracefully pauses, handles state, and resumes when interrupted by events such as incoming phone calls, SMS alerts, low battery warnings, or alarm notifications.",
                    "B": "Interrupting the developer while coding.",
                    "C": "Unplugging the battery during compilation.",
                    "D": "Testing keyboard shortcuts."
                },
                "correctAnswer": "A",
                "explanation": "Mobile apps operate in an environment with frequent unexpected system events. Interrupt testing ensures the app saves state when backgrounded and restores seamlessly.",
                "difficulty": "easy",
                "sourcePages": [4, 5]
            },
            {
                "id": "mat-003",
                "question": "What is the fundamental difference between an Emulator, a Simulator, and a Real Physical Device in mobile testing?",
                "options": {
                    "A": "An emulator mimics hardware and software architecture (CPU binary translation); a simulator mimics software behavior/APIs without hardware emulation; a real device provides the actual physical hardware environment.",
                    "B": "Emulators are for iOS only; Simulators are for Android only.",
                    "C": "Simulators are physical phones; Emulators are cloud servers.",
                    "D": "There is no technical difference."
                },
                "correctAnswer": "A",
                "explanation": "Emulators reproduce target device hardware architecture and OS (e.g. Android QEMU). Simulators replicate software environment at API level (e.g. iOS Simulator). Physical devices test real touch, thermal, and sensor behaviors.",
                "difficulty": "medium",
                "sourcePages": [6, 7]
            },
            {
                "id": "mat-004",
                "question": "What is 'Network Variability Testing' for mobile apps?",
                "options": {
                    "A": "Testing app behavior under varying network conditions: switching between Wi-Fi, 4G, 5G, high packet loss, high latency, and offline mode.",
                    "B": "Testing if the Wi-Fi router is plugged in.",
                    "C": "Testing fiber-optic cable durability.",
                    "D": "Measuring server room temperature."
                },
                "correctAnswer": "A",
                "explanation": "Mobile devices constantly change connections. Network variability testing verifies offline caching, connection retries, and graceful degradation during network handoffs.",
                "difficulty": "easy",
                "sourcePages": [8, 9]
            },
            {
                "id": "mat-005",
                "question": "What is 'Battery Drain Testing' (Power Profiling)?",
                "options": {
                    "A": "Measuring the energy consumption of the application to ensure it does not exhaust device battery through excessive background wake-locks, GPS polling, or CPU spinning.",
                    "B": "Draining the battery to 0% to test the charger.",
                    "C": "Testing battery chemical stability.",
                    "D": "Testing screen brightness settings."
                },
                "correctAnswer": "A",
                "explanation": "High battery consumption leads to immediate user uninstalls. Power profiling tools monitor wake-locks, background service frequency, and sensor usage.",
                "difficulty": "easy",
                "sourcePages": [10]
            },
            {
                "id": "mat-006",
                "question": "What is 'App Lifecycle Testing' in mobile OS environments (Android / iOS)?",
                "options": {
                    "A": "Testing that the app correctly transitions between lifecycle states (Created, Started, Resumed, Paused, Stopped, Destroyed) and restores state after process death.",
                    "B": "Testing how many years the app will be published on the App Store.",
                    "C": "Testing the marketing roadmap.",
                    "D": "Testing employee hiring cycles."
                },
                "correctAnswer": "A",
                "explanation": "Mobile OSes aggressively kill background apps to reclaim RAM. Testing lifecycle hooks (onSaveInstanceState, onResume) verifies that user input is not lost when returning to the app.",
                "difficulty": "medium",
                "sourcePages": [11, 12]
            },
            {
                "id": "mat-007",
                "question": "What is 'Screen Orientation Testing'?",
                "options": {
                    "A": "Verifying that rotating the device between portrait and landscape modes preserves view hierarchy, input field data, and user progress without crashing.",
                    "B": "Measuring compass accuracy.",
                    "C": "Checking device tilt angles.",
                    "D": "Testing camera optical zoom."
                },
                "correctAnswer": "A",
                "explanation": "In Android, screen rotation restarts the Activity by default. If state is not properly preserved, rotation causes immediate data loss or NullPointerExceptions.",
                "difficulty": "easy",
                "sourcePages": [13]
            },
            {
                "id": "mat-008",
                "question": "What unique UI interactions must be validated in mobile testing compared to traditional desktop applications?",
                "options": {
                    "A": "Multi-touch gestures such as pinch-to-zoom, swipe, fling, drag-and-drop, tap-and-hold (long press), and edge swipes.",
                    "B": "Mouse double-clicks.",
                    "C": "VGA monitor connections.",
                    "D": "Physical keyboard caps-lock keys."
                },
                "correctAnswer": "A",
                "explanation": "Touch-based interaction requires validating touch targets (minimum 48x48dp accessibility guideline), multi-finger gestures, and gesture responsiveness.",
                "difficulty": "easy",
                "sourcePages": [14]
            },
            {
                "id": "mat-009",
                "question": "What is 'Sensor Interaction Testing' in mobile apps?",
                "options": {
                    "A": "Testing application features that rely on hardware sensors such as Accelerometer, Gyroscope, GPS/Location, Ambient Light, Barometer, and Biometrics (Fingerprint/FaceID).",
                    "B": "Testing smoke detectors in the building.",
                    "C": "Testing server heat sensors.",
                    "D": "Testing water temperature."
                },
                "correctAnswer": "A",
                "explanation": "Mobile apps leverage rich onboard sensors; tests must inject mock sensor data (simulated GPS coordinates, shake events, biometric tokens) to verify features.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "mat-010",
                "question": "What is 'App Permission Testing'?",
                "options": {
                    "A": "Verifying that the application functions appropriately when runtime permissions (camera, microphone, contacts, location) are granted, denied, or revoked by the user.",
                    "B": "Checking if the developer has a developer license.",
                    "C": "Testing copyright law compliance.",
                    "D": "Testing App Store pricing permissions."
                },
                "correctAnswer": "A",
                "explanation": "Modern OSes require dynamic runtime permissions. Tests must confirm that denying a permission displays an informative rationale rather than crashing the app.",
                "difficulty": "medium",
                "sourcePages": [16]
            },
            {
                "id": "mat-011",
                "question": "What is a 'Mobile Device Cloud' in automated test execution?",
                "options": {
                    "A": "A cloud infrastructure service (e.g. Firebase Test Lab, BrowserStack, Sauce Labs) that provides remote access to hundreds of real mobile devices for automated parallel testing.",
                    "B": "A weather cloud containing smartphones.",
                    "C": "A mobile storage backup like iCloud.",
                    "D": "A database on a smartphone."
                },
                "correctAnswer": "A",
                "explanation": "Device clouds host real physical devices in data centers, enabling QA teams to run test scripts in parallel across dozens of device/OS combinations without purchasing them locally.",
                "difficulty": "easy",
                "sourcePages": [17]
            },
            {
                "id": "mat-012",
                "question": "What is 'Monkey Testing' (or UI Exerciser Monkey) on Android?",
                "options": {
                    "A": "A tool that sends pseudo-random streams of user events (clicks, touches, gestures, system events) into the device to stress-test stability and find crash bugs.",
                    "B": "Testing mobile games about animals.",
                    "C": "Testing user interface colors.",
                    "D": "Testing Bluetooth accessories."
                },
                "correctAnswer": "A",
                "explanation": "The Android Monkey tool generates rapid, randomized input events to stress the application and uncover memory leaks, race conditions, and unhandled exceptions.",
                "difficulty": "medium",
                "sourcePages": [18]
            },
            {
                "id": "mat-013",
                "question": "What is 'App Upgrade Testing'?",
                "options": {
                    "A": "Verifying that updating an older version of the app to a new version preserves user databases (e.g. SQLite/Room migrations), shared preferences, and cached state seamlessly.",
                    "B": "Buying a newer phone model.",
                    "C": "Upgrading the operating system compiler.",
                    "D": "Testing in-app purchase payments."
                },
                "correctAnswer": "A",
                "explanation": "Upgrade testing ensures that database schema migrations execute smoothly and user data/settings are not corrupted or wiped when an app update is installed.",
                "difficulty": "medium",
                "sourcePages": [19]
            },
            {
                "id": "mat-014",
                "question": "What is 'Memory Leak / Out of Memory (OOM) Testing' in mobile apps?",
                "options": {
                    "A": "Monitoring heap memory usage across repeated screen navigations to detect leaked Activity contexts or unreleased Bitmaps that cause the OS to kill the app with OutOfMemoryError.",
                    "B": "Removing the micro-SD card.",
                    "C": "Testing flash storage write cycles.",
                    "D": "Testing device RAM clock speed."
                },
                "correctAnswer": "A",
                "explanation": "Retaining references to destroyed Activities (e.g. via static listeners or background tasks) leaks substantial memory, eventually triggering OOM crashes.",
                "difficulty": "medium",
                "sourcePages": [12, 19]
            },
            {
                "id": "mat-015",
                "question": "Why is 'Cold Start' vs 'Warm Start' performance testing important for mobile apps?",
                "options": {
                    "A": "Cold start launches the app from scratch without prior process state, while warm start resumes from memory; slow cold start times lead to high user abandonment.",
                    "B": "Cold start is testing in winter.",
                    "C": "Warm start is testing in summer.",
                    "D": "It measures battery temperature."
                },
                "correctAnswer": "A",
                "explanation": "App launch latency directly impacts user perception. App stores track cold start metrics (time to initial display), penalizing apps that take longer than 2-3 seconds.",
                "difficulty": "easy",
                "sourcePages": [10, 20]
            },
            {
                "id": "mat-016",
                "question": "What is 'Localization / Internationalization (i18n / L10n) Testing' in mobile apps?",
                "options": {
                    "A": "Verifying that translated text strings fit within UI buttons without text clipping, and date, currency, and right-to-left (RTL) layouts render correctly.",
                    "B": "Testing GPS coordinates in Paris.",
                    "C": "Testing airplane mode.",
                    "D": "Measuring download size in different countries."
                },
                "correctAnswer": "A",
                "explanation": "Translated words often vary in length (e.g. German text is often 30% longer than English), causing UI truncation. L10n testing validates formatting, text fit, and RTL layout.",
                "difficulty": "medium",
                "sourcePages": [14]
            },
            {
                "id": "mat-017",
                "question": "In cross-platform mobile frameworks (such as Flutter or React Native), what additional testing layer is essential?",
                "options": {
                    "A": "Testing the JavaScript/native bridge or platform channel communication between framework code and underlying platform APIs.",
                    "B": "Testing only on Android.",
                    "C": "Testing with web browsers only.",
                    "D": "Deleting platform native libraries."
                },
                "correctAnswer": "A",
                "explanation": "Cross-platform frameworks bridge shared logic to native UI and platform services. Testing must verify that serialization and communication across the bridge work smoothly.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "mat-018",
                "question": "What is 'Push Notification Testing' in mobile applications?",
                "options": {
                    "A": "Testing that push notification payloads are properly received, displayed in the notification tray, and tapping them routes the user directly to the correct deep link screen.",
                    "B": "Testing physical phone buttons.",
                    "C": "Testing user email delivery.",
                    "D": "Testing push-to-talk walkie-talkies."
                },
                "correctAnswer": "A",
                "explanation": "Notifications involve cloud messaging (FCM/APNs), background handlers, payload parsing, and deep-linking into specific app activities when tapped.",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "mat-019",
                "question": "What is 'Low Storage Testing' on mobile devices?",
                "options": {
                    "A": "Verifying that the application handles device storage exhaustion gracefully without crashing or corrupting local databases.",
                    "B": "Testing devices with 1 GB storage.",
                    "C": "Deleting user photos.",
                    "D": "Measuring micro-SD card read speed."
                },
                "correctAnswer": "A",
                "explanation": "When device storage is almost full, file write and database transaction operations fail. Testing ensures the app informs the user rather than failing abruptly.",
                "difficulty": "medium",
                "sourcePages": [15]
            },
            {
                "id": "mat-020",
                "question": "Which of the following automated testing frameworks is standard for cross-platform mobile UI automation?",
                "options": {
                    "A": "Appium",
                    "B": "JUnit 3",
                    "C": "Valgrind",
                    "D": "GCC"
                },
                "correctAnswer": "A",
                "explanation": "Appium is an open-source, cross-platform mobile automation framework that uses the WebDriver protocol to automate Android and iOS applications natively.",
                "difficulty": "easy",
                "sourcePages": [17]
            }
        ]
    },
    {
        "topicId": "non-functional-testing",
        "topicName": "Non-Functional Testing (Performance & Security)",
        "sourcePdf": "non-functional-testing.pdf",
        "questions": [
            {
                "id": "nft-001",
                "question": "What is the primary difference between Functional Testing and Non-Functional Testing?",
                "options": {
                    "A": "Functional testing verifies WHAT the system does (behavior/features); Non-functional testing verifies HOW WELL the system performs (speed, scalability, security, reliability).",
                    "B": "Functional testing is automated; non-functional is manual.",
                    "C": "Functional testing tests hardware; non-functional tests software.",
                    "D": "Non-functional testing is optional in safety-critical systems."
                },
                "correctAnswer": "A",
                "explanation": "Functional testing checks feature correctness against requirements. Non-functional testing evaluates operational quality attributes like response time, throughput, security, and resource efficiency.",
                "difficulty": "easy",
                "sourcePages": [2, 3]
            },
            {
                "id": "nft-002",
                "question": "What is 'Load Testing' in performance engineering?",
                "options": {
                    "A": "Evaluating system performance, response time, and throughput under anticipated normal and peak user workloads over a period of time.",
                    "B": "Testing system behavior beyond maximum design capacity until it breaks.",
                    "C": "Testing shipping weight of servers.",
                    "D": "Testing with zero users."
                },
                "correctAnswer": "A",
                "explanation": "Load testing verifies that the system meets Service Level Agreements (SLAs) under expected concurrent user traffic and transaction volumes.",
                "difficulty": "easy",
                "sourcePages": [4, 5]
            },
            {
                "id": "nft-003",
                "question": "What is 'Stress Testing'?",
                "options": {
                    "A": "Subjecting the system to workloads beyond its design limits to determine its breaking point, stability thresholds, and how gracefully it recovers from failure.",
                    "B": "Testing stressed software engineers.",
                    "C": "Running unit tests once.",
                    "D": "Testing cooling fans."
                },
                "correctAnswer": "A",
                "explanation": "Stress testing pushes system demand beyond maximum capacity (CPU, memory, connection pools) to test graceful degradation, fault isolation, and self-recovery.",
                "difficulty": "easy",
                "sourcePages": [5]
            },
            {
                "id": "nft-004",
                "question": "What is 'Spike Testing'?",
                "options": {
                    "A": "Testing system stability and recovery by subjecting it to sudden, dramatic surges in user load followed by immediate drops back to normal levels.",
                    "B": "Testing electrical voltage spikes.",
                    "C": "Testing graph data flow.",
                    "D": "Testing with high CPU overclocking."
                },
                "correctAnswer": "A",
                "explanation": "Spike testing evaluates whether systems can absorb abrupt, flash traffic surges (e.g. ticket sales launch, breaking news alerts) without crashing and recover cleanly.",
                "difficulty": "medium",
                "sourcePages": [6]
            },
            {
                "id": "nft-005",
                "question": "What is 'Endurance / Soak Testing'?",
                "options": {
                    "A": "Running a sustained, realistic workload over an extended duration (hours or days) to detect slow memory leaks, resource exhaustion, or performance degradation over time.",
                    "B": "Testing underwater hardware.",
                    "C": "Testing battery charging speed.",
                    "D": "Testing compile times."
                },
                "correctAnswer": "A",
                "explanation": "Soak testing reveals issues that emerge only over long runtimes, such as memory leaks, database connection pool exhaustion, log file overflows, and OS handle leaks.",
                "difficulty": "medium",
                "sourcePages": [6]
            },
            {
                "id": "nft-006",
                "question": "In performance testing, what is the difference between 'Response Time' and 'Latency'?",
                "options": {
                    "A": "Latency is the transit delay for a request to reach the server; Response Time is the total elapsed time from sending the request until receiving the complete response (including server processing).",
                    "B": "Response time is network transit only; latency includes database processing.",
                    "C": "They are identical mathematical terms.",
                    "D": "Latency is measured in hours; response time in seconds."
                },
                "correctAnswer": "A",
                "explanation": "Latency measures transmission delay across the network pipeline. Response Time = Network Latency + Server Processing Time + Response Transfer Time.",
                "difficulty": "medium",
                "sourcePages": [7]
            },
            {
                "id": "nft-007",
                "question": "What does 'Throughput' measure in performance testing?",
                "options": {
                    "A": "The rate of successful transactions or requests processed by the system per unit of time (e.g. Transactions Per Second - TPS).",
                    "B": "The weight of the server in kilograms.",
                    "C": "The percentage of memory used.",
                    "D": "The number of lines of code compiled."
                },
                "correctAnswer": "A",
                "explanation": "Throughput quantifies processing capacity, typically expressed as Requests Per Second (RPS) or Transactions Per Second (TPS).",
                "difficulty": "easy",
                "sourcePages": [7]
            },
            {
                "id": "nft-008",
                "question": "What are the three pillars of information security in the classic CIA Triad?",
                "options": {
                    "A": "Confidentiality, Integrity, Availability",
                    "B": "Complexity, Inheritance, Abstraction",
                    "C": "Coverage, Infection, Assertion",
                    "D": "Centralized, Integrated, Automated"
                },
                "correctAnswer": "A",
                "explanation": "The CIA Triad constitutes the foundational model of information security: Confidentiality (data secrecy), Integrity (data accuracy/tamper-resistance), and Availability (system accessibility).",
                "difficulty": "easy",
                "sourcePages": [10, 11]
            },
            {
                "id": "nft-009",
                "question": "What is the difference between Authentication and Authorization in security testing?",
                "options": {
                    "A": "Authentication verifies identity (WHO you are); Authorization verifies access permissions (WHAT resources you are permitted to access).",
                    "B": "Authentication is for passwords; authorization is for usernames.",
                    "C": "They are synonymous in security engineering.",
                    "D": "Authorization occurs before authentication."
                },
                "correctAnswer": "A",
                "explanation": "Authentication checks credentials (e.g. password, MFA). Authorization determines whether that authenticated principal possesses privileges to execute the requested action.",
                "difficulty": "easy",
                "sourcePages": [12]
            },
            {
                "id": "nft-010",
                "question": "What is 'Penetration Testing' (Pen Testing)?",
                "options": {
                    "A": "An authorized simulated cyberattack against a software system to evaluate security vulnerabilities and exploit pathways before real adversaries do.",
                    "B": "Physical drill testing of server racks.",
                    "C": "Running unit tests with 100 threads.",
                    "D": "Checking network cable connections."
                },
                "correctAnswer": "A",
                "explanation": "Penetration testing employs ethical hacking techniques to actively discover and exploit vulnerabilities across network, application, and infrastructure layers.",
                "difficulty": "easy",
                "sourcePages": [13, 14]
            },
            {
                "id": "nft-011",
                "question": "What is a 'Denial of Service (DoS)' vulnerability in security testing?",
                "options": {
                    "A": "A flaw that allows an attacker to exhaust system resources (CPU, memory, network, threads), rendering the service unavailable to legitimate users.",
                    "B": "A password reset request.",
                    "C": "A database backup failure.",
                    "D": "An incorrect email address."
                },
                "correctAnswer": "A",
                "explanation": "DoS attacks overwhelm system capacities or exploit algorithmic complexity flaws (e.g. ReDoS in regex) to starve legitimate users of system availability.",
                "difficulty": "easy",
                "sourcePages": [15]
            },
            {
                "id": "nft-012",
                "question": "What is 'Scalability Testing'?",
                "options": {
                    "A": "Testing how well the software scales up (adding more CPU/RAM to a server) or scales out (adding more server nodes) to handle growing traffic gracefully.",
                    "B": "Scaling images to fit screen size.",
                    "C": "Measuring the physical dimensions of computer monitors.",
                    "D": "Testing with small fonts."
                },
                "correctAnswer": "A",
                "explanation": "Scalability testing measures whether system throughput increases proportionally when hardware resources (vertical or horizontal scaling) are added.",
                "difficulty": "medium",
                "sourcePages": [8]
            },
            {
                "id": "nft-013",
                "question": "What is a 'Performance Bottleneck'?",
                "options": {
                    "A": "A critical component, resource, or code section (e.g. unindexed database query, lock contention) that restricts the overall capacity and slows down the entire system.",
                    "B": "The shape of a network cable.",
                    "C": "A compiler error.",
                    "D": "A software license restriction."
                },
                "correctAnswer": "A",
                "explanation": "A bottleneck is the narrowest point in an execution pipeline that limits total throughput, regardless of how powerful other components in the system are.",
                "difficulty": "easy",
                "sourcePages": [8, 9]
            },
            {
                "id": "nft-014",
                "question": "What is 'Usability Testing' in non-functional testing?",
                "options": {
                    "A": "Evaluating how intuitive, learnable, and user-friendly the software is for its target audience to accomplish their goals effectively and satisfactorily.",
                    "B": "Testing if the software can be turned on.",
                    "C": "Testing with robots.",
                    "D": "Measuring server power usage."
                },
                "correctAnswer": "A",
                "explanation": "Usability testing measures user satisfaction, error rates during common tasks, navigation clarity, and the ease with which users learn the interface.",
                "difficulty": "easy",
                "sourcePages": [16]
            },
            {
                "id": "nft-015",
                "question": "What is 'Interoperability Testing'?",
                "options": {
                    "A": "Verifying that two or more distinct software systems, protocols, or hardware platforms can successfully exchange information and use the information exchanged.",
                    "B": "Testing within a single method.",
                    "C": "Testing code that has no inputs.",
                    "D": "Testing compiler speed."
                },
                "correctAnswer": "A",
                "explanation": "Interoperability testing confirms compliance with open industry standards and protocols, ensuring independent heterogeneous systems communicate seamlessly.",
                "difficulty": "medium",
                "sourcePages": [17]
            },
            {
                "id": "nft-016",
                "question": "What is 'Reliability / Availability Testing' (Mean Time Between Failures - MTBF)?",
                "options": {
                    "A": "Testing the probability that the software will execute without operational failures for a specified period in a specified environment.",
                    "B": "Testing if developers are available on call.",
                    "C": "Testing only on Mondays.",
                    "D": "Counting total lines of code."
                },
                "correctAnswer": "A",
                "explanation": "Reliability engineering measures operational stability, tracking metrics like MTBF (Mean Time Between Failures) and MTTR (Mean Time To Recovery).",
                "difficulty": "medium",
                "sourcePages": [18]
            },
            {
                "id": "nft-017",
                "question": "What is 'Maintainability Testing'?",
                "options": {
                    "A": "Assessing how easily software can be modified, debugged, modularized, and updated in response to defects or changing requirements.",
                    "B": "Cleaning computer fans.",
                    "C": "Testing server backup generators.",
                    "D": "Buying software warranties."
                },
                "correctAnswer": "A",
                "explanation": "Maintainability evaluates code modularity, documentation completeness, adherence to coding standards, and cyclomatic complexity to gauge long-term engineering cost.",
                "difficulty": "easy",
                "sourcePages": [19]
            },
            {
                "id": "nft-018",
                "question": "What tool is widely used for enterprise load and performance testing?",
                "options": {
                    "A": "Apache JMeter / k6 / Locust",
                    "B": "Microsoft Paint",
                    "C": "GDB debugger",
                    "D": "Notepad++"
                },
                "correctAnswer": "A",
                "explanation": "Apache JMeter, k6, and Locust are standard open-source tools designed to generate massive virtual user concurrent loads against web applications and APIs.",
                "difficulty": "easy",
                "sourcePages": [9]
            },
            {
                "id": "nft-019",
                "question": "In security testing, what is 'Vulnerability Scanning'?",
                "options": {
                    "A": "Using automated scanners (e.g. OWASP ZAP, Nessus, Snyk) to inspect systems for known CVE vulnerabilities, misconfigurations, and outdated libraries.",
                    "B": "Manually reviewing all code line-by-line.",
                    "C": "Scanning printed documents with OCR.",
                    "D": "Checking hard drive bad sectors."
                },
                "correctAnswer": "A",
                "explanation": "Automated vulnerability scanning compares system signatures, open ports, HTTP headers, and dependency manifests against public vulnerability databases.",
                "difficulty": "easy",
                "sourcePages": [14]
            },
            {
                "id": "nft-020",
                "question": "Why must performance testing be executed in a dedicated staging environment that mirrors production architecture?",
                "options": {
                    "A": "Because tests on developer laptops do not reflect real-world network latencies, database sizes, clustering, load balancers, or server hardware capacities.",
                    "B": "Because production environments are deleted after testing.",
                    "C": "Because performance tests cannot run on Linux.",
                    "D": "Because staging environments run at double speed."
                },
                "correctAnswer": "A",
                "explanation": "Valid performance metrics require architectural parity with production (similar CPU, RAM, network bandwidth, database volume, and topology) to yield realistic benchmarks.",
                "difficulty": "medium",
                "sourcePages": [9, 20]
            }
        ]
    },
    {
        "topicId": "exer-student",
        "topicName": "Comprehensive Testing Exercises & Case Studies",
        "sourcePdf": "exer-student.pdf",
        "questions": [
            {
                "id": "exer-001",
                "question": "In a Control Flow Graph with nodes N = {1, 2, 3, 4, 5, 6} and edges E = {(1, 2), (2, 3), (2, 4), (3, 5), (4, 5), (5, 2), (5, 6)}, what is the Cyclomatic Complexity V(G)?",
                "options": {
                    "A": "V(G) = 7 - 6 + 2 = 3",
                    "B": "V(G) = 6 - 7 + 2 = 1",
                    "C": "V(G) = 7 + 6 - 2 = 11",
                    "D": "V(G) = 4"
                },
                "correctAnswer": "A",
                "explanation": "Using McCabe's formula V(G) = |E| - |N| + 2P with P=1: V(G) = 7 - 6 + 2 = 3.",
                "difficulty": "easy",
                "sourcePages": [15, 16]
            },
            {
                "id": "exer-002",
                "question": "For a function with 3 input characteristics: C1 with 3 blocks, C2 with 2 blocks, and C3 with 4 blocks. If Base Choice Coverage (BCC) is used, how many tests are generated?",
                "options": {
                    "A": "1 + (3 - 1) + (2 - 1) + (4 - 1) = 1 + 2 + 1 + 3 = 7 tests",
                    "B": "24 tests",
                    "C": "9 tests",
                    "D": "8 tests"
                },
                "correctAnswer": "A",
                "explanation": "Formula for BCC: 1 + ∑ (|Bi| - 1) = 1 + (3 - 1) + (2 - 1) + (4 - 1) = 1 + 2 + 1 + 3 = 7 tests.",
                "difficulty": "easy",
                "sourcePages": [25]
            },
            {
                "id": "exer-003",
                "question": "For the same function (C1: 3, C2: 2, C3: 4), how many tests are required for All Combinations Coverage (ACoC)?",
                "options": {
                    "A": "3 × 2 × 4 = 24 tests",
                    "B": "7 tests",
                    "C": "9 tests",
                    "D": "12 tests"
                },
                "correctAnswer": "A",
                "explanation": "All Combinations Coverage computes the full Cartesian product: 3 × 2 × 4 = 24 tests.",
                "difficulty": "easy",
                "sourcePages": [25]
            },
            {
                "id": "exer-004",
                "question": "In a graph with nodes {1, 2, 3} and edges {(1, 2), (2, 3), (3, 1), (3, 2)}, what is the path [2, 3, 2]?",
                "options": {
                    "A": "A simple cycle and a prime path of length 2.",
                    "B": "A path of length 3.",
                    "C": "Not a simple path.",
                    "D": "A test path from initial to final node."
                },
                "correctAnswer": "A",
                "explanation": "The path [2, 3, 2] visits edge (2, 3) and edge (3, 2), starting and ending at node 2 without repeating internal nodes. It is a simple cycle and a prime path of length 2.",
                "difficulty": "medium",
                "sourcePages": [32, 33]
            },
            {
                "id": "exer-005",
                "question": "Consider predicate p = a ∧ (b ∨ c). Which test pair satisfies Restricted Active Clause Coverage (RACC) for major clause 'a'?",
                "options": {
                    "A": "(a=T, b=T, c=F) and (a=F, b=T, c=F)",
                    "B": "(a=T, b=T, c=F) and (a=F, b=F, c=T)",
                    "C": "(a=T, b=F, c=F) and (a=F, b=F, c=F)",
                    "D": "(a=T, b=T, c=T) and (a=F, b=F, c=F)"
                },
                "correctAnswer": "A",
                "explanation": "For major clause 'a', pa = b ∨ c. We must choose minor clauses making (b ∨ c) TRUE (e.g. b=T, c=F). RACC mandates that minor clauses stay identical in both tests: (T, T, F) gives p=T; (F, T, F) gives p=F.",
                "difficulty": "hard",
                "sourcePages": [48, 49]
            },
            {
                "id": "exer-006",
                "question": "If test suite TS executed 120 mutants and strongly killed 90 mutants, and 15 mutants were identified as equivalent mutants, what is the Mutation Score?",
                "options": {
                    "A": "90 / (120 - 15) = 90 / 105 ≈ 85.71%",
                    "B": "90 / 120 = 75.00%",
                    "C": "75 / 105 ≈ 71.43%",
                    "D": "100%"
                },
                "correctAnswer": "A",
                "explanation": "Mutation Score = K / (M - E) = 90 / (120 - 15) = 90 / 105 ≈ 85.71%.",
                "difficulty": "medium",
                "sourcePages": [65]
            },
            {
                "id": "exer-007",
                "question": "Given test suite T = {T1, T2, T3, T4} and 3 faults detected at test positions: Fault 1 at T1, Fault 2 at T3, Fault 3 at T4. What is the APFD value?",
                "options": {
                    "A": "APFD = 1 - (1 + 3 + 4) / (4 × 3) + 1 / (2 × 4) = 1 - 8/12 + 1/8 = 1 - 0.667 + 0.125 = 0.458 (45.8%)",
                    "B": "0.750 (75.0%)",
                    "C": "0.850 (85.0%)",
                    "D": "0.500 (50.0%)"
                },
                "correctAnswer": "A",
                "explanation": "APFD = 1 - (TF1 + TF2 + TF3) / (n × m) + 1 / (2n) = 1 - (1 + 3 + 4) / 12 + 1 / 8 = 1 - 2/3 + 1/8 = 1/3 + 1/8 = 11/24 ≈ 0.458 (45.83%).",
                "difficulty": "hard",
                "sourcePages": [82]
            },
            {
                "id": "exer-008",
                "question": "In a bounded stack program with capacity 3, which sequence of operations exercises an Exceptional / Error State transition?",
                "options": {
                    "A": "push(1); push(2); push(3); push(4); // attempting push when full",
                    "B": "push(1); pop();",
                    "C": "push(1); push(2); pop();",
                    "D": "push(1); top();"
                },
                "correctAnswer": "A",
                "explanation": "The stack has capacity 3. Pushing a 4th item attempts to transition past full capacity, testing the StackOverflow exception boundary.",
                "difficulty": "easy",
                "sourcePages": [90]
            },
            {
                "id": "exer-009",
                "question": "What is the du-path for variable 'sum' in: '1: sum = 0; 2: i = 1; 3: while (i <= N) { 4: sum = sum + a[i]; 5: i++; } 6: return sum;' from statement 1 to statement 6?",
                "options": {
                    "A": "[1, 2, 3, 6] (taking loop zero times, when N = 0)",
                    "B": "[1, 2, 3, 4, 5, 3, 6]",
                    "C": "[1, 4, 6]",
                    "D": "There is no def-clear path."
                },
                "correctAnswer": "A",
                "explanation": "If the loop executes 1 or more times, statement 4 redefines sum, killing def 1. The only def-clear path from def at 1 to use at 6 is when the loop condition at 3 is false immediately (N=0): [1, 2, 3, 6].",
                "difficulty": "hard",
                "sourcePages": [38, 39]
            },
            {
                "id": "exer-010",
                "question": "For a binary search method, which input represents an essential boundary test case for Input Space Partitioning?",
                "options": {
                    "A": "Empty array (size 0), single-element array with target present, single-element array with target absent, target at first index, target at last index.",
                    "B": "An array of 1,000,000 random strings.",
                    "C": "Running binary search on a linked list.",
                    "D": "Passing null function pointers."
                },
                "correctAnswer": "A",
                "explanation": "Standard boundary test cases for search probe: empty collection, singleton matching, singleton non-matching, extreme ends of range (first and last elements), and target not present.",
                "difficulty": "easy",
                "sourcePages": [22, 23]
            },
            {
                "id": "exer-011",
                "question": "Consider graph with edges (1, 2), (2, 3), (3, 2), (2, 4). Does test path [1, 2, 3, 2, 4] tour prime path [2, 3, 2] directly?",
                "options": {
                    "A": "Yes, [2, 3, 2] is a contiguous subpath of [1, 2, 3, 2, 4].",
                    "B": "No, it tours it with sidetrips.",
                    "C": "No, because node 1 is at the beginning.",
                    "D": "Only if node 4 is omitted."
                },
                "correctAnswer": "A",
                "explanation": "[2, 3, 2] appears directly as contiguous subpath in [1, 2, 3, 2, 4]. Therefore, the test path tours [2, 3, 2] directly without sidetrips.",
                "difficulty": "medium",
                "sourcePages": [34]
            },
            {
                "id": "exer-012",
                "question": "In logic coverage, if predicate p = (A ∨ B) ∧ (C ∨ D), how many clauses are in predicate p?",
                "options": {
                    "A": "4 clauses: A, B, C, D",
                    "B": "2 clauses",
                    "C": "1 clause",
                    "D": "8 clauses"
                },
                "correctAnswer": "A",
                "explanation": "There are 4 distinct atomic clauses: A, B, C, and D, connected by OR and AND operators.",
                "difficulty": "easy",
                "sourcePages": [50]
            },
            {
                "id": "exer-013",
                "question": "For the same predicate p = (A ∨ B) ∧ (C ∨ D), how many test cases are required for Combinatorial Coverage (CoC)?",
                "options": {
                    "A": "2^4 = 16 tests",
                    "B": "8 tests",
                    "C": "4 tests",
                    "D": "5 tests"
                },
                "correctAnswer": "A",
                "explanation": "Combinatorial Coverage tests all 2^N combinations of clause truth values. For 4 clauses: 2^4 = 16 tests.",
                "difficulty": "easy",
                "sourcePages": [50]
            },
            {
                "id": "exer-014",
                "question": "If original statement is 'if (count < MAX)' and a mutant replaces it with 'if (count <= MAX)', what input test value is uniquely required to strongly kill this mutant?",
                "options": {
                    "A": "count = MAX",
                    "B": "count = 0",
                    "C": "count = MAX - 1",
                    "D": "count = MAX + 1"
                },
                "correctAnswer": "A",
                "explanation": "When count < MAX, both evaluate to True. When count > MAX, both evaluate to False. Only at the exact boundary count == MAX does original evaluate to False while mutant evaluates to True.",
                "difficulty": "medium",
                "sourcePages": [68]
            },
            {
                "id": "exer-015",
                "question": "What is the relationship between Edge Coverage (EC) and Branch Coverage in standard source code testing?",
                "options": {
                    "A": "They are conceptually identical: executing every edge in a CFG guarantees executing every decision branch outcome.",
                    "B": "Branch coverage requires twice as many tests as edge coverage.",
                    "C": "Edge coverage applies only to hardware.",
                    "D": "Branch coverage does not cover if statements."
                },
                "correctAnswer": "A",
                "explanation": "In CFG representation of source code, edges departing from decision nodes represent conditional branches. Hence, 100% Edge Coverage is isomorphic to 100% Branch Coverage.",
                "difficulty": "easy",
                "sourcePages": [18]
            },
            {
                "id": "exer-016",
                "question": "In data flow testing, if variable 'total' has 2 definitions (node 1, node 4) and 3 reachable uses (node 3, node 5, node 6), what is the maximum number of du-pairs for 'total'?",
                "options": {
                    "A": "2 × 3 = 6 du-pairs (assuming def-clear paths exist for each combination)",
                    "B": "5 du-pairs",
                    "C": "2 du-pairs",
                    "D": "3 du-pairs"
                },
                "correctAnswer": "A",
                "explanation": "Each definition can potentially pair with each reachable use. With 2 defs and 3 uses, at most 2 × 3 = 6 du-pairs can be formed.",
                "difficulty": "medium",
                "sourcePages": [41]
            },
            {
                "id": "exer-017",
                "question": "Suppose a test suite achieves 100% Node Coverage on a CFG with an 'if (flag) { x = 1; }' without an else-block. Does this test suite necessarily achieve 100% Edge Coverage?",
                "options": {
                    "A": "No! A single test with flag=True visits all nodes (satisfying Node Coverage), but the False edge bypassing the if-block was never executed.",
                    "B": "Yes, Node Coverage always subsumes Edge Coverage.",
                    "C": "Yes, if the language is Java.",
                    "D": "Only when flag is boolean."
                },
                "correctAnswer": "A",
                "explanation": "This classic example demonstrates why Edge Coverage is strictly stronger than Node Coverage: the empty false branch edge is missed if only the true branch is tested.",
                "difficulty": "medium",
                "sourcePages": [19]
            },
            {
                "id": "exer-018",
                "question": "In a state machine for an online store order with states {Cart, Placed, Shipped, Delivered, Cancelled}, how many transitions are covered if a test path is [Cart, Placed, Shipped, Delivered]?",
                "options": {
                    "A": "3 transitions: (Cart→Placed), (Placed→Shipped), (Shipped→Delivered)",
                    "B": "4 transitions",
                    "C": "5 transitions",
                    "D": "1 transition"
                },
                "correctAnswer": "A",
                "explanation": "The path consists of 4 states and traverses 3 directed transitions between them.",
                "difficulty": "easy",
                "sourcePages": [58]
            },
            {
                "id": "exer-019",
                "question": "What is the primary objective of case study exercises in the NPTEL software testing course?",
                "options": {
                    "A": "To synthesize and apply multiple theoretical criteria (ISP, Graph Coverage, Logic Coverage, Mutation) to real-world software components and evaluate tradeoffs.",
                    "B": "To teach students how to write HTML.",
                    "C": "To replace software engineers with AI.",
                    "D": "To memorize compiler error codes."
                },
                "correctAnswer": "A",
                "explanation": "Case study exercises bridge theory and practice, developing skills to construct graphs, evaluate logic formulas, partition input spaces, and optimize test suites on practical programs.",
                "difficulty": "easy",
                "sourcePages": [2, 100]
            },
            {
                "id": "exer-020",
                "question": "Why is systematic coverage-based testing superior to purely ad-hoc / random testing?",
                "options": {
                    "A": "It provides measurable, objective stopping criteria, exposes boundary corner cases methodically, and ensures all structural and logical pathways are verified.",
                    "B": "It produces zero test cases.",
                    "C": "It is faster than compiling code.",
                    "D": "It eliminates the need for test execution."
                },
                "correctAnswer": "A",
                "explanation": "Coverage-driven engineering replaces guesswork with formal mathematical criteria (graphs, logic, partitions), ensuring systematic defect detection and quantifiable quality benchmarks.",
                "difficulty": "easy",
                "sourcePages": [105, 110]
            }
        ]
    }
]
