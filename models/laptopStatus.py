from pydantic import BaseModel, Field
from typing import Optional

class LaptopStatus(BaseModel):
    name: str = Field(description="Laptop name")
    status_message: str = Field(description="status message")
    ip_address: str = Field(description="IP address of the laptop")
    echo: str | None = Field(default=None, description="Optional echo (query param)")
    path_echo: str | None = Field(default=None, description="Echo from path param (/health/{path_echo})")

    # Pydantic v2 style
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "ROG",
                "status_message": "Running",
                "ip_address": "192.168.1.10",
                "echo": "Hello from query",
                "path_echo": "Hello from path"
            }
        }
    }