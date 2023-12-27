# Internet Speed Monitoring with Grafana

## Overview

This repository contains a Python application that performs internet speed tests and visualizes the results using Grafana. The application uses InfluxDB to store speed test data, and Grafana is used to create a dashboard for real-time monitoring.

## Components

- **Python App (`app.py`):** The Python script performs internet speed tests using the `speedtest-cli` library and stores the results in InfluxDB.

- **Dockerfile:** The Dockerfile defines the configuration for building the Docker image of the Python application.

- **docker-compose.yml:** The Docker Compose configuration file orchestrates the deployment of containers for the Python app, InfluxDB, and Grafana.

- **dashboard.json:** The JSON file contains the Grafana dashboard configuration for displaying internet speed metrics.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/[yourusername]/internet-speed-monitoring.git
   ```

2. **Navigate to the project directory:**

    ```bash
   cd internet-speed-monitoring
    ```

3. **Build and run the docker containers:**

    ```bash
   docker-compose up --build
    ```
   
4. **Access Grafana at [http://localhost:3000](http://localhost:3000) (default credentials: admin/admin).**

## Customization

- **Adjustment:** Modify the `app.py` file, `Dockerfile`, or `docker-compose.yml` to suit your specific requirements.

- **Metrics:** Customize the Grafana dashboard (`dashboard.json`) to include additional metrics or visualizations.

## License

This project is licensed under the [MIT License](LICENSE).
