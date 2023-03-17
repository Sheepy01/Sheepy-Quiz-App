
import requests
import json

from base_UI import AnswerUI
answerui = AnswerUI()

SELECT_ALL_VALUE = 0
CATEGORY_LIST = []
QUESTION = []
SELECTED_LIST = []
QUESTION_ANSWER_LIST = []
DIFFICULTY = 0
TYPE = ""


class Category:
    def __init__(self):
        self.category_list = CATEGORY_LIST
        self.difficulty_list = ["Easy", "Medium", "Hard"]
        self.type_list = ["True/False", "Multiple Choice Questions"]
        self.question_answer_list = QUESTION_ANSWER_LIST
        self.selected_list = SELECTED_LIST
        self.questions = QUESTION
        self.select_all = SELECT_ALL_VALUE
        self.index = 0
        self.difficulty = DIFFICULTY
        self.type = TYPE

    def getCategory(self):
        response = requests.get("https://opentdb.com/api.php?amount=50")
        data = response.json()
        for i in range(len(data["results"])):
            category = data["results"][i]["category"]
            question = data["results"][i]["question"]
            correct_answer = data["results"][i]["correct_answer"]
            incorrect_answer = data["results"][i]["incorrect_answers"]
            difficulty = data["results"][i]["difficulty"]
            type = data["results"][i]["type"]
            global CATEGORY_LIST
            if category in CATEGORY_LIST:
                pass
            else:
                CATEGORY_LIST.append(category)
                self.question_answer_list.append([category, question, [correct_answer, [incorrect_answer]], difficulty, type])

    def changeSelAttribute(self, value):
        global SELECT_ALL_VALUE
        SELECT_ALL_VALUE = value
    

class Questions(Category):
    def displayQuestions(self):
        super().__init__()
        if self.select_all == 1:
            # while self.index <= len(self.question_answer_list):
            question_text = self.question_answer_list[0][1]
            self.questions.append(question_text)
            return question_text
        else:
            self.questions.clear()
            for cat in self.category_list:
                for i in range(len(self.question_answer_list)):
                    if cat == self.question_answer_list[i][0]:
                        question = self.question_answer_list[0][1]
            self.questions.append(question)
            return question


class Difficulty(Category):
    def getDifficulty(self):
        super().__init__()
        if self.difficulty == 0 or self.difficulty == 1 or self.difficulty == 2:
            if self.type == "True/False":
                super().self.displayQuestions()
                answerui.answerTypeTrueFalse()
            elif self.type == "Multiple Choice Questions":
                super().self.displayQuestions()
                answerui.answerTypeMCQ(radio1=self.question_answer_list[2][0], radio2=self.question_answer_list[2][1])

    def changeDiffAttribute(self, value):
        global DIFFICULTY
        DIFFICULTY = value

    def changeTypeAttribute(self, value):
        global TYPE
        TYPE = value
