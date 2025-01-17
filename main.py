import uvicorn


def main() -> None:
    uvicorn.run("src.start.app:app", port=3000, reload=True)


if __name__ == "__main__":
    main()
