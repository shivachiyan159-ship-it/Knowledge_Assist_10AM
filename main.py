# def main():
#     print("Hello from knowledge-assist-10am!")


# if __name__ == "__main__":
#     main()


from dataclasses import dataclass


class Employee:
    def __init__(self, id, name, salary):
        self.empid = id
        self.empname = name
        self.salary = salary

    def __str__(self):
        return f"employee id is {self.empid} and name is {self.empname} and salary is {self.salary}"

    def dispaly(self):
        return f"employee id is {self.empid} and name is {self.empname} and salary is {self.salary}"


oobj = Employee(1, "sai", 34000)
print(oobj)
# print(oobj.dispaly())
