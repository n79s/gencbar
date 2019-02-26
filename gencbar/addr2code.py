import re
import unicodedata
from .knum import kansuji2arabic

class Addr2CBarData:

    reg_al = re.compile(r'[A-Z]')
    reg_ksuji_nomi = re.compile(r'[一二三四五六七八九〇壱弐参十拾]+')
    reg_ksuji_fukumu = re.compile('.*[一二三四五六七八九〇壱弐参十拾].*')
    req_sp_chiwari = re.compile(r'^地割')
    #reg_num = re.compile(r'[0-9]') # 正規表現よりisdecimal()の方が速い（全角入ってこない前提）
    space_haifun = [' ','-']
    sp_addr_strs = ['丁目','番地','地割','丁','番','号','線','の','ノ','-']

    #リスト内の要素を文字列として連結
    def get_list_joinstr(self,p_list:list):
        result = ''.join(p_list)
        return result

    #郵便番号と住所文字列をパラメータにカスバーコードを返す
    def get_ccode_all(self,p_yuubin:str, p_str:str):
        if(p_yuubin == None):
            return None
        wkstr = p_yuubin.replace('-','')
        if(len(wkstr) != 7 or p_str == None or len(p_str) <= 0):
            return None
        return ''.join([wkstr,self.get_ccode(p_str)])

    def get_char_type(self,p_str:str):
        if(p_str.isdecimal()):
            return 0
        elif(self.reg_al.match(p_str)):
            return 1
        elif(self.reg_ksuji_nomi.match(p_str)):
            return 2
        elif(p_str in self.space_haifun):
            return 3
        else:
            return 9

    def get_char_type2(self,p_str:str):
        if(p_str.isdecimal()):
            return 0
        elif(self.reg_al.fullmatch(p_str)):
            return 1
        else:
            return 9
    #住所文字列からコードを抽出
    def get_ccode(self,p_str:str):
        #正規化(全角→半角) と 小文字→大文字
        wkstr = unicodedata.normalize("NFKC", p_str).upper()

        #記号系を削除
        wkstr = wkstr.replace('&','').replace('/','').replace('.','').replace('．','').replace('・','')

        #一文字づつのListにする
        str_list = list(wkstr)

        #連続した数字、漢数字、スペース、ハイフン、その他漢字文字のリストにまとめる
        tmp_buff = []
        tmp_list01 = []
        tmp_cc_type = 0
        for cc in str_list:
            if(tmp_buff):
                if(tmp_cc_type == self.get_char_type(cc)):
                    tmp_buff.append(cc)
                else:
                    tmp_list01.append(self.get_list_joinstr(tmp_buff).replace(' ','-'))
                    tmp_buff.clear()
                    tmp_cc_type = self.get_char_type(cc)
                    tmp_buff.append(cc)
            else:
                tmp_cc_type = self.get_char_type(cc)
                tmp_buff.append(cc)
        
        if(tmp_buff):
            tmp_list01.append(self.get_list_joinstr(tmp_buff).replace(' ','-'))
        
        tmp_list02 = []
        tmp_buff=[]
        #ここは漢数字が入ってる場合のみやる（漢数字を数字に変換）
        if(self.reg_ksuji_fukumu.match(wkstr)):
            for cc in tmp_list01:
                if(self.reg_ksuji_nomi.match(cc)):
                    tmp_buff.append(cc)
                else:
                    if(tmp_buff):
                        if(cc in self.sp_addr_strs or self.req_sp_chiwari.match(cc)):
                            tmp_list02.append(kansuji2arabic(self.get_list_joinstr(tmp_buff)))
                        else:
                            tmp_list02.append(self.get_list_joinstr(tmp_buff))
                        tmp_buff.clear()
                    tmp_list02.append(cc)

            if(tmp_buff):
                tmp_list02.append(kansuji2arabic(self.get_list_joinstr(tmp_buff)))
                tmp_buff.clear()
        else:
            tmp_list02 = tmp_list01

        #"F"の場合だけ特殊な処理(文字列の最後にFがある場合はFは消す)
        current_idx = 0
        if 'F' in tmp_list02:
            for cc in tmp_list02:
                if(cc == 'F'):
                    if(current_idx == len(tmp_list02)-1):
                        tmp_list02.pop(current_idx)
                    else:
                        tmp_list02[current_idx] = '-'
                current_idx += 1

        # 数字とアルファベットを抜き出す（漢字等はハイフンにする）
        tmp_list03 = []
        tmp_cc_type = 0
        for cc in tmp_list02:
            tmp_cc_type = self.get_char_type2(cc)
            if(tmp_cc_type in [0,1]):
                tmp_list03.append(cc)
            else:
                tmp_list03.append('-')

        # 連続したハイフンを一つにする
        tmp_list04 = []
        for cc in tmp_list03:
            if(tmp_list04):
                if(not(cc == '-' and tmp_list04[-1]=='-')):
                    tmp_list04.append(cc)
            elif(not(cc=='-')):
                tmp_list04.append(cc)

        # 独立したアルファベットの前後にあるハイフンは削除
        current_idx = 0
        result_list = []
        for cc in tmp_list04:
            if(result_list):
                if(self.reg_al.fullmatch(cc)):
                    if(result_list[-1]=='-'):
                        result_list.pop()
                    result_list.append(cc)
                elif(not (self.reg_al.fullmatch(result_list[-1]) and cc == '-')):
                    result_list.append(cc)
            else:
                result_list.append(cc)

        #先頭と末尾のハイフンは削除する
        if(result_list):
            if(result_list[-1] == '-'):
                result_list.pop()
        if(result_list):
            if(result_list[0] == '-'):
                result_list.remove(0)

        #最後のListを連結して戻す
        return ''.join(result_list)

