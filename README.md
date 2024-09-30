# Journal Chatbot API for SlumberJack

## Description

하루를 정리하며 일기를 작성하는 것은 정신건강에 매우 이롭습니다. 하지만 매일 잠들기전에 일기를 쓴다는 것은 여간한 의지를 가지고 할 수 있는일이 아닙니다. SlumberJack의 핵심 기능인 일기 챗봇은 자신과 친한 친구와 오늘 있었던 일에 대해서 솔직하게 대화하다 보면 저절로 일기를 작성해주는 서비스입니다. 

## Introduction 

![service_diagram](https://github.com/user-attachments/assets/2b0c89b3-dad2-4f5f-97e4-ef703d75360e)

- 유저는 자신이 원하는 이름으로 불릴 수 있고 원하는 이름의 친구를 가질 수 있으며 친구의 성격 역시 유저가 원하는 성격을 선택할 수 있습니다. 
- 나에게 최적화된 친구와 오늘 있었던 일에 대해서 자연스럽게 대화하다보면 일기가 완성됩니다.

## Used Framework

1. fastAPI
2. langchain

## Environment
- python 3.11.5

## endpoints

### /chat/create/

1. input : 
   - Uuid : 사용자에게 부여된 고유 아이디
   - Nickname : 사용자의 닉네임
   - botname : 챗봇의 이름
   - bot style : 챗봇의 성격
2. output : 
   - input과 동일한 값을 확인차 보내준다. 

### /chat/
봇과 채팅하는 엔드포인트
1. Input : request로 묶어서 보낸다.
   - uuid : 사용자에게 부여된 고유 아이디
   - query : 사용자가 챗봇에게 보낸 질문
2. Output : 
    - uuid : 사용자에게 부여된 고유 아이디
    - nickname : 사용자의 닉네임
    - response : 챗봇이 사용자에게 보낸 답변

### /chat/complete
사용자가 진행한 대화를 인풋으로 하여 일기를 생성.
일기를 생성하고 나면 사용자의 대화 인스턴스를 삭제한다.
1. Input : 특별히 없음
2. Output : 
    - todaytasks : 사용자가 오늘 한 일과 감정
    - keywords : 오늘 한 일 중에서 키워드를 추출한 것
    - title : 일기의 제목
    - content : 일기의 내용
3. 최종형식
'''
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
### /chat/delete
생성되어있는 유저의 채팅 인스턴스와 일기 인스턴스를 삭제한다.
일반적인 경우에 일기를 작성하고 나면 사용했던 모든 인스턴스는 삭제된다. 
예외적인 경우를 위해 만들어둔 엔드포인트이다.
1. Input : 
    - uuid : 사용자에게 부여된 고유 아이디ㅏ
2. Output : "{request.uuid}'s Chatbot and Journalbot deleted"

