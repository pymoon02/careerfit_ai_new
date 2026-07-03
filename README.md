# careerfit\_ai\_new

# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치



## 프로젝트 개요



CareerFit AI는 사용자의 전공, 보유 기술, 관심 직무를 바탕으로 적합한 취업 공고를 추천하고 필요한 역량을 분석하는 AI 서비스입니다.
취업 준비생이 수많은 채용 공고를 직접 비교하지 않아도 자신의 역량과 적합한 직무를 쉽게 파악할 수 있도록 돕는 것을 목표로 합니다.


## 기술 스택



| 영역 | 기술 |

|---|---|

| 백엔드 | Python, FastAPI |

| AI API | Gemini 2.5 Flash-Lite |

| 데이터 | Pandas, SQLite, ChromaDB |

| 프론트엔드 | React, Vite |

| 실행 환경 | Docker |

## 로컬 실행 방법

## 사전 요구사항
- Python 3.12 이상
- Gemini API key

## 백엔드 실행
cd backend
python -m venv vene

#Windows
venv\Scripts\activate

pip install -r requirements.txt

# .env 파일 생성 (env.example 참고)
uvicorn main:app --reload --port 8000


API문서 : http://localhost:8000/docs

## API 엔드포인트
|메서드|경로|설명|
|---|---|---|
|GET|/health|서버 상태 확인|
|GET/jobs|취업 공고 목록 조회|
|POST|/analyze|역량 분석 및 추천|

## 데이터셋 구성
 jobs.csv는 한국 취업 시장을 반영한 목업 채용 공고 데이터입니다.

 - company : 기업명(유사 기업명 사용)
 - title : 채용 직무
 - required_skills : 필수 기술
 - preferred_skills : 우대 기술
 - description : 직무 설명
 - job_type : 직무 분야
 - deadline : 지원 마감일

## Pandas 데이터 전처리
 - 결측치 처리
 - 중복 데이터 제거
 - 스킬명 표준화
 - 분석 가능한 형태로 데이터 정제

## SQLite 저장
 - 전처리된 채용 공고 데이터를 SQLite 데이터베이스에 저장하여 구조화된 조회가 가능하도록 구성했습니다.

## RAG 문서 생성
 - 채용 공고 데이터를 LLM이 이해하기 쉬운 텍스트 형태로 변환하여 rag_documents.json을 생성했습니다.

## 진행 현황



- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅

- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결

- [x] 3일차: 데이터 파이프라인 구축

- [ ] 4일차: RAG 기반 서비스 + React UI

- [ ] 5일차: Docker + 포트폴리오 완성