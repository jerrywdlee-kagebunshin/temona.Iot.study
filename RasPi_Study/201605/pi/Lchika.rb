#SSH接続で直接実行のテスト用

exp = open("/sys/class/gpio/export", "w")
exp.write(27)
exp.close

dir = open("/sys/class/gpio/gpio27/direction", "w")
dir.write("out")
dir.close

10.to_i.times do
  val = open("/sys/class/gpio/gpio27/value", "w")
  val.write(out)
  val.close
  out = out == 1 ? 0 : 1
  sleep 0.5
end

uexp = open("/sys/class/gpio/unexport", "w")
uexp.write(27)
uexp.close