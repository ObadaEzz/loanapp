import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def create_plot(func, *args, **kwargs):
    """Helper function to create plots in parallel"""
    try:
        fig = func(*args, **kwargs)
        return json.loads(fig.to_json())
    except Exception as e:
        print(f"Error creating plot: {str(e)}")
        return None

def perform_eda(df):
    if len(df) == 0:
        return {}
        
    plots = {}
    
    try:
        # Pre-calculate common aggregations
        df['total_income'] = df['applicant_income'] + df['coapplicant_income']
        
        # Define plot configurations
        plot_configs = {
            'approval_distribution': {
                'func': px.pie,
                'args': [df],
                'kwargs': {
                    'names': 'prediction',
                    'title': 'Loan Application Results Distribution',
                    'color_discrete_sequence': px.colors.qualitative.Set3
                }
            },
            'income_distribution': {
                'func': px.box,
                'args': [df],
                'kwargs': {
                    'x': 'prediction',
                    'y': 'applicant_income',
                    'title': 'Monthly Income Distribution by Loan Status',
                    'color': 'prediction',
                    'color_discrete_sequence': px.colors.qualitative.Set3
                }
            },
            'education_approval': {
                'func': lambda: create_education_plot(df),
                'args': [],
                'kwargs': {}
            },
            'property_area_analysis': {
                'func': lambda: create_property_area_plot(df),
                'args': [],
                'kwargs': {}
            },
            'marriage_analysis': {
                'func': lambda: create_marriage_plot(df),
                'args': [],
                'kwargs': {}
            }
        }
        
        # Create plots in parallel
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {}
            for plot_id, config in plot_configs.items():
                futures[plot_id] = executor.submit(
                    create_plot,
                    config['func'],
                    *config['args'],
                    **config['kwargs']
                )
            
            # Collect results
            for plot_id, future in futures.items():
                result = future.result()
                if result:
                    plots[plot_id] = result
        
    except Exception as e:
        print(f"Error in EDA: {str(e)}")
        return {}
    
    return plots

def create_education_plot(df):
    education_counts = df.groupby(['education', 'prediction']).size().unstack(fill_value=0)
    education_pct = education_counts.div(education_counts.sum(axis=1), axis=0) * 100
    education_pct = education_pct.reset_index()
    
    fig = px.bar(education_pct, 
                 x='education',
                 y=education_pct.columns[1:],
                 title='Approval Rate by Education Level (%)',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(barmode='stack')
    return fig

def create_property_area_plot(df):
    property_counts = df.groupby(['property_area', 'prediction']).size().unstack(fill_value=0)
    property_pct = property_counts.div(property_counts.sum(axis=1), axis=0) * 100
    property_pct = property_pct.reset_index()
    
    fig = px.bar(property_pct,
                 x='property_area',
                 y=property_pct.columns[1:],
                 title='Loan Approval Rate by Property Area (%)',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(barmode='stack')
    return fig

def create_marriage_plot(df):
    marriage_counts = df.groupby(['married', 'prediction']).size().unstack(fill_value=0)
    marriage_pct = marriage_counts.div(marriage_counts.sum(axis=1), axis=0) * 100
    marriage_pct = marriage_pct.reset_index()
    
    fig = px.bar(marriage_pct,
                 x='married',
                 y=marriage_pct.columns[1:],
                 title='Loan Approval Rate by Marriage Status (%)',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(barmode='stack')
    return fig
