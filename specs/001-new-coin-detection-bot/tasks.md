# Task Breakdown: New Coin Detection Trading Bot

**Feature Branch**: `001-new-coin-detection-bot`  
**Created**: 2025년 10월 18일  
**Status**: Draft  

## Task List

### Phase 1: Setup & Infrastructure
- **T-001**: Python 가상환경 설정 및 의존성 설치 (`requirements.txt`).
- **T-002**: `.env` 파일 생성 및 API 키 설정.
- **T-003**: `coins.json` 초기화 (전체 코인 리스트 저장).

### Phase 2: Core Development
- **T-004**: `bot.py` 메인 스크립트 구현 (코인 감지 루프, 거래 로직).
- **T-005**: `trading_spec.py` 거래 함수 구현/수정 (`execute_buy_order`, `execute_sell_limit_order`).
- **T-006**: 로깅 및 예외 처리 추가.

### Phase 3: Testing & Documentation
- **T-007**: DRY_RUN 모드 테스트 및 로그 검증.
- **T-008**: 단위 테스트 작성 (선택적).
- **T-009**: `README.md` 및 `spec.md` 업데이트.
- **T-010**: 실제 실행 테스트 (주의: 실제 거래).

## Assignment
- **Developer**: 1rrock (본인).
- **Timeline**: 1-2일 (단순 구현).
- **Priority**: P1 (핵심 기능).

## Completion Criteria
- 모든 FR (Functional Requirements) 충족.
- 체크리스트 100% 통과.
- 실제 신규 코인 감지 시 거래 성공.