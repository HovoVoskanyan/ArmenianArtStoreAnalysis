We created a service for the **API** part of the project, which handles core functionalities such as managing projects, user feedback, and retrieving reports.

### **Features**  

- **Add New Project**:  
  Enter the project name, and under the bandits, enter the main page name and the quantity of bandits to create the project.  

- **User Feedback**:  
  Submit the bandit name and the reward as a Boolean (`true/false`).  

- **Get Champion Bandit**:  
  Retrieve the **champion bandit** of the predefined project to display to the user.  

- **Get Projects**:  
  List all already created projects.  

- **Get Project Report**:  
  Retrieve the bandits of a specific project along with their parameters (e.g., **alpha** and **beta** values).  

![Swagger](docs/apiscreen.png "Swagger")


### **Requests**  

- **POST** `/project`: Create a new project.  
- **GET** `/bandit/{project_id}`: Get the **champion bandit**.  
- **POST** `/user/bandit`: Submit user feedback for the current bandit.  
- **GET** `/projects`: Get all existing projects.  
- **GET** `/project/report/{project_id}`: Retrieve all bandits of a specific project, including **alpha** and **beta** values.  

---

## **Services**  

We use Docker services for efficient deployment and management of components.  

### **Database**  

```yaml
  db:
    container_name: postgresql_db
    image: postgres
    restart: always
    ports:
      - 5432:5432
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=${DB_NAME}
    healthcheck:
        test: ["CMD-SHELL", "pg_isready -U postgres"]
        interval: 60s
        timeout: 10s
        retries: 5
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
```

## Database 

::: armenianartstore.back.Database.database

## Models

::: armenianartstore.back.Database.models

