from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

class PostDto(BaseModel):
    title: str
    content: str

posts: List[Post] = []

@app.post("/")
def create_post(request: PostDto):
    post = Post(title=request.title, content=request.content)
    posts.append(post)
    return post

@app.get("/", response_model=List[Post])
def get_posts():
    return posts

@app.put("/{postId}")
def update_post(postId: int, request: PostDto):
    post = posts[postId - 1]
    post.content = request.content
    post.title = request.title
    return post

@app.delete("/{postId}")
def delete_post(postId: int):
    deleted = posts.pop(postId - 1)
    return deleted

# uvicorn 파일이름:app --reload