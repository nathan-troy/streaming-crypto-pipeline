import duckdb

conn = duckdb.connect("crypto_pipeline.db")

try:
    total_ticks = conn.execute("SELECT COUNT(*) FROM price_ticks;").fetchone()[0]
    print(f"\n TOTAL STREAMING RECORDSl {total_ticks}")

    print("\n LIVE METRICS:")
    metrics_query = """
        SELECT
            asset_id,
            COUNT(*) as data_points,
            MIN(price_usd) as lowest_price,
            MAX(price_usd) as highest_price,
            AVG(price_usd) as average_price
        FROM price_ticks
        GROUP BY asset_id;
"""
    df_metrics = conn.execute(metrics_query).df()
    print(df_metrics.to_string(index=False))

    print("\n HISTORY LOG (LAST 6 ROWS):") # Verify historical logging with time-series logs
    df_history = conn.execute("""
    SELECT asset_id, price_usd, timestamp
    FROM price_ticks
    ORDER BY timestamp DESC
    LIMIT 6;
""").df()
    print(df_history.to_string(index=False))

except Exception as e:
    print(f"Read failed: {e}")
finally:
    conn.close()