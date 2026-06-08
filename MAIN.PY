"""
Solana Meme Coin Trading Bot
Author : Fikri Abd al-Hamid
GitHub : github.com/fikrigoldbot
Version: 1.0.0
"""

import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    try:
        import config
    except ImportError:
        logger.error("config.py not found — copy config.example.py to config.py first!")
        return

    from bot import SolanaBot

    logger.info("=" * 50)
    logger.info("🚀  Solana Meme Coin Bot  v1.0.0")
    logger.info(f"   RPC  : {config.RPC_URL[:40]}...")
    logger.info(f"   Scan : every {config.SCAN_INTERVAL_SECONDS}s")
    logger.info(f"   Risk : max {config.MAX_SOL_PER_TRADE} SOL/trade | "
                f"daily limit {config.DAILY_LOSS_LIMIT_SOL} SOL")
    logger.info("=" * 50)

    bot = SolanaBot(
        telegram_token=config.TELEGRAM_TOKEN,
        chat_id=config.TELEGRAM_CHAT_ID,
    )
    await bot.start()


if __name__ == "__main__":
    asyncio.run(main())
