print("Welcome to 'Place the Rabbit' 🐇\n")

# إنشاء الحقل
field = [
    ["🌿","🌿","🌿"],
    ["🌿","🌿","🌿"],
    ["🌿","🌿","🌿"]
]

def print_field():
    for row in field:
        print(row)
    print()  # سطر فارغ للفصل

while True:
    print_field()
    print("Where should the rabbit go? 🐇")
    print("Enter row and column as two digits (e.g., 12 for row 1, column 2)")
    print("Or type 'exit' to quit the game.")

    position = input("Your choice: ").strip()

    if position.lower() == "exit":
        print("Thanks for playing! Goodbye 🐇")
        break

    # التحقق من صحة الإدخال
    if len(position) != 2 or not position.isdigit():
        print("Invalid input. Please enter two digits like 12.\n")
        continue

    row = int(position[0])
    column = int(position[1])

    if not (1 <= row <= 3 and 1 <= column <= 3):
        print("Invalid row or column. Please choose between 1 and 3.\n")
        continue

    # إزالة الأرنب القديم إذا موجود
    for r in range(3):
        for c in range(3):
            if field[r][c] == "🐇":
                field[r][c] = "🌿"

    # وضع الأرنب الجديد
    field[row-1][column-1] = "🐇"
    print("\nSuccess! The rabbit has moved.\n")
