import tkinter as tk
import datetime
from PIL import Image, ImageTk

window=tk.Tk()
window.geometry("300x400")
window.title("Calculate Age")

year_label=tk.Label(text="Year: ")
year_label.grid(column=0,row=1)

birth_year_entry=tk.Entry(master=window)
birth_year_entry.grid(column=1, row=1)

month_label=tk.Label(text="Month: ")
month_label.grid(column=0, row=2)

birth_month_entry=tk.Entry(master=window)
birth_month_entry.grid(column=1, row=2)

day_label=tk.Label(text="Day: ")
day_label.grid(column=0, row=3)

birth_day_entry=tk.Entry(master=window)
birth_day_entry.grid(column=1, row=3)


class Person():

	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	def age(self):
		todays_date = datetime.date.today()
		age = todays_date.year-self.birthdate.year
		return age


def calculate_age():
	# print(birth_year_entry.get())
	# print(birth_month_entry.get())
	# print(birth_day_entry.get())

	some_person = Person("You", datetime.date(
											int(birth_year_entry.get()),
											int(birth_month_entry.get()),
											int(birth_day_entry.get())
											)
						)
	print(some_person.age())

	field_for_text_answer=tk.Text(master=window, height=5, width=25)
	field_for_text_answer.grid(column=1, row=5)

	text_answer="{name} are {years} years old.".format(name=some_person.name, years=some_person.age())

	field_for_text_answer.insert(tk.END, text_answer)



button_for_calculating_ages=tk.Button(master=window, text="Calculate Age", command=calculate_age)
button_for_calculating_ages.grid(column=1, row=4)

filename = "logo.jpg"
image = Image.open(filename)
image.thumbnail((200, 200), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)



window.mainloop()