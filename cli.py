import argparse
import logging
from bot.logging_config import setup_logging
from bot.orders import BinanceOrderService
from bot.validators import Validators 

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--symbol", type=Validators.validate_non_empty_string, required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=Validators.validate_order_side, required=True, help="BUY or SELL")
    parser.add_argument("--type", type=Validators.validate_order_type, required=True, help="MARKET or LIMIT")
    parser.add_argument("--qty", type=Validators.validate_positive_number, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=Validators.validate_price_limit_for_orders, help="Required for LIMIT orders")

    try:
        args = parser.parse_args()
    except Exception:
        return

    if args.type == "LIMIT" and (args.price is None or args.price <= 0):
        logging.error("Invalid input: LIMIT order requires a positive price.")
        return

    # Bot Initialization & Execution
    logging.info(f"Order Request: {args.symbol} {args.side} {args.type} Qty:{args.qty} Price:{args.price}")
    
    bot_order = BinanceOrderService()
    resp = bot_order.place_futures_order(args.symbol, args.side, args.type, args.qty, args.price)

    if "error" in resp:
        logging.error(f"API Error: {resp['error']}")
    else:
        # Print Order Response details
        logging.info("Order Placed Successfully!")
        print("-" * 30)
        print(f"Order ID: {resp.get('orderId')}")
        print(f"Status: {resp.get('status')}")
        print(f"Executed Qty: {resp.get('executedQty')}")
        print(f"Avg Price: {resp.get('avgPrice', 'N/A')}")
        print("-" * 30)

if __name__ == "__main__":
    main()