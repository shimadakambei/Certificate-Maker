from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
from pandas import DataFrame

font = ImageFont.truetype('AlexBrush-Regular.ttf', size=78)
(x, y) = (800, 680)
color = 'rgb(0, 0, 0)'

# File Paths
sixth_grade_honors_file_path = '/Users/romanleal/Desktop/Certificates/6th Grade Honors'
sixth_grade_high_honors_file_path = '/Users/romanleal/Desktop/Certificates/6th Grade High Honors'

# Certificate Templates
honors_template = '/Users/romanleal/Desktop/Certificates/Honors.png'

# Data
spreadsheet = pd.read_csv('/Users/romanleal/Desktop/Certificates/Sorted T2 Honor Roll.csv')
student_characteristics = ['First Name', 'Last Name', 'Grade', 'Honors Status']
df = DataFrame(spreadsheet, columns=student_characteristics)
df = df.dropna()


# Data subsets
sixth_grade_honors_students = df.loc[(df['Honors Status'] == 'Honors') & (df['Grade'] == 6)]



def make_certificate(dataset,template,file_path):
    first_names = list(dataset['First Name'])
    last_names = list(dataset['Last Name'])
    for z in range(len(first_names)):
        image = Image.open(template)
        draw = ImageDraw.Draw(image)
        draw.text((x, y), first_names[z] + " " + last_names[z], fill=color, font=font)
        image.save(file_path + '/' + f'{last_names[z]}, {first_names[z]} Certificate.png', optimize=True, quality=20)

make_certificate(sixth_grade_honors_students, honors_template, sixth_grade_honors_file_path)