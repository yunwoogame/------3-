import pyautogui
import time

# 첫 번째 클릭 위치
pyautogui.click(3650, 360)
pyautogui.click(3650, 360)

x, y = 1900,1180
 
# 원하는 대기 시간 설정 (초 단위), 예를 들어 5초 후에 다시 클릭하고 싶다면
time_line = 45

# 설정한 시간만큼 대기
time.sleep(time_line)

# 동일한 위치에서 다시 클릭
pyautogui.click(x, y)

