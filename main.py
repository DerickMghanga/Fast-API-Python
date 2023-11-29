from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# Create an Instance for fastAPI
app = FastAPI()



# POST req schema(pydantic model) ensures expected data from client
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

#Memory to save the posts
my_posts = [
    {"title": "title of post", "content": "content of post 1", "id": 1},
    {"title":"favourite foods", "content": "I like pizza", "id": 2}
]


@app.get("/")
def root():
    return {"message": "Welcome to my first Python API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000)
    my_posts.append()
    return {"data": post}


# Schema example >> title: str, content: str, category: str, published: Bool