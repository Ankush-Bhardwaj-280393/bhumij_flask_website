from app import create_app, db
from app.models import Plant

app = create_app()

def seed_database():
    with app.app_context():
        # 1. Clear existing plants to avoid duplicates during testing
        db.drop_all()
        db.create_all()

        # 2. Define your starting inventory
        initial_plants = [
            # Indoor Category
            Plant(name="Snake Plant", price=499, category="Indoor", image_file="default.jpg", stock=15),
            Plant(name="Peace Lily", price=350, category="Indoor", image_file="default.jpg", stock=10),
            
            # Succulents Category
            Plant(name="Aloe Vera", price=199, category="Succulents", image_file="default.jpg", stock=25),
            Plant(name="Echeveria", price=250, category="Succulents", image_file="default.jpg", stock=20),
            
            # Air Purifying Category
            Plant(name="Spider Plant", price=299, category="Air Purifying", image_file="default.jpg", stock=12),
            Plant(name="Areca Palm", price=850, category="Air Purifying", image_file="default.jpg", stock=5),
            
            # Low Maintenance Category
            Plant(name="Zamioculcas (ZZ)", price=600, category="Low Maintenance", image_file="default.jpg", stock=8),
            Plant(name="Money Plant", price=150, category="Low Maintenance", image_file="default.jpg", stock=30)
        ]

        # 3. Add to session and commit
        db.session.add_all(initial_plants)
        db.session.commit()
        
        print("🌱 Bhumij Plants database seeded successfully!")

if __name__ == '__main__':
    seed_database()