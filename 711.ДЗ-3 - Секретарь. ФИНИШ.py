# Условие задачи
# Я работаю секретарём, и мне постоянно приходят различные документы. Я должен быть очень внимателен,
# чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
# 	documents = [
# 		{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
# 		{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
# 		{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
# 		{"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
# 	]
# Перечень полок, на которых находятся документы, хранится в следующем виде:
# 	directories = {
# 		'1': ['2207 876234', '11-2', '5455 028765'],
# 		'2': ['10006'],
# 		'3': []
# 	}
# Необходимо реализовать следующие функции.
#
# get_name — функция. Принимает номер документа и выводит имя человека, которому он принадлежит.
# Если такого документа не существует вывести “Документ не найден”.
# get_directory — функция. Принимает номер документа и выводит номер полки, на которой он находится.
# Если такой документ не найден на полках вывести “Полки с таким документом не найдено”.
# add — функция, которая добавит новый документ в каталог и перечень полок.
# В результате корректного выполнения задания будет выведен следующий результат:

# Аристарх Павлов
# 1
# Документ не найден
# 3
# Александр Пушкин
# Полки с таким документом не найдено


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }
# get_name — функция. Принимает номер документа и выводит имя человека, которому он принадлежит.
# Если такого документа не существует вывести “Документ не найден”.
def get_name(doc_number):
    # Создадим список значений по ключу "number"
    value_number_list= []
    for document in documents:
        value_number_list.append(document["number"])
    # print (value_number_list) # ['2207 876234', '11-2', '10006', '5455 028765']
    if doc_number in value_number_list:
        for document in documents:
            if document["number"]== doc_number:
                name = document["name"]
    else:
        name= 'Документ не найден'
    return name

# get_directory — функция. Принимает номер документа и выводит номер полки, на которой он находится.
# Если такой документ не найден на полках вывести “Полки с таким документом не найдено”
def get_directory(doc_number):
    # Создадим список значений словаря directories
    values_list_directories = []
    for element in directories.values():
        values_list_directories .extend(element) #['2207 876234', '11-2', '5455 028765', '10006']
    # Проверим , присутстует ли doc_number в directories
    if doc_number in values_list_directories:
        for key , value in directories.items():
            if doc_number in value:
                number= key
    else:
        number= 'Полки с таким документом не найдено'
    return number
# add — функция, которая добавит новый документ в каталог и перечень полок.
def add(document_type, number, name,shelf_number):
    # Добавляем словарь в список documents
    new_dict={}
    new_dict["type"] = document_type
    new_dict["number"] = number
    new_dict["name"]=name
    documents.append(new_dict)
    #print(documents)
    # Добавляем значение для номера полки в словаре directories
    key=str(shelf_number)
    directories[key].append(number)
    #print(directories)



if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))












