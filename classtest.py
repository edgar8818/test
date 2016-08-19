#!/usr/bin/env python
class Person:
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def Info(self):
		print 'My name is %s, I\'m %d years old!' % (self.name,self.age)

p = Person('frank',20,'m')
p.Info()
 
class Teacher(Person):
	def __init__(self,name,age,sex,salary):
		Person.__init__(self,name,age,sex)
		self.salary = salary

	def tell(self):
		Person.Info(self)
		print 'salary is %d ' % self.salary
t1 = Teacher('test',20,'m',10000)
t1.tell()
