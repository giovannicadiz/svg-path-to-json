# -*- coding: utf-8 -*-

"""
script to extract and structure data obtained from an SVG file and transform it to JSON.
This version requires minidom lib
"""
__author__ = "@Gio_Cadiz"
__version__ = "2"
__date__ = "2017-13-12"


from xml.dom import minidom


def svJson():
    try:
        while True:
            handFile = input("[Enter the name file - ]\n \tor \n[Press Enter to exit - ] \n :")

            if len(handFile) < 1:
                print("Exit !!!!!!!!!")
                break
            else:

                ref = input("Enter the cod REF - ").lower()

                if len(ref) < 1:
                    ref = 'Null'
                else:
                    ref = ref

                style = input("Enter the code style - ").lower()

                if len(style) < 1 :
                    style = 'Null'
                else:
                    style = style

                config = {

                    'svg_file': handFile,

                }

                svg = minidom.parse(config['svg_file'])
                paths = svg.getElementsByTagName('path')

                c = 0
                array = []
                for node in paths:
                    if node.getAttributeNode('id'):
                        c += 1
                        refCode = ref + str(c)
                        path = str(node.getAttributeNode('d').nodeValue)
                        array.append(
                            {"data_id": refCode, "seat_path": path, "path_style": '$' + style}
                        )

                # print in screen
                for i in array:
                    i = str(i).replace("'", '''"''')
                    print(i)
                print("\n#############################################################")
                print("TOTAL COUNT      : " + str(c) + '                                      ' + "#")
                print("NAME FILE OUTPUT : saveFileOut.json                         #")
                print("#############################################################\n")

                # create file output
                jsonArr = []
                jsonArr.append(array)
                for x in jsonArr:
                    x = str(x).replace("'", '''"''')
                    saveFile = open("saveFileOut2.json", "a")
                    saveFile.write(x)
                    saveFile.close()

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    svJson()