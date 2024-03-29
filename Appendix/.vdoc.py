# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
phases = "Understand Plan Collect Store Clean Explore Prepare Model Interpret Communicate Deploy Reflect".split()
sources = "Tukey KDD SEMMA Hayashi CRISPDM OSEMI Ojeda+ Caffo+ Donoho Géron Das Dataman Porter".split()
pipes = {source:'' for source in sources}
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Tukey'] = """
Understand | 
Plan | planning
Collect | gathering
Store | 
Clean | 
Explore | analyzing
Prepare | gathering
Model | analyzing
Interpret | interpret
Communicate | 
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['KDD'] = """
Understand | 
Plan | 
Collect | selection 
Store | 
Clean | pre-processing
Explore | 
Prepare | transformation
Model | data mining
Interpret | interpretation and evaluation
Communicate | 
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['SEMMA'] = """
Understand | 
Plan | 
Collect | sample 
Store | 
Clean | 
Explore | explore
Prepare | modify
Model | model
Interpret | assess
Communicate | 
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

pipes['Hayashi'] = """
Understand | design
Plan | design
Collect | collection
Store | collection
Clean | 
Explore | collection
Prepare | collection
Model | analysis
Interpret | analysis 
Communicate | 
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['CRISPDM'] = """
Understand | Business understanding
Plan | Business Understanding
Collect | Data Understanding
Store | Data Preparation
Clean | Data Preparation
Explore | Data Understanding*
Prepare | Data Preparation
Model | Modeling
Interpret | Evaluation
Communicate | Deployment
Deploy | Deployment
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['OSEMI'] = """
Understand | 
Plan | 
Collect | Obtain
Store | 
Clean | Scrub
Explore | Explore
Prepare | Scrub
Model | Model
Interpret | Interpret
Communicate | 
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Ojeda+'] = """
Understand | Exploration and understanding*
Plan | 
Collect | Acquisition
Store | Acquisition
Clean | Munging, wrangling, and manipulation
Explore | 
Prepare | Munging, wrangling, and manipulatiom
Model | Analysis and modeling
Interpret | 
Communicate | Communicating
Deploy | Operationalizing
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Caffo+'] = """
Understand | Question
Plan | Question
Collect | Question
Store | 
Clean | 
Explore | Exploratory data analysis
Prepare | 
Model | Formal modeling
Interpret | Interpretation
Communicate | Communication
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Donoho'] = """
Understand | 
Plan | Gathering
Collect | Gathering
Store | 
Clean | Preparation
Explore | Exploration
Prepare | Modern Databases, Mathematical Representation
Model | Data Modeling
Interpret | 
Communicate | Presentation
Deploy | 
Reflect | Science about Data Science
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Géron'] = """
Understand | Big Picture
Plan | 
Collect | Get
Store | 
Clean | Prepare
Explore | Discover
Prepare | Get, Prepare
Model | Select and train model, fine tune
Interpret | 
Communicate | Present
Deploy | Launch, monitor, maintain
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Das'] = """
Understand | Business Understanding
Plan | 
Collect | Data Mining
Store | 
Clean | Data Cleaning
Explore | Data Exploration
Prepare | Feature Engineering
Model | Predictive Modeling
Interpret | 
Communicate | Data Visualization
Deploy | 
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Dataman'] = """
Understand | Set objectives, Communicate with stakeholders
Plan | 
Collect | Collect for EDA
Store | 
Clean | Collect for EDA
Explore | Collect for EDA
Prepare | Determine functional form, split data
Model | Determine functional form, split data, Assess performance
Interpret | 
Communicate | 
Deploy | Deploy
Reflect | 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pipes['Porter'] = """
Understand | Disciplinary
Plan | 
Collect | Collection and Acquisition
Store | Storage and Representation
Clean | Manipulation and Transformation
Explore | 
Prepare | Manipulation and Transformation
Model | Computing, Analytics
Interpret | Summarizing
Communicate | Communicating
Deploy | 
Reflect | Practicing 
"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
import re
#
#
#
data = []
cols = ['Source', 'Std Phase', 'Src Phase']
for source in pipes:
    for row in pipes[source].lower().split("\n")[1:-1]:
        data.append([source] + re.split('\s*\|\s*', row))

# Convert CSV to wide table (using Xes)
df = pd.DataFrame(data, columns=cols)\
  .reset_index(drop=True)\
  .set_index(cols[:2])
# df['Src Phase'] = df['Src Phase'].astype('bool').astype('int') 
df.loc[df['Src Phase'] != '', 'Src Phase'] = '■' # '▪︎' '●' 
df = df.unstack()
df.columns = df.columns.droplevel(0)

# Convert CSV to wide table using names as values
# df = pd.DataFrame(data, columns=cols)\
#   .reset_index(drop=True)\
#   .set_index(cols[:2]).unstack() 
# df.columns = df.columns.droplevel(0)

# Preserve sorting
df = df[[phase.lower() for phase in phases]]
df = df.T[sources].T
# df.columns = [col[:3] for col in df.columns]
# df.columns = [str(i+1).zfill(2) for i in range(len(phases))]

df.columns.name = ''
df.index.name = ''
#
#
#
#| output: true

styles = [
  {
    'selector': 'th',
    'props': [
      ('font-weight', 'normal')
    ]
  },
  {
    'selector': "th.col_heading",
    'props': [
      ('width', '40px'),
      ('writing-mode', 'vertical-rl'),
      ('transform', 'rotateZ(210deg)'), 
      ('vertical-align', 'bottom')
    ]
  },
  {
    'selector': 'th.row_heading',
    'props': [
      ('width', '100px'),
      ('text-align', 'right'),
      ('padding-right', '1rem')
    ]
  },
  {
    'selector': 'td.data',
    'props': [
      ('color', 'darkgray')
    ]
  }
]

df.style.set_table_styles(styles)

#
#
#
#
#
#
#
#
#
