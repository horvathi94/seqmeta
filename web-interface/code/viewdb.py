from flask import render_template
from src.cursor import Cursor

def database_view():

    cursor = Cursor();
    samples = cursor.select_all("sample_data");
    cursor.close();

    if len(samples) == 0:
        return render_template("database_empty.html");

    column_names = [col for col in samples[0]];

    html = "<table>";
#    html+= quick_html.table_header(column_names);

    for sample in samples:
        sample_data = [sample[col] for col in column_names];
#        html+= quick_html.table_row(sample_data);

    html+= "</table>";

    return html;
