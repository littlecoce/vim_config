source ~/vim_config/.zshrc_normal

autoload -U colors && colors
if [ -z "$TMUX" ] 
then
	PS1="%{$fg[blue]%}%n%{$reset_color%}@%m: %{$fg[yellow]%}%~ %{$reset_color%}%% "
else 
	PS1="%{$fg[yellow]%}~>%{$reset_color%} "
fi
export PATH=$PATH:/home/nonce/vms/scripts/
