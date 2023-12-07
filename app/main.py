from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randranges
import psycopg
from psycopg2.extras import RealDictCursor

# Create an Instance for fastAPI
app = FastAPI()


# POST/PUT req schema(pydantic model) ensures expected data from client
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

try:
    conn = psycopg.connect(host='localhost', database="FastAPI", user='postgres', password="Derick3329", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successfull !")
except Exception as error:
    print("Connectiing to database failed !")



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

#Function to index
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i



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


#Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #delete post, find the index in the array then pop from the array
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} doesn't exist")
    
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def  update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} doesn't exist")
    #Convert recieved data(post) to a dictionary
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}