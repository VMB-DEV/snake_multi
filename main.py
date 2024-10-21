import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pygame
import asyncio

from engine.engine import Engine

async def main():
    pygame.init()
    engine = Engine()
    await engine.start()

if __name__ == "__main__":
    asyncio.run(main())
