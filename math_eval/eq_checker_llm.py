from openai import OpenAI

# Set up the OpenRouter.ai client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your OpenRouter API key
)

def check_equivalence_with_deepseek(expr1, expr2):
    # Set up the prompt
    prompt = f"Are the following two mathematical expressions equivalent? Expression 1: {expr1}, Expression 2: {expr2}. Respond with 'Equivalent' if they are, or 'Not Equivalent' if they are not. Don't explain too much just show which step is wrong thats all"

    # Call the OpenRouter.ai API
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Replace with your site URL.
            "X-Title": "<YOUR_SITE_NAME>",  # Optional. Replace with your site name.
        },
        model="deepseek/deepseek-r1:free",  # Use DeepSeek-V3 via OpenRouter.ai
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Extract the response
    result = completion.choices[0].message.content.strip()
    print(f"DeepSeek Response: {result}")

    # Check if the response indicates equivalence
    if "equivalent" in result.lower():
        return True
    else:
        return False

# Example usage
expression1 = "2*x + 3*x - 5 = 9"
expression2 = "5*x - 10 = 0"
is_equivalent = check_equivalence_with_deepseek(expression1, expression2)
print(f"Are the expressions equivalent? {is_equivalent}")