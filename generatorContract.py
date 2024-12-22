from datetime import datetime

#funcion para remplazar texto mediante respuestas a preguntas al usuario
def replaceText(text):

    # campos a reemplazar
    fields = [["[COMPANY_NAME]", "Company Name"],
                   ["[EMPLOYEE_NAME]", "Employee Name"],
                   ["[PRICE]", "Price"],
                   ["[CITY]", "City"],
                   ["[COUNTRY]", "Country"]
               ]
    
    # recorre cada campo y lo remplaza con la respuesta del usuario al input
    for i in fields:
        txtInput = input(f"What is the {i[1]}?: ")
        text = text.replace(i[0], txtInput)

    # remplaza el campo cuurent_dat con la fecha que tiene el ordenador utilizando la biblioteca datetime
    return text.replace("[CURRENT_DATE]", datetime.today().strftime('%Y-%m-%d'))

 
# abre el arhivo contract.txt y lo guarda en una variable
contractFile = open("contract.txt", "r")

# inicializa la variable result
result = ""

# recorre linea por linea a la variable contractFile y utiliza la funcion replaceText para hacer los cambios guardando en result
for i in contractFile:
    result += i
result = replaceText(result)

# genera un nuevo archivo
with open("contract_processed.txt", "w") as textFile:
    textFile.write(result)