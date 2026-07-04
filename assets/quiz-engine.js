/*
  Quiz engine for "Python for Everyone" fill-in-the-blank quizzes.

  Usage in HTML:
    <input type="text" class="fib-blank" data-answers="print,Print" aria-label="Answer for question 1">
    <button class="check-btn" data-check-for="the input's id">Check</button>
    <span class="fib-feedback" aria-live="polite"></span>

  Simplest usage — wrap input + button + feedback span in one element with
  class "fib-row" and the engine wires it up automatically; no JS needed per page.

  Answer matching: comma-separated values in data-answers are all accepted.
  Comparison is trimmed and case-insensitive so small phrasing differences
  don't unfairly mark a correct answer wrong.
*/

(function () {
  function normalize(value) {
    return value.trim().toLowerCase();
  }

  function isCorrect(input) {
    const accepted = (input.dataset.answers || "")
      .split(",")
      .map(normalize)
      .filter(Boolean);
    return accepted.includes(normalize(input.value));
  }

  function checkOne(row) {
    const input = row.querySelector(".fib-blank");
    const feedback = row.querySelector(".fib-feedback");
    if (!input) return null;

    const correct = isCorrect(input);
    input.classList.remove("correct", "incorrect");
    input.classList.add(correct ? "correct" : "incorrect");
    input.setAttribute("aria-invalid", correct ? "false" : "true");

    if (feedback) {
      feedback.textContent = correct ? "✅ Correct" : "❌ Try again";
      feedback.classList.remove("correct", "incorrect");
      feedback.classList.add(correct ? "correct" : "incorrect");
    }
    return correct;
  }

  function updateScore() {
    const scoreEl = document.getElementById("quiz-score");
    const fillEl = document.getElementById("quiz-progress-fill");
    const celebrationEl = document.getElementById("quiz-celebration");
    const rows = document.querySelectorAll(".fib-row");
    let correctCount = 0;

    rows.forEach((row) => {
      const input = row.querySelector(".fib-blank");
      if (!input) return;
      if (input.classList.contains("correct")) correctCount += 1;
    });

    if (scoreEl) {
      scoreEl.textContent = `Score: ${correctCount} / ${rows.length}`;
    }
    if (fillEl) {
      const pct = rows.length ? Math.round((correctCount / rows.length) * 100) : 0;
      fillEl.style.width = `${pct}%`;
    }
    if (celebrationEl) {
      celebrationEl.classList.toggle("show", rows.length > 0 && correctCount === rows.length);
    }
  }

  function wireUp() {
    document.querySelectorAll(".fib-row").forEach((row) => {
      const input = row.querySelector(".fib-blank");
      const button = row.querySelector(".check-btn");
      if (!input || !button) return;

      button.addEventListener("click", () => {
        checkOne(row);
        updateScore();
      });

      input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
          event.preventDefault();
          checkOne(row);
          updateScore();
        }
      });
    });

    const checkAllBtn = document.getElementById("check-all-btn");
    if (checkAllBtn) {
      checkAllBtn.addEventListener("click", () => {
        document.querySelectorAll(".fib-row").forEach(checkOne);
        updateScore();
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wireUp);
  } else {
    wireUp();
  }
})();
