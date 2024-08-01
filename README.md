# Arabic Wiki RAG

A RAG (Retrieval-Augmented Generation) application for Arabic Wiki utilizing the Aya model.

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

1. **Verify the Milvus server address:**
   - Execute the following command to ensure the Milvus server address is correct:
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

---

Feel free to contribute to the project by opening issues and submitting pull requests. For any questions, refer to the documentation or contact the maintainers.

Enjoy using Arabic Wiki RAG!