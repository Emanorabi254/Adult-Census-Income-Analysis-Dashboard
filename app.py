import dash
from dash import dcc, html, Input, Output
from data_processing import get_cleaned_data
from dashboard_layouts import create_figures

# 1. Initialize data
data = get_cleaned_data()

app = dash.Dash(__name__)

app.layout = html.Div([
    # Header
    html.Div([
        html.H1("📊 Adult Census Income",
                style={
                    'textAlign': 'center',
                    'color': 'white',
                    'padding': '30px',
                    'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                    'margin': '0',
                    'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
                }),
    ]),

    # 2. Age Range Filter Section
    html.Div([
        html.Label("🔍 Filter by Age Group:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
        dcc.Dropdown(
            id='age-filter',
            options=[{'label': age, 'value': age} for age in sorted(data['age_range'].unique())],
            value=list(data['age_range'].unique()), 
            multi=True,
            placeholder="Select age groups...",
            style={'width': '100%'}
        )
    ], style={'padding': '20px', 'backgroundColor': 'white', 'margin': '20px', 'borderRadius': '12px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.05)'}),
    
    # Navigation Tabs
    dcc.Tabs(id='tabs', value='overview', children=[
        dcc.Tab(label='📈 Overview', value='overview',
                style={'fontWeight': 'bold'},
                selected_style={'fontWeight': 'bold', 'color': '#667eea'}),
        dcc.Tab(label='👥 Demographics', value='demographics',
                style={'fontWeight': 'bold'},
                selected_style={'fontWeight': 'bold', 'color': '#667eea'}),
        dcc.Tab(label='💼 Work & Income', value='work',
                style={'fontWeight': 'bold'},
                selected_style={'fontWeight': 'bold', 'color': '#667eea'}),
        dcc.Tab(label='🎓 Education', value='education',
                style={'fontWeight': 'bold'},
                selected_style={'fontWeight': 'bold', 'color': '#667eea'}),
        dcc.Tab(label='💑 Relationships', value='relationships',
                style={'fontWeight': 'bold'},
                selected_style={'fontWeight': 'bold', 'color': '#667eea'}),
    ], style={'margin': '0 20px 20px 20px'}),
    
    # Content Area
    html.Div(id='tab-content', style={'padding': '0 20px 20px 20px'})
])

@app.callback(
    Output('tab-content', 'children'),
    [Input('tabs', 'value'),
     Input('age-filter', 'value')]
)
def render_content(tab, selected_ages):
    # 1. Filter data based on Age Dropdown
    if not selected_ages:
        return html.Div("Please select at least one age group.", style={'textAlign': 'center', 'padding': '50px'})
    
    filtered_df = data[data['age_range'].isin(selected_ages)]
    
    # 2. Generate updated figures for filtered data
    figs = create_figures(filtered_df)
    
    if tab == 'overview':
        return html.Div([
            # Cards Section (Updated with filtered values)
            html.Div([
                html.Div([
                    html.H3("Total Records", style={'color': '#667eea'}),
                    html.H2(f"{len(filtered_df):,}", style={'fontSize': '40px'})
                ], className='stat-card'),
                html.Div([
                    html.H3("High Earners", style={'color': '#10b981'}),
                    html.H2(f"{(filtered_df['income'] == '>50K').mean()*100:.1f}%", style={'fontSize': '40px'})
                ], className='stat-card'),
                html.Div([
                    html.H3("Avg Age", style={'color': '#f59e0b'}),
                    html.H2(f"{filtered_df['age'].mean():.1f}", style={'fontSize': '40px'})
                ], className='stat-card'),
                html.Div([
                    html.H3("Avg Hours/Week", style={'color': '#ef4444'}),
                    html.H2(f"{filtered_df['hours.per.week'].mean():.1f}", style={'fontSize': '40px'})
                ], className='stat-card'),
            ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '20px', 'marginBottom': '30px'}),
            
            # Graphs Section
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_age'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_income_dist'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}),
            
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_hours_income'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_gender'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px'}),
        ])
    
    elif tab == 'demographics':
        return html.Div([
            html.H2("👥 Demographic Analysis", style={'color': '#667eea', 'marginBottom': '20px'}),
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_race'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_native'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}),
            dcc.Graph(figure=figs['fig_gender_occ']),
        ])
    
    elif tab == 'work':
        return html.Div([
            html.H2("💼 Work & Income Analysis", style={'color': '#667eea', 'marginBottom': '20px'}),
            dcc.Graph(figure=figs['fig_work_pie']),
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_cond_prob'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_avg_hours'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}),
            dcc.Graph(figure=figs['fig_work_sex']),
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_occupation'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_occupation_hours'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}),
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_workclass'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_workclass_dist'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px'}),
        ])
    
    elif tab == 'education':
        return html.Div([
            html.H2("🎓 Education Impact", style={'color': '#667eea', 'marginBottom': '20px'}),
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_edu_box'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_edu_bar'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}),
            dcc.Graph(figure=figs['fig_heatmap']),
            dcc.Graph(figure=figs['fig_edu_occ']),
            dcc.Graph(figure=figs['fig_gender_gap']),
        ])
    
    elif tab == 'relationships':
        return html.Div([
            html.H2("💑 Relationship & Marital Status", style={'color': '#667eea', 'marginBottom': '20px'}),
            html.Div([
                html.Div([dcc.Graph(figure=figs['fig_marital'])], style={'width': '50%'}),
                html.Div([dcc.Graph(figure=figs['fig_relationship'])], style={'width': '50%'}),
            ], style={'display': 'flex', 'gap': '20px'}),
        ])

# CSS remains the same
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Adult Census Dashboard</title>
        {%favicon%}
        {%css%}
        <style>
            .stat-card {
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                text-align: center;
                border-left: 5px solid #667eea;
            }
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: #f8f9fa;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)