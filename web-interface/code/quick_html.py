def table_header(cols):

    html = "<tr>";
    for col in cols:
        html+= "<th>";
        html+= str(col);
        html+= "</th>";
    html+= "</tr>";
    return html;


def table_row(data):

    html = "<tr>";
    for col in data:
        html+= "<td>";
        html+= str(col);
        html+= "</td>";
    html+= "</tr>";
    return html;
