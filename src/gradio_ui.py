import gradio as gr
from utils.data_models import History
from rag import generate_response, generate_response_streaming


def rag_chat(query, history):
    history_list = [History(question=h[0], answer=h[1]) for h in history]
    complete_message = ""
    for message in generate_response_streaming(query, history_list):
        if message:
            complete_message += message
            yield complete_message


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(placeholder="Ask Me Anything", rtl=True)
    gr.ChatInterface(fn=rag_chat, chatbot=chatbot)

demo.launch(server_name="0.0.0.0", server_port=3000)
