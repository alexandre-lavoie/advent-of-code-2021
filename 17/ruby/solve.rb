ranges = File.open("../input.t1.txt").read().scan(/[xy]=([\-\d]*)\.\.([\-\d]*)/).flatten.map{|x| x.to_i}

def guass_sum(x)
    (x * (x + 1)) / 2
end

x_range = ranges[0..1]
y_range = ranges[2..4]

vy_max = -y_range[0] - 1
y_max = guass_sum(vy_max)

print("Task 1: ", y_max, "\n")

def inverse_guass_sum(t, v)
    if v <= 0 then
        v = 1
    end

    (-1 + Math.sqrt(1 + 4 * (2 * t + v * (v + 1)))) / 2
end

vxs = (x_range[0]*2..x_range[1]*2).to_a.map{|x| Math.sqrt(x)}.filter{|x| (x % 1).zero?}.map{|x| x.to_i}

count = 0
# Direct shot.
count += (y_range[1] - y_range[0]) * (y_range[1] - y_range[0])
# Parabolic shot.
count += (-y_range[0]) * vxs.count

## I give up on the math approach...

