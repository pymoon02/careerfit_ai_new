# PROJECT_PLAN.md — CareerFit AI 프로젝트 기획 초안



## 1. 문제 정의

Q1) 취업 또는 공모전을 준비하면서 어려웠던 점은?
- 어떤 스킬을 준비해야 할지 모른다.
- 어느 정도 수준으로 준비해야 하는지 모르겠다.

Q2) CareerFit AI가 이 문제를 어떻게 해결하는가?
- 직무별 요구 스킬을 데이터로 정리한다.
- 내 역량과 비교해 부족한 역량을 알려준다.

## 2. 사용자 정의

- 대상: 취업 준비 중인 대학교 3~4학년, 공모전을 처음 도전하는 학생



- 사용 시나리오:

1. 사용자가 전공, 보유 스킬, 관심 직무를 입력한다.

2. CareerFit AI가 데이터를 검색해 역량 매칭 결과를 반환한다.

3. 어떤 데이터를 기반으로 답변했는지 출처를 함께 표시한다.



## 3. 데이터 계획

- 취업 공고 데이터 (jobs.csv)

컬럼	설명
company	기업명(유사 이름 사용)
title	채용 직무
required_skills	필수 기술
preferred_skills	우대 기술
description	직무 설명
job_type	직무 분야
deadline	지원 마감일

- 공모전 데이터 (competitions.csv)

컬럼	설명
organizer	주최 기관
title	공모전명
category	분야
target	참가 대상
required_skills	관련 기술
description	공모전 소개
deadline	접수 마감일


- 데이터 출처: 강사 제공 목업 CSV (3일차)



## 4. 기능 목록

[3단계 표 복사]



## 5. 향후 개선 아이디어

지금은 구현하지 않지만, 나중에 해보고 싶은 것들

- 예: 이력서 PDF 자동 분석

- 예: 공모전 마감일 달력 연동