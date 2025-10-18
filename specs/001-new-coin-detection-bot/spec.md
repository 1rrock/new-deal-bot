# Feature Specification: New Coin Detection Trading Bot

**Feature Branch**: `001-new-coin-detection-bot`  
**Created**: 2025년 10월 18일  
**Status**: Draft  
**Input**: User description: "업비트 신규 상장 코인을 1.5초마다 감지하고, 신규 상장 시 자동으로 시장가 매수 후 매수가 대비 +2.4%로 지정가 매도 주문(limit order)을 등록하는 트레이딩 봇을 개발한다."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 신규 코인 자동 감지 및 거래 (Priority: P1)

트레이더가 트레이딩 봇을 실행하면, 봇이 1.5초마다 업비트 API를 통해 전체 코인 리스트를 조회하고, 이전 리스트와 비교하여 신규 상장 코인을 자동으로 감지한다. 신규 상장 감지 시 잔고의 50% (수수료 0.139% 고려)로 시장가 매수를 수행하고, 매수 체결 후 매수가의 +2.4% 가격으로 지정가 매도 주문을 등록한다.

**Why this priority**: 이 기능이 트레이딩 봇의 핵심 기능으로, 신규 코인 상장을 놓치지 않고 자동으로 거래할 수 있게 함.

**Independent Test**: 봇을 실행하고 테스트 코인을 상장시키면 자동으로 매수/매도 주문이 등록되는지 확인.

**Acceptance Scenarios**:

1. **Given** 봇이 실행 중, **When** 업비트에 신규 코인이 상장됨, **Then** 봇이 1.5초 이내에 감지하고 잔고 50% (수수료 고려)로 시장가 매수 주문 실행.
2. **Given** 매수 주문 체결됨, **When** 체결 가격 확보, **Then** +2.4% 가격으로 지정가 매도 주문 등록.
3. **Given** 매수 실패, **When** 에러 발생, **Then** 로그 기록 후 다음 감지 대기.

---

### Edge Cases

- API 호출 실패 시 재시도 또는 다음 주기로 넘김.
- 이미 매수한 코인이 다시 감지되면 중복 매수 방지.
- 매수 후 체결 전에 가격 변동 시 지정가 매도 가격 조정 필요성.
- 네트워크 문제로 감지 지연 시.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: 봇은 1.5초 주기로 전체 코인 리스트를 조회해야 함.
- **FR-002**: 이전 조회 결과와 비교하여 신규 추가된 코인을 판별해야 함.
- **FR-003**: 신규 코인 감지 시 시장가 매수 주문을 실행해야 함.
- **FR-004**: 매수 체결 후 평균 매수가와 수량을 확보해야 함.
- **FR-005**: 매수가의 +2.4% 가격으로 지정가 매도 주문을 등록해야 함.
- **FR-006**: 모든 거래 성공/실패를 로그와 콘솔에 기록해야 함.
- **FR-007**: 예외 발생 시 재시도하지 않고 로그 기록 후 계속 실행.

### Key Entities *(include if feature involves data)*

- **Coin**: 시장 코드(market), 코인 이름, 상장 상태.
- **Order**: 주문 타입(buy/sell), 가격, 수량, 상태.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 신규 코인 상장 후 2초 이내에 감지하고 매수 주문 실행.
- **SC-002**: 매수 성공률 95% 이상.
- **SC-003**: 지정가 매도 주문 등록 성공률 100%.
- **SC-004**: 봇 실행 중 외부 서비스 실패 시 1분 이내 복구.</content>
<parameter name="filePath">/Users/1rrock/Documents/new-deal-bot/specs/001-new-coin-detection-bot/spec.md