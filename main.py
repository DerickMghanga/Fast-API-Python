from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

# Create an Instance for fastAPI
app = FastAPI()



# POST request schema(pydantic model) expected data from client
class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Welcome to my first Python API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    return {"data": "new post"}


# Schema example >> title: str, content: str, category: str, published: Bool