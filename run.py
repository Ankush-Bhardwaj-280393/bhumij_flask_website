from app import create_app

app = create_app()

if __name__ == '__main__':
    # Running locally
    app.run(debug=True)