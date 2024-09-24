
# **PromptPowerSQL**

## **Overview**
PromptPowerSQL is an AI-driven tool that allows users to query their SQL database using natural language prompts. Tool developed by leveraging Gemini-Pro LLM, this translates English-language questions into SQL commands and retrieves data from your database. Ideal for users who aren't proficient in SQL, PromptPowerSQL simplifies database interaction by turning plain English prompts into precise SQL queries.

## **Features**
- **Natural Language to SQL**: Input questions, and PromptPowerSQL generates the corresponding SQL.
- **Execute on SQLite**: Automatically executes queries on your connected SQLite database.
- **AI-Powered**: Uses Google Gemini for accurate SQL generation.

## **Example Queries**
- **"How many students are in Data Science?"**
  - Generates: `SELECT COUNT(*) FROM STUDENT WHERE CLASS = 'Data Science';`

## **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/Sohampatel26/PromptPowerSQL.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Google API key in a `.env` file:
   ```bash
   GOOGLLE_API_KEY=your-key-here
   ```

## **Usage**
Run the application:
```bash
streamlit run app.py
```

Enter a natural language prompt in the app and receive SQL queries executed directly on your database.

## **Future Enhancements**
- **Support for Other Databases**: Extend support to other SQL engines.
- **Advanced Query Features**: Add filters and query optimizations.


## **Website Preview 1:**


<img width="925" alt="image" src="https://github.com/user-attachments/assets/d4ab27ff-e404-46db-b0f4-7f701c4067d6">

## **Website Preview 2:**


<img width="844" alt="image" src="https://github.com/user-attachments/assets/61f77dd7-5fdf-45e1-aec1-d2d126d7a662">

