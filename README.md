For this homework I created a visualization dashboard website using visualizations I created in my Python-API assignment. Specifically, I'll be plotting [weather data](Resources/weather_data.csv).

I created individual pages for each plot and a means by which people can navigate between them. These pages contain the visualizations and their corresponding explanations. There is also a landing page, a page where you can see a comparison of all of the plots, and another page where you can view the data used to build them.


### Website Requirements

For reference, see the ["Screenshots" section](#screenshots) below.

The website consist of 7 pages total, including:

* A [landing page](#landing-page) containing:
  * An explanation of the project.
  * Links to each visualizations page. There is a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.
* Four [visualization pages](#visualization-pages), each with:
  * A descriptive title and heading tag.
  * The plot/visualization itself for the selected comparison.
  * A paragraph describing the plot and its significance.
* A ["Comparisons" page](#comparisons-page) that:
  * Contains all of the visualizations on the same page so you can easily visually compare them.
  * Uses a Bootstrap grid for the visualizations.
    * The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.
* A ["Data" page](#data-page) that:
  * Displays a responsive table containing the data used in the visualizations.
    * The table is a bootstrap table component. [Hint](https://getbootstrap.com/docs/4.3/content/tables/#responsive-tables)
    * The data comes from exporting the `.csv` file as HTML, or converting it to HTML. For this, I used pandas. Pandas has a nifty method approprately called `to_html` that allowed me to generate a HTML table from a pandas dataframe. See the documentation [here](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.to_html.html)

The website has a navigation menu at the top of each page that:

* Has the name of the site on the left of the nav which allows users to return to the landing page from any page.
* Contains a dropdown menu on the right of the navbar named "Plots" that provides a link to each individual visualization page.
* Provides two more text links on the right: "Comparisons," which links to the comparisons page, and "Data," which links to the data page.
* Is responsive (using media queries). 
