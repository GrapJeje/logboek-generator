def heading(info, borderChar= "-", width= 30):
    """
    Print a heading with customizable borders and width.

    Parameters:
        info (str): The heading text to display.
        border_char (str): The character used for the border (default: '-').
        width (int): The width of the border line (default: 30).
    """
    borderLine = borderChar * width
    
    print(f"\n{borderLine}")
    print(info.center(width))
    print(f"{borderLine}\n")

def addTableContent(table, startTime= "01:00", endTime= "01:01", description= None, details= None):
    """
    Add content to a table in the document with activity details.

    Parameters:
        table (Table): The table object to which the activity information will be added.
        startTime (str): The start time of the activity (default is "01:00").
        endTime (str): The end time of the activity (default is "01:01").
        description (str): A description of the activity being done (default is None).
        details (str): Any additional details regarding the activity (default is None). If no details are provided, it will be set to "Nvt.".
    """
    header_cells = table.rows[0].cells
    header_cells[0].text = "Begintijd - Eindtijd"
    header_cells[1].text = "Activiteit"
    header_cells[2].text = "Bijzonderheden"
    
    # If you don't answer the question (Empty) put 'Nvt.'
    if not details:
            details = "Nvt."

    row_cells = table.add_row().cells
    row_cells[0].text = f"{startTime} - {endTime}"
    row_cells[1].text = description
    row_cells[2].text = details
