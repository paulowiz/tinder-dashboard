import pandas as pd
import plotly.graph_objs as go


# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    df = pd.read_csv('data/data_tinder.csv')
    df = df[df['App'] == 'Tinder']
    df['date'] = pd.to_datetime(df['Date&Time'], infer_datetime_format=True)
    df['year'] = pd.DatetimeIndex(df['date']).year
    df_group = df.groupby(['Rating', 'year']).count()
    df_group = df_group.reset_index()
    arr_ratings = df['Rating']
    arr_ratings = set(arr_ratings)

    graph_one = []
    colors = ['rgb(67,67,67)', 'rgb(255,88,100)', 'rgb(115,115,115)', 'rgb(115,115,115)', 'rgb(115,115,115)',
              'rgb(49,130,189)']
    mode_size = [8, 8, 8, 8, 8, 12]
    for rating, i in zip(arr_ratings, range(6)):
        x_value = df_group[df_group['Rating'] == rating]['year']
        y_value = df_group[df_group['Rating'] == rating]['Name']

        graph_one.append(
            go.Scatter(
                x=x_value,
                y=y_value,
                mode='lines',
                name=str(rating),
                marker=dict(color=colors[i], size=mode_size[i])
            )
        )
    layout_one = dict(title='The best rating in 2019 and worst in 2021.',
                      xaxis=dict(title='Year'),
                      yaxis=dict(title='Number of People')
                      )

    # second chart plots ararble land for 2015 as a bar chart
    df_group2 = df.groupby(['year']).mean()
    df_group2 = df_group2.reset_index()
    x_value = df_group2['year']
    y_value = df_group2['Rating']

    graph_two = []
    graph_two.append(
        go.Bar(
            x=x_value,
            y=y_value,
            marker=dict(color='rgb(255,88,100)')
        )
    )

    layout_two = dict(title='After 2018 the mean of ratings keep decreasing.',
                      title_x=0.5,
                      xaxis=dict(title='Years', tick0=min(x_value), dtick=1),
                      yaxis=dict(title='Rating Score'),
                      )

    # third chart plots percent of population that is rural from 1990 to 2015
    graph_four = []
    graph_four.append(
        go.Scatter(
            x=x_value,
            y=y_value,
            mode='lines',
            marker=dict(color='rgb(255,88,100)')
        )
    )

    layout_four = dict(title='Average Rating by Years',
                       xaxis=dict(title='Years'),
                       yaxis=dict(title='Average Rating'))

    # fourth chart shows rural population vs arable land
    graph_three = []
    df_group4 = df.groupby(['Rating']).count()
    df_group4 = df_group4.reset_index()
    x_value = df_group4['Name']
    y_value = df_group4['Rating']
    total = sum(x_value)
    size_arr = []
    for item in x_value:
        size_arr.append(((item / total) * 100) + 20)
    graph_three.append(
        go.Scatter(
            x=x_value,
            y=y_value,
            mode='markers',
            marker_size=size_arr,
            marker=dict(color='rgb(255,88,100)')
        )
    )

    layout_three = dict(title='Total of people by rating.',
                        xaxis=dict(title='Number of People'),
                        yaxis=dict(title='Rating number'),
                        )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
