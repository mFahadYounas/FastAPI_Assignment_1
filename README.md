# Task Manager CLI

## About The Project

This project consists of basic python end points made in python using Fast API as part of a course assignment.

## Getting Started

This section will guide you through setting up your project locally. To get a local copy up and running, follow these simple steps.

### Prerequisites

You need uv as your Python package and project manager.
Refer to https://docs.astral.sh/uv/#installation for details on installation

### Installation

1.  Clone the repo
    ```bash
    git clone git@github.com:mFahadYounas/FastAPI_Assignment_1.git
    ```
    If you already have a version of the repo, make sure to get the latest version but pulling from the above repo
2.  Navigate into the project directory
    ```bash
    cd FastAPI_Assignment_1
    ```
3.  Use the following command to prepare your environment for running
    ```bash
    uv sync
    ```

## Usage

1. Run the application by using the following command:

```bash
uvicorn main:app
```

2. Open localhost:8000/docs to try out the API