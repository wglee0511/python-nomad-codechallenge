days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(day_list, day):
  return day in day_list

def get_x(day_list, day_num):
  return day_list[day_num]

def add_x(day_list, day_add):
  return day_list.append(day_add)

def remove_x(day_list, day_remove):
  return day_list.remove(day_remove)


print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)