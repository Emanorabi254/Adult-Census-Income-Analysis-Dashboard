# ==============================
# Create All Figures
# ==============================
import plotly.express as px
import pandas as pd

def create_figures(data):
        
    # 1. Age Distribution
    fig_age = px.histogram(
        data, x='age', nbins=20, 
        title='Distribution of Age',
        color_discrete_sequence=['#3b82f6'],
        labels={'age': 'Age', 'count': 'Count'}
    )
    fig_age.update_layout(template="plotly_white", showlegend=False)

    # 2. Hours per Week vs Income
    fig_hours_income = px.box(
        data, x='income', y='hours.per.week',
        color='income',
        color_discrete_map={'<=50K':'#60a5fa', '>50K':'#f87171'},
        title='Hours per Week vs Income'
    )
    fig_hours_income.update_layout(template="plotly_white")

    # 3. Income by Gender
    fig_gender = px.histogram(
        data, x='sex', color='income',
        barmode='group',
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#f97316'},
        text_auto=True,
        title='Income Distribution by Sex'
    )
    fig_gender.update_traces(marker_line_width=0)
    fig_gender.update_layout(template="plotly_white")

    # 4. Income Distribution (Target)
    fig_income_dist = px.histogram(
        data, x="income",
        color_discrete_sequence=['#8b5cf6'],
        title="Income Distribution (Target Variable)"
    )
    fig_income_dist.update_layout(template="plotly_white")

    # 5. Income by Race
    fig_race = px.histogram(
        data, x="race", color="income",
        barmode="group",
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#10b981'},
        title="Income by Race"
    )
    fig_race.update_layout(template="plotly_white")

    # 6. US vs Non-US
    fig_native = px.histogram(
        data, x="native", color="income",
        barmode="group",
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#ef4444'},
        title="Income: US vs Non-US"
    )
    fig_native.update_layout(template="plotly_white")

    # 7. Education Level vs Income (Box)
    fig_edu_box = px.box(
        data, x="income", y="education.num",
        color='income',
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#10b981'},
        title="Education Level (Numeric) vs Income"
    )
    fig_edu_box.update_layout(template="plotly_white")

    # 8. Income by Education Level
    fig_edu_bar = px.histogram(
        data, x="education_level", color="income",
        barmode="group",
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#10b981'},
        title="Income by Education Level"
    )
    fig_edu_bar.update_xaxes(tickangle=-45)
    fig_edu_bar.update_layout(template="plotly_white")

    # 9. Conditional Probability - Work Intensity
    cond = (
        data.groupby("work_intensity")["income"]
        .apply(lambda x: (x == ">50K").mean())
        .reset_index(name="prob_>50K")
    )
    fig_cond_prob = px.bar(
        cond, x="work_intensity", y="prob_>50K",
        title="P(Income >50K | Work Intensity)",
        color_discrete_sequence=['#f59e0b']
    )
    fig_cond_prob.update_layout(template="plotly_white")

    # 10. Income by Occupation
    occupation_income = data.groupby(['occupation_grouped', 'income']).size().reset_index(name='count')
    fig_occupation = px.bar(
        occupation_income, x='occupation_grouped', y='count',
        color='income',
        barmode='group',
        color_discrete_map={'<=50K':'#ea580c', '>50K':'#fb923c'},
        title='Income Distribution by Occupation Group'
    )
    fig_occupation.update_layout(template="plotly_white")

    # 11. Hours per Week by Occupation
    fig_occupation_hours = px.box(
        data, x='occupation_grouped', y='hours.per.week',
        color='occupation_grouped',
        title='Hours per Week Distribution by Occupation'
    )
    fig_occupation_hours.update_layout(template="plotly_white", showlegend=False)

    # 12. Income by Workclass
    workclass_income = pd.crosstab(data['workclass'], data['income']).reset_index()
    workclass_income_melted = workclass_income.melt(id_vars='workclass', var_name='income', value_name='count')
    fig_workclass = px.bar(
        workclass_income_melted, x='workclass', y='count',
        color='income',
        barmode='group',
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#06b6d4'},
        title='Income Distribution by Workclass'
    )
    fig_workclass.update_xaxes(tickangle=-45)
    fig_workclass.update_layout(template="plotly_white")

    # 13. Workclass Distribution
    workclass_counts = data['workclass'].value_counts().reset_index()
    workclass_counts.columns = ['workclass', 'count']
    fig_workclass_dist = px.bar(
        workclass_counts, y='workclass', x='count',
        orientation='h',
        color='workclass',
        title='Workclass Distribution'
    )
    fig_workclass_dist.update_layout(template="plotly_white", showlegend=False)

    # 14. Gender & Occupation High Earners
    prop_df = (
        data.groupby(['occupation_grouped', 'sex'])['income']
        .apply(lambda x: (x == '>50K').mean())
        .reset_index(name='prob_>50K')
    )
    fig_gender_occ = px.bar(
        prop_df, x='occupation_grouped', y='prob_>50K',
        color='sex',
        barmode='group',
        color_discrete_map={'Male':'#8b5cf6', 'Female':'#ec4899'},
        title='Percentage of High Earners by Occupation and Sex'
    )
    fig_gender_occ.update_layout(template="plotly_white")

    # 15. Heatmap - Occupation vs Education
    pivot_table = data.pivot_table(
        index='occupation_grouped',
        columns='education_level',
        values='income_numeric',
        aggfunc='mean'
    )
    fig_heatmap = px.imshow(
        pivot_table,
        text_auto=".2f",
        color_continuous_scale="YlGnBu",
        title="Probability of Income >50K (Occupation vs Education)"
    )
    fig_heatmap.update_layout(template="plotly_white")

    # 16. Income by Education & Occupation
    edu_occ_income = data.groupby(['education_level', 'occupation_grouped'])['income_numeric'].mean().reset_index()
    fig_edu_occ = px.bar(
        edu_occ_income, x='education_level', y='income_numeric',
        color='occupation_grouped',
        barmode='group',
        title='Income Probability by Education and Occupation'
    )
    fig_edu_occ.update_xaxes(tickangle=-45)
    fig_edu_occ.update_layout(template="plotly_white")

    # 17. Gender Gap by Education
    gender_edu = data.groupby(['education_level', 'sex'])['income_numeric'].mean().reset_index()
    fig_gender_gap = px.line(
        gender_edu, x='education_level', y='income_numeric',
        color='sex',
        markers=True,
        color_discrete_map={'Male':'#3b82f6', 'Female':'#ec4899'},
        title='Income Gap: Education Growth by Gender'
    )
    fig_gender_gap.update_xaxes(tickangle=-45)
    fig_gender_gap.update_layout(template="plotly_white")

    # ==============================
    # NEW VISUALIZATIONS
    # ==============================

    # 18. Work Intensity Pie Chart by Income
    work_income_counts = (
        data.groupby(["income", "work_intensity"])
        .size()
        .reset_index(name="count")
    )
    fig_work_pie = px.pie(
        work_income_counts,
        names="work_intensity",
        values="count",
        color="work_intensity",
        facet_col="income",
        title="Work Intensity Distribution by Income",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_work_pie.update_layout(template="plotly_white")

    # 19. Work Intensity + Sex Impact on Income
    work_sex_income = (
        data.groupby(["income", "work_intensity", "sex"])
        .size()
        .reset_index(name="count")
    )
    fig_work_sex = px.bar(
        work_sex_income,
        x="work_intensity",
        y="count",
        color="income",
        facet_col="sex",
        barmode="group",
        title="Impact of Work Intensity and Sex on Income Level",
        text_auto=True,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_work_sex.update_layout(template="plotly_white")

    # 20. Average Hours by Work Intensity
    avg_hours = data.groupby("work_intensity")["hours.per.week"].mean().reset_index()
    avg_hours.columns = ['work_intensity', 'avg_hours']
    fig_avg_hours = px.bar(
        avg_hours, x='work_intensity', y='avg_hours',
        title="Average Weekly Hours by Work Intensity",
        color_discrete_sequence=['#f59e0b'],
        text_auto='.1f'
    )
    fig_avg_hours.update_layout(template="plotly_white")

    # 21. Income by Marital Status
    marital_income = (
        data.groupby(["marital_status", "income"])
        .size()
        .reset_index(name="count")
    )
    fig_marital = px.bar(
        marital_income, x='marital_status', y='count',
        color='income',
        barmode='stack',
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#10b981'},
        title="Income Distribution by Marital Status"
    )
    fig_marital.update_xaxes(tickangle=-30)
    fig_marital.update_layout(template="plotly_white")

    # 22. Income Percentage by Relationship Group
    relationship_income = (
        data.groupby(["relationship_group", "income"])
        .size()
        .unstack(fill_value=0)
    )
    relationship_pct = relationship_income.div(
        relationship_income.sum(axis=1), axis=0
    ) * 100
    relationship_pct_reset = relationship_pct.reset_index().melt(
        id_vars='relationship_group',
        var_name='income',
        value_name='percentage'
    )
    fig_relationship = px.bar(
        relationship_pct_reset, x='relationship_group', y='percentage',
        color='income',
        barmode='stack',
        color_discrete_map={'<=50K':'#3b82f6', '>50K':'#10b981'},
        title="Income Percentage by Relationship Group",
        text_auto='.1f'
    )
    fig_relationship.update_layout(template="plotly_white", yaxis_title="Percentage (%)")
    all_figs = {
            'fig_age': fig_age,
            'fig_hours_income': fig_hours_income,
            'fig_gender': fig_gender,
            'fig_income_dist': fig_income_dist,
            'fig_race': fig_race,
            'fig_native': fig_native,
            'fig_edu_box': fig_edu_box,
            'fig_edu_bar': fig_edu_bar,
            'fig_cond_prob': fig_cond_prob,
            'fig_occupation': fig_occupation,
            'fig_occupation_hours': fig_occupation_hours,
            'fig_workclass': fig_workclass,
            'fig_workclass_dist': fig_workclass_dist,
            'fig_gender_occ': fig_gender_occ,
            'fig_heatmap': fig_heatmap,
            'fig_edu_occ': fig_edu_occ,
            'fig_gender_gap': fig_gender_gap,
            'fig_work_pie': fig_work_pie,
            'fig_work_sex': fig_work_sex,
            'fig_avg_hours': fig_avg_hours,
            'fig_marital': fig_marital,
            'fig_relationship': fig_relationship
        }
    return all_figs