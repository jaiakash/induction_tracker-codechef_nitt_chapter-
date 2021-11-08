import webbrowser

# Add the IDs of partcipaants
username_atcoder = ["akashjaiswal03", "user2"]
username_codechef = ["akashjaiswal03", "user2"]
username_codeforces = ["johnAKJ", "user2"]

# Total number of partcipants
total_participants = len(username_atcoder)

# Set true for contest on for which performace is tracked
Codeforces = False
Codechef = False
Atcoder = True

for i in range(total_participants):
    if Atcoder:
        atcoder_url = "https://kenkoooo.com/atcoder#/user/"+username_atcoder[i]+"?userPageTab=Submissions"
        webbrowser.open(atcoder_url)

    if Codechef:    
        codechef_url = "https://www.codechef.com/users/"+username_codechef[i]
        webbrowser.open(codechef_url)

    if Codeforces:    
        codeforces_url = "https://codeforces.com/submissions/"+username_codeforces[i]
        webbrowser.open(codeforces_url)