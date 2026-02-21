Smart Room Monitor

Autonomous Light Monitoring System Based on Raspberry Pi

Project Overview

Smart Room Monitor is an embedded monitoring system built on Raspberry Pi that measures ambient light intensity using a BH1750 digital light sensor, detects light state changes (ON and OFF), logs events with timestamps, and displays real time information on a 16x2 I2C LCD screen.

The project is built using modular architecture and hardware abstraction principles. It demonstrates embedded systems development, low level sensor communication, signal filtering, and structured software design.

This project is not just a simple sensor reader. It is a complete autonomous monitoring system.

Main Features

Real time light intensity measurement in Lux
Light state detection (ON and OFF)
Event logging with timestamps in CSV format
Noise resistant threshold based logic
LCD display output
Custom BH1750 sensor driver implementation
Remote development via SSH
Version control using Git and GitHub

System Architecture

The BH1750 sensor communicates with the Raspberry Pi over the I2C protocol.
A custom Python driver handles raw byte communication with the sensor.
The driver converts raw sensor data into Lux values.
A state detection system determines when the light turns ON or OFF.
Events are stored in a CSV log file.
An LCD screen displays current system information.

Hardware Components

Raspberry Pi
BH1750 digital light sensor (I2C)
16x2 LCD display with PCF8574 I2C backpack
Jumper wires

Software Stack

Python 3
SMBus library for I2C communication
RPLCD library for LCD control
Raspberry Pi OS (Linux)
Git and GitHub
VS Code Remote SSH

Custom Sensor Driver

Instead of using a high level third party wrapper, this project implements a custom driver file called bh1750_smbus.py.

The driver directly communicates with the sensor using the SMBus interface.
It reads two raw bytes from the sensor.
It converts the raw data into a Lux value using the sensor formula.
It encapsulates hardware communication inside a clean Python class.

This demonstrates understanding of I2C communication, byte level data processing, hardware abstraction, and modular software design.

State Machine Logic

To prevent false triggers caused by sensor noise or small fluctuations in ambient light, the system uses a simple state machine.

The current light state is stored (ON or OFF).
A new event is only registered if the Lux difference exceeds a defined threshold.
Repeated triggers are ignored if the system state has not changed.

This ensures stable and realistic event detection.

Event Logging

Every detected light state change is written into a CSV file with a timestamp and event type.

This allows later data analysis and further system expansion.

LCD Interface

The LCD screen displays current Lux value and system status information.

The system can operate autonomously without a connected monitor, keyboard, or development environment.

Engineering Challenges Solved

I2C device communication
Hardware address detection
Raw byte conversion to physical units
Noise filtering logic
Modular architecture design
Remote Linux development
Git based version control workflow

Skills Demonstrated

Embedded systems development
Raspberry Pi and Linux usage
I2C communication protocol
Hardware abstraction
State machine logic
Signal filtering
Git and GitHub workflow
Remote development over SSH

Future Improvements

Automatic startup using systemd
Web dashboard interface
Data visualization
Multi sensor integration
Motion detection extension

Developed as a personal embedded systems portfolio project.
