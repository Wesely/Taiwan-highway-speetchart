# Taiwan-highway-speetchart
紀錄國道一號車速，以十分鐘為單位，可以24小時為單位輸出流速圖。

需要 `numpy` 與 `matplotlib`

沒有用資料庫，直接爬文字檔。
要輸出某日期的資訊直接修改 main() 的變數即可

```py
    month = 'Aug'
    day = '4'
    direction = 'SOUTH'
```

由於我跑爬蟲的主機偶爾會斷線，因此數據有部份缺失。

程式碼部份版權沒有歡迎指教。
數據部份是耗電爬的QQ 引用請註來源：
- FB-林口求生記 https://www.facebook.com/linkou.life 

| 解封後北上 | 解封後南下 |
|---|---|
| ![2021-Aug-4-NORTH](https://user-images.githubusercontent.com/5109822/128348412-449b7815-42eb-42d0-b97c-a78e909e058b.png) | ![2021-Aug-4-SOUTH](https://user-images.githubusercontent.com/5109822/128350312-ed8e83c4-62b5-4bd5-92e1-71523b9912e3.png) |

| 三級警戒中 | 警戒前 |
|---|---|
| ![image](https://user-images.githubusercontent.com/5109822/128350694-a42271ee-1335-4732-9110-7a43ad833d7c.png) | ![image](https://user-images.githubusercontent.com/5109822/128350751-e6a22877-af7d-4bcb-8973-fa07de8e3b2b.png)



不定期更新資料，如有需要我盡快更新可使用上面的臉書網址/Github頁面的email聯絡我或是發 issue :)
