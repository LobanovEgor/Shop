from windows import MainWindow
from unittest.mock import patch


def test_payment_window(mocker):
    mocker.patch('windows.messagebox.showinfo')
    mocker.patch('windows.MainWindow.destroy')

    your_instance = MainWindow()
    your_instance.balance = [100, 50, 20]
    your_instance.sum = 120

    with patch('windows.Tk'):
        with patch('your_module.StringVar') as MockStringVar:
            MockStringVar.return_value = '100 рублей на карте\n50 наличными\n20 бонусами'
            your_instance.payment_window()

    # Тут нужно добавить проверки на взаимодействие с графическим интерфейсом, например, ввод значений в Entry и проверку результата
    assert your_instance.balance == [80, 50, 20]  # Проверяем изменение баланса после оплаты
    your_instance.payment_window().messagebox.showinfo.assert_called()  # Проверяем, что showinfo был вызван
