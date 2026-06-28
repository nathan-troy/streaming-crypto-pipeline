import ccxt
import time
import uuid
import duckdb

try:
    exchange = ccxt.binance()

    while True:
        btc_raw = exchange.fetch_ticker('BTC/USDT')
        btc_price = btc_raw['last']
        btc_volume = btc_raw['baseVolume']

        eth_raw = exchange.fetch_ticker('ETH/USDT')
        eth_price = eth_raw['last']
        eth_volume = eth_raw['baseVolume']

        print("Saving record to crypto_pipeline.db...")
        conn = duckdb.connect("crypto_pipeline.db")
        cursor = conn.cursor()

        insert_sql = """
        INSERT INTO price_ticks (tick_id, asset_id, exchange_id, price_usd, volume_24h, timestamp)
        VALUES (?, ?, ?, ?, ?, ?);
        """

        cursor.execute(insert_sql, (str(uuid.uuid4()), "bitcoin", "BINANCE", float(btc_price), float(btc_volume), time.strftime('%Y-%m-%d %H:%M:%S')))
        cursor.execute(insert_sql, (str(uuid.uuid4()), "ethereum", "BINANCE", float(eth_price), float(eth_volume), time.strftime('%Y-%m-%d %H:%M:%S')))

        conn.commit()
        conn.close()

        print(f"Saved BTC: ${btc_price:,.2f} | ETH: ${eth_price:,.2f} to Database.")
        print("Wait 10 seconds for update...\n")

        time.sleep(10)

except KeyboardInterrupt:
    print("\n Pipeline stopped by user.")
except Exception as e:
    print(f"Pipeline failed: {e}")