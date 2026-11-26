
# print("Restoranimizga xush kelibsiz!")

# ism = input("Ismingiz nima? ")

# print("Assalomu alaykum", ism)
# print("Sizga menyu taqdim etamiz!")

# menu = {
#     "osh": 25000,
#     "shashlik": 18000,
#     "lagmon": 22000,
#     "somsa": 10000,
#     "cola": 8000
# }

# print("\n===== MENYU =====")

# for ovqat, narx in menu.items():
#     print(ovqat, "-", narx, "so'm")

# jami = 0

# while True:
#     tanlov = input("\nNima buyurtma qilasiz? ")

#     if tanlov == "tamom":
#         break

#     if tanlov in menu:
#         jami += menu[tanlov]
#         print(tanlov, "buyurtmaga qo'shildi!")
#         print("Hozirgi hisob:", jami, "so'm")
#     else:
#         print("Kechirasiz, bunday ovqat menyuda yo'q!")

# print("\n", ism, "buyurtmangiz uchun rahmat!")
# print("Umumiy hisob:", jami, "so'm")
# print("Yana tashrif buyuring!")





########## SECOND PRACTISE


# print("================================")
# print("     GOLDEN RESTAURANT")
# print("================================")

# ism = input("Assalomu alaykum! Ismingiz nima? ")

# print("\nXush kelibsiz,", ism, "!")
# print("Bugun sizga xizmat ko'rsatishdan xursandmiz! 😊")
# print("Marhamat, menyumiz bilan tanishing.")

# menu = {
#     "osh": 25000,
#     "shashlik": 18000,
#     "lagmon": 22000,
#     "somsa": 10000,
#     "manti": 20000,
#     "norin": 28000,
#     "lavash": 27000,
#     "burger": 30000,
#     "pizza": 55000,
#     "cola": 8000,
#     "fanta": 8000,
#     "choy": 5000
# }

# print("\n========== MENYU ==========")

# for ovqat, narx in menu.items():
#     print(f"{ovqat.title()} - {narx:,} so'm")

# print("===========================")

# buyurtmalar = []
# jami = 0

# while True:
#     tanlov = input(
#         "\nNima buyurtma qilmoqchisiz? "
#         "(Tugatish uchun 'boldim' deb yozing): "
#     ).lower().strip()

#     if tanlov in ["boldim", "bo'ldim", "yeb boldim",
#                   "yeb bo'ldim", "tamom"]:
#         break

#     if tanlov in menu:
#         buyurtmalar.append(tanlov)
#         jami += menu[tanlov]

#         print("Ajoyib tanlov! 😋")
#         print(tanlov.title(), "buyurtmangizga qo'shildi.")
#         print("Hozirgi hisob:", f"{jami:,}", "so'm")

#     else:
#         print("Kechirasiz, bunday taomimiz yo'q.")
#         print("Menyudan boshqa taom tanlab ko'ring.")

# print("\n================================")
# print("Hurmatli", ism + "!")
# print("Ovqatlanishingiz qanday o'tdi?")

# fikr = input(
#     "Taomlarimiz sizga yoqdimi? (ha/yo'q): "
# ).lower().strip()

# if fikr == "ha":
#     print("Buni eshitib juda xursandmiz! ❤️")
#     print("Yana kelishingizni kutib qolamiz!")
# elif fikr in ["yo'q", "yoq", "yomon"]:
#     print("Afsusdamiz! 😔")
#     sabab = input("Nima sizga yoqmadi? ")
#     print("Fikringiz uchun rahmat!")
#     print("Xizmatimizni yaxshilashga harakat qilamiz.")
# else:
#     print("Fikringiz biz uchun juda muhim!")

# print("\n========== CHEK ==========")

# for ovqat in buyurtmalar:
#     print(ovqat.title(), "-", f"{menu[ovqat]:,}", "so'm")

# print("--------------------------")
# print("Jami:", f"{jami:,}", "so'm")
# print("==========================")

# print("\nHurmatli", ism + "!")
# print("Restoranimizni tanlaganingiz uchun rahmat!")
# print("Sizni yana kutib qolamiz!")
# print("Xayr, yaxshi kun tilaymiz! 😊")













# import tkinter as tk
# import random

# CELL = 20
# COLS, ROWS = 24, 20
# SPEED = 120  # ms, kichikroq = tezroq

# class Snake:
#     def __init__(self, root):
#         self.root = root
#         root.title("Snake")
#         self.score_var = tk.StringVar()
#         tk.Label(root, textvariable=self.score_var, font=("Arial", 14)).pack()
#         self.canvas = tk.Canvas(root, width=COLS * CELL, height=ROWS * CELL, bg="#111")
#         self.canvas.pack()
#         root.bind("<Key>", self.on_key)
#         self.reset()
#         self.tick()

#     def reset(self):
#         self.snake = [(COLS // 2, ROWS // 2), (COLS // 2 - 1, ROWS // 2)]
#         self.dir = (1, 0)
#         self.next_dir = self.dir
#         self.score = 0
#         self.alive = True
#         self.place_food()

#     def place_food(self):
#         while True:
#             f = (random.randrange(COLS), random.randrange(ROWS))
#             if f not in self.snake:
#                 self.food = f
#                 return

#     def on_key(self, e):
#         keys = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0),
#                 "w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
#         if e.keysym in keys:
#             d = keys[e.keysym]
#             # teskari yo'nalishga burilib bo'lmaydi
#             if (d[0] + self.dir[0], d[1] + self.dir[1]) != (0, 0):
#                 self.next_dir = d
#         elif e.keysym == "space" and not self.alive:
#             self.reset()

#     def tick(self):
#         if self.alive:
#             self.dir = self.next_dir
#             hx, hy = self.snake[0]
#             head = (hx + self.dir[0], hy + self.dir[1])
#             if (not 0 <= head[0] < COLS or not 0 <= head[1] < ROWS
#                     or head in self.snake):
#                 self.alive = False
#             else:
#                 self.snake.insert(0, head)
#                 if head == self.food:
#                     self.score += 1
#                     self.place_food()
#                 else:
#                     self.snake.pop()
#         self.draw()
#         self.root.after(SPEED, self.tick)

#     def draw(self):
#         c = self.canvas
#         c.delete("all")
#         self.score_var.set(f"Ball: {self.score}")
#         fx, fy = self.food
#         c.create_oval(fx * CELL + 2, fy * CELL + 2, (fx + 1) * CELL - 2, (fy + 1) * CELL - 2, fill="#e74c3c")
#         for i, (x, y) in enumerate(self.snake):
#             color = "#2ecc71" if i else "#27ae60"
#             c.create_rectangle(x * CELL + 1, y * CELL + 1, (x + 1) * CELL - 1, (y + 1) * CELL - 1,
#                                fill=color, outline="")
#         if not self.alive:
#             c.create_text(COLS * CELL // 2, ROWS * CELL // 2 - 15, text="O'yin tugadi!",
#                           fill="white", font=("Arial", 24, "bold"))
#             c.create_text(COLS * CELL // 2, ROWS * CELL // 2 + 20, text="Qayta boshlash: SPACE",
#                           fill="white", font=("Arial", 14))

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.resizable(False, False)
#     Snake(root)
#     root.mainloop()




