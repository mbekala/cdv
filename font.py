import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

font_path = 'Inter_18pt-Regular.ttf'
fm.fontManager.addfont(font_path)
inter_font = fm.FontProperties(fname=font_path)

font_name = inter_font.get_name()
available_fonts = [f.name for f in fm.fontManager.ttflist]

def set_inter_font():
    plt.rcParams['font.family'] = inter_font.get_name()
    plt.rcParams['axes.unicode_minus'] = False
