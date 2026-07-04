# 🐍 Pradeepp Snake Game

A classic **Snake Game** built using **Python** and **Pygame**, featuring sound effects, background music, high-score tracking, pause functionality, and a standalone Windows executable.

---

## ✨ Features

- 🎮 Start Menu
- 🐍 Snake Growth
- 🍎 Random Food Generation
- 🔊 Eat Sound Effect
- 💀 Game Over Sound
- 🎵 Background Music
- 🏆 High Score Saving
- ⚡ Dynamic Speed Increase
- 🔁 Restart Game
- ⏸️ Pause & Resume
- 🚧 Wall Collision Detection
- 🐍 Self Collision Detection
- 🖥️ Custom Game Icon
- 📦 Windows Executable (.exe)

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬆️ ⬇️ ⬅️ ➡️ | Move Snake |
| **SPACE** | Start Game |
| **P** | Pause / Resume |
| **R** | Restart (Game Over Screen) |
| **ESC** | Quit Game |

---

## 📂 Project Structure

```
snake_game/
│
├── snakegame.py
├── highscore.txt
├── README.md
├── images/
│   ├── apple.png
│   ├── icon.png
│   └── icon.ico
└── sounds/
    ├── background.mp3
    ├── eat.wav
    └── gameover.wav
```

---

## 📦 Requirements

- Python 3.x
- Pygame

Install Pygame:

```bash
pip install pygame
```

---

## ▶️ Run the Game

```bash
python snakegame.py
```

---

## 🛠️ Build Executable (Windows)

Build using PyInstaller:

```bash
pyinstaller --windowed --icon=images/icon.ico snakegame.py
```

---

## 📝 Developer Notes

The game automatically detects whether it is running as a Python script or as a packaged executable, ensuring that images and sounds load correctly in both cases.

---

## 🚀 Technologies Used

- Python
- Pygame
- PyInstaller

---

## 👨‍💻 Author

**Pradeepp S K**

GitHub: https://github.com/SKPradeepp

---

⭐ If you enjoyed this project, consider giving the repository a **star**!