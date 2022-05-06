# QuantumCoda

Wecome to visit our repository! This repository is for **QuantumCoda (양자 다빈치 코드)** development. Our goal is making a new game including physics phenomenon on Capstone Design I Class at 2020 fall semester.

- 2020 PKNU Capstone Design
- Team "Explorer" repository
- Project: QuantumCoda (a.k.a Quantum Da Vinci Code '양자 다빈치 코드')
- Members: Jong hee Kim, Yong chul Lee, Yong Kwon, Sae hyeong Cho, Ji won Choi

# Download: v0.13

Now we released QuantumCoda version 0.13. This version is currently test version so we focused on being able to play the QuantumCoda. 

**[Download](https://github.com/jiwonchoi-phys/QuantumCoda/releases)**

Download latest version on zip file from **'Assets'**

You can play our game in English and Korean. 

게임 언어는 영어와 한국어로 제공됩니다.

## System Requirements
- Windows 10, Linux (Ubuntu 20.04) (We tested only two OS. It will probably run on macOS, or other linux OS, too.)
    > **FOR WSL USERS**; If you want to run our game you'll need to set X11 Forwarding and PulseAudio to send GUI & audio information to your PC. If you not set them, you **can not run the game** due to an interpreter error.
- Python 3.6.12 or higher
    > We recommend run the game using newest version of python.
- Python Modules
    > Pygame 1.9.3 or higher
    >> maybe you'll need to install using pip.
    >
    > Numpy 1.12.0 or higher
    >> maybe you'll need to install using pip.
    >
    > Python tkinter, Pillow
    >> maybe you'll need to install this module if you are Linux user. Turn on the bash and type 'apt install python3-tk'. With same context type 'pip3 install pillow' using pip.
    >
    > math, random, time, platform
    >> This modules are provided by python. If the modules are not installed, use pip to get modules.
- System fonts (for Korean Users)
    > Windows: 'Calibri' or 'malgungothic'
    >
    > macOS: 'AppleSDGothicNeo'
    >
    > Linux: 'notosanscjkkr'
    >
    > Others: 'nanumgothic'

    If you don't have the fonts above in your PC then written words in Hangul may look broken. Sure, there is no problem with running the game.

## Release Notes
### v0.13
Single Player Game
- Now you can do the 'Ability' mode to play the Quantum Coda easier. Basically It does not set the first time you run the game, so you need to go to the Game Settings then you turn on the 'ability' before you play the game.

How to Play
- Game rule description is updated. There is a description of the rule of general Coda and the rule of Quantum Coda. There is a problem with Pygame Print in the malgungothic font, so the description is only in English.

System
- Delayed the button click a little to use music control function anywhere.

## QuantumCoda Legacy
You can play the CLI-based version of Quantum Coda. Just download 'QCodalegacy.py (No joker card version)' then execute the file. this game used only 4 modules - random, numpy, copy, math. But the game is available in Korean only.

CLI 기반의 Quantum Coda를 즐겨볼 수 있습니다. 현재 브랜치에 있는 'Qcodalegacy.py'를 다운로드 하고 실행하면 됩니다. 또한 GUI 버전에 비해서 요구하는 모듈은 단지 random, numpy, copy, math 밖에 없어 쾌적하게 게임할 수 있습니다. 이 게임은 한국어로만 제공됩니다.

# Development Notes

We'll write recent development notes here. The notes can be written in Korean. If you want to watch previous update notes, see [Here](https://github.com/jiwonchoi-phys/QuantumCoda/tree/master/UpdateNotes)

## 1st Week ~ 4th Week
Update notes of 1st week to 4th week are now moved. See [Here](UpdateNotes/1st~4th.md).

## 5th Week ~ 9th Week
Update notes of 5th week to 9th week are now moved. See [Here](UpdateNotes/5th~9th.md).

## 10th Week ~ 15th Week
Update notes of 10th week to 15th week are now moved. See [Here](UpdateNotes/10th~15th.md).
