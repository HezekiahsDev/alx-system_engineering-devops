#!/usr/bin/env ruby
# This script contains a REGEX that matches only UPPERCASE letters

puts ARGV[0].scan(/[A-Z]/).join
