import uvicorn

from src.utils.env import env


def main():
    host = "localhost"
    port = env.PORT
    uvicorn.run("src.infra.server.server:app", host=host, port=port, server_header=False)


if __name__ == "__main__":
    main()
