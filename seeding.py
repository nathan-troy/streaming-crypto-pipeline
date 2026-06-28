import duckdb

print("Seeding Master Reference Tables...")

try:
    conn = duckdb.connect("crypto_pipeline.db")
    cursor = conn.cursor()

    print("Registering asset: Bitcoin (BTC)")
    cursor.execute("""
        INSERT INTO assets (asset_id, ticker_symbol, asset_name)
        VALUES ('bitcoin', 'BTC', 'Bitcoin')
        ON CONFLICT DO NOTHING;
""")
    
    print("Registering asset: Ethereum")
    cursor.execute("""
    INSERT INTO assets (asset_id, ticker_symbol, asset_name)
    VALUES ('ethereum', 'ETH', 'Ethereum')
    ON CONFLICT DO NOTHING;
""")
    
    print("Registering exchange: Binance")
    cursor.execute("""
    INSERT INTO exchanges (exchange_id, exchange_name, api_endpoint)
    VALUES ('BINANCE', 'Binance Exchange', 'https://binance.com')
    ON CONFLICT DO NOTHING;
""")
    
    conn.commit()
    conn.close()

except Exception as e:
    print(f"Seeding failed: {e}")