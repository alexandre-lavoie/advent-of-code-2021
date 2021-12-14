class Array
    def pairs
        self[..-2].zip(self[1..]).map{|v| v.join}
    end

    def counter
        self.pairs.inject(Hash.new(0)) {|c, v| 
            c[v] += 1 
            c
        }
    end
end

class Hash
    def step
        $mapping.inject(Hash.new(0)) {|c, (k, v)| 
            c[k[0] + v] += self[k]
            c[v + k[1]] += self[k]
            c
        }
    end

    def stepn(n)
        if n == 0 then
            self
        else
            self.stepn(n-1).step
        end
    end

    def +(obj)
        self.merge(obj){|_, c, d| c + d}.filter{|k, v| v > 0}
    end

    def -(obj)
        self.merge(obj){|_, c, d| c - d}.filter{|k, v| v > 0}
    end
end

data = File.open("../input.txt").readlines.map(&:strip)

$polymer = data[0].chars
$mapping = Hash[*data[2..].map{|v| v.split(" -> ")}.flatten]

def task(n)
    count = $polymer.counter.stepn(n).inject(Hash.new(0)) {|c, d| 
        c[d[0][0]] += d[1]
        c
    }
    count[$polymer[-1]] += 1
    count.values.max - count.values.min
end

puts("Task 1: " + task(10).to_s)
puts("Task 2: " + task(40).to_s)
