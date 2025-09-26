from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)

master_item_df=pd.read_excel("data/master_item_list.xlsx")

def filter_data(plant_category):
    category_filtered_df=master_item_df[master_item_df["main_category"]==plant_category]

    return category_filtered_df


main_categories=master_item_df["main_category"].unique().astype(str)
main_categories = list(set([x.strip() for x in main_categories if x and x.strip().lower() != "nan"]))
main_categories.sort() 

@app.route("/")
def index_page():
    
    return render_template("index.html",
                           main_categories=main_categories,
                           category="Our Top Products",)
    

# @app.route("/live_plants/")
# def live_plants():
#     live_plants_df=filter_data(plant_category="Live Plants")
#     live_plants_list = live_plants_df.to_dict(orient='records')
    
#     return render_template("live_plants/live_plants_index.html",
#                            live_plants=live_plants_list)

@app.route("/category/<category_name>/")
def show_category(category_name):
    # Filter products by category
    filtered = master_item_df[master_item_df["main_category"].astype(str).str.lower().str.strip() == category_name.lower()]

    # Pass filtered products to template
    return render_template("main_category/category.html", 
                           main_categories= main_categories, 
                           category=category_name, 
                           products=filtered.to_dict(orient="records"))

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)