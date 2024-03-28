from typing import Union
import httpx

class HTTP_TDB():
    def __init__(self, 
        url: str,
        cluster_id: str, 
        privacy_level: None = None, 
        public_key: str = "", 
        private_key: str = "",
        publish_changes: bool = True
        ):
        
        self.http_tdb_url = url
        self.http_client = httpx.AsyncClient()
        self.cluster_id = cluster_id
        self.privacy_level = privacy_level
        self.public_key = public_key
        self.private_key = private_key
        self.publish_changes = publish_changes

    async def open(self, database_name: str, init_query: str = "", index_query: str = ""):
        self.database_name = database_name
        
        response = await self.http_client.post(f"{self.http_tdb_url}/open", json={
            "database_name": self.database_name,
            "init_query": init_query
        })
        
        return response.text

    async def select(self, query: str):
        response = await self.http_client.post(f"{self.http_tdb_url}/select", json={
            "database_name": self.database_name,
            "query": query
        })
        
        return response.json()
    
    async def execute(self, query: str, publish_changes: Union[bool, None] = None):
        response = await self.http_client.post(f"{self.http_tdb_url}/execute", json={
            "database_name": self.database_name,
            "query": query
        })
        
        return response.text

    async def execute_async(self, query: str, publish_changes: Union[bool, None] = None, execute_after: int = 0):
        """
        You cannot set callback for this function.
        execute_after accepts integer (in milliseconds)
        """
        await self.http_client.post(f"{self.http_tdb_url}/execute", json={
            "database_name": self.database_name,
            "query": query,
            "execute_after": execute_after
        })

    def count(self, table_name: str, where_clause: str = ""):
        pass

    def destroy_local(self):
        pass