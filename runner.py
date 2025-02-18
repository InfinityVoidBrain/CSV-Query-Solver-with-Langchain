import os
import time
from pyngrok import ngrok

def install_dependencies():
    os.system("pip install -r requirements.txt")

def start_ngrok(port=8501):
    ngrok.kill()
    public_url = ngrok.connect(port=port)
    print(f"Public URL: {public_url}")
    return public_url

def run_streamlit():
    os.system("streamlit run main.py &")
    time.sleep(5)

if __name__ == "__main__":
    install_dependencies()
    url = start_ngrok()
    run_streamlit()
    print(f"Streamlit App Running at: {url}")
