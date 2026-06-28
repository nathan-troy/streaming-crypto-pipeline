CREATE TABLE IF NOT EXISTS assets (
    asset_id VARCHAR PRIMARY KEY,
    ticker_symbol VARCHAR NOT NULL,
    asset_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS exchanges (
    exchange_id VARCHAR PRIMARY KEY,
    exchange_name VARCHAR NOT NULL,
    api_endpoint VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS price_ticks (
    tick_id VARCHAR PRIMARY KEY,
    asset_id VARCHAR,
    exchange_id VARCHAR,
    price_usd DOUBLE NOT NULL,
    volume_24h DOUBLE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE RESTRICT,
    FOREIGN KEY (exchange_id) REFERENCES exchanges(exchange_id) ON DELETE RESTRICT
);