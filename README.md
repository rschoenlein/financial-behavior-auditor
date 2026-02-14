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