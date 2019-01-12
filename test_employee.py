from employee import Employee

#Manual Test

emp1 = Employee(100, "John Smith", 45000)
print(emp1)
print("Id: "+str(emp1.getId()))
print("Name:"+ emp1.getName())
print("Salary: "+str(emp1.getSalary()))
emp1.applyRaise()
print("New Salary: "+str(emp1.getSalary()))

for a in emp1.getName():
    print(a)




#unittest

import unittest


class test_Employee(unittest.TestCase):

    emp2 = Employee(101,"Mike Dane", 50000)

    def setUp(self):
        super().setUp()
        emp3 = Employee(101,"Mike Dane", 50000)

    def test_getName(self):
        self.assertEqual(self.emp2.getName(),"Mike Dane")
        self.assertIn("Mike",self.emp2.getName())

    def test_getId(self):
        self.assertIsNotNone(self.emp2.getId())
        self.assertEqual(self.emp2.getId(),101)



if __name__ == "__main__":
    unittest.main()


