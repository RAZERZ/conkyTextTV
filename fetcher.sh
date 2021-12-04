curl https://www.svt.se/text-tv/100 > /home/razerz/Documents/i3/textTv/data.txt &&
  python /home/razerz/Documents/i3/textTv/parser.py &&
  mogrify -format png -fill "#000000" -opaque "#0000FF" /home/razerz/Documents/i3/textTv/100.png &&
  mogrify -format png -fill "#FF00FF" -opaque "#FFFFFF" /home/razerz/Documents/i3/textTv/100.png &&
  convert /home/razerz/Documents/i3/textTv/100.png -transparent black /home/razerz/Documents/i3/textTv/100_transparent.png
