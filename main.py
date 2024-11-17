from docx import Document
from functions import heading

# Load the sjabloon
template = "documents/template.docx"
document = Document(template)

# Ask for document name
docName = input("Geef een document naam op: ")

#######################
#        Footer       #
#######################
heading("Footer info")

footerSection = document.sections[0]

footer = footerSection.footer

# Ask for user's full name
footerParagraph0 = footer.paragraphs[0]
footerParagraph0.text = input("Vul hier jouw volledige naam in: ")
footerParagraph0.style = 'Footer'

# Ask for class name
footerParagraph1 = footer.add_paragraph()
footerParagraph1.text = input("Vul hier jouw klas in: ")
footerParagraph1.style = 'Footer'

#######################
#       Content       #
#######################

heading(info="Table content info", width=45)

while True:
    date = input("Vul hier een datum in (of type 'stop' om te stoppen): ")
    if date.lower() == "stop":
        break 

    # Add the date as a heading
    document.add_paragraph(date, style="Heading 2")

    # Mak the table for the day
    table = document.add_table(rows=1, cols=3)
    header_cells = table.rows[0].cells
    header_cells[0].text = "Begintijd - Eindtijd"
    header_cells[1].text = "Activiteit"
    header_cells[2].text = "Bijzonderheden"

    # Ask for what happend that day
    while True:
        start_time = input("Wanneer ben je begonnen?: ")
        end_time = input("Wanneer ben je gestopt?: ")
        description = input("Wat heb je precies gedaan?: ")
        details = input("Waren er bijzonderheden?: ")

        # If you don't answer the question (Empty) put 'Nvt.'
        if not details:
            details = "Nvt."

        row_cells = table.add_row().cells
        row_cells[0].text = f"{start_time} - {end_time}"
        row_cells[1].text = description
        row_cells[2].text = details

        # Ask if the user want to add more days
        more = input("Wil je nog een activiteit toevoegen voor deze dag? (ja/nee): ")
        if more.lower() != "ja":
            break

# save the document
document.save(f"documents/{docName}.docx")
print(f"Document '{docName}' is succesvol gemaakt.")
