# backend/routers/jobs.py

from fastapi import APIRouter

from typing import List

router = APIRouter()



# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다

MOCK_JOBS = [

    {

    "id": 1,
    "company": "KB국민은행",
    "title": "IT 개발·운영",
    "required_skills": ["Java", "Spring Boot", "SQL", "Oracle"],
    "preferred_skills": ["Kubernetes", "AWS", "금융권 경력"],
    "description": "온라인 뱅킹 및 대고객 서비스의 백엔드 시스템을 개발·운영합니다. 계좌·이체·조회 등 핵심 금융 거래 API의 안정성과 성능을 관리합니다. 장애 대응 및 배치 작업 모니터링도 담당합니다.",
    "deadline": "2026-08-31"

    },

    {

    "id": 2,
    "company": "신한은행",
    "title": "디지털금융 IT",
    "required_skills": ["Python", "FastAPI", "PostgreSQL", "REST API"],
    "preferred_skills": ["Docker", "Redis", "마이크로서비스"],
    "description": "모바일 뱅킹·간편결제 등 디지털 금융 서비스의 서버 API를 설계·개발합니다. 외부 핀테크·결제 연동 및 데이터 파이프라인 구축을 수행합니다. 서비스 출시 후 운영·개선 업무도 함께 진행합니다.",
    "deadline": "2026-08-31"

    },

    {

    "id": 3,
    "company": "NH투자증권",
    "title": "IT 시스템 개발",
    "required_skills": ["Java", "Spring", "Linux", "네트워크 기초"],
    "preferred_skills": ["증권·투자 도메인 이해", "Shell Script", "CI/CD"],
    "description": "주식·채권 등 증권 거래 및 HTS·MTS 연동 시스템을 개발·유지보수합니다. 실시간 시세 처리와 주문·체결 관련 서버 로직을 담당합니다. 금융 규제 및 보안 요건을 반영한 안정적인 시스템 운영을 목표로 합니다.",
    "deadline": "2026-08-31"

    }

]



@router.get("/jobs", tags=["Jobs"])

def get_jobs():

    """

    취업 공고 목록을 반환하는 엔드포인트.

    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.

    """

    return {

        "count": len(MOCK_JOBS),

        "jobs": MOCK_JOBS

    }



@router.get("/jobs/{job_id}", tags=["Jobs"])

def get_job_by_id(job_id: int):

    """

    특정 공고의 상세 정보를 반환한다.

    """

    for job in MOCK_JOBS:

        if job["id"] == job_id:

            return job

    # 찾지 못한 경우

    from fastapi import HTTPException

    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")