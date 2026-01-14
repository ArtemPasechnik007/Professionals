#ДЕЛЕНИЕ LED ленты на 3 части и управление каждой из них
import rospy
from led_msgs.srv import SetLEDs
from led_msgs.msg import LEDStateArray, LEDState

rospy.init_node('flight')

set_leds = rospy.ServiceProxy('led/set_leds', SetLEDs)  # define proxy to ROS service

num_leds = 71
led_states = []

# Вычисляем размер каждой части
part_size = num_leds // 3
remainder = num_leds % 3  # Остаток для равномерного распределения

# Определяем границы для каждой части
first_part_end = part_size
second_part_end = 2 * part_size + (1 if remainder > 0 else 0)  # Учитываем остаток для второй части
# Третья часть до конца

for i in range(num_leds):
    if i < first_part_end:  # первая часть - красные
        led_states.append(LEDState(i, 255, 0, 0))  # красный цвет
    elif i < second_part_end:  # вторая часть - синие
        led_states.append(LEDState(i, 0, 0, 255))  # синий цвет
    else:  # третья часть - белые
        led_states.append(LEDState(i, 255, 255, 255))  # белый цвет (все компоненты на максимум)

# отправляем команду на установку цветов
set_leds(led_states)
