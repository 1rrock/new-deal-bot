import os
from dotenv import load_dotenv
import pyupbit
import json
import time
import logging
from datetime import datetime

def execute_buy_order(upbit, ticker, amount):
    """업비트 시장가 매수 주문"""
    try:
        result = upbit.buy_market_order(ticker, amount)
        if result:
            print(f"✅ {ticker} 매수 완료: {amount:,.0f}원")
            logging.info(f"BUY - {ticker}: {amount:,.0f}원")
            return result
        else:
            print(f"❌ {ticker} 매수 실패")
            logging.error(f"BUY_FAILED - {ticker}: {amount:,.0f}원")
            return None
    except Exception as e:
        print(f"❌ {ticker} 매수 오류: {e}")
        logging.error(f"BUY_ERROR - {ticker}: {e}")
        return None

def execute_sell_limit_order(upbit, ticker, volume, price):
    """업비트 지정가 매도 주문"""
    try:
        result = upbit.sell_limit_order(ticker, price, volume)
        if result:
            print(f"✅ {ticker} 지정가 매도 등록 완료: {volume:.6f}개 @ {price:,.0f}원")
            logging.info(f"SELL_LIMIT - {ticker}: {volume:.6f}개 @ {price:,.0f}원")
            return result
        else:
            print(f"❌ {ticker} 지정가 매도 실패")
            logging.error(f"SELL_LIMIT_FAILED - {ticker}: {volume:.6f}개 @ {price:,.0f}원")
            return None
    except Exception as e:
        print(f"❌ {ticker} 지정가 매도 오류: {e}")
        logging.error(f"SELL_LIMIT_ERROR - {ticker}: {e}")
        return None