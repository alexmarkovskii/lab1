# Перечень тестов

## Аттестационные тесты

### Тест А1 (позитивный)
 - **Цель:** Тестирование перехода в меню настроек игры перед её запуском
 - **Входные данные:** Пользователь нажимает на кнопку "START VS PC" или "START VS USER"
 - **Ожидаемый результат:** Пользователь попадает в меню выбора параметров игры

### Тест А2 (позитивный)
 - **Цель:** Тестирование выбора типа игры
 - **Входные данные:** Пользователь, находясь в меню настроек игры, нажатием на одну из кнопок изменяет тип игры
 - **Ожидаемый результат:** Изменяется тип игры

### Тест А3 (позитивный)
 - **Цель:** Тестирование ввода игрового параметра(время игры/лимит очков)
 - **Входные данные:** Пользователь вводит положительное целочисленное значение в поле для ввода игрового параметра и нажимает на кнопку сохранения
 - **Ожидаемый результат:** Игровой параметр сохраняется в текстовом поле, при запуске игры, в зависимости от её типа, он влияет на условие окончания игры

### Тест А4 (негативный)
 - **Цель:** Тестирование ввода игрового параметра(время игры/лимит очков)
 - **Входные данные:** Пользователь вводит не целочисленное/положительное значение в поле для ввода игрового параметра и нажимает на кнопку сохранения
 - **Ожидаемый результат:** При нажатии на кнопку сохранения игрового параметра выводится сообщение об ошибке и поле ввода очищается от некорректного значения

### Тест А5 (позитивный)
 - **Цель:** Тестирование текстового поля ввода
 - **Входные данные:** Пользователь нажимает на кнопку "очистить" находящуюся вместе с текстовым полем
 - **Ожидаемый результат:** Текствое поле очищается от текущего ввода

### Тест А6 (позитивный)
 - **Цель:** Тестирование возможности 
 - **Входные данные:** Пользователь, находясь в меню настроек игры нажимает на кнопоку "BACK"
 - **Ожидаемый результат:** Пользователь возвращается в главное меню игры из меню настроек

### Тест А7 (позитивный)
 - **Цель:** Тестирование запуска игры из меню настроек
 - **Входные данные:** Пользователь вводит игровой параметр в текстовое поле и нажимает на кнопку "START", находясь в меню настроек
 - **Ожидаемый результат:** Запускается игра с выбранным типом и игровым параметром из текстового поля меню настроек

### Тест А8 (негативный)
 - **Цель:** Тестирование запуска игры из меню настроек
 - **Входные данные:** Пользователь нажимает на кнопку "START" находясь в меню настроек, пропуская ввод игрового параметра
 - **Ожидаемый результат:** Вывод сообщения об ошибке, пользователь остается в меню настроек

### Тест А9 (позитивный)
 - **Цель:** Тестирование отображения статистики
 - **Входные данные:** Пользователь нажимает на кнопку "VEIW STATISTICS" в главном меню(ранее были игры)
 - **Ожидаемый результат:** На экране отображается статистика прошедших ранее игр

### Тест А10 (негативный)
 - **Цель:** Тестирование отображения статистики
 - **Входные данные:** Пользователь нажимает на кнопку "VEIW STATISTICS" в главном меню(ранее не было ни одной игры)
 - **Ожидаемый результат:** Вывод сообщения об отсутствии статистики, т.к. не было ещё ни одной записанной игры

### Тест А11 (позитивный)
 - **Цель:** Тестирование выхода из приложения
 - **Входные данные:** Пользователь нажимает на кнопку "QUIT" в главном меню
 - **Ожидаемый результат:** Приложение закрывается

## Блочные тесты

### Тест M1 (позитивный)
 - **Цель:** Проверка отскока мяча от нижней/верхней границы
 - **Входные данные:** Вызов метода move() класса BALL с передачей в него объектов ракеток, столкновение с нижней/верхней границей
 - **Ожидаемый результат:** Мяч изменяет свое вертикальное направление на противоположное

### Тест M2 (позитивный)
 - **Цель:** Проверка отскока мяча от ракетки
 - **Входные данные:** Вызов метода move() класса BALL с передачей в него объектов ракеток, столкновение с ракеткой
 - **Ожидаемый результат:** Мяч изменяет свое горизонтальное направление на противоположное

### Тест M3 (позитивный)
 - **Цель:** Проверка начисления очков игрокам
 - **Входные данные:** Вызов метода move() класса BALL с передачей в него объектов ракеток, пересечение левой/правой границы мячом
 - **Ожидаемый результат:** Изменение параметра score

### Тест M4 (позитивный)
 - **Цель:** Проверка движения ракетки
 - **Входные данные:** Вызов метода move() класса PADDLE с передачей параметра направления движения
 - **Ожидаемый результат:** Координаты ракетки изменяются в зависимости от направления движения

### Тест M5 (негативный)
 - **Цель:** Проверка ограничения движения ракетки
 - **Входные данные:** Вызов метода move() класса PADDLE с передачей параметра направления движения
 - **Ожидаемый результат:** При достижении границ игрового поля, изменение координат прекращается

### Тест M6 (позитивный)
 - **Цель:** Проверка записи статистики в новый файл
 - **Входные данные**: Вызов метода write_statistics() c параметром записываемого значения
 - **Ожидаемый результат:** Создается файл 'statistics.csv', записывается новое значени

### Тест M7 (позитивный)
 - **Цель:** Проверка записи статистики в существующий файл
 - **Входные данные**: Вызов метода write_statistics() c параметром записываемого значения
 - **Ожидаемый результат:** Значение записывается в файл 'statistics.csv'
