source ~/vim_config/.zshrc_normal

autoload -U colors && colors

# Thx Oh-My-ZSH (Spectrum)
typeset -AHg FG FX BG
FX=(
    reset     "%{[00m%}"
    bold      "%{[01m%}" no-bold      "%{[22m%}"
    italic    "%{[03m%}" no-italic    "%{[23m%}"
    underline "%{[04m%}" no-underline "%{[24m%}"
    blink     "%{[05m%}" no-blink     "%{[25m%}"
    reverse   "%{[07m%}" no-reverse   "%{[27m%}"
)

for color in {000..255}; do
    FG[$color]="%{[38;5;${color}m%}"
    BG[$color]="%{[48;5;${color}m%}"
done

if [ -z "$TMUX" ] 
then
	PS1="%{$fg[blue]%}%n%{$reset_color%}@%m: %{$fg[yellow]%}%~ %{$reset_color%}%% "
# 	PS1="$FG[019]%n%{$reset_color%}@%m: $FG[214]%~ %{$reset_color%}% "
else 
	PS1="%{$fg[yellow]%}~>%{$reset_color%} "
fi
