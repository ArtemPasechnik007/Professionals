# Методичка по установке и настройке сервера для Clever Show 0.4 Alpha 6

## 1. Установка Python 3.9.7

### 1.1 Скачивание и запуск установщика
- Скачайте Python 3.9.7 (64-bit) с официального сайта
- Запустите установочный файл `python-3.9.7-amd64.exe`

### 1.2 Настройка установки Python
**На первом экране установщика:**
1. Выберите **Customize installation**
2. **ВАЖНО:** Установите галочку **☑ Add Python 3.9 to PATH**

**На экране Optional Features:**
- Установите все галочки:
  - [x] Documentation
  - [x] pip
  - [x] tcl/tk and IDLE
  - [x] Python test suite
  - [x] py launcher for all users
- Нажмите **Next**

**На экране Advanced Options:**
1. Установите галочку **☑ Install for all users**
2. Проверьте путь установки: `C:\Program Files\Python39`
3. Нажмите **Install**
<img width="974" height="598" alt="image" src="https://github.com/user-attachments/assets/a3e5ce6d-d91a-4239-84b1-caba708f23cb" />
<img width="974" height="595" alt="image" src="https://github.com/user-attachments/assets/5d6c1543-9b8f-4c49-a5d4-64cee77932bd" />
<img width="974" height="595" alt="image" src="https://github.com/user-attachments/assets/2f42fffe-0a89-4f60-ae9e-27f4128847f3" />


## 2. Подготовка сервера Clever Show

### 2.1 Скачивание архива
- Скачайте архив [clever-show-0.4-alpha.6](https://github.com/CopterExpress/clever-show/archive/refs/tags/v0.4-alpha.6.zip)
- **Рекомендуется:** Сохраните архив на диск `C:\` для удобства

### 2.2 Распаковка архива
1. Извлеките все файлы из архива
2. Путь к серверу будет: `C:\clever-show-0.4-alpha.6\clever-show-0.4-alpha.6\server`

### 2.3 Настройка файла requirements.txt
1. Перейдите в папку: `C:\clever-show-0.4-alpha.6\clever-show-0.4-alpha.6\server`
2. Откройте файл `requirements.txt` в текстовом редакторе
3. Удалите версии библиотек, оставив только названия
4. Файл должен иметь вид:
```
configobj
numpy
PyQt5
PyQt5-sip
Quamash
selectors2
six
```
<img width="426" height="592" alt="image" src="https://github.com/user-attachments/assets/a10b034c-c078-41df-be6f-2ebd74e68704" />


## 3. Установка зависимостей

### 3.1 Запуск командной строки
1. Нажмите `Win + X`
2. Выберите **Командная строка (администратор)** или **Windows PowerShell (администратор)**

### 3.2 Установка библиотек
Выполните последовательно команды:

```bash
cd C:\clever-show-0.4-alpha.6\clever-show-0.4-alpha.6\server
pip3 install -r requirements.txt
```

## 4. Запуск сервера

### 4.1 Основной запуск
```bash
python server.py
```

## 5. Решение проблем с отображением дрона

Если после запуска сервера дрон не отображается:
<img width="1362" height="856" alt="image" src="https://github.com/user-attachments/assets/3ea08430-6ed4-494c-99d0-47b4d182fc96" />


### 5.1 Изменение метрики сети
1. Откройте **Панель управления**
2. Перейдите в **Сеть и Интернет → Центр управления сетями и общим доступом**
3. Нажмите на ваше подключение (беспроводная сеть, к которой подключен дрон)
4. Нажмите **Свойства**
5. Выберите **IP версии 4 (TCP/IPv4)**
6. Нажмите **Свойства**
7. Нажмите **Дополнительно**
8. **Снимите галочку** с "Автоматическое назначение метрики"
9. В поле "Метрика интерфейса" введите: **1**
10. Нажмите **ОК** во всех открытых окнах

### 5.2 Перезапуск сервера
1. Закройте сервер (Ctrl+C в командной строке)
2. Запустите заново:
```bash
python server.py
```

## 6. Проверка работоспособности

После настройки метрики и перезапуска сервера:
- Должен появиться интерфейс сервера
- Ваш дрон должен отображаться в списке доступных устройств

## 7. Дополнительные рекомендации

- Убедитесь, что дрон и компьютер находятся в одной сети
- Проверьте, что брандмауэр не блокирует соединение
- При возникновении ошибок проверьте лог сервера в командной строке

## 8. Быстрые команды для копирования

```bash
cd C:\clever-show-0.4-alpha.6\clever-show-0.4-alpha.6\server
pip3 install -r requirements.txt
python server.py
```
