# 🎰 Automated Roulette Betting Bot

A Python-based automation script that visually detects roulette outcomes on-screen and places bets accordingly using a progressive betting strategy.

**Author**: Michael  
**Email**: Mj33pvp@gmail.com

---

## 📌 Description

This script captures your screen, detects the result of a roulette game based on pixel colors, and automatically places bets using `pyautogui`. It uses a Martingale-like strategy by increasing bet size after each loss and switching colors based on outcomes.

---

## ⚙️ Features

- 🖥️ **Screen Pixel Monitoring** via `mss` and `PIL`
- 🎯 **Color Detection** for Red, Black, and Green
- 🤖 **Automatic Betting** using mouse clicks
- 📊 **Profit/Loss Tracking**
- 🔁 **Martingale-style Strategy** (increases bet size on loss)
- 🎲 **Random Delays** for realism and detection evasion

---

## 🧠 How It Works

1. **Waits** for the game to show "Placing Bets".
2. **Detects** the result (Red/Black) using screen color sampling.
3. **Calculates** the appropriate number of clicks based on the loss streak.
4. **Places a bet** on the opposite color of the last result.
5. **Tracks** total rounds, balance, and profit over time.

---

## 🎨 Color Codes

| Color  | RGB Value         |
|--------|-------------------|
| Red    | (122, 21, 22)     |
| Black  | (68, 68, 68)      |
| Green  | (44, 197, 36)     |

A `TOLERANCE` of 10 is used for approximate color matching.

---

## 📌 Pixel Positions (Adjust if needed)

| Element         | X     | Y     |
|----------------|-------|-------|
| Result Pixel   | 2939  | 881   |
| Betting Pixel  | 2642  | 464   |
| Red Button     | 2631  | 875   |
| Black Button   | 2708  | 875   |

---

## 💸 Betting Configuration

- **Base Bet per Click**: £0.10  
- **Bet Doubling Strategy**: Martingale (2x after loss)  
- **Maximum Clicks**: 128  
- **Balance Tracking**: Starts from £0.00

---

## 🧰 Requirements

Install the following Python packages:


---

## 🚀 Running the Script

> ⚠️ Make sure your game window is visible and not minimized. Position it correctly on the screen to match pixel coordinates.


Press `Ctrl+C` to stop at any time.

---

## 📅 Example Output


---

## 🛑 Disclaimer

This code is for **educational purposes only**. Automating betting systems may violate the terms of service of platforms and could lead to account bans or legal consequences. Use responsibly.

---

## 📬 Contact

Feel free to contact the author for questions, improvements, or collaboration ideas:

**Michael** – Mj33pvp@gmail.com


