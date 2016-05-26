# URLにアクセスするためのライブラリ読み込み
require 'open-uri'
# スクレイピングするためのライブラリ読み込み
require 'nokogiri'
require 'net/http'
require 'lchika'
Lchika.chikachika(27)

# num = 0
# while num < 2 do


p url = 'http://127.0.0.1:4567/switch'
charset = nil
html = open(url) do |f|
  charset = f.charset # 文字種別を取得
  f.read # htmlを読み込んで変数htmlに渡す
end

# htmlをパース(解析)してオブジェクトを生成
p doc = Nokogiri::HTML.parse(html, nil, charset)
# # タイトルを表示
# p "111111111"
# p doc.xpath('/html/body/a/img')
# p "111111111"
# sleep 1
# end


 # do |node|
# p "-------"
# p doc
# p "-------"
# p node.include?("")
# p "-------"
# end
num = 0
while num < 2 do
	url = open('http://127.0.0.1:4567/back_switch').read
	p "11111"
	p url.include?("switch1")
	sleep 1
end
# puts res

# end
# print("End")

# # puts res.body