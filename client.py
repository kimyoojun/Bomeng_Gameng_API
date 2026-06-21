from supabase import create_client, Client
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_PUBLISHABLE_KEY")
)

openai = OpenAI(
    os.environ.get("OPENAI_API_KEY")
)
