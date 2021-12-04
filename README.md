# conkyTextTV
SVT TextTV for Conky by generating image

# Install

- Clone repo in ~/Documents/i3
- Create an entry in /usr/share/conky to execute ~/Documents/i3/conkyTextTV/fetcher.sh, this will return 2 images, 100.png (not transparent) and 100_transparent.png (transparent). Create an entry to show the image

# How it works

The fetcher clones the official SVT page with Text TV, the parser parses the HTML and filters out the base64 encoded GIF and converts into a PNG. The PNG is then ran through the command "convert" to convert it into a transparent image. That's it.

# Result

![TextTV in Conky](https://github.com/RAZERZ/conkyTextTV/blob/main/repoImg.png)
