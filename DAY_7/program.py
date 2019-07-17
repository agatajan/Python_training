# #wywolanie modulu
# #zeby uruchomic funcke nalezy podac nazwe funcji, dopoki funcja nie zostanie wywolana - nie zadziala
#
import moj_modul

# #from moj_modul import show_dir
# #from moj_modul import show_dir as new_function
#
print('Program wywolujacy modul')
print(30 * '=')
# jesli mamy print w module mozemy wywolac funcje poleceniem:
#moj_modul.show_dir()
print(moj_modul.show_dir())

#printowanie kiedy zmienna jest lista
result = moj_modul.show_dir()
for item in result:
    print(item)





