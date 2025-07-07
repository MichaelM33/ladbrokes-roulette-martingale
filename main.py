import mss
from PIL import Image
import time
import pyautogui
import random

#Author Michael
#Email: Mj33pvp@gmail.com


# Pixel positions
x, y = 2939, 881        # Result
gx, gy = 2642, 464      # Placing Bets

# Colors
RED_TARGET = (122, 21, 22)
BLACK_TARGET = (68, 68, 68)
GREEN_TARGET = (44, 197, 36)
TOLERANCE = 10

# Buttons
RED_BUTTON = (2631, 875)
BLACK_BUTTON = (2708, 875)

# Betting config
BET_SIZE = 0.1          # £0.10 per click
BASE_CLICKS = 1
MAX_CLICKS = 128
STARTING_BALANCE = 0

# State
current_bet_side = None
last_result = None
loss_streak = 0
green_seen = False

# Stats
total_rounds = 0
balance = STARTING_BALANCE
profit = 0.0



from datetime import datetime

# Get formatted startup time
start_time = datetime.now()  # ✅ datetime object
formatted_start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")



def is_similar(c1, c2, tol):
    return all(abs(a - b) <= tol for a, b in zip(c1, c2))

def calculate_bet_clicks(streak):
    return sum([BASE_CLICKS * 2 ** i for i in range(streak)]) + BASE_CLICKS

def click_multiple(pos, count, delay_before=0.3, delay_between=0.1):
    time.sleep(delay_before)
    for _ in range(count):
        pyautogui.click(pos)
        time.sleep(delay_between)



print("📢 Waiting for 'Placing Bets' at (2642, 464)... Ctrl+C to stop.")

try:
    with mss.mss() as sct:
        monitor = sct.monitors[0]

        while True:
            screenshot = sct.grab(monitor)
            img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)

            gcolor = img.getpixel((gx, gy))

            if is_similar(gcolor, GREEN_TARGET, TOLERANCE) and not green_seen:
                green_seen = True

                result_color = img.getpixel((x, y))
                if is_similar(result_color, RED_TARGET, TOLERANCE):
                    last_result = 'red'
                    print("Detected: Red Wins")
                elif is_similar(result_color, BLACK_TARGET, TOLERANCE):
                    last_result = 'black'
                    print("Detected: Black Wins")
                else:
                    print(f"Unknown result RGB{result_color}")

                # Determine bet amount before updating streak
                clicks = calculate_bet_clicks(loss_streak)
                clicks = min(clicks, MAX_CLICKS)
                bet = clicks * BET_SIZE

                # Evaluate outcome
                if current_bet_side:
                    total_rounds += 1
                    if current_bet_side == last_result:
                        balance += bet 
                        profit = balance - STARTING_BALANCE
                        print(f"✅ Won. Balance: £{balance:.2f}  Profit: £{profit:.2f}")
                        loss_streak = 0
                
                        
                        delay = random.uniform(3, 12)
                        time.sleep(delay)
                    else:
                        balance -= bet
                        profit = balance - STARTING_BALANCE
                        print(f"❌ Lost. Balance: £{balance:.2f}  Profit: £{profit:.2f}")
                        loss_streak += 1

                
                # Place next bet
                clicks = calculate_bet_clicks(loss_streak)
                clicks = min(clicks, MAX_CLICKS)

                if last_result == 'red':
                    current_bet_side = 'black'
                    print(f"Placing {clicks}x on BLACK")
                    click_multiple(BLACK_BUTTON, clicks)
                elif last_result == 'black':
                    current_bet_side = 'red'
                    print(f"Placing {clicks}x on RED")
                    click_multiple(RED_BUTTON, clicks)
                else:
                    current_bet_side = 'black'
                    print(f"Placing {clicks}x on BLACK (default)")
                    click_multiple(BLACK_BUTTON, clicks)

            elif not is_similar(gcolor, GREEN_TARGET, TOLERANCE):
                green_seen = False

            time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Stopped.")

#Author Michael
#Email: Mj33pvp@gmail.com


