import csv

def csv_to_md(csv_file_path,type_del):
    # creating a file with .md extension for the output file
    output_file = csv_file_path.replace(".csv", ".md")

    # I used encoding UTF-8 as we won't have to worry about errors while decoding contents of a csv file
    csv_dict = csv.DictReader(open(csv_file_path, encoding="UTF-8"),delimiter=type_del)

    # storing the content of csv file in a list_of_rows. Each row is a dict.
    list_of_rows = [dict_row for dict_row in csv_dict]

    # For Headers of the csv file.
    headers = list(list_of_rows[0].keys())

    # The below code block makes md_string as per the required format of a markdown file.
    md_string = " | "
    for header in headers:
        md_string += header+" |"

    md_string += "\n |"
    for i in range(len(headers)):
        md_string += "--- | "

    md_string += "\n"
    for row in list_of_rows:
        md_string += " | "
        for header in headers:
            md_string += row[header]+" | "
        md_string += "\n"

    # writing md_string to the output_file
    file = open(output_file, "w", encoding="UTF-8")
    file.write(md_string)
    file.close()

    print("The markdown file has been created!!!")

if __name__=="__main__":
    csv_file_path = input("Input path of the csv file:")
    #takes input of the type of delimiter in CSV file
    type_del=input("Enter the type of delemiter example ',' '|' ';' for space enter 'space' for tab enter 'tab' or any other : ")

    if type_del=="space":
        type_del=" "

    if type_del=="tab":
        type_del="	"

    csv_to_md(csv_file_path,type_del)
