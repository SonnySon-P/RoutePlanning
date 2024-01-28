# Route planning based on time constraints

**作品名稱：** 在不同時段限制下的路徑規劃
	
**動機：** 該作品為本人在修讀人工智慧課程時的作業(該作業還有兩位同學參與，但程式大部分都為自己本人撰寫，同學幫忙除錯與確認答案正確與否)。

**開發環境：** Python

**題目解說：** 在地圖上有A~Z的節點，並規定好結點間的連結狀況。但是為了反映實際真實道路車輛行走時間，將一天中分成三個時段，分別為00:00:00~07:59:59、08:00:00~16:59:59、17:00:00~23:59:59。不同時間點，車輛通行同路線所需花費時間皆不盡相同。將可通行路線及耗費時間，運用相鄰建置完於程式中。

<br>
<div align="center">
	<img src="./遊戲截圖.png" alt="Editor" width="500">
</div>
<br>

**解題演算法：** 
主要運用三種方法來進行解題，分別如下所示：
<br>
1. 關於prob1.py，是採用UCS演算法撰寫而成。
2. 關於prob2.py，是使用Ａ*演算法撰寫而成，在評價節點的Cost時的ｈ(n)函數，本作業是採用AllPairs的演算法去計算最短路徑。
3. 關於prob3.py，主要是透過使用者輸入必須經過的節點，來作為基因序列，創建、交配與突變，但是當基因序列小於等於三時，則會透過切一刀，兩兩基因相同位置進行置換。基因序列點與點間的成本及中繼點位，則是透過UCS演算法來尋求。
<br>

```python
python prob1.py StartTime StartNode GoalNode
```
**計算結果說明：** 如([BCJKS],39)，[]中為所經過的節點，39為耗費時間。
