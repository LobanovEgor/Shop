from builtins import *
from tkinter import *
from tkinter import ttk, messagebox
from singleton import Singleton
from Products import *


class MainWindow(Tk, Singleton):
    def init(self):
        super().__init__()

    def __init__(self):
        self.balance = [100, 50, 150]
        self.vidgets(self.balance)

    def vidgets(self, balance):
        self.balance_text = StringVar()
        self.products_vidget = self.products_vidget()
        self.cart_vidget = self.cart_vidget()
        self.balance_text.set(f'{balance[0]} рублей на карте\n{balance[1]} наличными\n{balance[2]} бонусами')

        self.balance_show = Label(font=('Arial', 10), textvariable=self.balance_text)
        self.balance_show.grid(row=0, column=5, padx=0, pady=0)

        self.products_text = ttk.Label(text='Перетаскивайте из левой колонки в правую,\nчтобы добавить товары и '
                                            'наоборот, чтобы\nудалить товары', font=('Arial', 10))
        self.products_text.grid(row=0, column=0, rowspan=2, sticky=SW)
        self.add_btn = Button(text='>>>', command=self.add_selected_items)
        self.del_btn = Button(text='<<<', command=self.del_selected_items)

        self.add_btn.grid(row=2, column=1, columnspan=1, rowspan=1, padx=100, pady=100, sticky=NSEW)
        self.del_btn.grid(row=3, column=1, columnspan=1, rowspan=1, padx=100, pady=100, sticky=NSEW)
        self.payment()

    def products_vidget(self):
        self.products_factory = ProductFactory()

        self.products_name = self.products_factory.products_list
        self.fruit_name = self.products_factory.fruit_list

        self.products_cost = self.products_factory.products_cost
        self.fruit_cost = self.products_factory.fruit_cost

        self.products_list = Listbox(height=20, width=20, font=('Arial', 10), selectmode=SINGLE)
        self.products_list.grid(row=2, column=0, rowspan=2, sticky=NSEW)
        for i in range(len(self.products_name)):
            self.products_list.insert(1, self.products_name[i])
        for i in range(len(self.fruit_name)):
            self.products_list.insert(1, self.fruit_name[i])

    def cart_vidget(self):
        self.sum = 0
        self.sum_to_pay = f'{self.sum} сумма товаров в корзине'

        self.cart = Listbox(height=20, width=20, font=('Arial', 10))
        self.cart.grid(row=2, column=2, rowspan=2, sticky=NSEW)
        self.cart.insert(0, self.sum_to_pay)

    def add_selected_items(self):
        self.selected_item = self.products_list.get(self.products_list.curselection())
        if self.selected_item in self.products_name:
            self.sum += self.products_cost[self.products_name.index(self.selected_item)]
            self.cart.insert(1, self.selected_item)
            self.sum_to_pay = f'{self.sum} сумма товаров в корзине'
            self.cart.delete(0)
            self.cart.insert(0, self.sum_to_pay)
            if self.selected_item == 'Пиво 50 руб':
                self.disabled = IntVar()
                self.disabled.set(0)
                self.age_check = ttk.Radiobutton(text='Мне есть 18', variable=self.disabled, value=1)
                self.age_check.grid(row=2, column=4)
        elif self.selected_item in self.fruit_name:
            self.add_btn.config(state='disabled')

            self.entry_weight = ttk.Entry(text='Введите вес')
            self.entry_weight.grid(row=0, column=2)
            self.weight_btn = ttk.Button(text='Ввод веса', command=self.getWeight)
            self.weight_btn.grid(row=1, column=2)

    def del_selected_items(self):
        if self.cart.get(self.cart.curselection()) != self.sum_to_pay:
            self.selected_item = self.cart.curselection()
            self.selected_item_name = self.cart.get(self.selected_item)
            if self.selected_item_name in self.products_name:
                self.sum -= self.products_cost[self.products_name.index(self.selected_item_name)]
                self.sum_to_pay = f'{self.sum} сумма товаров в корзине'
                self.cart.delete(self.selected_item)
                self.cart.delete(0)
                self.cart.insert(0, self.sum_to_pay)
                if self.selected_item_name == 'Пиво 50 руб' and 'Пиво 50 руб' not in self.cart.get(0, END):
                    self.age_check.destroy()
            else:
                weight = self.selected_item_name.split(';')[1]
                self.selected_item_name = self.selected_item_name.split(';')[0]
                self.sum -= self.fruit_cost[self.fruit_name.index(self.selected_item_name)] * float(weight)
                self.sum_to_pay = f'{self.sum} сумма товаров в корзине'
                self.cart.delete(self.selected_item)
                self.cart.delete(0)
                self.cart.insert(0, self.sum_to_pay)
        else:
            pass

    def getWeight(self):
        weight = self.entry_weight.get()
        if float(weight) <= 0:
            messagebox.showinfo('Неправильный ввод', 'Вес не может быть меньше или равен нулю')
        else:
            self.add_btn.config(state='normal')
            self.sum += self.fruit_cost[self.fruit_name.index(self.selected_item)] * float(weight)
            self.sum_to_pay = f'{self.sum} сумма товаров в корзине'
            self.cart.delete(0)
            self.cart.insert(0, self.sum_to_pay)
            self.selected_item += f';{weight}'
            self.cart.insert(1, self.selected_item)

    def payment(self):
        def check_sum():
            balance_sum = 0
            for i in self.balance:
                balance_sum += i
            if self.sum > balance_sum:
                messagebox.showinfo('Не хватает денег!', 'Уберите товары из корзины, чтобы продолжить оплату!')
                return None
            elif sum == 0:
                messagebox.showinfo('В смысле не купили ничего..', 'Добавьте хоть что-то,\nпожалуйста...')
                return None
            elif 'Пиво 50 руб' in self.cart.get(0, END) and self.disabled.get() == 0:
                messagebox.showinfo('18+', 'Не продаём несовершеннолетним')
                return None
            else:
                self.payment_window()

        self.payment_btn = ttk.Button(text='К оплате', command=check_sum)
        self.payment_btn.grid(row=3, column=4, sticky=NSEW)

    def payment_window(self):
        def pay():
            entry = payment_window.entry_payment.get()
            if entry == '':
                messagebox.showinfo('Неправильный ввод', 'Введите оплату')
            else:
                entry = entry.split(';')
                for i in range(len(entry)):
                    entry[i] = int(entry[i])
                if (sum(entry) != self.sum):
                    messagebox.showinfo('Неправильный ввод!', 'Неправильный ввод')
                else:
                    for i in range(len(entry)):
                        self.balance[i] -= entry[i]
                        print(f'Успешная оплата! Осталось - {self.balance}')
                    payment_window.destroy()

        self.destroy()

        payment_window = Tk()

        payment_window.title('Оплата')
        payment_window.geometry('1280x720')

        for c in range(4):
            payment_window.columnconfigure(c, weight=1)
        for r in range(3):
            payment_window.rowconfigure(r, weight=1)

        payment_window.text_balance = StringVar()
        payment_window.text_balance.set(
            f'{self.balance[0]} рублей на карте\n{self.balance[1]} наличными\n{self.balance[2]} бонусами')
        payment_window.balance_show = Label(textvariable=payment_window.text_balance)
        payment_window.balance_show.grid(sticky=NE)

        payment_window.text_payment = ttk.Label(
            text=f'Введите ниже сколько вы хотите оплатить картой, наличными, бонусами\n'
                 f'в формате ***;***;***\n'
                 f'где вместо * сначала кол-во денег с карты, потом с налички, а потом\n'
                 f'бонусов, ваш баланс: {self.balance[0]} руб на карте, {self.balance[1]} руб наличными, {self.balance[2]} бонусами',
            font=('Arial', 15))
        payment_window.text_payment.grid(row=0, column=0, columnspan=2, sticky=NW)

        payment_window.entry_payment = ttk.Entry(width=20)
        payment_window.entry_payment.grid(row=1, column=1, columnspan=1, sticky=NSEW)

        payment_window.pay_btn = ttk.Button(text='Оплатить', command=pay)
        payment_window.pay_btn.grid(row=2, column=2, rowspan=2)

        payment_window.mainloop()
