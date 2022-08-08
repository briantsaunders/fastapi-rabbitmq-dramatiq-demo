from app import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        debug=True,
        log_config="log_config.yml"
    )
