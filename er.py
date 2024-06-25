from eralchemy2 import render_er
from database import Base
from models import Item

render_er(Base, "mermaid_erd.md", mode="mermaid_er")
render_er(Base, "models.er")
