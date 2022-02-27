
# Dwellers_Bot 
> Telegram бот для дружных и современных соседей + WEB-приложение. (Жителей жилых комплексов)
Стадия: Концепт

👋 Привет! Это проект веб-приложения для жителей частного посёлка. Пока что концепт умного инструмента для жителей, который будет развиваться и разрабатываться модульно.

Основная идея позволить жителям упростить, централизовать и цифровизовать жизнь в посёлке. Жизнь в стиле HighTech и все такое да. 

## Проблема
В коттеджном поселке где я вырос и сейчас живут мои родные всегда было проблематично собирать всех жителей на различные мероприятия, информировать о различных событиях, добавлять новых соседей в чатик, выставление счетов о оплате коммунальных услуг и постоянно писать охранику, чтобы пропустил машину.
Все это конечно решалось общим чатиком и активными жителями поселка, однако из-за не прозрачности, не централизованого процесса, флуда в общем чате и т.д. возникали различные не до понимания, конфликты, жители просто не участовали в жизни поселка. Это нужно было решать. 
## Решение
Первоначально я предложил разработать простенький телеграмм-бот для регистрации и пропуска в закрытый чат жильцов. Однако идея развилась и теперь это будет сайт, с различными полезными функциями и по типу соцсети соседей и с интеграцией Телеграм-бота. 
## Основные идеи:
- Для авторизации бот/сайт просит секретный код для входа, либо фото с видом из окна или селфи. Также указываете имя и где он живет. Администратору приходит заявку, он ее принимает или отклоняет. После этого бот генерирует одноразовую ссылку на закрытый чат и регестрирует в системе. 
- Принимать заявки на пропуск автомобилей и передавать в охрану.
- Уведомление о мероприятиях, событиях и т.д.
- Колл-центр. Возможность пожаловаться на мусор в поселке, высказать свое предложение или жалобу.
- Полезная информация для жителей. Номера телефонов различных служ, инженеров, охраны, вывоза мусора и т.д.
## В будущем
- Барахолвка. Возможность выставить объявление с возможностью аукциона. 
- Регистрация на различные мероприятия, занятия и т.д.
- Выставление счето за свет/воду, охрану и вывоз мусора. 
- Сервисы. Внутренняя реклама. Различные услуги и т.д.
# В далеком будущем если все получится.
- Возможность по нажатию открывать калитку и шлагбаум.
- Посмотреть с видеокамер. 
- На Raspberry Pi прикрутить нейронку, чтобы через камеру распозновал номер машины и автоматически открывал шлагбаум. Тем самым экономия головняка для охраны. 
- Возможность масшатибровать проект, чтобы его могли использовать кто хочет. 
## Технический стек
- Backend:
- - Python
- - Django
- - SQLAlchemy + Alembic
- - DB: PostgreSQL + Redis
- - Aiogram - телеграм
- Fronted: 
- - Flutter(dart)
- Для аналитики ClickHouse(дешборд) /* Для практики своих навыков

## Чему я планирую научиться?
- Разработка на Django и Python
- Практика с Telegram API и с AIOGRAM
- SQLAlchemy + Alembic
- Не множно в верстке по практиковаться
- Docker и прочая мелочь по DevOps
- Ведение проекта
- Визуализация отчетности и админка
- Ну и самая главная, бюрократическая. Это же все надо объяснить, показать и научить всех. Это самое сложное будет. 

## Что готово?
Чекайте Projects и Issues. 




