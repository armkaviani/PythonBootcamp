from datetime import datetime

PIXELA_API = "https://pixe.la/v1/users"
TOKEN = "your_token"
USERNAME = "your_username"

GRAPH_API = f"{PIXELA_API}/{USERNAME}/graphs"
GRAPH_ID = "graph-1"

POST_VALUE_API = f"{PIXELA_API}/{USERNAME}/graphs/{GRAPH_ID}"
TODAY = datetime(year=2025, month=4, day=24)

UPDATE_API = f"{PIXELA_API}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"
