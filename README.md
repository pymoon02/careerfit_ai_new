# careerfit\_ai\_new

# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치



## 프로젝트 개요

CareerFit AI는 취업 준비생이 자신의 전공과 보유 역량에 맞는 채용 공고를 쉽게 찾고, 부족한 역량을 파악할 수 있도록 돕는 AI 기반 커리어 코칭 서비스입니다.

취업 공고 데이터를 Pandas로 전처리하여 SQLite와 ChromaDB에 저장하고, RAG(Retrieval-Augmented Generation) 기반 검색 결과를 Gemini API와 결합하여 근거 기반의 맞춤형 역량 분석과 추천을 제공합니다.


## 기술 스택

| 영역              | 기술                    |
| --------------- | --------------------- |
| Backend         | Python 3.11, FastAPI  |
| Frontend        | React, Vite           |
| AI              | Gemini 2.5 Flash-Lite |
| Database        | SQLite, ChromaDB      |
| Data Processing | Pandas                |
| Deployment      | Docker, Render        |
| Version Control | Git, GitHub           |


## 시스템 아키텍쳐

사용자
    │
    ▼
React + Vite
    │
HTTP
    ▼
FastAPI
    │
 ┌───────────────┐
 │               │
 ▼               ▼
SQLite      ChromaDB
 │               │
 └───────┬───────┘
         ▼
   Gemini API
         │
         ▼
AI 분석 결과 + Sources


## 데이터 파이프라인

jobs.csv
      │
      ▼
Pandas 전처리
(결측치 제거 / 중복 제거 / 스킬 표준화)
      │
      ├────────► SQLite
      │          (구조화 데이터 저장)
      │
      └────────► RAG Document 생성
                   │
                   ▼
               ChromaDB


## 주요 기능

- 사용자 전공·보유 기술·관심 직무 입력
- RAG 기반 취업 공고 검색
- Gemini API 기반 역량 분석
- 부족한 기술 및 준비 방향 추천
- 추천 공고와 추천 이유 제공
- 분석 근거(sources) 함께 제공
- MOCK_MODE 지원
- Docker 기반 실행 및 배포 지원

## 프로젝트 구조

careerfit-ai/

backend/
 ├── routers/
 ├── services/
 ├── data/
 ├── chroma_db/
 ├── main.py
 └── Dockerfile

frontend/
 ├── src/
 ├── public/
 └── Dockerfile

docs/

README.md


## 로컬 실행

<백엔드>
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload

<FastAPI>
http://localhost:8000/docs

<프론트엔드>
cd frontend

npm install

npm run dev

<리액트>
http://localhost:5173


## Docker 실행

<이미지 생성>
docker build -t careerfit-ai .

<컨테이너 실행>
docker run -p 8000:8000 --env-file .env careerfit-ai

<API 확인>
http://localhost:8000/docs


## API

| Method | Endpoint | 설명       |
| ------ | -------- | -------- |
| GET    | /health  | 서버 상태 확인 |
| GET    | /jobs    | 채용 공고 조회 |
| POST   | /analyze | AI 역량 분석 |


## 사용한 데이터

- 취업 공고 CSV
- 기업명
- 직무명
- 필수 기술
- 우대 기술
- 직무 설명
- 직무 분야
- 마감일


## 전처리 과정

- 결측치 제거
- 중복 제거
- 기술명 표준화
- SQLite 저장
- RAG 문서 생성
- ChromaDB 저장


## 개발 과정에서 어려웠던 점

<Docker>
로컬 환경에서는 정상적으로 실행되었지만 Docker 컨테이너에서는 환경변수(.env) 전달과 실행 경로 문제를 해결해야 했습니다.

Dockerfile과 .dockerignore를 수정하고 Docker 컨테이너에서 동일한 환경으로 실행될 수 있도록 개선했습니다.

<RAG>
검색된 공고를 Gemini가 충분히 활용하지 못하는 문제가 있었습니다.

검색 결과를 프롬프트에 포함하고 출처(sources)를 함께 반환하도록 수정하여 근거 기반 응답이 가능하도록 개선했습니다.


## 향후 개선 사항

- 이력서 PDF 업로드 분석
- 실시간 채용 공고 API 연동
- 공모전 추천 기능
- RAG 검색 품질 평가(Ragas)
- 사용자 맞춤 학습 로드맵 제공


- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅

- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결

- [x] 3일차: 데이터 파이프라인 구축

- [x] 4일차: RAG 기반 서비스 + React UI

- [x] 5일차: Docker + 포트폴리오 완성
