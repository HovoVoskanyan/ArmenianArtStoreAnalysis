## Web Application

We created a service for the **front-end** part of the project, which is responsible for hosting the **Streamlit web application**.

To open the main web app, visit: [here](http://localhost:8501/)

Additionally, we have an analytical page of our results, which you can access at: [here](http://localhost:8501/admin)

![Admin Page](docs/Admin.png "Adminpage")

![Variant 1](docs/Var1.png "Variant 1")
![Variant 2](docs/Var2.png "Variant 2")
![Variant 3](docs/Var3.png "Variant 3")

### Dockerfile

```Dockerfile
# Dockerfile

# Pull the official Docker image
FROM python:3.10-slim-bullseye

# Install system dependencies required by some Python packages
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev libfreetype6-dev libpng-dev libjpeg-dev \
    libblas-dev liblapack-dev gfortran \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the contents of the frontend directory into the container
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true", "--server.runOnSave=true"]
```

### Service

```yaml
  app:
    container_name: streamlit_app
    build:
      context: ./front  # Directory where the Dockerfile for the frontend is located
      dockerfile: Dockerfile
    volumes:
      - ./front:/app  # Sync the local frontend directory with the container
    ports:
      - "8501:8501"  
    environment:
      - STREAMLIT_APP=app.py  
    depends_on:
      - api 
```

## App
::: armenianartstore.front.app

## Styles
::: armenianartstore.front.styles.style

## Admin page ans sample variant pages
::: armenianartstore.front.pages.admin
::: armenianartstore.front.pages.page1
::: armenianartstore.front.pages.page2
::: armenianartstore.front.pages.page3




