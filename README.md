📊 Data Analyst Agent 🤖


This is a simple but powerful API that behaves like a data analyst. It can read questions written in plain English, fetch or process the right dataset, perform the required analysis, and return the answer — even as a plot — all within 3 minutes.

This project was built for the TDS Data Analyst Agent Challenge.

🧠 What It Does
This AI agent can:

Accept a .txt file that describes a data task in natural language

Automatically fetch or read the appropriate dataset (web scraping, S3, or local files)

Perform analysis using Pandas or DuckDB (SQL engine)

Calculate values like totals, averages, correlations, etc.

Create plots such as scatter plots or regression charts

Return the result as a clean JSON response

Strings, numbers, and base64-encoded image data (for charts)

📦 Technologies Used
Python 3.11 – core programming language

Flask – to build the API

Pandas – for data manipulation and transformation

DuckDB – for running SQL queries on local files (Parquet, CSV, etc.)

Matplotlib & Seaborn – for data visualization and regression plots

Requests & BeautifulSoup – for web scraping tasks

LocalTunnel – to expose the API to a public URL for testing

🚀 How to Run This Project Locally
Clone the repository
git clone https://github.com/priiya2907/data-analyst-agent.git
cd data-analyst-agent

Create a virtual environment
python -m venv venv
venv\Scripts\activate (for Windows users)

Install the required dependencies
pip install flask pandas matplotlib seaborn duckdb requests beautifulsoup4

Run the Flask API server
python app.py
The server will start at http://127.0.0.1:5000/api/

Send a test request using cURL
curl http://127.0.0.1:5000/api/ -F "file=@question.txt"
(Make sure question.txt is in the same folder)

(Optional) Make it accessible publicly
npx localtunnel --port 5000
Copy the generated public URL for submissions

📂 Sample Question Format (question.txt)
csharp
Copy
Edit
Scrape the list of highest grossing films from Wikipedia.  
Answer the following:
1. How many $2 bn movies were released before 2020?
2. Which is the earliest film that grossed over $1.5 bn?
3. What is the correlation between Rank and Peak?
4. Draw a scatterplot of Rank and Peak with a red dotted regression line.
🧪 Sample Output (JSON)
arduino
Copy
Edit
[
  1,
  "Titanic",
  0.485782,
  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
]
📄 License
This project is licensed under the MIT License.
You are free to use, modify, and share it with credit.

🙌 Credits
Created for the TDS Data Analyst Agent Challenge.
Built using Python, curiosity, and determination 🧠✨
