# Arabic Wiki RAG

A RAG (Retrieval-Augmented Generation) application for Arabic Wiki utilizing the Aya model.

![](https://github.com/hbenyamina/arabic_wiki_rag/blob/f69445b250a34819b10d8b2a56e4b34f0f736458/assets/demo.gif)

## Project Overview
This project implements a high-speed, local Retrieval-Augmented Generation (RAG) system. It combines vLLM, Huggingface's text embedding inference, and Milvus to deliver efficient RAG performance using only a single GPU.

## Hardware Requirements
The project has been successfully tested on an NVIDIA L4 GPU with 24GB of VRAM. GPUs with less VRAM might not be sufficient to run the project due to the high memory requirements of the components involved.



## Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create and configure the `.env` file:**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Open the `.env` file and update the values accordingly. Ensure to include the correct IP address (use the network card IP, e.g., `172.0.0.1`).

3. **Run the project using Docker Compose:**
   ```bash
   docker-compose up -d
   ```

## Project Properties

- **Generation Model:**
  - Can run any generation model. The default model is `CohereForAI/aya-23-8B`.

- **Embedding Model:**
  - Can run any embedding model. Ensure to adjust the vector embedding size according to the model. The default model is `intfloat/multilingual-e5-base`.

## Data Indexing

To index the data in Milvus, follow these steps after running Docker Compose:

1. **Ensure Milvus is running correctly:**
   - Execute the following command to ensure that Milvus is running correctly:
     ```bash
     curl http://<ip_address>:19530/v1/vector/collections
     ```

2. **Ensure the embedding model is running correctly:**
   - Execute the following command to verify the embedding model status:
     ```bash
     curl http://<ip_address>:8080/info
     ```

3. **Index the dataset:**
   - Run the following command to index the dataset:
     ```bash
     docker exec -it rag_server python3 index_dataset.py
     ```

4. **Learn more about the indexing script:**
   - Use the following command to get detailed information about the indexing script:
     ```bash
     docker exec -it rag_server python3 index_dataset.py --help
     ```

## Launching the Demo
A demonstration of the project is available using Gradio, located in the `demo/` directory. Follow these steps to launch the demo:

1. Ensure all required services are up and running.
2. Navigate to the `demo/` directory.
3. Execute the following command:

```bash
python gradio_ui.py --rag_api_host "http://127.0.0.1:3000" --port 7860
```

This command will start the Gradio demo interface on port 7860, connecting to the RAG API hosted locally at `http://127.0.0.1:3000`.



---

Feel free to contribute to the project by opening issues and submitting pull requests. For any questions, refer to the documentation or contact the maintainers.

Enjoy using Arabic Wiki RAG!