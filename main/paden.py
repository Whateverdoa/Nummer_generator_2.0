""""this module generates the directories and paths . it will also contain a filenaam maker"""

from pathlib import Path


dir_names_lijst = ["summary", "tmp", "VDP_final", "VDP_map"]
pad_naam_lijst = ["pad_sum", "pad_tmp","pad_VDP_final", "pad_VDP_map"]

paden_dict = dict(zip(pad_naam_lijst, dir_names_lijst))

for naam in paden_dict.keys():
    print(naam)


wdir = Path.cwd()

# pad_summary = wdir / "summary/"
# file = "VDP_map"
# print(pad_summary.is_dir())
#
# path_vdp = wdir / file
# path_final =  wdir / "VDP_final"
# path = wdir / "tmp"

# print(path_vdp)
# print(path_final)

# def paden_maker(dirname):
#     """"maak dirs"""
#     path = Path(wdir / dirname)
#     print(path)
#     return path.mkdir(parents=True, exist_ok=True)


class DirMaker():
    """all path making and deleting features"""
    def __init__(self, padname, filename, dirname, amount_of_rolls):

        self.padname = padname
        self.filename = filename
        self.dirname = dirname
        self.amount_of_rolls = amount_of_rolls

    def paden_maker(self, dirname):
        """"maak dirs"""
        wdir = Path.cwd()
        path = Path(wdir / dirname)
        print(path)
        # return path.mkdir(parents=True, exist_ok=True)
        return path

    def file_name_maker(self, filename, exp=".csv", amount_of_rolls=1):
        """a list comprehension to supply names for csv files
        give a start naam and it will generate a list  of names for the amount of rolls """
        man_fac_name_lijst = []
        for naam in range(amount_of_rolls):
            manufactored_name = f'{filename}_{naam+1:>{0}{5}}{exp}'
            print(manufactored_name)
            man_fac_name_lijst.append(manufactored_name)

        return man_fac_name_lijst

    def directory_maker(paden_maker):
        pass


class FilenameMaker():
    pass


