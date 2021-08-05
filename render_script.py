# -*- coding: utf-8 -*-
import re, datetime, time, os
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

files = ['1-基隆端(0) - 基隆(1).txt','2-基隆(1) - 八堵(2).txt','3-八堵(2) - 大華系統(5).txt','4-大華系統(5) - 五堵(6).txt','5-五堵(6) - 汐止(10).txt','6-汐止(10) - 汐止系統(11).txt','7-汐止系統(11) - 高架汐止端(13).txt','8-高架汐止端(13) - 東湖(15).txt','9-東湖(15) - 內湖(17).txt','10-內湖(17) - 圓山(23).txt','11-圓山(23) - 台北(25).txt','12-台北(25) - 三重(27).txt','13-三重(27) - 五股轉接道(32).txt','14-五股轉接道(32) - 五股(33).txt','15-五股(33) - 高公局(35).txt','16-高公局(35) - 泰山轉接道(36).txt','17-泰山轉接道(36) - 林口(41).txt','18-林口(41) - 桃園(49).txt','19-桃園(49) - 機場系統(52).txt','20-機場系統(52) - 中壢服務區(55).txt','21-中壢服務區(55) - 內壢(57).txt','22-內壢(57) - 中壢轉接一(59).txt','23-中壢轉接一(59) - 中壢轉接二(60).txt','24-中壢轉接二(60) - 中壢(62).txt','25-中壢(62) - 平鎮系統(65).txt','26-平鎮系統(65) - 幼獅(67).txt','27-幼獅(67) - 楊梅(69).txt','28-楊梅(69) - 高架楊梅端(71).txt','29-高架楊梅端(71) - 湖口(83).txt','30-湖口(83) - 湖口服務區(86).txt','31-湖口服務區(86) - 竹北(91).txt','32-竹北(91) - 新竹(95).txt','33-新竹(95) - 新竹系統(99).txt','34-新竹系統(99) - 頭份(110).txt','35-頭份(110) - 頭屋(125).txt','36-頭屋(125) - 苗栗(132).txt','37-苗栗(132) - 銅鑼(140).txt','38-銅鑼(140) - 三義(150).txt','39-三義(150) - 泰安服務區(159).txt','40-泰安服務區(159) - 后里(160).txt','41-后里(160) - 台中系統(165).txt','42-台中系統(165) - 豐原(168).txt','43-豐原(168) - 大雅(174).txt','44-大雅(174) - 台中(178).txt','45-台中(178) - 南屯(181).txt','46-南屯(181) - 王田(189).txt','47-王田(189) - 彰化系統(192).txt','48-彰化系統(192) - 彰化(198).txt','49-彰化(198) - 埔鹽系統(207).txt','50-埔鹽系統(207) - 員林(211).txt','51-員林(211) - 北斗(220).txt','52-北斗(220) - 西螺服務區(229).txt','53-西螺服務區(229) - 西螺(230).txt','54-西螺(230) - 虎尾(235).txt','55-虎尾(235) - 斗南(240).txt','56-斗南(240) - 雲林系統(243).txt','57-雲林系統(243) - 大林(250).txt','58-大林(250) - 民雄(257).txt','59-民雄(257) - 嘉義(264).txt','60-嘉義(264) - 水上(270).txt','61-水上(270) - 嘉義系統(272).txt','62-嘉義系統(272) - 新營服務區(284).txt','63-新營服務區(284) - 新營(288).txt','64-新營(288) - 下營系統(299).txt','65-下營系統(299) - 麻豆(303).txt','66-麻豆(303) - 安定(311).txt','67-安定(311) - 台南系統(315).txt','68-台南系統(315) - 永康(319).txt','69-永康(319) - 大灣(324).txt','70-大灣(324) - 仁德(327).txt','71-仁德(327) - 仁德系統(330).txt','72-仁德系統(330) - 仁德服務區(335).txt','73-仁德服務區(335) - 路竹(338).txt','74-路竹(338) - 高科(342).txt','75-高科(342) - 岡山(349).txt','76-岡山(349) - 楠梓(356).txt','77-楠梓(356) - 鼎金系統(362).txt','78-鼎金系統(362) - 高雄(367).txt','79-高雄(367) - 瑞隆路(369).txt','80-瑞隆路(369) - 五甲系統(370).txt','81-五甲系統(370) - 五甲(371).txt','82-五甲(371) - 中山四路(372).txt','83-中山四路(372) - 漁港路(373).txt','84-漁港路(373) - 高雄端(374).txt']
dir = './'

def main():
    titles = []
    data = []
    times = []
    month = 'Aug'
    day = '4'
    direction = 'SOUTH'
    output_filename = f'2021-{month}-{day}-{direction}.png'
    for filename in files[::-1] :
        title = filename.split('(')[1].split(')')[0]
        print(filename.replace('.txt', ''))
        titles.append(title)
        res = readFile(filename, month, day)
        # 0 : south, 1 : north
        speeds = res[ 0 if direction == 'SOUTH' else 1]
        # print(res)
        times = res[2]
        data.append(speeds)
    
    fig, ax = plt.subplots(1, figsize=(16, 16), dpi=120)
    ax.set_xticks(range(0, len(speeds), 6))
    ax.set_xticklabels(range(0, 24))
    ax.set_yticks(range(0, len(titles)))
    ax.set_yticklabels(titles)

    top = cm.get_cmap('Oranges_r', 160)
    bottom = cm.get_cmap('Blues', 96)
    newcolors = np.vstack((top(np.linspace(0, 1, 160)),
                        bottom(np.linspace(0, 1, 96))))
    newcmp = ListedColormap(newcolors, name='OrangeBlue')

    cmap2 = LinearSegmentedColormap.from_list("", ["red","yellow","green"])
    p = ax.pcolormesh(data, cmap=cmap2, vmin=10, vmax=140)

    fig.autofmt_xdate(rotation=45)
    fig.colorbar(p)
    
    fig.savefig(f'{dir}{output_filename}')

    

def readFile(filename, month, day):
    south = []
    north = []
    time = []
    fo = open(f'{dir}{filename}', 'r+')
    line = fo.readline()
    print(filename)
    while(line):
        data = line.replace('  ', ' ').split(' ')
        if ' ' in data: data.remove(' ')
        line = fo.readline()
        dd = data[0]
        MM = data[1]
        DD = data[2]
        T = data[3]
        others = data[4].replace('\n','').split(';')
        YY = others[0]
        # print(data)
        _south = others[1].replace('資料不足', '-1').replace('道路封閉', '-1')
        _north = others[2].replace('資料不足', '-1').replace('道路封閉', '-1')
        if MM == month and DD == day :
            south.append(int(_south))
            north.append(int(_north))
            time.append(T)
    fo.close()
    return [south, north, time]

if __name__ == '__main__':
    main()
    
