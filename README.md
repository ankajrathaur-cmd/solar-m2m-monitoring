
# Solar M2M Smart Machine Monitoring System

## Project Overview
A real-time machine monitoring system built using Python, MQTT, Flask, SQLite, and Docker.

## Technologies Used
- Python
- Flask
- MQTT (Mosquitto)
- SQLite Database
- Docker
- Docker Compose

## Project Features
- Real-time machine temperature monitoring
- MQTT-based communication
- Automatic data storage in SQLite
- Web-based monitoring dashboard
- Docker containerization

## Project Architecture
1. Machine Simulator publishes temperature data.
2. MQTT Broker receives machine messages.
3. Receiver subscribes to MQTT topics.
4. SQLite stores machine readings.
5. Flask Dashboard displays monitoring data.

## How to Run

Clone the repository:

```bash
git clone https://github.com/ankajrathaur-cmd/solar-m2m-monitoring.git
cd solar-m2m-monitoring
```

Start the project:

```bash
docker compose up -d --build
```

Open dashboard:

http://localhost:5000

## Author
Ankaj Rathaur

## Project Status
Working Prototype
Jenkins automatic deployment testing.
