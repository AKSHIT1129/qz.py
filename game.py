import json
import os
import random
import time
import tkinter as tk
from dataclasses import dataclass
from datetime import datetime
from tkinter import messagebox
from typing import List, Dict, Any

@dataclass
class Question:
    prompt: str
    options: List[str]
    answer_index: int

SCORES_FILE_DEFAULT = "quiz_scores.json"

def save_score(filepath: str, username: str, score: int, total: int, duration: float):
    """Save a quiz score to the JSON file."""
    scores = load_scores(filepath)
    
    entry = {
        "username": username,
        "score": score,
        "total": total,
        "percent": (score / total * 100) if total > 0 else 0,
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    scores.append(entry)
    
    try:
        with open(filepath, 'w') as f:
            json.dump(scores, f, indent=2)
    except Exception as e:
        print(f"Error saving scores: {e}")

def load_scores(filepath: str) -> List[Dict[str, Any]]:
    """Load scores from the JSON file."""
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading scores: {e}")
        return []

class QuizGUI:
    def __init__(self, root: tk.Tk, questions: List[Question]):  
        self.root = root
        self.root.title("Quiz Game")
        self.questions = questions[:]
        random.shuffle(self.questions)
        self.current_index = 0
        self.correct = 0
        self.username = tk.StringVar()
        self.selected_option = tk.IntVar(value=-1)
        self.start_time = None
        self.answers = {}

        self._build_start_screen()

    def _clear(self):
        for w in list(self.root.children.values()):
            w.destroy()

    def _build_start_screen(self):
        self._clear()
        container = tk.Frame(self.root, padx=16, pady=16)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="Welcome to the Quiz Game", font=("Segoe UI", 16, "bold")).pack(pady=(0, 12))
        tk.Label(container, text="Enter your name:").pack(anchor="w")
        entry = tk.Entry(container, textvariable=self.username)
        entry.pack(fill=tk.X)
        entry.focus_set()

        tk.Button(container, text="Start Quiz", command=self._start_quiz).pack(pady=12)
        tk.Button(container, text="View Leaderboard", command=self._show_leaderboard).pack()

    def _start_quiz(self):
        if not self.username.get().strip():
            self.username.set("Player")
        self.current_index = 0
        self.correct = 0
        self.answers = {}
        self.start_time = time.perf_counter()
        self._build_question_screen()

    def _build_question_screen(self):
        if self.current_index >= len(self.questions):
            self._finish_quiz()
            return

        self._clear()
        q = self.questions[self.current_index]

        container = tk.Frame(self.root, padx=16, pady=16)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text=f"Question {self.current_index + 1} / {len(self.questions)}", 
                font=("Segoe UI", 12, "bold")).pack(anchor="w")
        tk.Label(container, text=q.prompt, wraplength=600, justify="left", 
                font=("Segoe UI", 12)).pack(anchor="w", pady=(8, 12))

        self.selected_option.set(self.answers.get(self.current_index, -1))

        for idx, opt in enumerate(q.options):
            tk.Radiobutton(
                container,
                text=opt,
                variable=self.selected_option,
                value=idx,
                anchor="w",
                justify="left",
                wraplength=600,
                font=("Segoe UI", 11),
            ).pack(anchor="w", pady=2)

        btn_frame = tk.Frame(container)
        btn_frame.pack(fill=tk.X, pady=(12, 0))

        if self.current_index > 0:
            tk.Button(btn_frame, text="Previous", command=self._previous_question).pack(side=tk.LEFT, padx=4)

        tk.Button(btn_frame, text="Submit", command=self._submit_answer).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Quit", command=self._build_start_screen).pack(side=tk.RIGHT, padx=4)

    def _submit_answer(self):
        choice = self.selected_option.get()
        if choice < 0:
            messagebox.showinfo("Select an option", "Please select an answer before continuing.")
            return
        self.answers[self.current_index] = choice
        self.current_index += 1
        self._build_question_screen()

    def _previous_question(self):
        self.answers[self.current_index] = self.selected_option.get()
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = 0
        self._build_question_screen()

    def _finish_quiz(self):
        self.correct = sum(
            1 for i, q in enumerate(self.questions)
            if self.answers.get(i, -1) == q.answer_index
        )

        duration = time.perf_counter() - self.start_time if self.start_time else 0.0
        total = len(self.questions)
        save_score(SCORES_FILE_DEFAULT, self.username.get().strip() or "Player", self.correct, total, duration)

        self._clear()
        container = tk.Frame(self.root, padx=16, pady=16)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="Results", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        tk.Label(container, text=f"Score: {self.correct}/{total}").pack(anchor="w", pady=(8, 0))
        tk.Label(container, text=f"Time: {duration:.2f} seconds").pack(anchor="w")

        btn_frame = tk.Frame(container)
        btn_frame.pack(fill=tk.X, pady=(12, 0))
        tk.Button(btn_frame, text="Play Again", command=self._start_quiz).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Leaderboard", command=self._show_leaderboard).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="Home", command=self._build_start_screen).pack(side=tk.RIGHT)

    def _show_leaderboard(self):
        self._clear()
        container = tk.Frame(self.root, padx=16, pady=16)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(container, text="Leaderboard", font=("Segoe UI", 16, "bold")).pack(anchor="w")

        scores = load_scores(SCORES_FILE_DEFAULT)
        if not scores:
            tk.Label(container, text="No scores yet.").pack(anchor="w", pady=8)
        else:
            scores_sorted = sorted(scores, key=lambda s: (-s.get("percent", 0), s.get("duration_seconds", 0)))
            listbox = tk.Listbox(container, width=80, height=12)
            listbox.pack(fill=tk.BOTH, expand=True, pady=8)
            for i, s in enumerate(scores_sorted[:25], start=1):
                line = (
                    f"{i:2}. {s.get('username','?'):<12} "
                    f"{s.get('score',0):>2}/{s.get('total',0):<2} "
                    f"({s.get('percent',0):>5.1f}%) in {s.get('duration_seconds',0):>5.2f}s "
                    f"on {s.get('timestamp','')}"
                )
                listbox.insert(tk.END, line)

        btn_frame = tk.Frame(container)
        btn_frame.pack(fill=tk.X, pady=(12, 0))
        tk.Button(btn_frame, text="Back", command=self._build_start_screen).pack(side=tk.LEFT)
if __name__ == "__main__":
   
    sample_questions = [
        Question("What is the capital of France?", 
                ["London", "Berlin", "Paris", "Madrid"], 2),
        Question("What is capital of Australia?", 
                ["Sydney", "Melbourne", "Perth", "Newcastle"], 0),
        Question("Which planet is known as the Red Planet?", 
                ["Venus", "Mars", "Jupiter", "Saturn"], 1),
        Question("Who painted the Mona Lisa?", 
                ["Van Gogh", "Picasso", "Da Vinci", "Monet"], 2),
        Question("What is the Worlds largest ocean?", 
                ["Atlantic", "Indian", "Arctic", "Pacific"], 3),
        Question("Which programming language is compiled in JVM?",
                ["Java", "Python", "C++", "JavaScript"], 0),
        Question("What is the square root of 90000?",
                ["3000", "300", "30000", "30"], 1),
        Question("Which year did World War II end?",
                ["1943", "1944", "1945", "1946"], 2),
    ]
    root = tk.Tk()
    root.geometry("700x550")
    app = QuizGUI(root, sample_questions)
    root.mainloop()
