
#understanding functions
def format_name(first, last):
  if first == "" or last == "":
    return "You didn't provide valid input"
  formatted_first_name = first.title()
  formatted_last_name = last.title()
  return f"{formatted_first_name} {formatted_last_name}"

full_formatted_name = format_name(input("What is your first name:\n"), input("What is your last name:\n"))

print(full_formatted_name)