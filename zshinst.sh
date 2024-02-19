mkdir -p ${HOME}/.local/bin
git clone --depth=1 git@github.com:ohmyzsh/ohmyzsh.git "${HOME}/.oh-my-zsh"
git clone --depth=1 git@github.com:romkatv/powerlevel10k.git "${HOME}/.oh-my-zsh/themes/powerlevel10k"
git clone git@github.com:ahmetb/kubectx.git /tmp/kubectx
mv /tmp/kubectx/kubectx ${HOME}/.local/bin
mv /tmp/kubectx/kubens ${HOME}/.local/bin
# cp ${HOME}/git/ansible/files/zsh/gitstatusd ${HOME}/.oh-my-zsh/themes/powerlevel10k/gitstatus/usrbin/
sudo chsh -s /bin/zsh marcusc
