# جمع بيانات المهمة
task = input("Enter your task: ")

# التحقق من الأولوية باستخدام loop
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority! Please enter high, medium, or low.")

# التحقق من الوقت المحدد باستخدام loop
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input! Please enter yes or no.")

# معالجة المهمة حسب الأولوية
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# تعديل الرسالة لو المهمة محددة بالوقت
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# طباعة التذكير
print("\nReminder:",reminder)