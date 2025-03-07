from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)

master_item_df=pd.read_excel("data/master_item_list.xlsx")

def filter_data(plant_category):
    category_filtered_df=master_item_df[master_item_df["main_category"]==plant_category]

    return category_filtered_df

@app.route("/")
def index_page():
    live_plants_df=filter_data(plant_category="Live Plants")
    live_plants_list = live_plants_df.to_dict(orient='records')

    return render_template("index.html",
                           live_plants=live_plants_list)

@app.route("/live_plants/")
def live_plants():
    live_plants_df=filter_data(plant_category="Live Plants")
    live_plants_list = live_plants_df.to_dict(orient='records')
    
    return render_template("live_plants/live_plants_index.html",
                           live_plants=live_plants_list)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)