import pyautogui
import pygetwindow as gw
from PIL import Image

# ===== 설정 =====
MINECRAFT_WINDOW_TITLE = "Minecraft* 1.21"
activated_once = False          # 창 활성화 1회
esc_pressed_once = False        # ESC 1회

# ===== 마인크래프트 창 활성화 =====
def activate_minecraft_once():
    global activated_once, esc_pressed_once

    if not activated_once:
        windows = gw.getWindowsWithTitle(MINECRAFT_WINDOW_TITLE)
        if not windows:
            raise Exception(f'"{MINECRAFT_WINDOW_TITLE}" 창을 찾을 수 없음.')

        win = windows[0]
        try:
            win.activate()
        except Exception:
            win.minimize()
            win.restore()

        activated_once = True

        # === 처음 창 활성화 후 ESC 한 번 눌러 일시정지 해제 ===
        pyautogui.sleep(0.3)
        if not esc_pressed_once:
            pyautogui.press('esc')
            esc_pressed_once = True
            pyautogui.sleep(0.2)


# ===== 채팅 입력 함수 =====
def send_chat(msg):
    activate_minecraft_once()

    pyautogui.press('t')   # 채팅창 열기
    pyautogui.write(msg)
    pyautogui.press('enter')


# ===== 이미지 → ASCII 변환 =====
ASCII_CHARS = ['@', '%', '#', '``', '+', '=', '-', ':::', '...', ' ', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def resize_image(image, new_width=30):
    w, h = image.size
    ratio = h / w
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    result = ""
    for pixel in pixels:
        # 기존 밝기 구간 기준으로 문자 선택
        if pixel < 25:
            char = '@'
        elif pixel < 50:
            char = '#'
        elif pixel < 75:
            char = '*'
        elif pixel < 100:
            char = '+'
        elif pixel < 125:
            char = ':'
        elif pixel < 150:
            char = '.'
        else:
            char = ' '

        # 폭 맞춤
        if char == '.':
            char = '...'
        elif char == ':':
            char = ':::'
        elif char == '*':
            char = '**'

        result += char
    return result


def convert_image_to_ascii(path, width=30):
    img = Image.open(path)
    img = resize_image(img, width)
    img = grayify(img)

    ascii_str = pixels_to_ascii(img)

    result = []
    for i in range(0, len(ascii_str), img.width):
        result.append(ascii_str[i:i + img.width])

    return result


# ===== 이미지 → 마인크래프트 ASCII 전송 =====
def send_image_as_ascii(path, width=30, delay=0.1):
    lines = convert_image_to_ascii(path, width)

    print(f"[INFO] 총 {len(lines)}줄 전송 시작")

    for line in lines:
        send_chat(line)
        pyautogui.sleep(delay)


# ===== 메인 =====
if __name__ == "__main__":
    img_path = input("이미지 파일 경로 입력: ").strip()
    width = int(input("ASCII 가로 길이 (기본 30): ") or "30")

    send_image_as_ascii(img_path, width=width, delay=0.15)
    print("전송 완료!")
