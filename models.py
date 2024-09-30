import openai
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import load_prompt


from typing import Dict
import os
from dotenv import load_dotenv

# OpenAI API 키를 설정합니다.
load_dotenv()  # .env 파일의 환경 변수를 로드합니다.
api_key = os.getenv('API_KEY')
port_num = os.getenv('PORT_NUM')


# 요청 데이터를 정의하기 위한 Pydantic 모델입니다.
uuids2chatbot: Dict[str, LLMChain] = {}
uuids2journalbot: Dict[str, LLMChain] = {}
uuids2nickname: Dict[str, str] = {}  # 유저 닉네임 저장
uuids2botname: Dict[str, str] = {}  # 챗봇 이름 저장


def get_chatbot_instance(uuid: str, nickname: str, botname: str) -> LLMChain:
    """사용자의 세션 ID에 해당하는 챗봇 인스턴스를 가져오거나 생성합니다."""
    # 대화 프롬프트를 로드합니다.
    chat_prompt = load_prompt("prompts/chat.yaml")
    partial_variables = {"nickname": nickname, "botname": botname}
    # 대화 프롬프트에 partial_variables를 추가합니다.
    chat_prompt.partial_variables = partial_variables

    if uuid not in uuids2chatbot:
        # 새 챗본 인스턴스를 생성하고 저장합니다.

        # OpenAI의 GPT 모델을 사용하는 LLMChain을 생성합니다.
        llm = ChatOpenAI(model_name="gpt-4",  # 모델명
                         temperature=0.2,  # 창의성 0으로 설정
                         max_tokens=None,  # 최대 토큰 길이
                         api_key=api_key  # API 키
                         )
        memory = ConversationBufferMemory(memory_key='history',
                                          inpyt_key='input',
                                          human_prefix="태종", ai_prefix="챗챗")
        chatbot = ConversationChain(llm=llm,
                                    prompt=chat_prompt,
                                    memory=memory,
                                    verbose=True)  # 대화를 기억하는 인스턴스

    return chatbot


def get_journal_instance(uuid: str) -> LLMChain:
    # 일기 프롬프트를 로드합니다.
    # extracter_prompt = load_prompt("prompts/extract.yaml") # 대화에서 사용자가 오늘 한 일을 추출하는 프롬프트
    jouranl_prompt = load_prompt("prompts/journal.yaml")  # 일기를 작성하는 프롬프트

    if uuid not in uuids2journalbot:
        llm = ChatOpenAI(model_name="gpt-4",  # 모델명
                         temperature=0.2,  # 창의성 parameter
                         max_tokens=None,  # 최대 토큰 길이
                         api_key=api_key  # API 키
                         )
        journalbot = LLMChain(prompt=jouranl_prompt,
                              llm=llm,
                              verbose=True)
    return journalbot
