require 'mizlab'
require 'csv'
require 'bio'

#ゲノムデータをサーバーのディレクトリに保存しないで実行すると実行時間が大きくなる！
#
def accession_number_gain

  data_list = CSV.read('organelles.csv')
  length = data_list[0].size()
  
  for i in 0..length do
    if data_list[0][i] == "Replicons"
        n = i
    end
  end
  
  data_list = data_list.map{|row| row[n]}
  
  data_list.each do |s|
    if s.include?("/")
      s.sub!(/\/.*/m, "")
    end
  
    if s.include?("MT:")
      s.gsub!(/MT:/, "")
    end
  
    if s.include?("MIT:")
      s.gsub!(/MIT:/, "")
    end
  
    if s.include?("mt:")
      s.gsub!(/mt:/, "")
    end
  end
  
  data_list.delete_at(0)
  
  return data_list
end

accession_number_list = accession_number_gain.uniq
#ゲノム配列ダウンロード

=begin
accession_number_list.each do |lang|
    ent = Mizlab.getobj(lang)
    Mizlab.savefile("#{ent.accession}.gbk", ent)
    sleep(0.5)
end
=end

codon_sum = Hash.new(0)
$codon_cost = Hash.new(0)

atgc = ['a', 't', 'g', 'c']
check = []

atgc.repeated_permutation(3).to_a.each do |elm|
  check.push(elm.join)
end

accession_number_list.each do |number|
  number_length = number.size() - 3
  Bio::FlatFile.auto(number.slice!(0..number_length) + ".gbk") do |ff|
    ff.each_entry do |entry|
      entry.seq.window_search(3) do |dna_codon|
        if check.include?(dna_codon)
          codon_sum[dna_codon] += 1
        end
      end
    end
  end
end

codon_sum = codon_sum.sort.to_h

codon_sum.each do |codon, value|
  cacl = (codon_sum[codon[0..1]+'a'] + codon_sum[codon[0..1]+'t'] + codon_sum[codon[0..1]+'g'] + codon_sum[codon[0..1]+'c']).to_f
  cacl = (value / cacl)
  $codon_cost[codon] = -(Math.log2(cacl))
end

#$codon_cost.each do |key, value|
#  puts "#{key} : #{value}"
#end