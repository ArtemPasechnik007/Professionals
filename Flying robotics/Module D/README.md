# Модуль D: Посадка на движущуюся платформу

Данный модуль содержит программное обеспечение для автономного управления квадрокоптером в рамках двух задач:
1. **Доставка груза** на движущуюся платформу с использованием сервопривода.
2. **Следование за движущимся объектом** и посадка на него.

Проект включает два независимых скрипта, каждый из которых решает соответствующую задачу. Все необходимое оборудование установлено, программа написана и протестирована в ходе тестовых и зачетных полетов. Предпочтительно выполнение посадки или доставки с первой попытки.

---

## Скрипт 1: Доставка груза на движущуюся платформу

*Описание:*  
Данный скрипт обеспечивает взлет, поиск движущейся платформы (маркер ArUco), точное зависание над ней и сброс груза с помощью сервопривода. Алгоритм включает стабилизацию позиции относительно маркера и управление сервомеханизмом для release груза.

*Место для кода:*  
```python
# Код для доставки груза будет размещен здесь
# Основная логика: 
# 1. Взлет и поиск маркера
# 2. Позиционирование над платформой
# 3. Активация сервопривода для сброса груза
# 4. Возврат или посадка
```

---

## Скрипт 2: Следование за объектом и посадка на него

*Описание:*  
Скрипт реализует алгоритм слежения за движущейся платформой (по маркеру ArUco) и мягкую посадку на неё. Квадрокоптер отслеживает высоту платформы, корректирует свою позицию и выполняет постепенное снижение до контакта.

### Код скрипта слежения и посадки:
```python
#coding: Utf8
#!/usr/bin/env python
from math import isnan
from math import pi
import rospy
from clover import srv
from std_srvs.srv import Trigger
from clover.srv import SetLEDEffect
from mavros_msgs.srv import CommandBool


rospy.init_node('flight')
get_telemetry = rospy.ServiceProxy('get_telemetry',srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
arming = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)


z=2
def follow(z):

    while(True):
        navigate(x=0, y=0, z=1.5-z, speed=0.5, frame_id='navigate_target')
        
        if isnan(get_telemetry(frame_id='aruco_72').z):
            rospy.sleep(0.2)
            pass


        z=get_telemetry(frame_id='aruco_72').z
        while (z >= 0.3):
            set_position(x=0, y=-0.15, z=z, yaw=pi*0.5, frame_id='aruco_72')
            z = z - 0.05
            r.sleep()

        if (z <= 0.3):
            navigate(x=0, y=0, z=-1, speed=2, frame_id='body')
            rospy.sleep(0.2)
            arming(False)
            break

r=rospy.Rate(5)
navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
rospy.sleep(3)

follow(2)
```

### Логика работы:
1. **Инициализация** — взлет на высоту 1.5 м.
2. **Слежение** — поддержание позиции относительно маркера `aruco_72`.
3. **Последовательное снижение** — плавное уменьшение высоты до 0.3 м над платформой.
4. **Посадка** — финальное снижение и отключение моторов.

---

## Требования
- ROS (Robot Operating System)
- Пакет `clover` для симуляции/реального квадрокоптера
- Камера и система распознавания ArUco маркеров
- Настроенная движущаяся платформа с маркером

## Запуск
1. Убедитесь, что ROS и необходимые пакеты установлены.
2. Запустите симулятор или подключитесь к реальному коптеру.
3. Для запуска скрипта посадки выполните:
   ```bash
   python landing_script.py
   ```
4. Для запуска скрипта доставки (код будет добавлен) используйте аналогичную команду.

---

## Примечания
- Оба скрипта написаны для работы в реальном времени и требуют точной калибровки камеры и системы позиционирования.
- Рекомендуется проводить тестовые полеты в безопасной зоне.
- Для увеличения надежности можно настроить параметры скорости, высоты и частоты опроса маркера.
