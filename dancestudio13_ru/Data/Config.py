
from dataclasses import dataclass



@dataclass
class Config:
    adminEmail: str = "XXXXXXXXXXXXXXXXXXXX"

    SMTPEmailLogin: str = "XXXXXXXXXXXXXXXXXXXX"
    SMTPEmailPassword:str = "XXXXXXXXXXXXXXXXXXXX"
    SMTPHost: str = "XXXXXXXXXXXXXXXXXXXX"
    SMTPPort: int = 0