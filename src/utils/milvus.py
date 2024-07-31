from pymilvus import MilvusClient, DataType
from utils.config import MilvusConfig
from pymilvus import utility, connections


def get_client():
    client_config = MilvusConfig()
    client = MilvusClient(uri=client_config.uri)
    return client


def create_collection(client):
    if "wikipedia" not in client.list_collections():
        print("Collection does not exist. Creating ....")
        schema = MilvusClient.create_schema(
            auto_id=True,
            enable_dynamic_field=True,
        )

        # 3.2. Add fields to schema
        schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
        schema.add_field(field_name="url", datatype=DataType.VARCHAR, max_length=256)
        schema.add_field(field_name="article_id", datatype=DataType.INT64)
        schema.add_field(
            field_name="text", datatype=DataType.VARCHAR, max_length=512 * 4
        )
        schema.add_field(field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=768)

        index_params = client.prepare_index_params()

        index_params.add_index(
            field_name="vector",
            metric_type="IP",
        )
        client.create_collection(
            collection_name="wikipedia", schema=schema, index_params=index_params
        )
        return True
    else:
        print("Collection already exists")
        return False
