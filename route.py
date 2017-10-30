from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, Place
from read_boss_dev import reqbossdata
import pandas as pd
import numpy as np
from bokeh.layouts import gridplot
from bokeh.models import HoverTool
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components

#create an instance of the flask class
app = Flask(__name__)

#configure the flask app to use the learning flask database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://h2mau:4dm1n@localhost:5432/learningflask'
#db.init_app(app)

# Protect the form using a security exploit called cross sight
# request forgery, or CSRF


#map the url / to the function index
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/population")
def population():
    df = pd.read_csv('./static/population_projections.csv')
    
    year= df.Year.as_matrix()
    sc1= df.Scenario1.as_matrix()/1000
    sc2= df.Scenario2.as_matrix()/1000
    sc3= df.Scenario3.as_matrix()/1000
    sc4= df.Scenario4.as_matrix()/1000
    
    plot = figure(plot_width=600, plot_height=600, 
                toolbar_location=None, title='China Population 2015-2050')

    plot.line(year, sc1, line_dash="4 4", line_width=1, color='gray')
    plot.line(year, sc2, line_dash="4 4", line_width=1, color='gray')
    plot.line(year, sc3, line_dash="4 4", line_width=1, color='gray')
    plot.line(year, sc4, line_dash="4 4", line_width=1, color='gray')
    
    plot.xaxis.axis_label = "year"
    plot.yaxis.axis_label = "population (in million)"

    cr = plot.circle(year, sc1, size=8,
                    fill_color="grey", hover_fill_color="firebrick",
                    fill_alpha=0.05, hover_alpha=0.3,
                    line_color="blue", hover_line_color="white",legend="Scenario 1")

    cr2 = plot.circle(year, sc2, size=8,
                    fill_color="grey", hover_fill_color="firebrick",
                    fill_alpha=0.05, hover_alpha=0.3,
                    line_color="green", hover_line_color="white",legend="Scenario 2")

    cr3 = plot.circle(year, sc3, size=8,
                    fill_color="grey", hover_fill_color="firebrick",
                    fill_alpha=0.05, hover_alpha=0.3,
                    line_color="orange", hover_line_color="white",legend="Scenario 3")
    
    cr4 = plot.circle(year, sc4, size=8,
                    fill_color="grey", hover_fill_color="firebrick",
                    fill_alpha=0.05, hover_alpha=0.3,
                    line_color="red", hover_line_color="white",legend="Scenario 4")

    plot.add_tools(HoverTool(tooltips=None, renderers=[cr, cr2, cr3, cr4], mode='hline'))
    
    scenarios = 4
    script, div = components(plot)
    return render_template("population.html", script=script, div=div, count=scenarios)

@app.route("/urbanization")
def urbanization():
     return render_template('urbanization.html')

@app.route("/appliances")
def appliances():
     return render_template('appliances.html')

@app.route("/sensors")
def sensors():
  reqbossdata()
  return render_template("sensors.html")


#statement if 'email' not in session, added to access the home.html webpage
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

if __name__== "__main__":
    app.run(debug=True)