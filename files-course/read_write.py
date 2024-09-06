import csv,json, pickle
import xml.etree.ElementTree as ET

# ====================== text ====================== #

def read_txt(fn):
    with open(fn) as file:
        print(file.read())

def read_txt_by_line(fn):
    with open(fn) as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')
            line = file.readline()

def write_new_txt(fn, txt):
    with open(fn,'w', encoding='utf-8') as file:
        file.write(txt)

def append_line_txt(fn, txt):
    with open(fn,'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(txt)

# read_txt('./files_to_read/backup.py')
# read_txt_by_line('./files_to_read/backup.py')
# write_new_txt('./files_to_read/example.txt', 'Yehia ..........')
# append_line_txt('./files_to_read/example.txt', 'Yehia 2 ..........')

# ===================== CSV ====================== #

def read_csv(fn, delimiter):
    with open(fn) as csvf:
        cnt = -1
        rows = csv.reader(csvf, delimiter=delimiter)
        for r in rows:
            if cnt == -1:
                print(f"{' | '.join(r)}")
            else:
                print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
            cnt += 1
        print(f"{cnt} lines")

def write_csv(fn, header, row):
    with open(fn, mode='w', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

# read_csv('./files_to_read/names.csv', ',')
# write_csv('./files_to_read/names2.csv',
#           ['name', 'lastname', 'age', 'sex'],
#           ['Foo', 'Fighter', '82', 'male'])

# ====================== xml ====================== #

def parse_xml_et(fn):
    tree = ET.parse(fn)
    root = tree.getroot()
    print('Domains for: ' + root.attrib['name'])
    for child in root:
        print('\t' + child.attrib['name'], child.tag)

def add_xml_element_et(fn, el, attr, val):
    tree = ET.parse(fn)
    root = tree.getroot()
    child = ET.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(fn)

def change_xml_element_et(fn, el, attr, oldval, newval):
    tree = ET.parse(fn)
    root = tree.getroot()
    child = root.find("./" + el + "[@" + attr + "='" + oldval + "']")
    child.attrib[attr] = newval
    tree.write(fn)

# parse_xml_et('./files_to_read/ef_author.xml')
# add_xml_element_et('./files_to_read/ef_author.xml', 'domain', 'name', 'Java')
# change_xml_element_et('./files_to_read/ef_author.xml', 'domain', 'name', 'Java', 'TypeScript')
# change_xml_element_et('./files_to_read/ef_author.xml', 'domain', 'name', 'TypeScript', 'Java')

# ====================== json ====================== #

def read_print_json(fn, pretty, sort):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=sort, indent=4)
        if pretty else data)

def update_author_json(fn, arr_name, pos, key, value):
    with open(fn, 'r') as read_file:
        data = json.load(read_file)
        data[arr_name][pos][key] = value
        with open(fn, 'w') as write_file:
            json.dump(data, write_file)

# read_print_json('./files_to_read/authors.json', True, True)
# update_author_json(
#     './files_to_read/authors.json',
#     'authors', 0, 'courses', 8)

# ====================== pickle ====================== #

class Person:
    age = 45
    name = 'John Smith'
    kids = ['Pete', 'Lilly', 'Kate']
    employers = {'AWS': 2022, 'Microsoft': 2018, 'Yahoo': 2005}
    shoe_sizes = (11, 12)

def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: \n{pickled}\n')
    return pickled

def deserialize(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized: \n{unpickled}\n')

def deserialize_employers(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized employers: \n{unpickled.employers}\n')

def obj_to_file(fn, obj):
    with open(fn, 'wb') as pf:
        pickle.dump(obj, pf, protocol=pickle.HIGHEST_PROTOCOL)

def file_to_obj(fn, obj):
    with open(fn, 'rb') as pf:
        obj = pickle.load(pf)
        print(obj)
        return obj

# pickled = serialize(Person())
# deserialize(pickled)
# deserialize_employers(pickled)

# obj = obj_to_file('./files_to_read/person.xyz', Person())
# person = file_to_obj('./files_to_read/person.xyz', obj)

