import json
import os

class MadLibs:
    path="D:\\python projects\\mad_libs_generator\\templates"
    def __init__(self,word_descriptions,problem):
        self.problem=problem
        self.word_descriptions=word_descriptions
        self.user_input=[]
        self.your_answer= None
    @classmethod
    def from_problems(cls,name,path=None):
        if not path:
            path=cls.path
        fpath=os.path.join(path,name)
        with open(fpath,"r") as f:
            problem=json.load(f)
        mad_lib=cls(**problem)
        return mad_lib
    def get_input_from_user(self):
        print("Please Enter the words according to their descriptions:")
        for desc in self.word_descriptions:
            ui=input(desc+" ")
            self.user_input.append(ui)
        return self.user_input
    def build_answer(self):
        self.your_answer=self.problem.format(*self.user_input)
        return self.your_answer
    def show_answer(self):
        print(answer)
def select_problem():
    print("Please select the problem of your choice from the following problems:")
    files=os.listdir(MadLibs.path)
    global problems
    problems=[os.path.splitext(filename)[0] for filename in files]
    for problem in problems:
        print(problem)
    problem=input("Enter the problem of your choice:")
    return problem
def check(problem_name):
    if problem_name not in problems:
        print('invalid input ,Retry:')
        problem_name=select_problem()
        check(problem_name)
    else:
        problem_name+=".json"
        mad_lib=MadLibs.from_problems(problem_name)
        global words
        global answer
        print('raw data:')
        print(mad_lib.problem)
        words=mad_lib.get_input_from_user()
        answer=mad_lib.build_answer()
        mad_lib.show_answer()
problem_name=select_problem()
check(problem_name)


    