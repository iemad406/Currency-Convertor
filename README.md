# 💱 Currency Converter

A desktop application built with Python and Tkinter that provides a clean, user-friendly interface for currency conversion with secure user authentication.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Currency Converter is a desktop GUI application that allows users to register, log in, and perform real-time currency conversions. The application is built using Python's built-in `tkinter` library, making it lightweight and easy to run on any platform without heavy dependencies.

---

## ✨ Features

- **User Authentication** — Secure Login and Sign Up system before accessing the converter
- **Clean GUI** — Simple and intuitive interface built with Tkinter
- **Modular Design** — Separated modules for login, signup, and main window logic
- **Lightweight** — No external GUI framework required; runs on standard Python

---

## 📁 Project Structure

```
currency-converter/
│
├── main.py                 # Entry point — launches the main window
├── images/
│   └── icon1.ico           # Application icon
└── modules/
    ├── login.py            # Login window module
    └── signup.py           # Sign Up window module
```

---

## ⚙️ Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)

> **Note:** On some Linux distributions, you may need to install `tkinter` separately:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/currency-converter.git
   cd currency-converter
   ```

2. **Ensure Python 3 is installed:**
   ```bash
   python --version
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

---

## 🖥️ Usage

1. Launch the application by running `main.py`.
2. The **Main Window** will appear with two options:
   - **Login** — Access your existing account.
   - **Signup** — Create a new account.
3. After authenticating, you will be directed to the Currency Converter interface.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Built with ❤️ using Python & Tkinter
