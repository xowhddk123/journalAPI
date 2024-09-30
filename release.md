## Release Note
2024.08.28
- version 1.0.0 released

2024.09.02
- journal.yaml의 prompt를 수정
    - 일기 제목을 생성하고 줄 바꿈을 두 번 실행하도록 수정
    - 일기 내용을 생성할 때 문장마다 줄 바꿈을 하도록 수정

2024.09.06
- version 1.0.1 released
- journal.yaml의 prompt를 수정
    - 일기 제목을 생성할 때 줄 바꿈을 두 번 실행하도록 수정
    - 일기 내용을 생성할 때 문장마다 줄 바꿈을 하도록 수정
- chat.yaml의 prompt를 수정
- test script 추가

2024.09.07
- version 1.0.2 released
- journal.yaml의 prompt를 수정
    - 출력형식을 json으로 변경

- langchain 관련 오류 수정
    - langchain version 0.2.0에서는 더 이상 지원하지 않아 기존의 langchain -> langchain_community 변경.
- user의 nickname을 추가하는 기능에서 오류가 발생해서 우선 제거 -> 향후 추가 예정

2024.09.08
- version 1.1.0 released
- journal.yaml의 prompt를 수정
    - 대화에서 먼저 사용자가 한 일을 추출하도록 수정
    - 한 일에서 키워드를 추출하도록 수정
    - 한일을 바탕으로 일기를 작성하도록 수정
- chat.yaml의 prompt를 수정
    - 사용자와 bot의 이름을 지정할 수 있도록 수정