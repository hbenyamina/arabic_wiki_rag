import gradio as gr
from typing import List
import requests
import argparse


HOST = "http://localhost:3000"


def generate_response_streaming(query: str, history: List[dict]):
    global HOST
    search_model = {"query": query, "history": history}
    print(search_model)
    response = requests.get(f"{HOST}/ask/stream", json=search_model, stream=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            print(decoded_line)
            if decoded_line.startswith("data: "):
                if decoded_line[6:]:
                    yield decoded_line[6:]


def rag_chat(query, history):
    history_list = [{"question": h[0], "answer": h[1]} for h in history]
    complete_message = ""
    for message in generate_response_streaming(query, history_list):
        if message:
            complete_message += message
            yield complete_message


def main():
    global HOST
    parser = argparse.ArgumentParser(description="Launch a Gradio demo with chatbot.")
    parser.add_argument(
        "--rag_api_host",
        type=str,
        required=False,
        help="Host to the RAG service.",
        default=HOST,
    )
    parser.add_argument(
        "--port",
        type=int,
        required=False,
        help="Port number to launch the Gradio app.",
        default=7860,
    )

    args = parser.parse_args()

    HOST = args.rag_api_host

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(placeholder="اسئلني أي شيء", rtl=True)
        gr.ChatInterface(fn=rag_chat, chatbot=chatbot)

    demo.launch(server_port=args.port)


if __name__ == "__main__":
    main()
