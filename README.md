# MCImageChat

This Python script converts an image into ASCII art and sends it line-by-line to a Minecraft chat window. It is designed to work with Minecraft 1.21 but can be adapted for other versions.

## Features

- **Automatic Window Activation**: Finds and activates the Minecraft window automatically.
- **Pause Menu Handling**: Automatically presses ESC if the game is paused when activated.
- **Optimized ASCII Characters**: Uses a specific set of characters chosen for consistent width in Minecraft's default font to prevent image distortion.
- **Customizable**: Adjustable output width and transmission delay.

## Prerequisites

You need Python installed along with the following libraries:

```bash
pip install pyautogui pygetwindow pillow
```

## Usage

1.  Run the script:
    ```bash
    python chat.py
    ```
2.  Enter the **absolute path** to the image file you want to send.
3.  Enter the desired **width** (default is 30 characters).
4.  The script will switch to the Minecraft window and start typing the ASCII art into the chat.

## Configuration

You can modify the following variables in `chat.py` to suit your needs:

-   `MINECRAFT_WINDOW_TITLE`: Change this if your Minecraft window title is different (e.g., for a different version).
-   `ASCII_CHARS`: The list of characters used for mapping pixel brightness.

## Notes

-   **Do not touch the mouse or keyboard** while the script is running, as it takes control of your input to type the message.
-   If the image looks distorted, try adjusting the width or the image itself.
