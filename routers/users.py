from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

import os
from dotenv import load_dotenv

from models import *

# # FastAPI 인스턴스를 생성합니다.
# app = FastAPI()

# router 객체 생성
router = APIRouter()

# OpenAI API 키를 설정합니다.
load_dotenv()  # .env 파일의 환경 변수를 로드합니다.
api_key = os.getenv('API_KEY')
port_num = os.getenv('PORT_NUM')


class CreateChatbotResponse(BaseModel):
    uuid: str
    nickname: str
    botname: str


class ChatRequest(BaseModel):
    uuid: str
    query: str


class JournalRequest(BaseModel):
    uuid: str


class DeleteChatbotRequest(BaseModel):
    uuid: str


#### 챗봇 API 엔드포인트를 정의합니다. ####
# 1. 챗봇 인스턴스 생성 엔드포인드
@router.post('/chat/create/', response_model=CreateChatbotResponse)
async def create_chatbot(request: CreateChatbotResponse):
    '''
    만약 사용자의 uuid에 해당하는 챗봇 인스턴스가 없다면 새로 생성하고,
    사용자의 uuid에 해당하는 챗봇 인스턴스가 있다면 해당 인스턴스를 삭제하고 새로 생성합니다.

    request : {"uuid": "사용자의 uuid", "nickname": "사용자의 닉네임", "botname": "사용자가 원하는 챗봇 이름"}
    '''
    try:
        if request.uuid in uuids2chatbot:
            del uuids2chatbot[request.uuid]  # 기존재하는 챗봇 인스턴스를 삭제합니다.
        if request.uuid in uuids2journalbot:
            del uuids2journalbot[request.uuid]
        if request.uuid in uuids2nickname:
            del uuids2nickname[request.uuid]
        if request.uuid in uuids2botname:
            del uuids2botname[request.uuid]

        # id를 키로 사용하여 챗봇 인스턴스를 저장합니다.
        uuids2chatbot[request.uuid] = get_chatbot_instance(uuid=request.uuid,
                                                           nickname=request.nickname,
                                                           botname=request.botname)  # uuid에 해당하는 챗봇 인스턴스 생성
        uuids2journalbot[request.uuid] = get_journal_instance(
            request.uuid)  # uuid에 해당하는 일기생성봇 인스턴스 생성
        uuids2nickname[request.uuid] = request.nickname  # 유저 닉네임 저장
        uuids2botname[request.uuid] = request.botname  # 유저가 원하는 챗봇 이름 저장
        return {"uuid": request.uuid, "nickname": request.nickname, "botname": request.botname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. 챗봇 대화 엔드포인트


@router.post("/chat/")
async def get_chat(request: ChatRequest):
    try:
        uuid = request.uuid
        nickname = uuids2nickname[uuid]
        query = request.query

        chatbot = uuids2chatbot[uuid]

        # 사용자 입력을 처리하고 응답을 생성합니다.
        response = chatbot.predict(input=query)
        return {"uuid": uuid, "nickname": nickname, "response": response}
    except Exception as e:
        # 오류 발생 시 HTTP 예외를 반환합니다.
        raise HTTPException(status_code=500, detail=str(e))

# 3. 일기생성 엔드포인트


@router.post("/chat/complete/")
async def gen_journal(request: JournalRequest):
    '''
    input : uuid
    output : 
    {"uuid":uuid, 
     "response":
        '{
        "todaytasks": "1. 헬스장에서 PT 받음\n2. 가슴운동 함\n3. 인클라인 덤벨프레스 운동이 어려웠음",
        "keywords": ["헬스장", "PT", "인클라인 덤벨프레스"],
        "title": "오늘의 헬스장에서의 도전",
        "content": "오늘은 헬스장에서 PT를 받았다.\n가슴운동을 했는데 혼자 할 때보다 훨씬 잘 되는 것 같아서 기분이 좋았다.\n그런데 인클라인 덤벨프레스 운동이 좀 어려웠다.\n밸런스를 잡는 게 힘들었는데, 계속하다 보면 익숙해질 것 같다.\n오늘 하루도 힘들었지만, 보람찬 하루였다.\n내일도 좋은 하루가 되길 바란다."
        }'
    }
    '''
    try:
        journalbot = uuids2journalbot[request.uuid]
        chatbot = uuids2chatbot[request.uuid]  # 대화 기록을 가져오기 위해 인스턴스를 가져옴

        response = journalbot.predict(history=chatbot.memory.buffer)
        return {"uuid": request.uuid, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 4. 챗봇 삭제 엔드포인드


@router.post('/chat/delete/', response_model=DeleteChatbotRequest)
async def del_chat(request: DeleteChatbotRequest):
    try:
        # 요청이 들어오면 챗봇을 삭제한다.
        if request.uuid in uuids2chatbot:
            del uuids2chatbot[request.uuid]
        # 요청이 들어오면 일기생성봇을 삭제한다.
        if request.uuid in uuids2journalbot:
            del uuids2journalbot[request.uuid]

            response = f"{request.uuid}'s Chatbot and Journalbot deleted"
        return {"uuid": request.uuid, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# test 주석 추가
