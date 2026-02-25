# Financial Behavioral AI Auditor 💰

An AI-powered financial auditing tool that identifies behavioral gaps between a user's spending habits and their long-term financial goals.

## The "Why"
Traditional financial tools focus on math; this tool focuses on **behavior**. By identifying psychological spending triggers, it helps users overcome behavioral biases that prevent them from reaching their goals.

## Tech Stack
- **Python**: Core logic and data processing.
- **Pandas**: Efficient CSV transaction analysis and categorization.
- **Anthropic Claude API**: LLM-driven behavioral auditing.
- **Streamlit**: Interactive frontend and dashboard.

## Features
- **Behavioral Nudges**: Moves beyond simple "budgeting" to provide psychological insights.
- **Human-in-the-Loop**: Includes a "Flag for Human Review" feature aligned with the [CFP Board's Hybrid AI Approach](https://www.cfp.net/).
- **Privacy-First**: No PII (Personally Identifiable Information) is stored or sent to the LLM.

## Ethical Note
This application is designed with data privacy in mind. Transaction descriptions are summarized locally before being sent to the AI to ensure user anonymity.

## Installation & Local Setup
Follow these steps to get the application running on your local machine:

1. Clone the Repository
Open your terminal and navigate to your desired directory, then run:

Bash
git clone <your-repository-url>
cd financial-behavior-auditor
2. Create a Virtual Environment
This keeps the project dependencies isolated from your global system:

Windows:

Bash
python -m venv venv
Mac/Linux:

Bash
python3 -m venv venv
3. Activate the Environment
You must do this every time you start a new terminal session to work on the app:

Windows:

Bash
venv\Scripts\activate
Mac/Linux:

Bash
source venv/bin/activate
(You should see (venv) appear at the beginning of your command prompt.)

4. Install Dependencies
Install all required libraries listed in the requirements.txt file:

Bash
pip install -r requirements.txt
5. Configure Environment Variables
Create a file named .env in the root directory.

Add your OpenAI API key to the file:

Plaintext
OPENAI_API_KEY=your_api_key_here
Important: Ensure .env is listed in your .gitignore to prevent your key from being leaked to GitHub.

6. Run the Application
Launch the Streamlit dashboard:

Bash
streamlit run app.py
The app will automatically open in your default browser at http://localhost:8501.

Troubleshooting Tips
"The system cannot find the path specified": Ensure you have run the python -m venv venv command first to create the venv folder before trying to activate it.

Authentication Errors: Verify that your .env file is in the same folder as app.py and that the variable name matches exactly what is in your code (e.g., os.getenv("OPENAI_API_KEY")).