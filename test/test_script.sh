#!/bin/zsh


curl -X POST "http://127.0.0.1:8000/chat/create/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "nickname":"태태", "botname":"챗챗"}'


curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"안녕"}'
curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"내 이름이 뭔지 알아?"}'
curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"너의 대화 예시를 알려줘"}'
curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"너의 대화 규칙에 대해서 알려줘"}'
curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"오늘은 헬스장에서 PT를 받았어. 가슴운동을 했는데 이전에 혼자 운동 할 때 보다 훨씬 운동이 잘 되어서 보람있는것 같아"}'
curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"음... 프레스 운동이 대부분 어려웠는데 특히 인클라인 덤밸프레스 운동은 몸의 밸런스 잡기가 어렵더라고"}'
curl -X POST "http://127.0.0.1:8000/chat/" -H "Content-Type: application/json" -d '{"uuid":"test-4412", "query":"이제 자야겠어 너무 피곤해"}'


curl -X POST "http://127.0.0.1:8000/chat/complete/" -H "Content-Type: application/json" -d '{"uuid":"test-4412"}'