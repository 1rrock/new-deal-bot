# New Coin Detection Trading Bot

업비트 신규 상장 코인을 자동으로 감지하고 시장가 매수 후 지정가 매도하는 트레이딩 봇.

## 기능

- 1.5초마다 업비트 전체 코인 리스트 조회
- 이전 리스트와 비교해 신규 상장 코인 감지
- 신규 코인 시 시장가 매수 (10,000 KRW)
- 매수 체결 후 매수가의 102.4%로 지정가 매도 주문 등록

## 설치

1. Python 3.9+ 설치
2. 의존성 설치: `pip install -r requirements.txt`
3. `.env` 파일에 API 키 설정:
   ```
   UPBIT_ACCESS_KEY=your_access_key
   UPBIT_SECRET_KEY=your_secret_key
   DRY_RUN=true  # 테스트 모드
   ```

## 실행

```bash
python bot.py
```

## 테스트

DRY_RUN=true로 설정하여 실제 거래 없이 시뮬레이션 실행.

## 주의

실제 거래 시 자산 손실 가능성 있음. 테스트 후 사용.