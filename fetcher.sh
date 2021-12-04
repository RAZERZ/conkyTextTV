curl https://www.svt.se/text-tv/100 > ~/Documents/i3/conkyTextTV/data.txt &&
  python ~/Documents/i3/conkyTextTV/parser.py &&
  #mogrify -format png -fill "#000000" -opaque "#0000FF" ~/Documents/i3/conkyTextTV/100.png &&
  #mogrify -format png -fill "#FF00FF" -opaque "#FFFFFF" ~/Documents/i3/conkyTextTV/100.png &&
  convert ~/Documents/i3/conkyTextTV/100.png -transparent black ~/Documents/i3/conkyTextTV/100_transparent.png
