# Test App - Quick Start Guide

Welcome to the Test App! This application is Docker-based, providing a straightforward setup process. Along with this README, you should have received a pre-built Docker image (`univariate_soft_sensor.tar`) and sample data.

## Prerequisites
- **Docker** must be installed. If Docker isn’t installed on your machine, follow the steps below to install it.

---

### Steps to Run the App

#### 1. Install Docker
   - **Download Docker**: Visit [Docker’s official website](https://www.docker.com/get-started) to download and install Docker for your operating system.
   - **Verify Installation**: Open a terminal and run:
     ```bash
     docker --version
     ```
   - You should see the Docker version displayed, confirming it’s installed.

#### 2. Clone the Repository
   - Clone the provided repository to access the necessary folder structure and configuration files:
     ```bash
     git clone <repository_url>
     cd <repository_folder>
     ```
   - This will set up the folder structure for the application, but please note that the `data` directory will not be included (as it is in `.gitignore`).
   - **Create a `data` directory** inside the cloned repository:
     ```bash
     mkdir data
     ```
   - Next, unzip the `1st_test.zip` file you received by email, and place the extracted `1st_test` folder inside the newly created `data` directory. This step will ensure the application has access to the required data files.

#### 3. Download the Docker Image
   - **Download the `univariate_soft_sensor.tar`** file sent via email. This file contains the entire app structure, configuration, and necessary dependencies.

#### 4. Load the Docker Image
   - **Load the image** into Docker by running the following command in your terminal:
     ```bash
     docker load -i /path/to/your/univariate_soft_sensor.tar
     ```
   - After loading, you’ll see a confirmation that the image was successfully imported.

#### 5. Add the Data File
   - Copy the data file you received into the `data` folder within the cloned repository directory. The folder structure should look like this:
     ```
     univariate_soft_sensor/
     ├── data/
     │   └── 1st_test
     ├── config.yaml
     ├── test_app.py
     └── other_app_files...
     ```

#### 6. Run the Docker Container
   - To start the application, use the following command:
     ```bash
     docker run -p 8050:8050 -v "$(pwd)/data/1st_test:/univariate_soft_sensor/data/1st_test" univariate_soft_sensor
     ```
   - This command:
     - Maps port `8050` on your local machine to the app’s port `8050`.
     - Mounts your `data` folder to the `/univariate_soft_sensor/data/1st_test` directory in the container, so the app can access your data file.

---

### Viewing the App
- Open your web browser and go to [http://localhost:8050](http://localhost:8050).
- You should see a basic Dash application with:
  - A title reading **Hello, Dash!**
  - A paragraph showing the status of the data file, confirming it is detected and accessible.

---

### Verifying the App
If everything is set up correctly, the app will display a simple Dash page confirming the data file is available. 

### Troubleshooting
- **Docker issues**: Refer to [Docker’s Troubleshooting Guide](https://docs.docker.com/config/daemon/).
- **Data file access**: Make sure the data file is in the correct directory and you’ve mounted it correctly using `-v "$(pwd)/data/1st_test:/univariate_soft_sensor/data/1st_test"`.

This setup should help you get started smoothly and verify that Docker and the app are working as expected.