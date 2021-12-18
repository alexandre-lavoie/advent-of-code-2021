require 'json'

def explode(snail)
    index = -1
    depth = 0

    snail.each_with_index{|c, i|
        if c == "[" then
            depth += 1
        elsif c == "]" then
            depth -= 1
        end

        if c.is_a? Integer and snail[i+1].is_a? Integer and depth > 4 then
            index = i
            break
        end
    }

    if index == -1 then
        return snail
    end

    l, r = snail[index], snail[index+1]
    snail = snail[0..index-2] + [0] + snail[index+3..]

    (index-2).downto(0).each{|i| 
        if snail[i].is_a? Integer then
            snail[i] += l
            break
        end
    }

    (index..snail.count-1).each{|i|
        if snail[i].is_a? Integer then
            snail[i] += r
            break
        end
    }

    snail
end

def split(snail)
    index = -1

    snail.each_with_index{|c, i|
        if c.is_a? Integer and c >= 10 then
            index = i
            break
        end
    }

    if index == -1 then
        return snail
    end

    snail[0..index-1] + ["[", (snail[index] / 2.0).floor, (snail[index] / 2.0).ceil ,"]"] + snail[index+1..]
end

def snail_1d(raw)
    raw.chars.filter{|x| x != ","}.map{|x| if x.match(/^(\d)+$/) then x.to_i else x end}
end

def snail_str(snail)
    snail.join(",").gsub("[,", "[").gsub(",]", "]")
end

def snail_nd(snail)
    JSON.parse snail_str snail
end

def reduce(snail)
    while true
        next_snail = explode(snail)
    
        if not next_snail == snail then
            snail = next_snail
            next
        end
    
        next_snail = split(snail)
    
        if not next_snail == snail then
            snail = next_snail
            next
        end
    
        return snail
    end
end

def snail_add(s1, s2)
    ["["] + s1 + s2 + ["]"]
end

def snail_sum(snails)
    snails.inject(0) {|snail, next_snail|
        if snail == 0 then
            reduce next_snail
        else
            reduce snail_add(snail, next_snail)
        end
    }
end

def snail_file_1d(path)
    File.open(path).readlines.map(&:chomp).map{|line| snail_1d line}
end

def snail_magnitude(snail)
    if snail.is_a? Integer then
        return snail
    end

    3 * snail_magnitude(snail[0]) + 2 * snail_magnitude(snail[1]) 
end

snails = snail_file_1d "../input.txt"

print "Task 1: "
print snail_magnitude snail_nd snail_sum snails
print "\n"

print "Task 2: "
print (snails.combination(2).to_a + snails.reverse.combination(2).to_a).map{|snails| snail_magnitude snail_nd snail_sum snails}.max
print "\n"
