page: 20140310-zathura-fsearch.md
subject: Works also without script
name: Dino
email: unknown@email.id
avatar: http://cdn.libravatar.org/avatar/99daad327e93a79b9b1a785c70649146
date: 2016-01-27 06:43:37 EST
ip: 128.131.42.203
referer: http://www.math.cmu.edu/~gautam/sj/blog/20140310-zathura-fsearch.html

Hi,
you can get it to not open a new instance by changing the zathurarc config as follows:
  set synctex true
  set synctex-editor-command "gvim --remote-silent +%{line} %{input}"

Hope this helps!
