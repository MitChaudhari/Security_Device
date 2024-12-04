
# Security Device

A project demonstrating the use of Finite Automata concepts to solve real-life problems by simulating a security device.

## Author
**Mitansh Chaudhari**  
License: Public Domain - Anyone can use, modify, or incorporate code from this software into their applications.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [How to Build and Run](#how-to-build-and-run)
4. [Generating Unit Test Coverage](#generating-unit-test-coverage)
5. [Platform Tested On](#platform-tested-on)
6. [Screenshots](#screenshots)
---

## Introduction
This program simulates a security device, similar to those found in homes and offices. It uses a combination of user-entered strings and random number-generated strings to simulate locking and unlocking mechanisms.  
The project is divided into two parts:  
1. User input-based locking/unlocking.
2. Random number generator-based locking/unlocking.

---

## Features

### Part 1: User Input Simulation
- Unlocks or locks the device based on valid access codes.
- Outputs current state (Locked/Unlocked) along with statistics:
  - Number of attempts.
  - Times unlocked.
  - Times locked.
- Handles invalid inputs by ignoring non-digit characters.
- Python Files:
  - **`SecurityEngine.py`**: Core functionality.
  - **`test_security_engine.py`**: Unit tests for `SecurityEngine.py`.
  - **`InterfaceSecurityEngine.py`**: User interface for interacting with `SecurityEngine.py`.

### Part 2: Random Number Generator Simulation
- Generates random numerical sequences to simulate unlocking attempts.
- Outputs:
  - Minimum, maximum, and average digits required to unlock.
  - Average time to unlock when considering a one-second delay.
- Python Files:
  - **`RanNumGen.py`**: Core functionality.
  - **`test_ranNumGen.py`**: Unit tests for `RanNumGen.py`.
  - **`InterfaceRanNumGen.py`**: User interface for interacting with `RanNumGen.py`.

---

## How to Build and Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MitChaudhari/Security_Device.git
   ```
2. Install Python 3 if not already installed:
   ```bash
   python3 --version
   ```
   If not installed, download from [Python Official Website](https://www.python.org/downloads/).
3. Navigate to the `app` folder:
   ```bash
   cd Security_Device/app
   ```
4. Run the interface files to test functionalities:
   - For Part 1:
     ```bash
     python InterfaceSecurityEngine.py
     ```
   - For Part 2:
     ```bash
     python InterfaceRanNumGen.py
     ```

---

## Generating Unit Test Coverage

### Prerequisites
Ensure `pip` and `coverage` are installed:
```bash
python3 -m pip install coverage
```

### Steps
1. Navigate to the `app` folder:
   ```bash
   cd Security_Device/app
   ```
2. Generate coverage for `SecurityEngine.py`:
   ```bash
   coverage run test_security_engine.py
   coverage report
   ```
3. Generate coverage for `RanNumGen.py`:
   ```bash
   coverage run test_ranNumGen.py
   coverage report
   ```

---

## Platform Tested On
- **Development Environment**: Python on Eclipse.
- **Tested On**: Eclipse IDE and Terminal Command Line.

---

## Screenshots

### Terminal View
#### InterfaceSecurityEngine.py
![InterfaceSecurityEngine.py](https://github.com/MitChaudhari/Security_Device/raw/main/assets/run1.png)

#### InterfaceRanNumGen.py
![InterfaceRanNumGen.py](https://github.com/MitChaudhari/Security_Device/raw/main/assets/run2.png)

---
