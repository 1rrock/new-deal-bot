import os
from dotenv import load_dotenv
import pyupbit
import json
import time
import logging
import requests
from trading_spec import execute_buy_order, execute_sell_limit_order

# 로깅 설정
logging.basicConfig(filename='trading_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    load_dotenv()
    access = os.getenv('UPBIT_ACCESS_KEY')
    secret = os.getenv('UPBIT_SECRET_KEY')
    dry_run = os.getenv('DRY_RUN', 'false').lower() == 'true'

    if not access or not secret:
        print("❌ 환경변수 UPBIT_ACCESS_KEY 또는 UPBIT_SECRET_KEY가 설정되지 않았습니다.")
        return

    upbit = pyupbit.Upbit(access, secret)

    # 초기 코인 리스트 로드
    try:
        with open('coins.json', 'r') as f:
            previous_coins = json.load(f)
    except FileNotFoundError:
        previous_coins = []
        with open('coins.json', 'w') as f:
            json.dump(previous_coins, f)

    print("🚀 트레이딩 봇 시작...")

    while True:
        try:
            # 전체 마켓 리스트 조회
            response = requests.get('https://api.upbit.com/v1/market/all')
            markets = response.json()

            # KRW 마켓만 필터링
            current_coins = [m['market'] for m in markets if m['market'].startswith('KRW-')]

            # 신규 코인 감지
            new_coins = [c for c in current_coins if c not in previous_coins]

            if new_coins:
                print(f"🆕 신규 코인 {len(new_coins)}개 감지")
            else:
                print("🔄 코인 조회 완료, 신규 코인 없음")

            for coin in new_coins:
                print(f"🆕 신규 코인 감지: {coin}")
                logging.info(f"NEW_COIN_DETECTED: {coin}")

                # KRW 잔고 조회 및 50% 계산
                balances = upbit.get_balances()
                krw_balance = 0
                for balance in balances:
                    if balance['currency'] == 'KRW':
                        krw_balance = float(balance['balance'])
                        break
                buy_amount = krw_balance * 0.5  # 50%
                if buy_amount < 5000:  # 최소 금액 체크 (업비트 최소 주문 금액)
                    print(f"❌ 잔고 부족: {krw_balance}원")
                    continue

                if dry_run:
                    print(f"[DRY RUN] 매수 시뮬레이션: {coin} {buy_amount}원")
                    buy_result = {'uuid': 'dry-run-uuid'}
                else:
                    buy_result = execute_buy_order(upbit, coin, buy_amount)

                if buy_result:
                    # 주문 UUID로 체결 정보 조회
                    order_uuid = buy_result['uuid']
                    if dry_run:
                        order_info = {'state': 'done', 'executed_volume': '1.0', 'avg_buy_price': '1000'}
                    else:
                        time.sleep(1)  # 체결 대기
                        order_info = upbit.get_order(order_uuid)

                    if order_info and order_info['state'] == 'done':
                        executed_volume = float(order_info['executed_volume'])
                        avg_buy_price = float(order_info['avg_buy_price'])

                        # 지정가 매도: 매수가의 2.4%
                        sell_price = avg_buy_price * 0.024
                        if dry_run:
                            print(f"[DRY RUN] 매도 시뮬레이션: {coin} {executed_volume}개 @ {sell_price}원")
                            sell_result = {'uuid': 'dry-run-sell-uuid'}
                        else:
                            sell_result = execute_sell_limit_order(upbit, coin, executed_volume, sell_price)

                        if sell_result:
                            print(f"✅ {coin} 거래 완료")
                        else:
                            print(f"❌ {coin} 매도 주문 실패")
                    else:
                        print(f"❌ {coin} 매수 체결 실패")
                else:
                    print(f"❌ {coin} 매수 실패")

            # 현재 코인 리스트 저장
            with open('coins.json', 'w') as f:
                json.dump(current_coins, f)

            previous_coins = current_coins

        except Exception as e:
            print(f"❌ 봇 실행 오류: {e}")
            logging.error(f"BOT_ERROR: {e}")

        print("⏳ 1.5초 대기 중...")
        time.sleep(1.5)

if __name__ == "__main__":
    main()