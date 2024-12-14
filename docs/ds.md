# Data Science

We created a service for the **data-science** part of the project, which is responsible for writing and testing the **Thompson Sampling** code, which is then transferred to the Back-End branch to work with FastAPI.

```Dockerfile

# Pull the official Python image
FROM python:3.10-slim-bullseye

# Install system dependencies required for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev libfreetype6-dev libpng-dev libjpeg-dev \
    libblas-dev liblapack-dev gfortran \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /ds

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the DS code into the container
COPY . .

# Expose a relevant port for DS tools (if necessary)
EXPOSE 8888  # Optional: If using Jupyter or other tools

# Command to run the Thompson Sampling script
CMD ["python", "Thompson_sampling.py"]
```

### Service

```yaml
ds:
    container_name: ds
    build:
      context: ./ds  # Directory where the Dockerfile for the DS is located
      dockerfile: Dockerfile
    volumes:
      - ./ds:/ds  # Sync the local DS directory with the container
    ports:
      - "8888:8888"  # Useful if using Jupyter or other DS tools
    environment:
      - DATABASE_URL=${DATABASE_URL}  # Environment variable for database URL
    depends_on:
      - db  # Ensure DS container waits for the database container

```

## Thompson Sampling with binary reward

::: armenianartstore.ds.Thompson_sampling