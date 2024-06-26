# Лабораторная работа №11

С докером работаем здесь: https://labs.play-with-docker.com

## Задание №1

Как результат выполнения лабораторной работы, предоставить отчёт (в свободной форме) со всеми командами и скриншотами ИЛИ выписать себе команды и затем показать весь запуск команд лично преподавателю.


### Контейнер с httpd

Необходимо создать контейнер из образа `httpd`. Ссылка на образ, где вы найдёте различную информацию об образе: https://hub.docker.com/_/httpd

1) Запустить контейнер указав ему имя и порты (внешний порт выбрать любой)
2) Проверьте, что контейнер появился в списке контейнеров
3) Откройте сервис в контейнере по нужному порту, сверху сайта нажмите `OPEN PORT` и введите нужный порт. Проверьте, открывается ли сайт в контейнере.
4) Проверьте, скачен ли образ `httpd`
5) Попробуйте войти внутрь контейнера. Внутри перейдите в нужный каталог командой:
   
```bash
cd /usr/local/apache2/htdocs/
```
Установите `nano` с помощью команд:

```bash
apt update
apt install nano
```

Откройте файл `index.html` командой:

```bash
nano index.html
```

и замените html-код на другой. Чтобы выйти из редактирования нажмите по очереди: `ctrl+o`, `enter`, `ctrl+x`. Снова перейдите в браузер и проверьте изменения.

После выйдете из контейнера, написав команду `exit`.

6) Остановите и удалите ваш контейнер

### Контейнер с сервисом на выбор

1) Найдите на [Docker Hub](https://hub.docker.com/) интересный для вас сервис
2) Скачайте образ этого сервиса самостоятельно с помощью команды `docker pull <имя образа>`
3) Запуститье контейнер из этого образа с выбранными настройками

## Задание №2

Необходимо написать программу на любом языке программирования, такую, чтобы её можно было запустить на сервере linux (без интерфейса, максисмум - web-интерфейс). Для этой программы необходимо создать образ с помощью `Dockerfile` и далее создать контейнер на основе этого образа.

## Задание №3

С помощью virtualbox создать виртуальную машину с Debian.

Порядок действий:
1. Скачать образ Debian с [оффициального сайта](https://www.debian.org/download)
2. Запустить virtualbox и выбрать создание новой виртуальной машины
3. Указать имя виртуальной машины, выбрать скаченный образ, поставить галочку "Пропустить автоматическую установку"
4. Указать любое значение для основной памяти в диапазоне от 4 ГБ до 8 ГБ, указать любое значение для процессора в диапазоне от 2 ЦП до 4 ЦП
5. Создать новый виртуальный жёсткий диск, размером не менее 20 ГБ
6. Запустить машину, выбрать пункт `Install` (второй по счёту) и самостоятельно (интуитивно) произвести установку
7. После входа в систему, нажатием на ПКМ по рабочему столу открыть параметры дисплея и выставить большее разрешение дисплея
8. Открыть терминал (можно найти в меню приложений) и последовательно прописать следующие команды:

```bash
sudo apt update

sudo apt install neofetch

neofetch
```

На этом выполение задания завершено, можно выключать виртуальную машину.
