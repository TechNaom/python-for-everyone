/*
  Single source of truth for the course's chapter roster, used by
  assets/sidebar.js to render the persistent left-hand navigation, and by
  docs/curriculum/index.html conceptually (kept in sync by hand there).

  `path` is the file path from the repo root to that chapter's lesson.html.
  Leave `path: null` for chapters that haven't been built yet — the
  sidebar renders those as plain, non-clickable "coming soon" text.

  `subtopics`, when present, is the list of that chapter's lesson.html
  sub-sections — `{ id, title }`, where `id` matches the anchor id on that
  section's <h2> (or its wrapping <div class="subtopic">) in lesson.html.
  The sidebar renders these nested under the chapter link as `#id` anchors.
  Leave it off (or empty) for chapters without a `path` yet.
*/

window.PFE_MODULES = [
  {
    title: "Module 1 — Foundations",
    examPath: "assessments/written-exams/module-1-exam.md",
    chapters: [
      { id: "chapter-01", num: 1, title: "Your First Python Program", path: "chapters/chapter-01-first-program/lesson.html", subtopics: [
        { id: "what-is-a-program", title: "What is a \"program,\" really?" },
        { id: "print", title: "Your first instruction: print()" },
        { id: "variables", title: "Storing information: variables" },
        { id: "types", title: "Basic types: text vs. numbers" },
        { id: "input", title: "Asking the user a question: input()" },
        { id: "recap", title: "Putting it all together" }
      ] },
      { id: "chapter-02", num: 2, title: "Variables & Data Types", path: "chapters/chapter-02-variables-data-types/lesson.html", subtopics: [
        { id: "naming", title: "Naming variables properly" },
        { id: "auto-types", title: "Python decides the type for you" },
        { id: "type-id", title: "Peeking under the hood: type() and id()" },
        { id: "conversion", title: "Converting between types" }
      ] },
      { id: "chapter-03", num: 3, title: "Operators", path: "chapters/chapter-03-operators/lesson.html", subtopics: [
        { id: "arithmetic", title: "Arithmetic & assignment operators" },
        { id: "relational-logical", title: "Relational & logical operators" },
        { id: "bitwise", title: "Bitwise operators" },
        { id: "special", title: "Special operators: is / in" }
      ] },
      { id: "chapter-04", num: 4, title: "Control Flow (if / elif / else)", path: "chapters/chapter-04-control-flow/lesson.html", subtopics: [
        { id: "simple-if", title: "Simple if" },
        { id: "if-else", title: "if-else" },
        { id: "elif", title: "elif — more than two possibilities" },
        { id: "nested", title: "Nested if" }
      ] },
      { id: "chapter-05", num: 5, title: "Loops (while / for)", path: "chapters/chapter-05-loops/lesson.html", subtopics: [
        { id: "while", title: "while loops" },
        { id: "for-range", title: "for loops and range()" },
        { id: "patterns", title: "Common loop patterns" },
        { id: "break-continue", title: "break & continue" }
      ] }
    ]
  },
  {
    title: "Module 2 — Data Structures & Functions",
    examPath: null,
    chapters: [
      { id: "chapter-06", num: 6, title: "Strings Deep Dive", path: "chapters/chapter-06-strings-deep-dive/lesson.html", subtopics: [
        { id: "indexing-slicing", title: "Indexing & slicing" },
        { id: "string-methods", title: "Common string methods" },
        { id: "f-strings", title: "String formatting: f-strings" },
        { id: "immutability", title: "Immutability & string identity" },
        { id: "searching-validating", title: "Searching & validating strings" },
        { id: "bringing-together", title: "Real-world text processing" }
      ] },
      { id: "chapter-07", num: 7, title: "Lists & Tuples", path: "chapters/chapter-07-lists-tuples/lesson.html", subtopics: [
        { id: "creating-accessing", title: "Creating lists & accessing elements" },
        { id: "list-methods", title: "List methods: grow, shrink, reorder" },
        { id: "tuples", title: "Tuples: immutability & packing/unpacking" },
        { id: "nested-lists", title: "Nested lists & 2D data" },
        { id: "copying-lists", title: "Copying lists & the is-vs-== trap" },
        { id: "bringing-together", title: "Real-world lists & tuples in production" }
      ] },
      { id: "chapter-08", num: 8, title: "Dictionaries & Sets", path: "chapters/chapter-08-dictionaries-sets/lesson.html", subtopics: [
        { id: "creating-accessing", title: "Creating dictionaries & accessing values" },
        { id: "dict-methods", title: "Dict methods: add, update, remove" },
        { id: "looping-dicts", title: "Looping over dictionaries" },
        { id: "sets", title: "Sets: unique collections & set operations" },
        { id: "nested-dicts", title: "Nested dictionaries & real-world records" },
        { id: "bringing-together", title: "Real-world dicts & sets in production" }
      ] },
      { id: "chapter-09", num: 9, title: "Comprehensions, Lambda & Functional Tools", path: "chapters/chapter-09-comprehensions-lambda/lesson.html", subtopics: [
        { id: "list-comprehensions", title: "List comprehensions" },
        { id: "dict-set-comprehensions", title: "Dict & set comprehensions" },
        { id: "nested-comprehensions", title: "Nested comprehensions & readability" },
        { id: "lambda", title: "Lambda functions" },
        { id: "functional-tools", title: "map(), filter(), sorted(key=lambda)" },
        { id: "bringing-together", title: "Real-world use in production" }
      ] },
      { id: "chapter-10", num: 10, title: "Functions Deep Dive", path: "chapters/chapter-10-functions-deep-dive/lesson.html", subtopics: [
        { id: "function-basics", title: "def, parameters & return" },
        { id: "default-args", title: "Default arguments" },
        { id: "args-kwargs", title: "*args and **kwargs" },
        { id: "scope", title: "Scope: local, global, nonlocal" },
        { id: "recursion", title: "Recursive functions" },
        { id: "closures", title: "Closures" },
        { id: "decorators", title: "Decorators" },
        { id: "bringing-together", title: "Real-world functions in production" }
      ] }
    ]
  },
  {
    title: "Module 3 — OOP & Robust Code",
    examPath: null,
    chapters: [
      { id: "chapter-11", num: 11, title: "Modules & Packages", path: "chapters/chapter-11-modules-packages/lesson.html", subtopics: [
        { id: "what-is-a-module", title: "What is a module?" },
        { id: "import-variations", title: "Import variations" },
        { id: "math-module", title: "The math module" },
        { id: "datetime-module", title: "The datetime module" },
        { id: "random-module", title: "The random module" },
        { id: "bringing-together", title: "Real-world module use" }
      ] },
      { id: "chapter-12", num: 12, title: "Exception Handling", path: "chapters/chapter-12-exception-handling/lesson.html", subtopics: [
        { id: "try-except-basics", title: "try/except basics" },
        { id: "multiple-except-else-finally", title: "Multiple except, else, finally" },
        { id: "exception-object", title: "The exception object" },
        { id: "raise", title: "Raising exceptions" },
        { id: "custom-exceptions", title: "Custom exception classes" },
        { id: "bringing-together", title: "Real-world exception handling" }
      ] },
      { id: "chapter-13", num: 13, title: "File Handling & CSV", path: "chapters/chapter-13-file-handling-csv/lesson.html", subtopics: [
        { id: "opening-files", title: "Opening & reading files" },
        { id: "writing-files", title: "Writing to files" },
        { id: "file-modes-paths", title: "File modes & paths" },
        { id: "csv-module", title: "The csv module" },
        { id: "file-exceptions", title: "Handling file exceptions" },
        { id: "bringing-together", title: "Real-world file & CSV processing" }
      ] },
      { id: "chapter-14", num: 14, title: "OOP Basics", path: "chapters/chapter-14-oop-basics/lesson.html", subtopics: [
        { id: "classes-objects", title: "Classes & objects" },
        { id: "init-attributes", title: "__init__ & instance attributes" },
        { id: "instance-methods", title: "Instance methods" },
        { id: "class-attributes", title: "Class vs. instance attributes" },
        { id: "dunder-methods", title: "Dunder methods (__str__, __repr__)" },
        { id: "bringing-together", title: "Real-world OOP basics" }
      ] },
      { id: "chapter-15", num: 15, title: "OOP Deeper", path: "chapters/chapter-15-oop-deeper/lesson.html", subtopics: [
        { id: "static-methods", title: "@staticmethod" },
        { id: "class-methods", title: "@classmethod & alternative constructors" },
        { id: "encapsulation-privacy", title: "Encapsulation & privacy" },
        { id: "properties-getters", title: "@property getters" },
        { id: "property-setters", title: "Property setters" },
        { id: "bringing-together", title: "Real-world deeper OOP" }
      ] },
      { id: "chapter-16", num: 16, title: "Inheritance & Polymorphism", path: "chapters/chapter-16-inheritance-polymorphism/lesson.html", subtopics: [
        { id: "basic-inheritance", title: "Basic inheritance" },
        { id: "super-init", title: "super().__init__()" },
        { id: "method-overriding", title: "Method overriding" },
        { id: "polymorphism", title: "Polymorphism" },
        { id: "isinstance-type-checking", title: "isinstance() vs type()" },
        { id: "bringing-together", title: "Real-world inheritance & polymorphism" }
      ] }
    ]
  },
  {
    title: "Module 4 — Real-World Python",
    examPath: null,
    chapters: [
      { id: "chapter-17", num: 17, title: "Generators, Iterators & Context Managers", path: "chapters/chapter-17-generators-iterators-context-managers/lesson.html", subtopics: [
        { id: "iterables-vs-iterators", title: "Iterables vs. iterators" },
        { id: "generator-functions", title: "Generator functions (yield)" },
        { id: "generator-expressions", title: "Generator expressions" },
        { id: "context-managers-with", title: "The with protocol" },
        { id: "custom-context-managers", title: "Custom context managers" },
        { id: "bringing-together", title: "Real-world generators & context managers" }
      ] },
      { id: "chapter-18", num: 18, title: "Regular Expressions", path: null },
      { id: "chapter-19", num: 19, title: "Working with APIs & JSON", path: null },
      { id: "chapter-20", num: 20, title: "Multithreading", path: null },
      { id: "chapter-21", num: 21, title: "Working with Databases (MySQL)", path: null }
    ]
  },
  {
    title: "Module 5 — Data Analysis, Testing & Career",
    examPath: null,
    chapters: [
      { id: "chapter-22", num: 22, title: "NumPy for Data Analysis", path: null },
      { id: "chapter-23", num: 23, title: "Pandas for Data Analysis", path: null },
      { id: "chapter-24", num: 24, title: "Testing Your Code", path: null },
      { id: "chapter-25", num: 25, title: "Professional Python", path: null },
      { id: "chapter-26", num: 26, title: "Capstone Projects", path: null },
      { id: "chapter-27", num: 27, title: "Interview & Career Prep", path: null }
    ]
  }
];
