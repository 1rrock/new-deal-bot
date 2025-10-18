# Implementation Plan: New Coin Detection Trading Bot

**Feature Branch**: `001-new-coin-detection-bot`  
**Created**: 2025년 10월 18일  
**Status**: Draft  

## Implementation Strategy

- **Architecture**: Python 기반, `pyupbit` 라이브러리 사용. 메인 스크립트(`bot.py`)에서 루프 실행, `trading_spec.py`에 거래 함수 분리.
- **Key Components**:
  - 코인 감지: `requests`로 API 호출, JSON 비교.
  - 거래: 시장가 매수(잔고 50%, 수수료 0.139% 고려), 지정가 매도(+2.4%).
  - 로깅: 콘솔 + 파일(`trading_bot.log`).
- **Dependencies**: `pyupbit`, `python-dotenv`, `requests`.
- **Risks**: API 제한, 네트워크 오류 → 예외 처리 강화.

## Quality Assurance Checklist

- [x] 코드 리뷰: DRY_RUN 모드 테스트.
- [x] 단위 테스트: `execute_buy_order`, `execute_sell_limit_order` 함수 테스트.
- [x] 통합 테스트: 신규 코인 시뮬레이션.
- [x] 성능 테스트: 1.5초 루프 유지.
- [x] 보안: API 키 환경변수 사용.
- [x] 문서화: README.md, spec.md 업데이트.

## Success Metrics

- 감지 정확도: 100%.
- 거래 성공률: 95% 이상.
- 실행 안정성: 24시간 연속 실행.