from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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


#Memory to save the posts. Array of dictionaries
my_posts = [
    {"title": "title of post", "content": "content of post 1", "id": 1},
    {"title":"favourite foods", "content": "I like pizza", "id": 2}
]


#Find the specific post in the my_posts array using id passed
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():
    return {"message": "Welcome to my first Python API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


#add a new post to the new_posts array with specific status code
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


#create a new post
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    return {"post_details": post}


