from flask import Blueprint, render_template
from app.models import Plant

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)

@main_bp.route('/product/<int:plant_id>')
def product_detail(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    return render_template('product_detail.html', plant=plant)