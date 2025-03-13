# WiFi QR Code Generator

This Python script allows users to generate a QR code for connecting to a WiFi network. The generated QR code can be scanned by any device to automatically connect to the specified WiFi network.


---

### **Keywords for Search Engines:**
- WiFi QR Code
- QR Code Generator Python
- Generate WiFi QR Code
- Python WiFi QR Code Generator
- Tkinter WiFi QR Code
- Python Tkinter app
- WiFi password QR code generator
- WiFi QR Code Generator for Mac/Windows

---

## Pre-installation Instructions

Before running the script, ensure you have the necessary tools installed on your system.

### 1. Install Python
Ensure that Python is installed on your system:

- **Mac**: Python is pre-installed on most Mac systems. You can check by running `python3 --version` in the terminal.
- **Windows**: Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).

### 2. Install Required Modules

To run this script, you need to install the following Python packages:

- `qrcode` - to generate the QR code.
- `Pillow` (PIL) - to handle image processing.
- `tkinter` - to create the graphical user interface (GUI).

#### Install the dependencies:

1. Open a terminal or command prompt.
2. Run the following commands to install the necessary modules:

```bash
pip install qrcode[pil]
pip install pillow

```
For tkinter:

Mac: tkinter comes pre-installed with Python on macOS, so no further installation is needed.
Windows: tkinter is also bundled with Python on Windows by default.
If tkinter is not installed, you can install it using:

bash
Copy
Edit
```
pip install tk
```

How to Execute Locally
Once you’ve installed the necessary dependencies, you can execute the script on your local machine.

Clone or download this repository.
Navigate to the folder where the script is saved in your terminal or command prompt.
Run the script with the following command:
```
python wifi_qr_code_generator.py
```

The script will open a graphical user interface (GUI) where you can input your WiFi SSID and password to generate the QR code.

How to Create the App
If you want to package the script into a standalone application, you can use tools like PyInstaller to bundle the Python script into an executable file.

1. Install PyInstaller
Install PyInstaller to create the executable:

```
pip install pyinstaller
```

2. Create the Executable
Navigate to the directory containing the script and run:
```
pyinstaller --onefile --windowed wifi_qr_code_generator.py
```

--onefile bundles everything into a single executable.
--windowed prevents the terminal window from appearing (useful for GUI apps).
After this, PyInstaller will generate a dist folder containing the executable for your system.

3. Running the App
Once you have the executable, you can run it directly by double-clicking the app, or distribute it to others who don’t have Python installed.

