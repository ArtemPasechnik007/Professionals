### Первый запуск и подключение


* После записи образа на SD-карту вставьте её в Raspberry Pi и подайте питание.
* Плата начнёт загружать образ, который по умолчанию работает в режиме точки доступа.
* Для подключения найдите Wi-Fi сеть и введите пароль: **«cloverwifi»**
  
<img width="374" height="263" alt="image" src="https://github.com/user-attachments/assets/8bdedbd8-d028-4b65-afc9-7226f6a37a28" /> <img width="405" height="261" alt="image" src="https://github.com/user-attachments/assets/edc75907-09bd-4576-9ab1-553b00fc424c" />



### Доступ к веб-интерфейсу

После успешного подключения к точке доступа откройте веб-браузер и перейдите по адресу:

```
http://192.168.11.1
```



<img width="602" height="320" alt="image" src="https://github.com/user-attachments/assets/d028a2eb-7985-4fb5-92b9-95c2f09eb3a2" />


**Режимы работы Wi-Fi адаптера:**

* **Режим клиента** – Raspberry Pi подключается к существующей Wi-Fi сети.
* **Режим точки доступа** – Raspberry Pi создаёт собственную Wi-Fi сеть (используется по умолчанию).

# Настройка Wi-Fi на Raspberry Pi

### Первоначальное подключение к образу


* После установки образа вставьте SD-карту в Raspberry Pi и включите питание
* Система загрузится в режиме **точки доступа** по умолчанию
* Найдите Wi-Fi сеть Raspberry Pi и подключитесь с паролем: **«cloverwifi»**

### Доступ к веб-интерфейсу

После подключения к точке доступа откройте браузер и перейдите по адресу:

```
http://192.168.11.1
```



**Режимы работы Wi-Fi адаптера Raspberry Pi:**

* **Режим клиента** – Raspberry Pi подключается к существующей Wi-Fi сети
* **Режим точки доступа** – Raspberry Pi создаёт собственную Wi-Fi сеть (режим по умолчанию)

### Переключение в режим клиента (подключение к домашней Wi-Fi сети)
Открываем **web terminal**
пароль от него:
   ```
   Raspberry
   ```
Для переключения адаптера из режима точки доступа в режим клиента выполните следующие действия:

1. **Выключите службу dnsmasq**
   ```
   sudo systemctl stop dnsmasq
   sudo systemctl disable dnsmasq
   ```

2. **Настройте получение IP-адреса через DHCP**  
   Удалите из файла `/etc/dhcpcd.conf` строки:
   ```
   interface wlan0
   static ip_address=192.168.11.1/24
   ```

3. **Настройте подключение к вашей Wi-Fi сети**  
   Замените содержимое файла `/etc/wpa_supplicant/wpa_supplicant.conf` на:
   ```
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1
   country=GB
   
   network={
       ssid="ВАШ_SSID"
       psk="ВАШ_ПАРОЛЬ"
   }
   ```
   Где `ВАШ_SSID` – название вашей Wi-Fi сети, а `ВАШ_ПАРОЛЬ` – пароль от неё.

4. **Перезапустите сетевую службу**
   ```
   sudo systemctl restart dhcpcd
   ```

После выполнения этих шагов Raspberry Pi переподключится к вашей домашней Wi-Fi сети как клиент. Для доступа к веб-интерфейсу потребуется узнать новый IP-адрес устройства в вашей локальной сети.

---

Перейдем к навигации нашего дрона 

# Навигация по картам ArUco-маркеров

Модуль `aruco_map` распознает карты ArUco-маркеров как единое целое и поддерживает навигацию с использованием механизма **Vision Position Estimate (VPE)**.



### Конфигурация системы

#### 1. Базовая настройка в `clover.launch`
Установите значение `true` для аргумента `aruco` в файле: `~/catkin_ws/src/clover/clover/launch/clover.launch`


```xml
<arg name="aruco" default="true"/>
```

#### 2. Настройка модуля ArUco в `aruco.launch`
В файле `~/catkin_ws/src/clover/clover/launch/aruco.launch` установите:
```xml
<arg name="aruco_detect" default="true"/>
<arg name="aruco_map" default="true"/>
<arg name="aruco_vpe" default="true"/>
```
Где `aruco_vpe` включает передачу координат в полетный контроллер по механизму VPE.

#### 3. Структура файла карты маркеров
Карта загружается из текстового файла формата:
```
id_маркера размер_маркера x y z угол_z угол_y угол_x
```
* `угол_N` – угол поворота маркера вокруг оси N в радианах

#### 4. Расположение и загрузка карт
* Файлы карт размещаются в каталоге: `~/catkin_ws/src/clover/aruco_pose/map`
* Название файла карты задается аргументом `map`:
  ```xml
  <arg name="map" default="map.txt"/>
  ```

### Генерация карты маркеров

Для создания файла карты используйте инструмент `genmap.py`:

```bash
rosrun aruco_pose genmap.py length x y dist_x dist_y first -o имя_файла.txt
```

**Параметры команды:**

* `length` – размер маркера (в метрах)
* `x` – количество маркеров по оси X
* `y` – количество маркеров по оси Y
* `dist_x` – расстояние между центрами маркеров по оси X
* `dist_y` – расстояние между центрами маркеров по оси Y
* `first` – ID первого маркера (левого нижнего)
* `-o имя_файла.txt` – название выходного файла

**Дополнительные опции:**
* `--bottom-left` – нумерация маркеров с левого нижнего угла

**Пример генерации карты:**
```bash
rosrun aruco_pose genmap.py 0.33 2 4 1 1 0 -o test_map.txt
```
Создает карту 2×4 маркеров размером 0.33 м с расстоянием 1 м между ними, начиная с ID 0.

---

Устанавливаем требуемые файлы для шоу

# Установка ПО clever-show на образ clever v0.23
Настройте подключение к WiFi сети вашего роутера согласно [инструкции](https://clover.coex.tech/ru/network.html#%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B0%D0%B4%D0%B0%D0%BF%D1%82%D0%B5%D1%80%D0%B0-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D0%B0)

Обновите репозитории apt:
```bash
sudo apt-get update
```

Загрузите репозиторий clever-show и установите необходимые для клиента зависимости
```
git clone https://github.com/CopterExpress/clever-show.git --branch python3
sudo chown -R root:root /home/pi/clever-show/
sudo pip3 install -r /home/pi/clever-show/drone/requirements.txt --upgrade
```

Установите chrony и установите конфигурацию по умолчанию:
```bash
sudo apt-get install -y chrony
```

```bash
sudo cp /home/pi/clever-show/examples/chrony/client.conf /etc/chrony/chrony.conf
sudo systemctl restart chrony
```

Скопируйте файлы сервисов clever-show и запустите их:
```bash 
sudo cp /home/pi/clever-show/builder/assets/clever-show.service /lib/systemd/system/
sudo systemctl enable clever-show.service
sudo systemctl start clever-show.service


sudo cp /home/pi/clever-show/builder/assets/failsafe.service /lib/systemd/system/
sudo systemctl enable failsafe.service
sudo systemctl start failsafe.service
```
После успешной установки перезапустите RPi и проверьте наличине вашего дрона в сервере 

Также для успешной анимации и навигации дрона нам нужно изменить несколько параметров в файле:
```bash
ДОБАВИТЬ
```

