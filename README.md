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
    
         **Example Request:**
         1. With count = 2
            
            ```bash
            curl -X 'GET' \'http://localhost:8000/top-news?count=2' \-H 'accept: application/json'
         **Example Response:**
      
         ```json
            [
              {
                "by" : "dhouston",
                 "descendants" : 71,
                 "id" : 8863,
                 "kids" : [ 8952, 9224, 8917, 8884, 8887, 8943, 8869, 8958, 9005, 9671, 8940, 9067, 8908, 9055, 8865, 8881, 8872, 8873, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8878, 8870,                      8980, 8934, 8876 ],
                 "score" : 111,
                 "time" : 1175714200,
                 "title" : "My YC app: Dropbox - Throw away your USB drive",
                 "type" : "story",
                 "url" : "http://www.getdropbox.com/u/2/screencast.html"
              },
              {
                
                    "by" : "norvig",
                    "id" : 2921983,
                    "kids" : [ 2922097, 2922429, 2924562, 2922709, 2922573, 2922140, 2922141 ],
                    "parent" : 2921506,
                    "text" : "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?",
                    "time" : 1314211127,
                    "type" : "comment"
                  
              }
            ]
         ```


### API Endpoints
* **`/top-news?count={count}`**: Retrieves the top `count` news items from Hacker News.

### Hacker News API

The Hacker News API provides a simple interface for accessing data from the popular Hacker News website. This project utilizes the following Hacker News API endpoints and parameters:

**Base URL:** https://hacker-news.firebaseio.com/v0/

* **`/topstories.json`**: Retrieves a list of top story IDs.
* **`/item/{id}.json`**: Retrieves details about a specific story, where `{id}` is the story ID.

This project leverages the Hacker News API to fetch top news stories and display them through a RESTful API.

### Caching
The application employs an in-memory cache to store fetched story details, optimizing performance and reducing API calls.

### Error Handling
Robust error handling is implemented to gracefully manage exceptions and provide informative error messages.

### Dockerization
A Dockerfile is included for containerization, enabling easy deployment and isolation.





