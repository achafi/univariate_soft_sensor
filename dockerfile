# Use a Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /univariate_soft_sensor

# Copy the application files into the container
COPY . /univariate_soft_sensor

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Dash will run on
EXPOSE 8050

# Run the Dash app when the container starts
CMD ["python", "test_app.py"]
