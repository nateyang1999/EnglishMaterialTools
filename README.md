# EnglishMaterialTools
## 說明
用於節省英文講義編輯時間的簡單python scripts。
translate.py 使用googletrans套件，輸出例句翻譯。
lookup.py 使用爬蟲批量查詢劍橋辭典、Yahoo辭典，輸出單詞中文解釋、詞性、kk音標。(僅抓取查詢結果第一項詞性/解釋/音標，使用後務必校對)
## 輸入格式(.txt)
### translate.py
* 請參考demo_translate.txt
    * 一句一列，勿在句子中間換列
### lookup.py
* 請參考demo_lookup.txt
    * 一字一列
## 輸出格式
* out_{輸入檔名}.txt
* out_demo_translate.txt
```
The doctor warned my father that he shouldn't ingest too much high-fat food.
(醫生警告我父親不要攝入過多的高脂肪食物。)
I knew he was only flattering me because he wanted to borrow some money.
(我知道他只是在奉承我，因為他想藉點錢。)
The engineer showed us a sketch of the design to give us a rough idea of the new device.
(工程師向我們展示了設計草圖，讓我們對新設備有一個大致的了解。)
Sticking to a healthy diet isn't easy. I often feel the urge to eat junk food whenever I feel stressed.
(堅持健康的飲食並不容易。每當我感到壓力時，我常常會有吃垃圾食品的衝動。)
```
* out_demo_lookup.txt
```
comment (n.) 評論；意見；評價；評語 [ˋkɑmɛnt] 
movement (n.) 動；移動；運動 [ˋmuvmənt] 
current (adj.) 現時的，當前的；現行的 [ˋkɝənt] 
scene (n.) 場景，場面；鏡頭 [sin] 
plot (n.) 情節 [plɑt] 
bumper (n.) 保險杆 [ˋbʌmpɚ] 
heaven (n.) 天堂，天國 [ˋhɛvən] 
vaccine (n.) 疫苗 [ˋvæksin] 
critics (n.) 批評者，反對者 [查無音標]
instinct (n.) 本能，直覺 [ɪnˋstɪŋkt] 
jdkfl (查無詞性) 查無中文解釋 [查無音標]
restore (v.) 修復；使重定；使復職 [rɪˋstor] 
```

## 使用方式
* 需先安裝python(3.8或以上) https://www.python.org/downloads/
* 從github下載zip (右上角Code->Download Zip)
    * 或者(需先安裝git http://git-scm.com/download/win)  
    ```
    git clone https://github.com/nateyang1999/EnglishMaterialTools.git
    ```
* 打開終端機(windows左下角搜尋cmd)，依序輸入
    * 安裝pip
    ```
    python -m ensurepip --upgrade
    ```
    * 移動至檔案資料夾下
    ```
    cd {你的檔案路徑(如:\github\EnglishMaterialTools)}
    ```
    * 安裝所需套件
    ```
    pip install --upgrade -r requirements.txt
    ```
    * 執行script (檔案需和 translate.py、lookup.py 放在同一個資料夾)
    ```
    python3 translate.py {檔名(如:test.txt)}
    ```
    ```
    python3 lookup.py {檔名(如:test.txt)}
    ```
## macOS
* 安裝pyhton(3.8以上)
在終端機輸入
```
python3 --version
```
若出現 Python 3.X.X 表示安裝成功
* 安裝pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python3 get-pip.py
```
```
pip3 list
```
出現Package和Version的列表代表安裝成功
![](https://i.imgur.com/RsG8dNw.png)

* 移動到檔案路徑(假設檔案在Downloads/EnglishMaterialTools-main)
```
cd Downloads/EnglishMaterialTools-main
```
* 安裝所需套件
```
pip3 install -r requirements.txt
```
```
pip3 install googletrans==3.1.0a0
```
```
pip3 install matplotlib==3.5.2
```
* 執行script (檔案需和 translate.py、lookup.py 放在同一個資料夾)。假設要翻譯的檔案為test_translate.txt
```
python3 translate.py test_translate.txt
```
* 假設要查詢的檔案為test_lookup.txt
```
python3 lookup.py test_lookup.txt
```
