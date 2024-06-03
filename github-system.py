#Create a program similar to the Github

# Asking the user to fill all the credentials correctly
userName = input('Please enter your username here: ').strip().lower()
userEmail = input('Please enter your email address here: ').strip().lower()
userPassword = input('Please enter your password here: ').strip()

# Checking if the user has not filled any of the credentials properly
while userName != 'tayyab' or userEmail != 'tayyabali78013@gmail.com' or userPassword != 'tayyabali20':
    
    print("Error: Invalid username, email, or password. Please try again.")
    
    userName = input('Please enter your username here: ').strip().lower()
    userEmail = input('Please enter your email address here: ').strip().lower()
    userPassword = input('Please enter your password here: ').strip()

input('Greetings! Hopefully you are doing well. Press enter to continue.')
input('Welcome to GitHub. Press enter to continue.')

print(f'Dear {userName}, please add a repository here:')
print('Repository name *')
createRepository = input().strip()

print(f'Dear {userName}, your repository ({createRepository}) has been successfully created. Press enter to continue.')
input()

# Asking user to create a file with a .py extension
while True:
    
    print(f'Dear {userName}, please create a new file with a .py extension to add your Python code.')
    
    newFile = input().strip()
    
    if newFile.endswith('.py'):
        break
    
    else:
        print("Error: The file extension must be '.py'. Please try again.")

print(f'Dear {userName}, your file has been created. Please add your Python code here. \n')

print('Code Editor \n')

linesOfCode = []

# Collecting code lines
for i in range(1, 100):
    
    lineOfCode = input(f'{i}: ').strip()
    
    if lineOfCode.lower() == 'exit':
        break
    
    linesOfCode.append(lineOfCode)

code = '\n'.join(linesOfCode)

# Displaying the collected code
print('\n' + '='*40)
print('          Your Code Output           ')
print('='*40)
print(code)
print('='*40)

if newFile and linesOfCode:
    
    print(f'Dear {userName}, below is a list of all the necessary Git commands. To push your code, please enter each command one by one.')

    githubCommand1 = 'git init'
    githubCommand2 = 'git add .'
    githubCommand3 = 'git commit -m "first commit"'
    githubCommand4 = 'git branch -M main'
    githubCommand5 = 'git remote add origin https://github.com/TAYYABALI-20/Python-Programs.git'
    githubCommand6 = 'git push -u origin main'

    print(githubCommand1)
    print(githubCommand2)
    print(githubCommand3)
    print(githubCommand4)
    print(githubCommand5)
    print(githubCommand6)

    def handle_git_command(expected_command):
        
        entered_command = input('Write the command here: ').strip()
        
        while entered_command != expected_command:
            
            print(f'Error: Command "{entered_command}" is incorrect. Please try again.')
            
            if expected_command == 'git init':
                print('fatal: Not a git repository (or any of the parent directories): .git')
            
            elif expected_command == 'git add .':
                print('fatal: pathspec "." did not match any files')
            
            elif expected_command == 'git commit -m "first commit"':
                print('On branch main\nNo commits yet\nnothing to commit, create/copy files and use "git add" to track')
            
            elif expected_command == 'git branch -M main':
                print("error: refname refs/heads/main not found\nfatal: Branch rename failed")
            
            elif expected_command == 'git remote add origin https://github.com/TAYYABALI-20/Python-Programs.git':
                print('fatal: not a git repository (or any of the parent directories): .git')
            
            elif expected_command == 'git push -u origin main':
                print('error: src refspec main does not match any\nerror: failed to push some refs to \'https://github.com/TAYYABALI-20/Python-Programs.git\'')
            
            entered_command = input('Write the command here: ').strip()
        
        return entered_command

    # Handle each git command with error handling
    if handle_git_command(githubCommand1) == githubCommand1:
        print('Initialized empty Git repository in C:/Users/TAYYAB/OneDrive/Desktop/python/.git/')
    
    if handle_git_command(githubCommand2) == githubCommand2:
        print('Press enter to continue')
    
    if handle_git_command(githubCommand3) == githubCommand3:
        print('[main 6cde7f1] first commit \n1 file changed, 27 insertions(+) \ncreate mode 100644 github-system.py \n')
    
    if handle_git_command(githubCommand4) == githubCommand4:
        print('Press enter to continue')
    
    if handle_git_command(githubCommand5) == githubCommand5:
        print('Press enter to continue')
    
    if handle_git_command(githubCommand6) == githubCommand6:
        print('Enumerating objects: 4, done. \nCounting objects: 100% (4/4), done. \nDelta compression using up to 4 threads \nCompressing objects: 100% (3/3), done. \nWriting objects: 100% (3/3), 514 bytes | 257.00 KiB/s, done. \nTotal 3 (delta 1), reused 0 (delta 0), pack-reused 0 \nremote: Resolving deltas: 100% (1/1), completed with 1 local object. \nTo https://github.com/TAYYABALI-20/Python-Programs.git \n   4c0f024..6cde7f1  main -> main \nbranch "main" set up to track "origin/main".')

    repositoryOpen = input('Type "open" to access your GitHub repository: ').strip().lower()

    if repositoryOpen == 'open':
        
        print(f'Dear {userName}, your repository ({createRepository}) contains the following code:')
        print(code)