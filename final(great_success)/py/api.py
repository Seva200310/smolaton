from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json



class Input_topic(BaseModel):
    topic: str

class Input_link(BaseModel):
    link: str

class Input_id(BaseModel):
    zone_id: str

class Input_capture_checkup(BaseModel):
    zone_id: str
    zone_conqueror: str
    zone_capture_time:int

    

 
app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/game_setup")
async def setup_game(topic:Input_topic):
    print('--------------------------------------------------')
    topic=dict(topic)["topic"]
    #спарсить страницы из вики
    #классифицировать их
    #добавить в бд
    resp="ну типа работает"
    return resp

@app.get("/get_new_wikipage")
async def get_new_wikipage(link:Input_link):
    link=dict(link)["link"]
    #отредактировать страницу и вернуть ее html код(это значит 1)заменить буквы 2)убрать лишние поля 3)заменить гиперссылки на обращение к текущему методу апи)
    resp="ну типа работает"
    return resp

@app.get("/get_field_info")
async def get_field_info(zone_id:Input_id):
    zone_id=Input_id["zone_id"]
    #Вернуть из бд информацию  о зоне а именно ссылку на первую фотку, информацию о ценности,первый абзац из статьи
    resp="ну типа работает"
    return resp

@app.post("/capture_checkup")
async def capture_checkup(capture_data:Input_capture_checkup):
    capture_data=dict(Input_capture_checkup)
    #проверка захвата и изменение бд в случае успеха
    resp="ну типа работает"
    return resp

@app.get("/get_neighbour")
async def get_neighbour(zone_id:Input_id):
    zone_id=Input_id["zone_id"]
    #возвращает id граничных с зоной терииторий
    resp="ну типа работает"
    return resp