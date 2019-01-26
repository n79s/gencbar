import re
import unicodedata
from .knum import kansuji2arabic

class Addr2CBarData:

    reg_al = re.compile(r'[A-Z]')
    reg_ksuji_nomi = re.compile(r'[一二三四五六七八九〇壱弐参十拾]+')
    reg_ksuji_fukumu = re.compile('.*[一二三四五六七八九〇壱弐参十拾].')
    req_sp_chiwari = re.compile(r'^地割')
    #reg_num = re.compile(r'[0-9]') # 正規表現よりisdecimal()の方が速い（全角入ってこない前提）
    space_haifun = [' ','-']
    sp_addr_strs = ['丁目','番地','地割','丁','番','号','線','の','ノ','-']

    def get_stack_str(self,stack:list):
        result = ''.join(stack)
        return result

    def get_ccode_all(self,p_yuubin,p_str:str):
        if(p_yuubin == None):
            return None
        wkstr = p_yuubin.replace('-','')
        if(len(wkstr) != 7 or p_str == None or len(p_str) <= 0):
            return None
        return ''.join([wkstr,self.get_ccode(p_str)])

    def get_ccode(self,p_str:str):
        #正規化(全角→半角) と 小文字→大文字
        wkstr = unicodedata.normalize("NFKC", p_str).upper()
        # print(wkstr)

        #記号系を削除
        wkstr = wkstr.replace('&','').replace('/','').replace('.','').replace('．','').replace('・','')

        str_list = list(wkstr)
        # print(str_list)


        # print('#1')
        stack_num = []
        stack_kanji = []
        stack_ksuuji = []
        stack_al = []
        wklist = []
        for cc in str_list:
            if(cc.isdecimal()):
                stack_num.append(cc)
                if(stack_kanji):
                    wklist.append(self.get_stack_str(stack_kanji))
                    stack_kanji.clear()
                if(stack_al):
                    wklist.append(self.get_stack_str(stack_al))
                    stack_al.clear()
                if(stack_ksuuji):
                    wklist.append(self.get_stack_str(stack_ksuuji))
                    stack_ksuuji.clear()
            elif(self.reg_al.match(cc)):
                stack_al.append(cc)
                if(stack_kanji):
                    wklist.append(self.get_stack_str(stack_kanji))
                    stack_kanji.clear()
                if(stack_num):
                    wklist.append(self.get_stack_str(stack_num))
                    stack_num.clear()
                if(stack_ksuuji):
                    wklist.append(self.get_stack_str(stack_ksuuji))
                    stack_ksuuji.clear()
            elif(self.reg_ksuji_nomi.match(cc)):
                stack_ksuuji.append(cc)
                if(stack_kanji):
                    wklist.append(self.get_stack_str(stack_kanji))
                    stack_kanji.clear()
                if(stack_num):
                    wklist.append(self.get_stack_str(stack_num))
                    stack_num.clear()
                if(stack_al):
                    wklist.append(self.get_stack_str(stack_al))
                    stack_al.clear()
            elif(cc in self.space_haifun):
                if(stack_kanji):
                    wklist.append(self.get_stack_str(stack_kanji))
                    stack_kanji.clear()
                if(stack_num):
                    wklist.append(self.get_stack_str(stack_num))
                    stack_num.clear()
                if(stack_al):
                    wklist.append(self.get_stack_str(stack_al))
                    stack_al.clear()
                if(stack_ksuuji):
                    wklist.append(self.get_stack_str(stack_ksuuji))
                    stack_ksuuji.clear()
                wklist.append('-')#スペースは-にする
            else:
                stack_kanji.append(cc)
                if(stack_num):
                    wklist.append(self.get_stack_str(stack_num))
                    stack_num.clear()
                if(stack_al):
                    wklist.append(self.get_stack_str(stack_al))
                    stack_al.clear()
                if(stack_ksuuji):
                    wklist.append(self.get_stack_str(stack_ksuuji))
                    stack_ksuuji.clear()
        if(stack_kanji):
            wklist.append(self.get_stack_str(stack_kanji))
            stack_kanji.clear()
        if(stack_num):
            wklist.append(self.get_stack_str(stack_num))
            stack_num.clear()
        if(stack_al):
            wklist.append(self.get_stack_str(stack_al))
            stack_al.clear()
        if(stack_ksuuji):
            wklist.append(self.get_stack_str(stack_ksuuji))
            stack_ksuuji.clear()

        # print(wklist)



        wklist2 = []
        tmp_stack=[]
        if(self.reg_ksuji_fukumu.match(wkstr)):
            # print('#1-2')#ここは漢数字が入ってる場合のみやる
            for cc in wklist:
                if(self.reg_ksuji_nomi.match(cc)):
                    tmp_stack.append(cc)
                else:
                    if(tmp_stack):
                        if(cc in self.sp_addr_strs or self.req_sp_chiwari.match(cc)):
                            wklist2.append(kansuji2arabic(self.get_stack_str(tmp_stack)))
                        else:
                            wklist2.append(self.get_stack_str(tmp_stack))
                        tmp_stack.clear()
                    wklist2.append(cc)

            if(tmp_stack):
                wklist2.append(kansuji2arabic(self.get_stack_str(tmp_stack)))
                tmp_stack.clear()
            # print(wklist2)
        else:
            wklist2 = wklist

        # print('#2')
        current_idx = 0
        if 'F' in wklist2:
            for cc in wklist2:
                if(cc == 'F'):
                    if(current_idx == len(wklist2)-1):
                        wklist2.pop(current_idx)
                    else:
                        wklist2[current_idx] = '-'
                current_idx += 1
        # print(wklist2)

        # print('#3')
        final_list = []
        tmp_stack_num = []
        tmp_stack_al = []
        for cc in wklist2:
            if(cc.isdecimal()):
                tmp_stack_num.append(cc)
                if(tmp_stack_al):
                    final_list.append(self.get_stack_str(tmp_stack_al))
                    final_list.append('-')
                    tmp_stack_al.clear()

            elif(self.reg_al.fullmatch(cc)):
                tmp_stack_al.append(cc)
                if(tmp_stack_num):
                    final_list.append(self.get_stack_str(tmp_stack_num))
                    final_list.append('-')
                    tmp_stack_num.clear()
            else:
                if(tmp_stack_al):
                    final_list.append(self.get_stack_str(tmp_stack_al))
                    final_list.append('-')
                    tmp_stack_al.clear()
                if(tmp_stack_num):
                    final_list.append(self.get_stack_str(tmp_stack_num))
                    final_list.append('-')
                    tmp_stack_num.clear()

        if(tmp_stack_al):
            tmpstr = self.get_stack_str(tmp_stack_al)
            if(tmpstr != '-'):
                final_list.append(self.get_stack_str(tmp_stack_al))
            tmp_stack_al.clear()
        if(tmp_stack_num):
            tmpstr = self.get_stack_str(tmp_stack_num)
            if(tmpstr != '-'):
                final_list.append(self.get_stack_str(tmp_stack_num))
            tmp_stack_num.clear()

        # print(final_list)

        # print('#4')
        final_tmp = []
        for cc in final_list:
            if(final_tmp):
                if(not(cc == '-' and final_tmp[-1]=='-')):
                    final_tmp.append(cc)
            elif(not(cc=='-')):
                final_tmp.append(cc)
        # print(final_tmp)

        # print('#5')
        current_idx = 0
        result_list = []
        for cc in final_tmp:
            if(result_list):
                if(self.reg_al.fullmatch(cc)):
                    if(result_list[-1]=='-'):
                        result_list.pop()
                    result_list.append(cc)
                elif(not (self.reg_al.fullmatch(result_list[-1]) and cc == '-')):
                    result_list.append(cc)
            else:
                result_list.append(cc)

        if(result_list):
            if(result_list[-1] == '-'):
                result_list.pop()

        if(result_list):
            if(result_list[0] == '-'):
                result_list.remove(0)

        # print(result_list)
        return ''.join(result_list)

