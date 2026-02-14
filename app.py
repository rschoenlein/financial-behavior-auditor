import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import anthropic

# 1. Load environment variables from .env file
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# 2. Configure the Claude Client
client = anthropic.Anthropic(api_key=api_key)

# 3. UI Header Section
st.set_page_config(page_title="Behavioral Alpha Auditor", page_icon="💰")
st.title("Behavioral Alpha AI Auditor")
st.subheader("Identify spending patterns vs. financial goals")

# 4. Sidebar / Input Section
with st.sidebar:
    st.header("Settings")
    user_goal = st.text_input(
        "Financial Goal", 
        placeholder="e.g., Save $5,000 for a house down payment"
    )
    uploaded_file = st.file_uploader("Upload transaction CSV", type=['csv'])

# 5. Main Logic Block
if uploaded_file is not None and user_goal:
    # Read the data
    df = pd.read_csv(uploaded_file)
    
    # Display a preview to the user
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Create the Summary (Grouping by Category)
    # Note: This assumes your CSV has 'Category' and 'Amount' columns
    try:
        summary = df.groupby('Category')['Amount'].sum().to_string()
        
        # 6. The "Audit" Trigger
        if st.button("Run Behavioral Audit"):
            with st.spinner("Analyzing spending habits against your goal..."):
                # Construct the Prompt
                prompt_content = f"""
                The user's financial goal is: {user_goal}
                
                Here is a summary of their recent spending by category:
                {summary}
                
                Based on 'Behavioral Alpha' principles, provide 3 specific behavioral nudges 
                to help them reach their goal. Focus on psychological triggers, not just math.
                """

                # Call the Claude API
                message = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[
                        {"role": "user", "content": prompt_content}
                    ]
                )
                
                # Display Results
                st.success("Audit Complete!")
                st.markdown("### AI Behavioral Insights")
                st.write(message.content[0].text)

    except Exception as e:
        st.error(f"Error processing CSV: Ensure it has 'Category' and 'Amount' columns. {e}")

elif not uploaded_file:
    st.info("Please upload a CSV file to begin the audit.")
elif not user_goal:
    st.warning("Please enter a financial goal in the sidebar.")