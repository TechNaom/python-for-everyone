/*
  Single source of truth for the course's chapter roster, used by
  assets/sidebar.js to render the persistent left-hand navigation, and by
  docs/curriculum/index.html conceptually (kept in sync by hand there).

  `path` is the file path from the repo root to that chapter's lesson.html.
  Leave `path: null` for chapters that haven't been built yet — the
  sidebar renders those as plain, non-clickable "coming soon" text.
*/

window.PFE_MODULES = [
  {
    title: "Module 1 — Foundations",
    examPath: "assessments/written-exams/module-1-exam.md",
    chapters: [
      { id: "chapter-01", num: 1, title: "Your First Python Program", path: "chapters/chapter-01-first-program/lesson.html" },
      { id: "chapter-02", num: 2, title: "Variables & Data Types", path: "chapters/chapter-02-variables-data-types/lesson.html" },
      { id: "chapter-03", num: 3, title: "Operators", path: "chapters/chapter-03-operators/lesson.html" },
      { id: "chapter-04", num: 4, title: "Control Flow (if / elif / else)", path: "chapters/chapter-04-control-flow/lesson.html" },
      { id: "chapter-05", num: 5, title: "Loops (while / for)", path: "chapters/chapter-05-loops/lesson.html" }
    ]
  },
  {
    title: "Module 2 — Data Structures & Functions",
    examPath: null,
    chapters: [
      { id: "chapter-06", num: 6, title: "Strings Deep Dive", path: "chapters/chapter-06-strings-deep-dive/lesson.html" },
      { id: "chapter-07", num: 7, title: "Lists & Tuples", path: null },
      { id: "chapter-08", num: 8, title: "Dictionaries & Sets", path: null },
      { id: "chapter-09", num: 9, title: "Comprehensions, Lambda & Functional Tools", path: null },
      { id: "chapter-10", num: 10, title: "Functions Deep Dive", path: null }
    ]
  },
  {
    title: "Module 3 — OOP & Robust Code",
    examPath: null,
    chapters: [
      { id: "chapter-11", num: 11, title: "Modules & Packages", path: null },
      { id: "chapter-12", num: 12, title: "Exception Handling", path: null },
      { id: "chapter-13", num: 13, title: "File Handling & CSV", path: null },
      { id: "chapter-14", num: 14, title: "OOP Basics", path: null },
      { id: "chapter-15", num: 15, title: "OOP Deeper", path: null },
      { id: "chapter-16", num: 16, title: "Inheritance & Polymorphism", path: null }
    ]
  },
  {
    title: "Module 4 — Real-World Python",
    examPath: null,
    chapters: [
      { id: "chapter-17", num: 17, title: "Generators, Iterators & Context Managers", path: null },
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
