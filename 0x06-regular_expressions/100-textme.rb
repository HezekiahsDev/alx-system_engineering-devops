#!/usr/bin/env ruby
# This script contains a REGEX that matches a pattern

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
