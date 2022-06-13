require 'bio'
require '~/sotuken/omomi/get_entry'

def size_gain(object)
    answer = object.size() - 1
    return answer
end

coordinate = [[0], [0]]  #座標の配列([x], [y])
x, y = 0, 0
base_sequence = String.new

mapping = { "a" => [1, 1], "t" => [-1, 1], "g" => [-1, -1], "c" => [1, -1] }

Bio::FlatFile.auto(ARGF) do |ff|
    ff.each_entry do |entry|
        base_sequence += entry.seq.to_s
    end
end

base_sequence_length = size_gain(base_sequence)

for element in 0..base_sequence_length do
    base = base_sequence[element]

    if !(mapping.keys.include?(base)) && base != nil
        base_sequence.delete!(base)
    end
end

for element in 0..1 do
    x += mapping[base_sequence[element]][0]
    y += mapping[base_sequence[element]][1]
    coordinate[0].push(x)
    coordinate[1].push(y)
end

base_sequence_length = size_gain(base_sequence)

for element in 2..base_sequence_length do
    codon = base_sequence[element-2..element]
    x += mapping[base_sequence[element]][0] * $codon_cost[codon]
    y += mapping[base_sequence[element]][1] * $codon_cost[codon]
    coordinate[0].push(x)
    coordinate[1].push(y)
end

coordinate_lenght = size_gain(coordinate[0])

for element in 0..coordinate_lenght do
    puts "#{coordinate[0][element]} #{coordinate[1][element]}"
end
