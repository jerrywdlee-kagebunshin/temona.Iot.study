# URLにアクセスするためのライブラリ読み込み
require 'open-uri'
require 'lchika'
num = 0
while num < 2 do
	# 読み込むIPを指定
	url = open('http://***.***.***.***:4567/back_switch').read
	if url.include?("1")
		Lchika.chikachika(27,1)
	end
end