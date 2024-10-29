def test_function ():
    def inner_function ():
        print("Я в области видимости функции test_function")
    inner_function()  # ничего не возвращает


test_function()  # inner_function успешно срабатывает при вызове test_function
inner_function() # вызов inner_function вне ф-ции test_function приводит к ошибке (имя этой ф-ции не определено)

