Markdown
## Hacker News Top Stories API

### Overview
This Python project leverages the FastAPI framework to create a RESTful API that fetches and displays top news items from Hacker News. The application incorporates caching for enhanced performance and robust error handling.

### Prerequisites
* Python 3.6+
* Docker 

### Installation
1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/prakash200/Harmony.git

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

### Running the Application
1. **Without Docker:**
 
   ```bash
   uvicorn main:app --reload
2. **With Docker**
   
   * **Build the Docker image:**
   
      ```Bash
      docker build -t my_fastapi_app .
   
   * **Run the Docker container:**
      ```bash
      docker run -p 8000:8000 my_fastapi_app

### Testing

   * To test the API locally:
   
      * Run the application using `uvicorn main:app --reload` or start the Docker container.
      * Open a web browser and navigate to `http://localhost:8000/top-news?count=10` to test the API with a count of 10.
      * Experiment with different values for the `count` parameter to see the results.

### API Endpoints
* **`/top-news?count={count}`**: Retrieves the top `count` news items from Hacker News.

### Caching
The application employs an in-memory cache to store fetched story details, optimizing performance and reducing API calls.

### Error Handling
Robust error handling is implemented to gracefully manage exceptions and provide informative error messages.

### Dockerization
A Dockerfile is included for containerization, enabling easy deployment and isolation.





