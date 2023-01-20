from app import create_app
import dotenv

# app = create_app()


if __name__ == "__main__":
    dotenv.load_dotenv()
    create_app().run(debug=True)
