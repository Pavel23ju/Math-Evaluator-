import os
import time
from openai import OpenAI
import openai
from sympy import Eq, symbols, simplify, sympify

# Load API key from environment variables
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key or len(api_key) < 20:  # Ensuring API key is valid
    raise ValueError("Invalid API key! Ensure OPENROUTER_API_KEY is set correctly.")

# Set up the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def check_equivalence_locally(expr1, expr2):
    """Check if two expressions are equivalent using SymPy."""
    x = symbols("x")  # Define the variable
    try:
        expr1_sym = sympify(expr1)  # Convert string to symbolic expression
        expr2_sym = sympify(expr2)
        return simplify(Eq(expr1_sym, expr2_sym))
    except Exception as e:
        print(f"⚠️ SymPy Error: {e}. Falling back to LLM check.")
        return None  # Indicates failure, so LLM should be used

def check_equivalence_with_deepseek(expr1, expr2):
    """Check expression equivalence using OpenRouter API with DeepSeek."""
    
    prompt = (f"Are these mathematical expressions equivalent? "
              f"Expression 1: {expr1}, Expression 2: {expr2}. "
              f"Respond with 'Equivalent' or 'Not Equivalent'. "
              f"Show only the incorrect step if any.")

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Replace with your site URL.
                "X-Title": "<YOUR_SITE_NAME>",  # Optional. Replace with your site name.
            },
            model="deepseek/deepseek-r1:free",  # Primary model
            messages=[{"role": "user", "content": prompt}]
        )

        result = completion.choices[0].message.content.strip()
        print(f"DeepSeek Response: {result}")

        result_lower = result.lower()
        if "equivalent" in result_lower and "not equivalent" not in result_lower:
            return True
        else:
            return False

    except openai.AuthenticationError:
        print("❌ Authentication Error: Invalid API Key.")
        return None
    except openai.RateLimitError:
        print("⚠️ Rate limit exceeded. Retrying in 60 seconds...")
        time.sleep(60)
        return check_equivalence_with_deepseek(expr1, expr2)
    except openai.OpenAIError as e:
        print(f"⚠️ OpenRouter API Error: {e}")
        return None

# Example usage
expression1 = "2*x + 3*x - 5 = 9"
expression2 = "5*x - 10 = 0"

# Step 1: Try local checking first
local_check = check_equivalence_locally(expression1, expression2)
if local_check is not None:
    print(f"✅ Expressions are equivalent (checked locally).")
else:
    # Step 2: Fallback to DeepSeek API check
    is_equivalent = check_equivalence_with_deepseek(expression1, expression2)
    print(f"Are the expressions equivalent? {is_equivalent}")
