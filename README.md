# WordMaterialTools
## 說明
用於節省英文講義編輯時間的簡單python scripts。
translate.py 使用googletrans套件，輸出例句翻譯。
lookup.py 使用爬蟲批量查詢劍橋辭典、Yahoo辭典，輸出單詞中文解釋、詞性、kk音標。
## 輸入格式(.txt)
### translate.py
* 請參考demo_translate.txt
    * 一句一列，勿在句子中間換列
### lookup.py
* 請參考demo_lookup.txt
    * 一字一列
## 使用方式
* 需先安裝python(3.8或以上) https://www.python.org/downloads/
* 從github下載zip (右上角Code->Download Zip)
    * 或者(需先安裝git http://git-scm.com/download/win)  
    ```
    git clone https://github.com/nateyang1999/WordMaterialTools.git
    ```
* 打開終端機(windows左下角搜尋cmd)，依序輸入
    * 移動至檔案資料夾下
    ```
    cd {你的檔案路徑(如:\github\WordMaterialTools)}
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
