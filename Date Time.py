import datetime

def print_formatted_date(format_string="%Y-%m-%d"):
  now = datetime.datetime.now()

  formatted_date = now.strftime(format_string)

  print("Current date:", formatted_date)

print_formatted_date()

custom_format = "%d/%m/%Y"
print_formatted_date(custom_format)
