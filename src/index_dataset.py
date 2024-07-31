from langchain_text_splitters import CharacterTextSplitter
from utils.embedding import embed_batch
from utils.milvus import get_client, create_collection, insert_data
import click
from datasets import load_dataset
import traceback
import copy

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=512, chunk_overlap=3
)
MAX_BATCHES = 10


def index_batch(client, batch):
    batch = dict(batch)
    big_batch = []
    for index, id_ in enumerate(batch["id"]):
        for chunk in batch["chunks"][index]:
            text = chunk["text"]
            text = text[:2000]
            big_batch.append(
                {
                    "article_id": int(id_),
                    "url": batch["url"][index],
                    "vector": chunk["vector"],
                    "text": text,
                }
            )
    res = insert_data(client=client, data=big_batch)


def process_batch(batch):
    new_batch = copy.copy(batch)
    new_batch["chunks"] = []
    try:
        for index, _ in enumerate(new_batch["id"]):
            text = new_batch["text"][index]
            texts = text_splitter.split_text(text)[:MAX_BATCHES]
            texts = ["passage: " + text for text in texts]
            embeddings = embed_batch(texts)
            new_batch["chunks"].append(
                [
                    {"text": text, "vector": vector}
                    for (text, vector) in zip(texts, embeddings)
                ]
            )
        client = get_client()
        index_batch(client, new_batch)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
    return batch


@click.command()
@click.option("--dataset", default="wikimedia/wikipedia", help="Dataset to load.")
@click.option("--version", default="20231101.ar", help="Version of the dataset.")
@click.option(
    "--percentage",
    default=0.001,
    type=float,
    help="Percentage of the dataset to index.",
)
@click.option("--shuffle", is_flag=True, help="Whether or not to shuffle the dataset.")
def main(dataset, version, percentage, shuffle):
    client = get_client()
    create_collection(client)
    ds = load_dataset(dataset, version)
    length = len(ds["train"])
    dataset = ds["train"].select(range(int(length * percentage)))
    print(len(dataset))
    if shuffle:
        dataset = dataset.shuffle(seed=42)
    dataset = dataset.map(process_batch, batched=True, batch_size=32)


if __name__ == "__main__":
    main()
