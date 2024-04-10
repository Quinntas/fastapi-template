from __future__ import annotations

import uvicorn

from src.utils.env import env


def main():
    host = "0.0.0.0"
    port = env.PORT
    uvicorn.run(
        "src.infra.server.server:app",
        host=host,
        port=port,
        server_header=False,
        reload=True,
    )


if __name__ == "__main__":
    main()
