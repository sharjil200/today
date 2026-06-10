password = "lala200"
enter_pass = input("Enter your password: ")

while enter_pass != password:
    enter_pass = input("Wrong password please try again: ")

print("Congratulations! You have entered the correct password.")

  new

After the merge, if there are no conflicts, Git will create a merge commit automatically.

If you get any error or conflict, paste the exact output here and I'll help you fix it.

# Switch to main branch
git checkout main

# Get latest changes (optional)
git pull origin main

# Merge new branch into main
git merge new

# Push merged changes to GitLab/GitHub
git push origin main
