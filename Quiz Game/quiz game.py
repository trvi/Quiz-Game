import tkinter as tk
from tkinter import messagebox

# Quiz data with more questions
questions = {
    "Geography": [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        {
            "question": "Which is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        },
        {
            "question": "What country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "Thailand", "South Korea"],
            "answer": "Japan"
        },
        {
            "question": "Which river is the longest in the world?",
            "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
            "answer": "Nile"
        },
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        },
        {
            "question": "What planet is known for its rings?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Saturn"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
            "answer": "Mitochondria"
        },
    ],
    "Math": [
        {
            "question": "What is 5 * 6?",
            "options": ["30", "25", "35", "40"],
            "answer": "30"
        },
        {
            "question": "What is 12 / 4?",
            "options": ["2", "3", "4", "5"],
            "answer": "3"
        },
        {
            "question": "What is the value of π (pi) approximately?",
            "options": ["3.14", "3.16", "3.12", "3.18"],
            "answer": "3.14"
        },
        {
            "question": "What is 7 + 8?",
            "options": ["15", "16", "14", "17"],
            "answer": "15"
        },
    ],
}

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.score = 0
        self.question_index = 0
        self.current_category = None

        self.setup_ui()

    def setup_ui(self):
        self.category_label = tk.Label(self.master, text="Select Category:", font=("Helvetica", 14))
        self.category_label.pack(pady=10)

        self.category_var = tk.StringVar(value="Geography")
        self.category_menu = tk.OptionMenu(self.master, self.category_var, *questions.keys(), command=self.start_quiz)
        self.category_menu.pack(pady=10)

        self.question_label = tk.Label(self.master, text="", wraplength=300, font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack(pady=20)

        self.options = []
        for _ in range(4):
            option = tk.Radiobutton(self.options_frame, variable=self.var, value="", font=("Helvetica", 12))
            option.pack(anchor='w')
            self.options.append(option)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="Reset Quiz", command=self.reset_quiz)
        self.reset_button.pack(pady=5)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

    def start_quiz(self, category):
        self.current_category = category
        self.score = 0
        self.question_index = 0
        self.load_question()
        self.next_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.score}")

    def load_question(self):
        if self.question_index < len(questions[self.current_category]):
            question_data = questions[self.current_category][self.question_index]
            self.question_label.config(text=question_data["question"])
            self.var.set(None)  # Reset selection

            for i, option in enumerate(self.options):
                option.config(text=question_data["options"][i], value=question_data["options"][i])

        else:
            self.show_score()

    def check_answer(self):
        selected_option = self.var.get()
        if selected_option == questions[self.current_category][self.question_index]["answer"]:
            self.score += 1

    def next_question(self):
        self.check_answer()
        self.question_index += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"Your score in {self.current_category} is: {self.score}/{len(questions[self.current_category])}")
        self.next_button.config(state=tk.DISABLED)

    def reset_quiz(self):
        self.score = 0
        self.question_index = 0
        self.score_label.config(text="")
        self.var.set(None)
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()