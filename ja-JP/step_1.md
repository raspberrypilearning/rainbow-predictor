## はじめに

このプロジェクトでは、いつ虹（にじ）に出会えるかを予測するためにSense HAT上にある温度(おんど)センサーと湿度(しつど)センサーを使います。 適切な条件がそろったときにSense HAT LED Matrixに虹（にじ）を表示します。

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/eaea4cb76c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark">
</iframe> <img src="images/rainbow-final.png" />
</div>

Trinketエミュレータでは、以下のようにスライダーを動かして温度と湿度を変更できます。

![スクリーンショット](images/rainbow-sliders.png)

気温が20度を超えて、かつ、湿度が80パーセントを超えると虹（にじ）が出ます。 晴れ（黄色）や雪（白）になる気象条件を見つける実験をしてみてください。

### クラブリーダーのための追加情報

このプロジェクトを印刷する必要がある場合は、 [印刷用バージョン](https://projects.raspberrypi.org/en/projects/rainbow-predictor/print)を使用してください。

## \--- collapse \---

## title: クラブリーダー用メモ

## はじめに

このプロジェクトでは、子どもたちがSense HATセンサーの使って天気を検知し、あたたかくて湿度が高いときにLEDマトリックスを使って虹（にじ）を表示する方法を学びます。

## オンライン・リソース

**このプロジェクトではPython 3を使います。**オンライン上でPythonを書ける[Trinket](https://trinket.io/)を使うことをおすすめします。 このプロジェクトでは、以下のTrinketが用意されています：

* [「虹（にじ）の予測」基本Trinket -- jumpto.cc/rainbow-go](http://jumpto.cc/rainbow-go)

また、完成版プログラムが入力済みのtrinketも用意されています。

* [「虹（にじ）の予測」完成 -- trinket.io/python/eaea4cb76c](https://trinket.io/python/eaea4cb76c)

## オフライン・リソース

このプロジェクトはSense HATをつけたRaspberry Piを使って[オフラインでも完了](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/)できます。 「プロジェクト資料」のリンクをクリックすると、このプロジェクトのリソースにアクセスできます。 This link contains a 'Project Resources' section, which includes resources that children will need to complete this project offline. Make sure that each child has access to a copy of these resources. This section includes the following files:

* rainbow/rainbow.py

You can also find a completed version of this project in the 'Volunteer Resources' section, which contains:

* rainbow-finished/rainbow.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

## Learning Objectives

* Physical computing - sensors;
* Boolean AND; 
* RGB Colours;
* Sense HAT display;

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

* [Combine programming constructs to solve a problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Challenges

* More Weather - display different images under different weather conditions. 

\--- /collapse \---

## \--- collapse \---

## title: Project materials

## Project resources

* [.zip file containing all project resources](resources/rainbow-project-resources.zip)
* [Starter project](http://jumpto.cc/rainbow-go)
* [Offline starter Python file](resources/rainbow-rainbow.py)

## Club leader resources

* [.zip file containing all completed project resources](resources/rainbow-volunteer-resources.zip)
* [Online completed Trinket project](https://trinket.io/python/eaea4cb76c)
* [rainbow-finished/rainbow.py](resources/rainbow-final-rainbow.py)

\--- /collapse \---