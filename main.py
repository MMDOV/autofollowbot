from bot import InstaFollower
import ttkbootstrap as ttk


def start():
    bot = InstaFollower()
    user = username.get()
    pas = password.get()
    bot.login(user=user, pas=pas)
    bot.find_followers(similar_acc=acc_name.get())
    bot.follow()


# ----------------UI------------------#
if __name__ == "__main__":
    window = ttk.Window()
    window.title("AutoFollow Bot")
    window.config(pady=20, padx=20)
    label1 = ttk.Label(text="Your Email : ", padding=10)
    label1.grid(row=0, column=0)
    username = ttk.Entry(width=25)
    username.insert(0, "vmamad24@gmail.com")
    username.grid(row=0, column=1)
    label2 = ttk.Label(text="Your Password : ", padding=10)
    label2.grid(row=1, column=0)
    password = ttk.Entry(width=25)
    password.insert(0, "Mm187252715118")
    password.grid(row=1, column=1)
    label3 = ttk.Label(text="Target account Name : ", padding=10)
    label3.grid(row=2, column=0)
    acc_name = ttk.Entry(width=25)
    acc_name.insert(0, "konusanlar__farsi")
    acc_name.grid(row=2, column=1)
    button = ttk.Button(text="Start!", width=20, bootstyle='danger', command=start)
    button.config(padding=10)
    button.grid(row=3, column=0, columnspan=2)
    window.mainloop()
