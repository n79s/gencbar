import re
import io
from PIL import Image

class GenCBar:
    imgs = {}
    bardeg = {}
    aldeg = {}

    def __init__(self):
        self.width = 12
        self.height = 12

        self.regc = re.compile("[A-Z]")
        self.regc1 = re.compile("[A-J]")
        self.regc2 = re.compile("[K-T]")
        self.regc3 = re.compile("[U-Z]")
        self.regd = re.compile("[0-9]")

        #カスバー1文字分の画像
        self.imgs["-"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x13IDATx\x9cc\xf8\xfc\x81\x01\x8e\x8c\r\x10\x08I\x1c\x00+\xcd\x10\xa5\xa0\xa1\xbf,\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["0"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x13IDATx\x9cc\xb0\xff\xc0\x00G\xc6\x06\x08\x84$\x0e\x00\xc3\xae\x0b\x05}\xd2\xa1j\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["1"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc0\xfe\xc0\x80@\x06H\x08!\x0e\x00\xbc\xbe\n\xa5\xd2\xd2\x8f\xed\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["2"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc\xb07`\x80#cd\xf4\x01\x8e\x00i\xf6\x07\xd5\x8a\x81\x0e\xbe\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["3"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x13IDATx\x9cc\xf8l\xc0\x00G\xc6\xc8\xe8\x03\x1c\x01\x00\xbf\xbe\n\xa5\xa6A\x89u\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["4"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc0\xfe\xc0\x80@\x06\x08d\x8f@\x00\xadv\x07\xd5;p\x02B\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["5"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc\xb07`\x80#c$\x84$\x0e\x00Z\xae\x05\x05O\xa2\x06\xdb\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["6"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc\xf8l\xc0\x00G\xc6H\xc8\x1e\x81\x00\xb0v\x07\xd5Wa\xe8\xfd\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["7"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc0\xfe\xc0\x80@\x06\x08\xf4\x19\x81\x00\xbf\xbe\n\xa5\xc2[o9\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["8"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc\xb07`\x80#c$\xf4\x19\x81\x00l\xf6\x07\xd5\xc6\xaa\x9d\xf7\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["9"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc\xf8l\xc0\x00G\xc6H\x08I\x1c\x00\xc2\xbe\n\xa5\xd1l\xdd\xf0\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c1"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x15IDATx\x9cc\xf8\xfc\x81\x01\x8e\x8c\r\x10\xc8\xfe\x03\x1c\x01\x00\x19\x85\r\xd5\xc3\x89Zc\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c2"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x14IDATx\x9cc\xf8o\xc0\x00G\xc6H\xc8\xfe\x03\x1c\x01\x00\xc6\xae\x0b\x05NK\x07\t\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c3"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x15IDATx\x9cc\xb0\xff\xc0\x00G\xc6\x06\x08\xf4\xf9\x03\x1c\x01\x00\xd5\xf6\r\xd5\xf6Iz\x9e\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c4"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x14IDATx\x9cc\xf8o\xc0\x00G\xc6H\xe8\xf3\x078\x02\x00\xd8\xf6\r\xd5\xcb\x95\xa8\xa3\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c5"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x13IDATx\x9cc\xb0\xff\xc0\x00G\xc6\x06\x08\xf4\x1f\x81\x00\xc6\xae\x0b\x05\xa3\xde\x97m\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c6"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x14IDATx\x9cc\xf8\xfc\x81\x01\x8e\x8c\r\x10\xe8?\x02\x01\x00\x1c\x85\r\xd5\x0f\x88\xa5S\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c7"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x12IDATx\x9cc\xf8o\xc0\x00G\xc6H\x08I\x1c\x00\xc9\xae\x0b\x05\xa9\xe7N\xf3\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["c8"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\rIDATx\x9cc06` \x84\x00S\xbe\x04\xa5y\xe4\xcb\x0b\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["start"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x10IDATx\x9cc\xf8\xfc\x81\x01\x81\x0c\xb0"\x00R\xcd\x10\xa5\x19\xc2\xaf\x0e\x00\x00\x00\x00IEND\xaeB`\x82'))
        self.imgs["end"] = Image.open(io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x01\x03\x00\x00\x00l\xbb\xce\xa4\x00\x00\x00\x06PLTE\x00\x00\x00\xff\xff\xff\xa5\xd9\x9f\xdd\x00\x00\x00\x10IDATx\x9cc\xf8\xfc\x81\x01\x8e\x8c\xb1#\x00L\xcd\x10\xa5H\xad\x1d\xb8\x00\x00\x00\x00IEND\xaeB`\x82'))

        self.bardeg["0"] = 0
        self.bardeg["1"] = 1
        self.bardeg["2"] = 2
        self.bardeg["3"] = 3
        self.bardeg["4"] = 4
        self.bardeg["5"] = 5
        self.bardeg["6"] = 6
        self.bardeg["7"] = 7
        self.bardeg["8"] = 8
        self.bardeg["9"] = 9
        self.bardeg["-"] = 10
        self.bardeg["c1"] = 11
        self.bardeg["c2"] = 12
        self.bardeg["c3"] = 13
        self.bardeg["c4"] = 14
        self.bardeg["c5"] = 15
        self.bardeg["c6"] = 16
        self.bardeg["c7"] = 17
        self.bardeg["c8"] = 18

        self.aldeg["A"] = "0"
        self.aldeg["B"] = "1"
        self.aldeg["C"] = "2"
        self.aldeg["D"] = "3"
        self.aldeg["E"] = "4"
        self.aldeg["F"] = "5"
        self.aldeg["G"] = "6"
        self.aldeg["H"] = "7"
        self.aldeg["I"] = "8"
        self.aldeg["J"] = "9"
        self.aldeg["K"] = "0"
        self.aldeg["L"] = "1"
        self.aldeg["M"] = "2"
        self.aldeg["N"] = "3"
        self.aldeg["O"] = "4"
        self.aldeg["P"] = "5"
        self.aldeg["Q"] = "6"
        self.aldeg["R"] = "7"
        self.aldeg["S"] = "8"
        self.aldeg["T"] = "9"
        self.aldeg["U"] = "0"
        self.aldeg["V"] = "1"
        self.aldeg["W"] = "2"
        self.aldeg["X"] = "3"
        self.aldeg["Y"] = "4"
        self.aldeg["Z"] = "5"

    def get_checkdig(self, p_sum):
        val = p_sum % 19
        if(val != 0):
            val = 19 - val
        return val

    def get_key_from_value(self, d, val):
        keys = [k for k, v in d.items() if v == val]
        if keys:
            return keys[0]
        return None

    def write_one_bar(self,p_img,p_barlist,p_char,p_idx,p_sum,p_x):
        p_barlist[p_idx] = p_char
        p_idx += 1
        p_sum += self.bardeg[p_char]
        p_img.paste(self.imgs[p_char],
                            (p_x, 0, p_x+self.width, self.height))
        p_x += self.width
        return p_img,p_barlist,p_idx,p_sum,p_x

    def create_bar(self, bardata:str):
        try:
            return self.create_bar_inner(bardata)
        except TypeError as te:
            print(te)
            return None,[]

    # bardataのアルファベットは大文字の前提
    def create_bar_inner(self, bardata:str):
        if(bardata=='' or not bardata):
            return None,[]

        result_img = Image.new('RGB', (276, 12))
        cbar_sum = 0
        current_x = 0
        current_idx = 0

        cbar_list = [""] * 21
        barc_list = list(bardata)
        

        # スタートコード
        result_img.paste(self.imgs["start"], (current_x, 0, current_x+self.width, self.height))
        current_x += self.width

        for cc in barc_list:
            # 数字でもアルファベットでも-でも無い場合は無視

            # 数字かｰの場合
            if self.regd.match(cc) or cc == "-":
                result_img,cbar_list,current_idx,cbar_sum,current_x = self.write_one_bar(result_img,cbar_list,cc,current_idx,cbar_sum,current_x)
                if current_idx >= 20:
                    break

            # アルファベットの場合
            elif self.regc.match(cc):
                #アルファベットに対応する制御コード
                ctrl_code = "c1"
                if self.regc2.match(cc):
                    ctrl_code = "c2"
                elif self.regc3.match(cc):
                    ctrl_code = "c3"
                result_img,cbar_list,current_idx,cbar_sum,current_x = self.write_one_bar(result_img,cbar_list,ctrl_code,current_idx,cbar_sum,current_x)
                if current_idx >= 20:
                    break
                #アルファベットに対応する数字
                result_img,cbar_list,current_idx,cbar_sum,current_x = self.write_one_bar(result_img,cbar_list,self.aldeg[cc],current_idx,cbar_sum,current_x)
                if current_idx >= 20:
                    break

        # 20まで行ってなかったらc4で埋める
        if current_idx < 20:
            for i in range(20 - current_idx):
                blank = "c4"
                result_img,cbar_list,current_idx,cbar_sum,current_x = self.write_one_bar(result_img,cbar_list,blank,current_idx,cbar_sum,current_x)

        # チェックディジットの計算とバーコードに反映
        cddeg = self.get_checkdig(cbar_sum)
        cddegstr = self.get_key_from_value(self.bardeg, cddeg)
        result_img,cbar_list,current_idx,cbar_sum,current_x = self.write_one_bar(result_img,cbar_list,cddegstr,current_idx,cbar_sum,current_x)

        # ストップコード
        result_img.paste(self.imgs["end"], (current_x, 0, current_x+self.width, self.height))
        current_x += self.width

        return result_img, cbar_list
