def find_second_largest(numbers):
  """
  پیدا کردن دومین عدد بزرگتر در لیست اعداد

  Args:
      numbers: لیست اعداد

  Returns:
      دومین عدد بزرگتر و اندیس آن
  """
  # پیدا کردن بزرگترین عدد
  largest = max(numbers)
  # حذف بزرگترین عدد از لیست
  numbers.remove(largest)
  # پیدا کردن دومین عدد بزرگتر
  second_largest = max(numbers)
  # پیدا کردن اندیس دومین عدد بزرگتر
  index = numbers.index(second_largest)
  # بازگرداندن دومین عدد بزرگتر و اندیس آن
  return second_largest, index

# دریافت اعداد از کاربر
numbers = list(map(int, input("اعداد را با فاصله وارد کنید: ").split()))

# پیدا کردن دومین عدد بزرگتر و اندیس آن
second_largest, index = find_second_largest(numbers)

# چاپ دومین عدد بزرگتر و اندیس آن
print(f"دومین عدد بزرگتر: {second_largest}")
print(f"اندیس: {index + 1}")



###################
اندیس در پایتون
اندیس در پایتون به موقعیت یک عنصر در یک دنباله، مانند لیست، رشته یا توپل اشاره می کند. اندیس ها از 0 شروع می شوند و به ترتیب تا انتهای دنباله ادامه می یابند.
