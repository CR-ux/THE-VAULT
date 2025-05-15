#!/bin/zsh

# Prompt for alias name
echo "Enter alias name:"
read alias_id

# Prompt for command or script the alias should run
echo "Enter alias command/script:"
read alias_script

# Append the properly formatted alias to ~/.zshrc
echo "alias $alias_id=\"$alias_script\"" >> ~/.zshrc

# Reload zshrc to apply the new alias
source ~/.zshrc

# Confirm and show what was added
echo "✅ Alias added to ~/.zshrc:"
echo "alias $alias_id=\"$alias_script\""
echo "printing updated zshrc..."
cat ~/.zshrc
