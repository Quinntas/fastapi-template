# FastAPI Template

This is a template project for FastAPI, a modern web framework for building APIs with Python.

## Installation

To install the project dependencies, make sure you have Poetry installed. You can install it via pip if you haven't
already:

```bash
pip install poetry
```

Once you have Poetry installed, you can clone this repository and install the dependencies:

```bash
poetry install
```

## Running the project

To run the project, you can use the following command:

```bash
poetry run uvicorn src.start.app:app --reload
```

This will start the FastAPI server and make it available at `http://localhost:8000`.

## Project structure

The project is structured as follows:

- `src/core`: Contains the core components of the project, such as controllers, middlewares, and DTOs.
- `src/shared`: Contains the shared components of the project, such as the shared router and the health check
  controller.
- `src/start`: Contains the main application file and the routes.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.