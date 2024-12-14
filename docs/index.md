# Welcome to Our **Bayesian A/B Testing Tool** Documentation  

## **Problem**  

Armenian artists, renowned for their **rich and culturally significant work**, face challenges in **showcasing and selling their art** to a **global audience**. Despite the growing demand for **unique and authentic artistic creations**, there is **no dedicated online platform** effectively bridging the gap between Armenian artists and **international buyers**.  

A **well-designed and appealing digital storefront** could create immense opportunities for these artists, allowing them to **expand their reach** and thrive in the **global art market**. However, the main challenge is **identifying the most effective website design** that captivates customers and **encourages interaction**, **browsing**, and **purchases**.  

## **Solution**  

To tackle this issue, we have developed a **Bayesian A/B testing tool** tailored for comparing various **design options** of an art store website.  

Unlike **traditional A/B testing**, which relies on **fixed sample sizes** and is **time-consuming**, our **Bayesian testing approach** updates **probabilities in real-time**. This enables a **dynamic evaluation process**, identifying the design that resonates with users more efficiently.  

### **How It Works**:  
- Tracks and analyzes **customer behavior**, including:  
  - Buttons clicked.  
  - Navigation patterns.  
- Provides valuable insights into **user engagement** and **preferences**.  
- **Adaptive mechanism**:  
  - Prioritizes the **most effective design variant** once sufficient data is collected.  
  - Enhances the **overall customer experience**.  

## **Expected Outcomes**  

The implementation of this tool will yield several **significant outcomes**:  

1. **Visual and Quantitative Insights**:  
   - Helps website managers understand **visitor interactions** with different design variants.  
   - Offers a **data-driven approach** for identifying the **best-performing design**.  

2. **Broader Marketing and Product Strategies**:  
   - Uncovers **trends** and **preferences** that guide **long-term planning**.  

3. **Higher Engagement and Conversion Rates**:  
   - The **adaptive mechanism** ensures the **optimal design** is prominently displayed.  
   - **Drives better user engagement** and **purchase rates**.  

4. **Competitive Edge**:  
   - Creates a **more engaging and personalized user experience**.  
   - Continuously improves the website based on **customer feedback**.  

### **Impact on Armenian Artists**:  
- Provides a platform that **showcases talent** effectively.  
- **Builds stronger connections** with a **global audience**.  


## **Services**  

- **`Etl`** - **Postgres** database.  
- **`Front`** - **UI** of our Marketing Analytics Tool and Website **variants** in comparison.  
- **`Back`** - **Streamlit**, which connects with **Fast API**.  
- **`Ds`** - **Bayesian A/B testing implementation**.  


### Project Schema
```plaintext
.
├── .github
├── ArmenianArtstoreAnalysis
│   ├── back
│   │   ├── Database
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   ├── models.py
│   │   │   └── schema.py
│   │   ├── Models 
│   │   │   ├── Request
│   │   │   │   ├── __init__.py
│   │   │   │   └── request_classes.py
│   │   │   ├── Response
│   │   │   │   ├── __init__.py
│   │   │   │   └── response_classes.py
│   │   ├── .env
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── etl
│   │   ├── __init__.py
│   │   ├── .env
│   │   ├── crud_testing.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── Dockerfile
│   │   ├── ERD.png
│   │   ├── models.py
│   │   └── requirements.txt
│   ├── ds
│   │   ├── __init__.py
│   │   ├── .env
│   │   ├── database.py
│   │   ├── Dockerfile
│   │   ├── models.py
│   │   ├── analysis.py
│   │   └── requirements.txt
│   ├── front
│   │   ├── .streamlit
│   │   │   └── config.toml
│   │   ├── assets
│   │   ├── pages
│   │   ├── styles
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── db_admin 
│   ├── init.py
│   ├── .env
│   ├── docker-compose.yml
│   ├── documentation
│   │   ├── mkdocs.yml
│   │   └── README.md
└── requirements.txt
```

## Installation

Before getting started, ensure you have the following prerequisites installed:

1. Clone the repository:
   ```bash
   git clone https://github.com/HovoVoskanyan/ArmenianArtStoreAnalysis.git
   ```

2. Change Directory:
   ```bash
   cd armenianartstore
   ```

3. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

## Access the Application

After running `docker-compose up --build`, you can access each component of the application at the following URLs:

- **Streamlit Frontend**: [http://localhost:8501](http://localhost:8501)  
  The main interface for managing employees, built with Streamlit. Use this to add, view, update, and delete employee records.

- **FastAPI Backend**: [http://localhost:8000](http://localhost:8000)  
  The backend API where requests are processed. You can use tools like [Swagger UI](http://localhost:8000/docs) (provided by FastAPI) to explore the API endpoints and their details.

- **PgAdmin** (optional): [http://localhost:5050](http://localhost:5050)  
  A graphical tool for PostgreSQL, which allows you to view and manage the database. Login using the credentials set in the `.env` file:
  
  - **Email**: Value of `PGADMIN_EMAIL` in your `.env` file
  - **Password**: Value of `PGADMIN_PASSWORD` in your `.env` file

To see the web page, create project via **Swagger UI**, it will return you a project ID. In front folder config.py, change the value of project id to the given id.

Finally, open the **Streamlit** application.

> Note: Ensure Docker is running, and all environment variables in `.env` are correctly configured before accessing these URLs.

When running for the first time, you must create a server. 

  Hostname: db
  Maintenance database: ArmenianArtStore
  Username: postgres
  Password: group3

