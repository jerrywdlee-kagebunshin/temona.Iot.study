require "lchika/version"

module Lchika
  def chikachika(pin,sec)
        exp = open("/sys/class/gpio/export", "w")
        exp.write(pin)
        exp.close

        dir = open("/sys/class/gpio/gpio#{pin}/direction", "w")
        dir.write("out")
        dir.close

        out = 1
        sec = sec * 2
        "#{sec}".to_i.times do
          val = open("/sys/class/gpio/gpio#{pin}/value", "w")
          val.write(out)
          val.close
          out = out == 1 ? 0 : 1
          sleep 0.5
        end

      uexp = open("/sys/class/gpio/unexport", "w")
      uexp.write(pin)
      uexp.close
  end
  module_function :chikachika
end

