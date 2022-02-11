from enum import Enum
import json

class data_base():  # class for storage and processing user's information

    class User(): # class for processing a user's information
        def __init__(self, name, age, level):
            self.name = name
            self.age = age
            self.level = level

        def __repr__(self):
            return f"Имя:{self.name}, возраст:{self.age}, подписка:{self.level.name}"

        def user_high_vos(self): # для сортировки по возрастанию, и возраста, и имени
            return str(self.age) + self.name
        def user_high_ub(self): # для сортировки по убыванию возраста и по возрастанию имени
            return str(100-self.age) + self.name

    class Level(Enum):  # class for choosing level of subscribe
        Standart = "Стандартный"
        Gold = "Золотой"
        Platinum = "Платиновый"

    def __init__(self):
        self.user_list = list()

    def __getitem__(self, item):
        return self.user_list[item]

    def add_User(self, name, age, level: str):  # method for adding a user in database
        self.user_list.append(self.User(name, int(age), self.Level(level)))

    def remove_User(self, ID):  # method of removing a user by id
        ID = int(ID)
        if len(self.user_list) > ID >= 0:
            del self.user_list[ID]
            return "success"
        else:
            return ""

    def check_level(self, ID) -> str:  # method of output user's subscribe level by id
        ID = int(ID)
        if len(self.user_list) > ID >= 0:
            return f"Уровень подписки: {self.user_list[ID].level.name}"
        else:
            return ""

    def check_user(self, ID) -> str:  # method of output user's information by id
        ID = int(ID)
        if len(self.user_list) > ID >= 0:
            return str(self.user_list[ID])
        else:
            return ""

    def users_current_level(self, lvl) -> str:  # method of output of users with the selected level
        answer = ""
        for i, temp in enumerate(self.user_list):
            if temp.level.value == lvl:
                answer += f"Id:{i}, Имя: {temp.name}, возраст: {temp.age}\n"
        return answer

    def check_age(self, ID) -> str:  # method of checking for adulthood
        ID = int(ID)
        if self.user_list[ID].age >= 18:
            return "True"
        else:
            return "False"
        return ""

    def age_sort_vos(self):  # ascending sorting by age method
        self.user_list = sorted(self.user_list, key=self.User.user_high_vos)

    def age_sort_ub(self) -> str:  # descending sorting by age method
        self.user_list = sorted(self.user_list, key=self.User.user_high_ub)

    def adult_list(self) -> str:
        answer = ""
        for i, temp in enumerate(self.user_list):
            if temp.age >= 18:
                answer += f"Id:{i}, {str(temp)}\n"
        return answer

    def safe(self):
        data = {}
        for i in range(len(self.user_list)):
            data[i] = {"name": self.user_list[i].name}
            data[i]["age"] = self.user_list[i].age
            data[i]["level"] = self.user_list[i].level.value
        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file, ensure_ascii=False, indent=4, separators=(',', ': '))
