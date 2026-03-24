from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Plant, CartItem

# 1. DEFINE the blueprint FIRST
cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart')
@login_required
def view_cart():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.plant.price * item.quantity for item in items)
    return render_template('cart.html', items=items, total=total)

@cart_bp.route('/add_to_cart/<int:plant_id>')
@login_required
def add_to_cart(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    existing_item = CartItem.query.filter_by(user_id=current_user.id, plant_id=plant.id).first()
    
    if existing_item:
        existing_item.quantity += 1
    else:
        new_item = CartItem(user_id=current_user.id, plant_id=plant.id)
        db.session.add(new_item)
        
    db.session.commit()
    flash(f'{plant.name} added to cart!', 'success')
    return redirect(url_for('main.index'))

@cart_bp.route('/checkout')
@login_required
def checkout():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not items:
        flash("Your cart is empty!", "warning")
        return redirect(url_for('main.index'))
    
    total = sum(item.plant.price * item.quantity for item in items)
    return render_template('checkout.html', items=items, total=total)