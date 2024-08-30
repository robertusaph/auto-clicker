import pyautogui
import time
import tkinter as tk
from pynput import keyboard
from threading import Thread

# Set the delay between continuous clicks in seconds
delay = 0.001  # This will click very quickly

# Set the interval for clicking at the specified coordinates
special_click_interval = 30  # Once every 10 seconds

# Variable to control the clicker's running state
clicking = False  # Start with clicking off
special_clicking = False  # Control the special clicking

# Function to update the mouse position display
def update_mouse_position_label():
    while True:
        x, y = pyautogui.position()
        position_label.config(text=f'X: {x} Y: {y}')
        root.geometry(f"+{x+20}+{y+20}")  # Position the window near the cursor
        time.sleep(0.05)  # Update every 50ms

# Function to handle spacebar press
def on_press(key):
    global clicking, special_clicking
    if key == keyboard.Key.space:
        if clicking:
            clicking = False
            special_clicking = False
            print("Spacebar pressed. Pausing clicking.")
        else:
            clicking = True
            special_clicking = True
            print("Spacebar pressed. Starting clicking.")

# Function to run the auto clicker
def auto_clicker():
    global clicking, special_clicking
    last_special_click_time = time.time()
    
    try:
        while True:
            current_time = time.time()
            
            # Perform continuous clicking
            if clicking:
                pyautogui.click()  # Perform the click at the current cursor position
            
            # Check if it's time for the special click and if clicking is active
            if clicking and special_clicking and current_time - last_special_click_time >= special_click_interval:
                last_special_click_time = current_time
                
                # Save the current mouse position
                current_position = pyautogui.position()
                
                # Move to the special coordinates and click
                pyautogui.moveTo(1460, 240)
                pyautogui.click()
                pyautogui.moveTo(1460, 1053)
                pyautogui.click()
                pyautogui.moveTo(1460, 990)
                pyautogui.click()
                pyautogui.moveTo(1460, 927)
                pyautogui.click()
                pyautogui.moveTo(1460, 864)
                pyautogui.click()
                pyautogui.moveTo(1460, 801)
                pyautogui.click()
                pyautogui.moveTo(1460, 738)
                pyautogui.click()
                pyautogui.moveTo(1460, 675)
                pyautogui.click()
                pyautogui.moveTo(1460, 612)
                pyautogui.click()
                pyautogui.moveTo(1460, 549)
                pyautogui.click()
                pyautogui.moveTo(1460, 486)
                pyautogui.click()
                pyautogui.moveTo(1460, 423)
                pyautogui.click()
                pyautogui.moveTo(1460, 360)
                pyautogui.click()
                pyautogui.moveTo(1460, 240)
                pyautogui.click()

                # Move back to the original position and continue clicking
                pyautogui.moveTo(current_position)
            
            time.sleep(delay)  # Wait before the next click
    except KeyboardInterrupt:
        print("Auto clicker stopped.")

# Setting up the tkinter window
root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes('-topmost', True)  # Keep the window on top

# Create a label to show the mouse position
position_label = tk.Label(root, text='', font=('Helvetica', 12), bg='yellow', fg='black')
position_label.pack()

# Start the thread to update the mouse position
position_thread = Thread(target=update_mouse_position_label, daemon=True)
position_thread.start()

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Start the auto clicker in the main thread
clicker_thread = Thread(target=auto_clicker, daemon=True)
clicker_thread.start()

# Run the tkinter main loop
root.mainloop()