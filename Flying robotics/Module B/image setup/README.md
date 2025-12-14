# Настройка образа Raspberry Pi

### Шаг 1: Первый запуск и подключение

<img width="700" height="450" alt="Подключение к Raspberry Pi" src="https://github.com/user-attachments/assets/example-image-path" />

* После записи образа на SD-карту вставьте её в Raspberry Pi и подайте питание.
* Плата начнёт загружать образ, который по умолчанию работает в режиме точки доступа.
* Для подключения найдите Wi-Fi сеть и введите пароль: **«cloverwifi»**

### Шаг 2: Доступ к веб-интерфейсу

После успешного подключения к точке доступа откройте веб-браузер и перейдите по адресу:

```
http://192.168.11.1
```

---

**Режимы работы Wi-Fi адаптера:**

* **Режим клиента** – Raspberry Pi подключается к существующей Wi-Fi сети.
* **Режим точки доступа** – Raspberry Pi создаёт собственную Wi-Fi сеть (используется по умолчанию).

### Шаг 3: Переключение в режим точки доступа (расширенная настройка)

Для принудительного переключения адаптера в режим точки доступа выполните следующие шаги:

1. **Настройте статический IP адрес**  
   Добавьте в файл `/etc/dhcpcd.conf` следующие строки:
   ```
   interface wlan0
   static ip_address=192.168.11.1/24
   ```

2. **Настройте wpa_supplicant**  
   Замените содержимое файла `/etc/wpa_supplicant/wpa_supplicant.conf` на:
   ```
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1
   country=GB
   
   network={
       ssid="clover-1234"
       psk="cloverwifi"
       mode=2
       proto=RSN
       key_mgmt=WPA-PSK
       pairwise=CCMP
       group=CCMP
       auth_alg=OPEN
   }
   ```
   Где `clover-1234` – название вашей сети, а `cloverwifi` – пароль.

3. **Включите службу dnsmasq**  
   ```
   sudo systemctl enable dnsmasq
   sudo systemctl start dnsmasq
   ```

4. **Перезапустите службу dhcpcd**  
   ```
   sudo systemctl restart dhcpcd
   ```

После выполнения этих шагов Raspberry Pi будет работать как точка доступа с указанными параметрами сети.
