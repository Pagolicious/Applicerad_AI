from app import create_app
import dotenv
from RandomForest import random_forest_model


if __name__ == "__main__":
    random_forest_model.main()
    dotenv.load_dotenv()
    create_app().run(debug=True)
