# **Pong**
>   *Pong* является простым спортивным симулятором настольного тенниса. Небольшой квадратик, заменяющий пинг-понговый мячик, двигается по экрану по линейной траектории. Если он ударяется о периметр игрового поля, то его траектория изменяется в зависимости от угла столкновения. Если шарик отбивается ракеткой игрока, то его движение дополнительно зависит от скорости и направления движения ракетки. 

<img src="https://github.com/alexmarkovskii/lab1/blob/main/pong.gif" data-canonical-src="https://github.com/alexmarkovskii/lab1/blob/main/pong.gif" width="800" height="300" />


## Пользователь может:
- Запустить игру в одном из двух режимов(против компьютера или против другого пользователя) и выбрать один из двух типов игры.
- Выбрать тип игры (По времени или по достижению определенного счёта).
- Сохранить свой счёт в таблице рекордов.
- Отобразить таблицу рекордов на экране.

### Выбор типа игры:
- Пользователь нажимает на кнопку "Выбрать режим" в графическом интерфейсе игры.
Приложение отображет форму, на которой пользователь может выбрать один из двух режимов игры.
    - Игра на время. Пользователь в графическом интерфейсе выбирает время, в течение которого будет продолжаться игра.
    - Игра до "победного" счёта. Пользователь в графическом интерфейсе выбирает счёт, при достижении которого одним из игроков, игра заканчивается.

### Запуск игры против компьютера:
- Пользователь нажимает на кнопку "Играть одному" в графическом интерфейсе игры.
Приложение отображает игровое поле Pong'а, где слева "ракетка" пользователя, а справа - компьютера. В левом верхнем углу интерфейса отображается текущее время игры, а в правом - счёт. 
 - Пользователь управляет своей ракеткой при помощи кнопок "Up" и "Down" на клавиатуре. На экране ракетка изменяет своё положение.
 - Игра продолжается в зависимости от выбранного режима до тех пор, пока не выйдет время или не будет достигнут "победный" счёт. После окончания игры пользователю будет предложено внести свой текущий результат в таблицу рекордов.

### Запуск игры против другого пользователя:
- Пользователь нажимает на кнопку "Играть вдвоём" в графическом интерфейсе игры.
Приложение отображает игровое поле Pong'а, где слева "ракетка" пользователя, а справа - противника. В левом верхнем углу интерфейса отображается текущее время игры, а в правом - счёт. 
- Игрок "слева" управляет своей ракеткой при помощи клавиш **W** и **S**, игрок "справа" управляет ракеткой при помощи клавиш **UP** и **Down** на клавиатуре. На экране обе ракетки изменяют своё положение в зависимости от действий пользователя.
- Игра продолжается в зависимости от выбранного режима до тех пор, пока не выйдет время или не будет достигнут “победный” счёт. После окончания игры "победителю" будет предложено внести свой результат в таблицу рекордов.

### Сохранение результата в таблицу рекордов:
- В конце каждой игры на экране появляется форма, запрашивающая имя пользователя.
Пользователь может ввести своё имя и подтвердить внесение результата игры в таблицу рекордов нажатием кнопки "OK", расположенной внизу отображаемой формы.
Пользователь может закрыть появившуюся форму, в таком случае результат не будет внесен в таблицу рекордов.

### Отображение таблицы рекордов на экране:
- Пользователь нажимает на кнопку "Таблица рекордов" в графическом интерфейсе игры.
На экране отображается таблица рекордов, отображающая отсортированные по счёту записи в двух режимах(по счёту и по времени). 
