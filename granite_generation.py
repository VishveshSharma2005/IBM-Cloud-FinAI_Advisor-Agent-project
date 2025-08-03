import os
import requests
import json
from dotenv import load_dotenv

# ✅ Load secrets from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
ENDPOINT_URL = os.getenv("ENDPOINT_URL")

FOLDER_PATH = "knowledge_base/"
keywords = {
    "upi": "upi_info.txt",
    "fraud": "fraud_tips.txt",
    "budget": "budgeting.txt",
    "card": "cards.txt",
    "interest": "interest.txt"
}

def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("❗ Failed to get IAM token:", response.text)
        return None

def local_retrieval(question):
    question_lower = question.lower()
    for keyword, filename in keywords.items():
        if keyword in question_lower:
            try:
                with open(os.path.join(FOLDER_PATH, filename), "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                print(f"❗ Error reading file {filename}: {e}")
                return None
    return None

def call_granite(question):
    """
    Call AI service stream endpoint & collect streamed response
    """
    token = get_iam_token(API_KEY)
    if not token:
        return "Failed to get IAM token."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    try:
        response = requests.post(ENDPOINT_URL, headers=headers, json=payload, stream=True)
        if response.status_code != 200:
            print(f"❗ Granite request failed ({response.status_code}):", response.text)
            return "Error calling Granite."

        answer = ""
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith("data: "):
                    json_data = json.loads(line_str[6:])
                    delta = json_data.get("choices", [{}])[0].get("delta", {})
                    content_piece = delta.get("content")
                    if content_piece:
                        answer += content_piece
        return answer.strip() if answer else "No answer generated."
    except Exception as e:
        print(f"❗ Error streaming Granite response: {e}")
        return "Error calling Granite."

if __name__ == "__main__":
    print("🤖 FinAI_Advisor.ai - Retrieval + Generation")
    question = input("Ask your digital finance question: ")

    retrieved = local_retrieval(question)
    if retrieved:
        print("\n📚 Retrieved from local knowledge base:")
        print(retrieved)
    else:
        print("\n⚠ No local content matched your question.")

    granite_answer = call_granite(question)
    print("\n🤖 Granite AI answer:")
    print(granite_answer)
