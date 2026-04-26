# Pheynix Investment Account

## Overview
Investment division of Pheynix managing capital and tracking returns across various assets.

## Assets

### Cryptocurrency
- **Bitcoin (BTC)**: Store of value, digital gold
- **Ethereum (ETH)**: Smart contract platform, DeFi backbone

### Prediction Markets
- **Polymarket**: Event-based prediction markets
- **Markets**: Crypto prices, political events, sports outcomes

## Trading Strategy

### Entry Criteria
1. Market analysis before trading
2. Position sizing based on confidence level
3. Diversification across multiple markets

### Risk Management
- Max 5% of capital per trade
- Stop-loss on position size
- Track performance monthly

## Tools

### Polymarket CLI
- Browse markets: `polymarket markets list`
- Search markets: `polymarket markets search "bitcoin"`
- Check prices: `polymarket clob midpoint TOKEN_ID`
- Place orders: `polymarket clob market-order --token TOKEN_ID --side buy --amount 5`

### CoinGecko API
- Get prices: `python3 /tmp/btc_price.py`
- Multi-coin: `python3 /tmp/eth_price.py`

## Performance Tracking

| Date | BTC Price | ETH Price | Portfolio Value |
|------|-----------|-----------|-----------------|
| 2026-04-25 | $77,531 | $2,316 | TBD |

## Notes
- Prices updated regularly via tracker.py
- Track all trades in trades.log
- Monthly performance review
