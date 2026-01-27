# api-docs

API reference and SDK documentation for Waldur cloud management platform

## About

This repository contains the source code for the Waldur API documentation. It is built using [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Local Development

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

### Setup

Install the dependencies:

```bash
uv sync
```

### Running the development server

Start the development server:

```bash
uv run mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000/`.

## Building

To build the documentation, run:

```bash
uv run mkdocs build
```

The built site will be in the `site` directory.
